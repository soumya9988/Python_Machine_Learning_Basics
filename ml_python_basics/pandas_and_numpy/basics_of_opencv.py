import cv2
import numpy

# Reading and writing the numpy
img = cv2.imread('smallgray.png', 0)
print(img)
img1 = cv2.imread('smallgray.png', 1)
print(img1)
cv2.imwrite('newgraysmall.png', img)

print('Size of the array is: ', img.size)
print('Dimension of the array is:', img.ndim)
# Slicing
print(img[0:2, 2:4])

# Looping through the elements in the numpy array
print('Elements in the array are')
for i in img:
    print(i)

# Printing transpose
print('Transpose of the array is:')
for i in img.T:
    print(i)

# Flattening the array
print('Flattened array is:')
for i in img.flat:
    print(i)

# Horizontal & Vertical stacking
img_hs = numpy.hstack((img, img))
print(img_hs)
img_vs = numpy.vstack((img, img))
print(img_vs)

# Splitting
splt = numpy.vsplit(img_vs, 3)
print(splt)