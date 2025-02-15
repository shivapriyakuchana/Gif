import imageio.v3 as iio
filenames = ['p1.png','p2.png']
img = []
for file in filenames:
    img.append(iio.imread(file))
    
iio.imwrite('sri.gif',img,duration=500,loop=0)
