import telebot 
import requests 
from bs4 import BeautifulSoup 
import re
bot = telebot.TeleBot("YOUR TELEGRAM TOKEN")

@bot.message_handler(commands=['start'])
def send_welcome(message):

	bot.reply_to(message, "Привет! Напиши 'курс'")

@bot.message_handler(content_types=["text"])
def echo_all(message):

	DOLLAR_= ('https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4')
	headers_ ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"}
	full_page_ = requests.get(DOLLAR_, headers=headers_)	
	soup_ = BeautifulSoup(full_page_.content, 'html.parser')
	convert_ = soup_.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})#конвертирование 
	was = str(convert_[0])
	was = re.findall(r'\d+\.\d+', was)
	was = float(was[0])
	text = "Сейчас 1 доллар = "+ str(was)+ " (рубль)"
		

	bot.reply_to(message,text )

bot.infinity_polling()
