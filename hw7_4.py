from os import walk
from os.path import join as path_join, getsize

key = []
for root, dirs, files in walk('.'):
    if not files:
        continue
    key.extend((getsize(path_join(root, name)) for name in files))

len_max = len(list(str(max(key))))
bins = [10 ** i for i in range(2, len_max + 1)]

result = {}
for i in key:
    for j in bins:
        if i < j:
            result.update({j: result.get(j, 0) + 1})
            break
result = dict(sorted(result.items(), key = lambda x: x))

for max_size, count in result.items():
    print(f'Файлов с размером не более {max_size}: {count} шт.')