import random

from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.delfi.lt/').text

soup = BeautifulSoup(source, 'html.parser')

blocks = soup.find_all('div', class_='C-block-type-102-headline__title')

list1 = []
list2 = []

for block in blocks:
    # print(block.h5.text.split(':'))
    if len(block.h5.text.split(':')) == 2:
        list1.append(block.h5.a.text.split(':')[0])
        list2.append(block.h5.a.text.split(':')[1])

random.shuffle(list1)
random.shuffle(list2)

for i in range(0, len(list2)):
    print(list1[i] + ":" + list2[i])
# C-block-type-102-headline__title
