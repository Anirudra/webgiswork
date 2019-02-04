import rasterio
import numpy
import matplotlib.pyplot as plt

# opening file and reading band 3 and 4 into red_band and nir_band
with rasterio.open('Data/murrells-inlet_cams_1997-08-02', 'r') as dataSet:
    red_band = dataSet.read(3)
    nir_band = dataSet.read(4)

# setting divide by zero and treatment for invalid floating-point operation.
numpy.seterr(divide='ignore', invalid='ignore')

# calculating nvdi
ndvi = (nir_band.astype(rasterio.float32) + red_band.astype(rasterio.float32)) / (nir_band + red_band)

# setting pyplot axis scale
plt.axis('equal')

# showing the plot
plt.imshow(ndvi)
plt.show()

# extracting metadata as kwargs and updating it
kwargs = dataSet.meta

kwargs.update(
    count=1,
    dtype=rasterio.float32
)

# writing to file
with rasterio.open('data/ndvi','w', **kwargs) as out_file:
    out_file.write(ndvi, 1)