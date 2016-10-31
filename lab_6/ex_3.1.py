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
values = [3, 4, 1, 2, 5, 6, 7, 8, 9, 10]
a = get_percentile(values, 4)
print(a)