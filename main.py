import telebot as tb
import requests as req
from config import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver_citate = webdriver.Chrome()
driver_rifma = webdriver.Chrome()
driver_anekdot = webdriver.Chrome()

driver_citate.get(citate_url)
driver_rifma.get(rifma_url)
driver_anekdot.get(anekdot_url)

citate_button = driver_citate.find_element("class name", "random-button")
anekdot_button = driver_anekdot.find_element("class name", "random-button")

bot = tb.TeleBot(bot_token)
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Я мультизадачный бот!")


@bot.message_handler(regexp = r'/citate')
def citate_message(message):
    bot.send_message(message.chat.id, "Понял")
    citate_button.click()
    text = BeautifulSoup(driver_citate.page_source, features="html.parser")
    text = text.find("div", "citata")
    text = text.text
    print(text)
    bot.send_message(message.chat.id, text)
    
@bot.message_handler(regexp = r'/describe')
def describe_message(message):
    bot.send_message(message.chat.id, "Понял")
    text = citate_url, rifma_url,anekdot_url
    print(text)
    bot.send_message(message.chat.id, text)


bot.infinity_polling()