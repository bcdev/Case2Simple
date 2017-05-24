import os
import sys
import numpy as np

from c2x import Supported_Sensors

# Maybe add snappy to you python path
# sys.path.append('/home/user/.snap/snap-python/')

from snappy import File
from snappy import Product
from snappy import ProductIO
from snappy import ProductUtils
from snappy import jpy

Color = jpy.get_type('java.awt.Color')


def process_product(file, Sensor):
    in_product = ProductIO.readProduct(file)
    width = in_product.getSceneRasterWidth()
    height = in_product.getSceneRasterHeight()
    in_name = in_product.getName()
    in_description = in_product.getDescription()
    in_band_names = in_product.getBandNames()
    size = in_product.getSceneRasterSize()


    print("Product:     %s, %s" % (in_name, in_description))
    print("Raster size: %d x %d pixels" % (width, height))
    print("Start time:  " + str(in_product.getStartTime()))
    print("End time:    " + str(in_product.getEndTime()))
    print("Bands:       %s" % (list(in_band_names)))
    print(size)

    # Output product Definition
    # 1. define the target product and its file format
    c2x_product = Product('C2X', 'C2X', width, height)
    writer = ProductIO.getProductWriter('BEAM-DIMAP')
    c2x_product.setProductWriter(writer)
    fpath = in_product.getFileLocation().getAbsolutePath()
    fpath = os.path.split(fpath)[0] + "/out/" + os.path.split(fpath)[1]
    fpath = fpath.split(".")[0]
    fpath = fpath + "_InWater.dim"
    c2x_product.setFileLocation(File(fpath))

    # 2. define the bands for the results of the different algorithms
    outbands = {}
    for cnt in range(len(Sensor["outputs"])):
        outbands[Sensor["outputs"][cnt][0]] = c2x_product.addBand(Sensor["outputs"][cnt][0], Sensor["outputs"][cnt][1])


    # 3. copy tie point grids from input product to target product
    ProductUtils.copyTiePointGrids(in_product, c2x_product)
    ProductUtils.copyMetadata(in_product, c2x_product)
    ProductUtils.copyGeoCoding(in_product, c2x_product)
    ProductUtils.copyFlagBands(in_product, c2x_product, False)


    # 4. write the header to disk
    location = c2x_product.getFileLocation()
    c2x_product.writeHeader(c2x_product.getFileLocation().toString())
    writer.writeProductNodes(c2x_product, location)

    # assigning aux arrays
    rhow_arrays = dict()
    for wls in Sensor["wavelengths"]:
        rhow_arrays[str(wls)] = np.zeros(width, dtype=np.float32)

    #  get all specified bands from input product
    print("Processing %s with algos" % file)
    [print(algo[0]) for algo in Sensor["outputs"]]
    bsource = dict()
    for i in range(len(Sensor["wavelengths"])):
        bsource["band" + str(Sensor["wavelengths"][i])] = in_product.getBand(
            Sensor["band" + str(Sensor["wavelengths"][i])])

    bands = in_product.getBands()
    flag_bands = []
    for b in bands:
        if b.isFlagBand():
            flag_bands.append(b)

    flags_data = np.zeros (width, dtype=np.int32)

    # loop through the product line by line and application of algorithms
    for y in range(height):
        rhow = dict()
        for wl in Sensor["wavelengths"]:
            source_band = bsource["band" + str(wl)]
            # dealing with no-data; setting no-data to to NaN
            invalidMask = read_invalid_mask(source_band, width, y)
            source_band.readPixels(0, y, width, 1, rhow_arrays[str(wl)])
            rhow["band" + str(wl)] = np.ma.array(rhow_arrays[str(wl)], mask=invalidMask, fill_value=np.nan)
        for algo in range(len(Sensor["outputs"])):
            res = Sensor["outputs"][algo][2](rhow, Sensor["outputs"][algo][4], Sensor["outputs"][algo][5])
            name = Sensor["outputs"][algo][0]
            outbands[name].writePixels(0, y, width, 1, res)
        for fband in flag_bands:
            fband.readPixels(0, y, width, 1, flags_data)
            c2x_product.getBand(fband.getName()).writePixels(0, y, width, 1, flags_data)

    # all computations and writing is completed; close all data streams and finish the program
    c2x_product.closeIO()

    print("Done.")
    return 0

def read_invalid_mask(sourc_band, width, y):
    validMask = np.zeros(width, dtype=np.uint8)
    sourc_band.readValidMask(0, y, width, 1, validMask)
    invalidMask = np.where(validMask == 0, 1, 0)
    return invalidMask


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("usage: %s <file> <sensor>" % sys.argv[0])
        sys.exit(1)

    file = sys.argv[1]
    sensorName = sys.argv[2]

    useSensor = None
    for sensor in Supported_Sensors:
        if sensor['Name'].lower() == sensorName.lower():
            useSensor = sensor

    if useSensor is None:
        raise NotImplementedError("Unknown sensor name: " , sensorName)

    process_product(file, useSensor)
