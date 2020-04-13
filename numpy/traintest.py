import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

# in noraml(3-srating point,1-end point,100- random numer generation time)
x = numpy.random.normal(3, 1, 100)
# in noraml(150-srating point,40-end point,100- random numer generation time)
y = numpy.random.normal(150, 40, 100) / x
# print('\nX value: ',x)
# print('\ny value: ',y)
train_x = x[80:]
train_y = y[:80]
print(train_x)

# plt.scatter(x, y)
# plt.show()