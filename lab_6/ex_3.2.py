import numpy as np
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
values = [3, 4, 1, 2, 5, 6, 7, 8, 9, 10]
a = get_percentile(values, 4)
print(get_percentile_number(2.5, a))
print(get_percentile_number(5.5, a))
print(get_percentile_number(100, a))
