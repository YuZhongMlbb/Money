from config import TOKEN
from bs4 import BeautifulSoup
import telebot
import requests

class Optima():
    
    def __init__(self, url) -> None:
        self.url = url
    
    def parse(self):
        r = requests.get(url=self.url)
        soup = BeautifulSoup(r.content, 'html.parser')

        items_1 = soup.find_all('div', class_="iso-USD row0")
        new_list_1 = list()
        for elem in items_1:
            try:
                new_list_1.append(
                    {
                        'title': elem.find('div', class_="currency code").get_text(strip=True),
                        'buy': elem.find('div', class_="rate buy").find('span', class_="up").get_text(strip=True),
                        'sell': elem.find('div', class_="rate sell").find('span', class_="up").get_text(strip=True)
                    }
                )
            except:
                print('Ошибка')
        
        items_2 = soup.find_all('div', class_="iso-EUR row1")
        new_list_2 = list()
        for elem in items_2:
            try:
                new_list_2.append(
                    {
                        'title': elem.find('div', class_="currency code").get_text(strip=True),
                        'buy': elem.find('div', class_="rate buy").find('span', class_="up").get_text(strip=True),
                        'sell': elem.find('div', class_="rate sell").find('span', class_="up").get_text(strip=True)
                    }
                )
            except:
                print('Ошибка')

        items_3 = soup.find_all('div', class_="iso-KZT row0")
        new_list_3 = list()
        for elem in items_3:
            try:
                new_list_3.append(
                    {
                        'title': elem.find('div', class_="currency code").get_text(strip=True),
                        'buy': elem.find('div', class_="rate buy").find('span', class_="up").get_text(strip=True),
                        'sell': elem.find('div', class_="rate sell").find('span', class_="up").get_text(strip=True)
                    }
                )
            except:
                print('Ошибка')

        items_4 = soup.find_all('div', class_="iso-RUB row1")
        new_list_4 = list()
        for elem in items_4:
            try:
                new_list_4.append(
                    {
                        'title': elem.find('div', class_="currency code").get_text(strip=True),
                        'buy': elem.find('div', class_="rate buy").find('span', class_="up").get_text(strip=True),
                        'sell': elem.find('div', class_="rate sell").find('span', class_="up").get_text(strip=True)
                    }
                )
            except:
                print('Ошибка')
        return [new_list_1, new_list_2, new_list_3, new_list_4]
    
    def save_us(self, items):
        for i in items[0]:
            return f"Валюта: {i['title']}\nПокупка: {i['buy']}\nПродажа: {i['sell']}"
    
    def save_eu(self, items):
        for i in items[1]:
            return f"Валюта: {i['title']}\nПокупка: {i['buy']}\nПродажа: {i['sell']}"
    
    def save_kz(self, items):
        for i in items[2]:
            return f"Валюта: {i['title']}\nПокупка: {i['buy']}\nПродажа: {i['sell']}"
    
    def save_ru(self, items):
        for i in items[3]:
            return f"Валюта: {i['title']}\nПокупка: {i['buy']}\nПродажа: {i['sell']}"

optima = Optima(url="https://www.optimabank.kg/index.php?option=com_nbrates&view=default&Itemid=196&lang=ru")
opt = optima.parse()

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Здравствуйте, здесь вы можете узнать цену валют\nЕсли желаете узнать инструкцию, нажмите /help")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "/ru - рубли\n/kz - тенге\n/eu - евро\n/us - доллары")

@bot.message_handler(commands=['ru'])
def ru(message):
    bot.send_message(message.chat.id, optima.save_ru(items=opt))

@bot.message_handler(commands=['us'])
def us(message):
    bot.send_message(message.chat.id, optima.save_us(items=opt))

@bot.message_handler(commands=['eu'])
def eu(message):
    bot.send_message(message.chat.id, optima.save_eu(items=opt))

@bot.message_handler(commands=['kz'])
def kz(message):
    bot.send_message(message.chat.id, optima.save_kz(items=opt))

bot.polling(non_stop=True)