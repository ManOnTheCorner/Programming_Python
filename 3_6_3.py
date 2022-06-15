"""
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
"""
import requests
link = "https://stepic.org/media/attachments/course67/3.6.3/"
with open("dataset_3378_3.txt") as p:
    l = p.readline().strip()
l = str(requests.get(l).text)
while "we" not in l:
    print(l)
    l = requests.get(link + l).text
print(l)