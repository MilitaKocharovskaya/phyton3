import numpy as np
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
values = [3.0, 4.0, 1.0, 2.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
percentiles = get_percentile(values, 5)
print(percentiles)
print(value_equalization(5.5, percentiles))
print(value_equalization(5.5, percentiles))
print(value_equalization(5.5, percentiles))