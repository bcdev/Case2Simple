import os
import sys

import numpy as np
from snappy import (File, Product, ProductIO, ProductUtils)

from c2x import *


# Maybe add snappy to you python path
# sys.path.append('/home/user/.snap/snap-python/')

# Eventually set log level to debug
c2x_log.setLevel(logging.DEBUG)


def process_product(file, sensor):
    in_product = ProductIO.readProduct(file)
    width = in_product.getSceneRasterWidth()
    height = in_product.getSceneRasterHeight()
    in_name = in_product.getName()
    in_description = in_product.getDescription()
    in_band_names = in_product.getBandNames()

    c2x_log.info("Product:     %s, %s" % (in_name, in_description))
    c2x_log.debug("Raster size: %d x %d pixels" % (width, height))
    c2x_log.debug("Start time:  " + str(in_product.getStartTime()))
    c2x_log.debug("End time:    " + str(in_product.getEndTime()))
    c2x_log.debug("Bands:       %s" % (list(in_band_names)))

    # Output product Definition
    # 1. define the target product and its file format
    c2x_product = Product('%s_%s' % (in_name, PRODUCT_TYPE), '%s' % PRODUCT_TYPE, width, height)
    writer = ProductIO.getProductWriter('BEAM-DIMAP')
    c2x_product.setProductWriter(writer)
    fpath = in_product.getFileLocation().getAbsolutePath()
    fpath = os.path.split(fpath)[0] + "/out/" + os.path.split(fpath)[1]
    fpath = fpath.split(".")[0]
    fpath = "{0}_{1}.dim".format(fpath, PRODUCT_TYPE.lower())
    c2x_product.setFileLocation(File(fpath))

    sensor_outputs = sensor["outputs"]
    sensor_wavelengths = sensor["wavelengths"]

    # 2. define the bands for the results of the different algorithms
    outbands = dict()
    for cnt in range(len(sensor_outputs)):
        cnt = sensor_outputs[cnt]
        outbands[cnt[0]] = c2x_product.addBand(cnt[0], cnt[1])

    # 3. copy tie point grids from input product to target product
    ProductUtils.copyTiePointGrids(in_product, c2x_product)
    ProductUtils.copyMetadata(in_product, c2x_product)
    ProductUtils.copyGeoCoding(in_product, c2x_product)
    ProductUtils.copyFlagBands(in_product, c2x_product, False)

    # 4. write the header to disk
    location = c2x_product.getFileLocation()
    c2x_product.writeHeader(location)

    # assigning aux arrays
    rhow_arrays = dict()
    for wls in sensor_wavelengths:
        rhow_arrays[str(wls)] = np.zeros(width, dtype=np.float32)

    #  get all specified bands from input product
    c2x_log.info("Processing and writing to %s" % file)
    algo_names = dict()
    for cnt in range(len(sensor_outputs)):
        algo_names[cnt] = sensor_outputs[cnt][0]
    c2x_log.debug("Processing with following algos: %s " % list(algo_names.values()))

    bsource = dict()
    for i in range(len(sensor_wavelengths)):
        band_name = create_source_band_name(sensor_wavelengths[i])
        bsource[band_name] = in_product.getBand(sensor[band_name])

    flag_bands = []
    for b in in_product.getBands():
        if b.isFlagBand():
            flag_bands.append(b)

    flags_data = np.zeros (width, dtype=np.int32)

    # loop through the product line by line and application of algorithms
    for y in range(height):
        rhow = dict()
        for wl in sensor_wavelengths:
            source_band = bsource[create_source_band_name(wl)]
            # dealing with no-data; setting no-data to to NaN
            invalidMask = read_invalid_mask(source_band, width, y)
            source_band.readPixels(0, y, width, 1, rhow_arrays[str(wl)])
            rhow["band" + str(wl)] = np.ma.array(rhow_arrays[str(wl)], mask=invalidMask, fill_value=np.nan)
        for algo in range(len(sensor_outputs)):
            res = sensor_outputs[algo][2](rhow, sensor_outputs[algo][4], sensor_outputs[algo][5])
            name = sensor_outputs[algo][0]
            outbands[name].writePixels(0, y, width, 1, res)
        for fband in flag_bands:
            fband.readPixels(0, y, width, 1, flags_data)
            c2x_product.getBand(fband.getName()).writePixels(0, y, width, 1, flags_data)

    # all computations and writing is completed; close all data streams and finish the program
    c2x_product.closeIO()

    print("Done.")
    return 0


def create_source_band_name(wl):
    return "band%d" % wl


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

    if not os.path.exists(file):
        raise FileNotFoundError('Path \'%s\' does not exist' % file)

    useSensor = None
    for sensor in Supported_Sensors:
        if sensor['Name'].lower() == sensorName.lower():
            useSensor = sensor

    if useSensor is None:
        raise NotImplementedError("Unknown sensor name: " , sensorName)

    process_product(file, useSensor)
