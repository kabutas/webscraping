from bs4 import BeautifulSoup
import requests
import random
import os

source = requests.get('https://quotes.toscrape.com/page/2/')
soup = BeautifulSoup(source.text, 'html.parser')

quotes = soup.find_all('div', class_='quote')

quote_list = []
# loading_screen = ''
loading_screen = '\n\n\n\n\n\t\t\t\t'
for quote in quotes:
    quote_text = quote.find('span', class_='text').text
    quote_author = quote.find('small', class_='author').text
    author_page_link = quote.find('a')['href']

    author_source = requests.get(f'https://quotes.toscrape.com{author_page_link}')
    author_soup = BeautifulSoup(author_source.text, 'html.parser')
    birth_date = author_soup.find('span', class_='author-born-date').text
    birth_place = author_soup.find('span', class_='author-born-location').text
    birth_date_place = f"{birth_date}, {birth_place}"

    quote_list.append({
        'quote_text': quote_text,
        'quote_author': quote_author,
        'birth_date_place': birth_date_place,
    })

    loading_screen += "O"
    os.system('cls')
    print(loading_screen)
os.system('cls')
while True:
    if input("press 'ENTER' to start") == '':
        game_data = random.choice(quote_list)
        print('Who said that?\n')
        print(game_data['quote_text'])
        if input() == game_data['quote_author']:
            print('You have won!')
        else:
            if input(f'Not Right\nAuthor was born in: {game_data["birth_date_place"]}\n') == game_data['quote_author']:
                print('You have won!')
            else:
                print('You have lost!')
                print(f"Author was : {game_data['quote_author']}")
    else:
        break
