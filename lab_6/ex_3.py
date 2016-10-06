import random
import numpy as np
import matplotlib.pyplot as plt

#1
def get_percentile(values, bucket_number):
    n = 100/bucket_number
    a = []
    for i in range(1, bucket_number):
         a.append(np.percentile(values, n*i))
    return a

#2
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

#3
def value_equalization(value, percentiles, add_random=False):
    idx = get_percentile_number(value, percentiles)
    step = 1/len(percentiles)
    if add_random == True:
        random_noise = random.uniform(idx*step/100, (idx+1)*step/100)
    else:
        random_noise = 0
    new_value = idx*step + random_noise
    return new_value

#4,5
def values_equalization(values, percentiles, add_random=False):
    for i in range(len(values)):
        values[i] = value_equalization(values[i], percentiles, add_random)
    return values

#6
B = []
with open('img.txt', 'r') as img:
    for line in img:
        p = list(map(float, line.strip().split()))
        B.append(p)
data = np.array(B)

#7
plt.subplot(221)
plt.imshow(data, cmap=plt.get_cmap('gray'))

#8
plt.subplot(222)
values = [data.flatten()]
plt.hist(values, bins=10)

#9, 11
perc = get_percentile(values, 1000)
data1 = values_equalization(data.flatten(), perc, add_random=True)
data2 = data1.reshape(200, 267)

#10
plt.subplot(223)
plt.imshow(data2, cmap=plt.get_cmap('gray'))

plt.subplot(224)
values = [data1.flatten()]
plt.hist(values, bins=10)

#plt.show()

#12
A = []
for i in range(100):
    a = random.choice(data)
    A.append(a)
plt.subplot(211)
plt.imshow(A, cmap=plt.get_cmap('gray'))

#13
d = [i for i in range(1,200)]
C = []
c = random.sample(d, 100)
for i in range(100):
    C.append(data[c[i]])
plt.subplot(212)
plt.imshow(C, cmap=plt.get_cmap('gray'))

#plt.show()

#14
s = 0
for i in range(200*267):
    s = s + data1[i]
average = s/(len (data1))
print(average)