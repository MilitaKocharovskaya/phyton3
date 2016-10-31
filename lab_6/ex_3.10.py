import numpy as np
import matplotlib.pyplot as plt
import random

def get_percentile(values, bucket_number):
    n = 100/bucket_number
    a = []
    f = 0
    a.append(0.0)
    for j in range(bucket_number):
         a.append(np.percentile(values, f))
         f += n
    return a

def get_percentile_number(value, percentiles):
    i = 0
    k = 0
    while percentiles[i] <= value:
        k = i
        if i < len (percentiles)-1:
            i += 1
        else:
            break
    return k

def value_equalization(value, percentiles, add_random = False):
    idx = get_percentile_number(value, percentiles)
    step = 1/len(percentiles)
    new_value = idx*step
    if add_random == True:
        random_noise = random.uniform(0, step)
        new_value = idx*step + random_noise
    return new_value

def values_equalization(values, percentiles, add_random = False):
    for i in range(len(values)):
        values[i] = value_equalization(values[i], percentiles, add_random)
    return values

data = []
with open('img.txt', 'r') as img:
    for line in img:
        p = list(map(float, line.strip().split()))
        data.append(p)
data = np.array(data)

plt.subplot(221)
plt.imshow(data, cmap=plt.get_cmap('gray'))
plt.title(r'$Before$')

plt.subplot(222)
values = [data.flatten()]
plt.title(r'$Image hist before equalization$')
plt.hist(values, bins=10)

perc = get_percentile(values, 5)
data1 = values_equalization(data.flatten(), perc, add_random=True)
data2 = data1.reshape(200, 267)

plt.subplot(223)
plt.imshow(data2, cmap=plt.get_cmap('gray'))
plt.title(r'$After$')

plt.subplot(224)
values = [data2]
plt.hist(values, bins=10)
plt.title(r'$Image hist after equalization$')

plt.show()