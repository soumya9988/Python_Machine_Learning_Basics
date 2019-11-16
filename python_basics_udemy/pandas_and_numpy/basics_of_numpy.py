import numpy

n = numpy.arange(27)
print(n)
print(type(n))
n = n.reshape(3,9) # Converting it into a 3 D array
print(n)
n = n.reshape(3,3,3)
print(n)
print('Dimension of n is: ', n.ndim)
print('Size of the array is:', n.size)
print('Shape of the array is:', n.shape)
print('Elements in the array are of type:', n.dtype)

m = numpy.asarray([[121,122,123,124], 1, []])
print(m)