import os
import sys
import math

import array

import statistics
import networkx as nx

from matplotlib import rc
rc('font', family='Droid Sans', weight='normal', size=14)

import matplotlib.pyplot as plt


class WikiGraph:

    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename)

        with open(filename) as f:
            n, _nlinks = map(int, f.readline().split())
            self._m = n
            self._l = _nlinks
            self._titles = []
            self._sizes = array.array('L', [0]*n)
            self._links = array.array('L', [0]*_nlinks)
            self._redirect = array.array('B', [0]*n)
            self._offset = array.array('L', [0]*(n+1))
            for i in range(n):
                t = f.readline().strip()
                self._titles.append(t)
                s, r, k = map(int, f.readline().split())
                self._sizes[i] = s
                self._redirect[i] = r
                for j in range(k):
                    self._links[self._offset[i] + j] = int(f.readline())
                    self._offset[i + 1] = self._offset[i] + k
        print('Граф загружен')

    def get_number_of_links_from(self, _id):
        return len(self.get_links_from(_id))

    def get_links_from(self, _id):
        return self._links[self._offset[_id]:self._offset[_id+1]]

    def get_id(self, title):
        return self._titles.index(title)

    def get_number_of_pages(self):
        return self._m

    def is_redirect(self, _id):
        if self._redirect[_id]!= 0:
            return True

    def get_title(self, _id):
        return self._titles[_id]

    def get_page_size(self, _id):
        return self._sizes[_id]


def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()
    # TODO: нарисовать гистограмму и сохранить в файл

'''
if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Использование: wiki_stats1.py <файл с графом статей>')
        sys.exit(-1)

    if os.path.isfile(sys.argv[1]):
        wg = WikiGraph()
        wg.load_from_file(sys.argv[1])
    else:
        print('Файл с графом не найден')
        sys.exit(-1)

    # TODO: статистика и гистограммы
    '''
wg = WikiGraph()
wg.load_from_file('wiki_small.txt')

l = wg.get_number_of_pages()
x = wg.get_id('Python')
y = wg.get_id('Список_файловых_систем')
d = [float('+inf') for i in range(l)]
d[x] = 0
used = [False]*l
prev = [None]*l
min_d = 0
min_v = x
while min_d < float('+inf'):
    i = min_v
    used[i] = True
    for neighbour in wg.get_links_from(i):
        if d[i] + 1 < d[neighbour]:
            d[neighbour] = d[i] + 1
            prev[neighbour] = i
    min_d = float('+inf')
    for i in range(l):
        if not used[i] and d[i] < min_d:
            min_d = d[i]
            min_v = i
path = []
j = y
while j is not None:
    path.append(j)
    j = prev[j]
path = path[::-1]
print('Найден путь:', *path)
for i in range(len(path)):
    print(*wg.get_title(path[i]))

print(wg.get_id('UNIX'))

r2 = 0
for i in range(l):
    if wg.is_redirect(i):
        r2 += 1
print('Количество статей с перенаправлением:',r2)

r3 = l
for i in range(l):
    h = wg.get_number_of_links_from(i)
    r3 = min(r3, h)
print('Минимальное количество ссылок из статьи:', r3)

r4 = 0
for i in range(wg.get_number_of_pages()):
    if wg.get_number_of_links_from(i) == r3:
        r4 += 1
print('Количество статей с минимальным количеством ссылок:', r4)

r5 = 0
for i in range(l):
    h = wg.get_number_of_links_from(i)
    r5 = max(r5, h)
print('Максимальное количество ссылок из статьи:', r5)

r6 = 0
for i in range(wg.get_number_of_pages()):
    if wg.get_number_of_links_from(i) == r5:
        r6 += 1
print('Количество статей с максимальным количеством ссылок:', r6)

for i in range(l):
    if wg.get_number_of_links_from(i) == r5:
        print('Cтатья с наибольшим количеством ссылок:', wg.get_title(i))

r8 = 0
for i in range(l):
    r8 += wg.get_number_of_links_from(i)
print('Среднее количество ссылок в статье', "%.2f"%(r8/l))

r9 = l
g = [0 for i in range(l)]
for i in range(l):
    for j in wg.get_links_from(i):
        g[j] += 1
for i in range(l):
    r9 = min(r9, g[i])
print('Минимальное количество ссылок на статью', r9)

r10 = 0
for i in range(l):
    if g[i] == r9:
        r10 += 1
print('Количество статей с минимальным количеством внешних ссылок', r10)

r11 = 0
for i in range(l):
    r11 = max(r11, g[i])
print('Максимальное количество ссылок на статью', r11)

r12 = 0
r13 = []
for i in range(l):
    if g[i] == r11:
        r12 += 1
        r13 = wg.get_title(i)
print('Количество статей с максимальным количеством внешних ссылок:', r12)

print('Cтатья с наибольшим количеством внешних ссылок:', r13)

print('Среднее количество внешних ссылок на статью:', "%.2f" % (statistics.mean(g)))

r15 = [0 for i in range(l)]
for i in range(l):
    if wg.is_redirect(i):
        for j in wg.get_links_from(i):
            r15[j] += 1
print('Минимальное количество перенаправлений на статью:', min(r15))

r16 = 0
for i in range(l):
    if r15[i] == min(r15):
        r16 += 1
print('Количество статей с минимальным количеством внешних перенаправлений:', r16)

print('Максимальное количество перенаправлений на статью', max(r15))

r18 = 0
for i in range(l):
    if r15[i] == max(r15):
        r18 += 1
print('Количество статей с максимальным количеством внешних перенаправлений', r18)

r19 = []
for i in range(l):
    if r15[i] == max(r15):
        r19.append(wg.get_title(i))
print('Статья с наибольшим количеством перенаправлений:', *r19)

print('Среднее количество внешних перенаправлений на статью:', "%.2f" % (statistics.mean(r15)))

'''def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()
    # TODO: нарисовать гистограмму и сохранить в файл


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Использование: wiki_stats.py <файл с графом статей>')
        sys.exit(-1)

    if os.path.isfile(sys.argv[1]):
        wg = WikiGraph()
        wg.load_from_file(sys.argv[1])
    else:
        print('Файл с графом не найден')
        sys.exit(-1)

    # TODO: статистика и гистограммы'''