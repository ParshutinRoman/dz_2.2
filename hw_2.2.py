import chardet
from collections import Counter
path = "/Users/admin/Desktop/netology/PY/dz_2.2"

files = ('newsafr.txt', 'newscy.txt', 'newsfr.txt', 'newsit.txt')

result = {}
for file in files:
    with open(file, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)

    with open(file, 'r', encoding = result['encoding']) as f:
        data = f.read()
        words = data.split(' ')
        words_short = []
        for word in words:
            if len(word) > 6:
                words_short.append(word)
        words_short.sort()
        count = Counter(words_short)
        print('топ 10 самых часто встречающихся слов длиннее 6 символов:', count.most_common(10))
