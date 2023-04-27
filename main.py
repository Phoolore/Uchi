import telebot as tb
import requests as req
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

citate_url = "http://castlots.org/generator-citat-online/"
rifma_url = "http://castlots.org/podbor-rifmi-k-slovu/"
anecdote_url = "http://castlots.org/generator-anekdotov-online/"
driver_citate = webdriver.Chrome()
driver_rifma = webdriver.Chrome()
driver_anecdote = webdriver.Chrome()

driver_citate.get(citate_url)
driver_rifma.get(rifma_url)
driver_anecdote.get(anecdote_url)

citate_button = driver_citate.find_element("class name", "random-button")
anecdote_button = driver_anecdote.find_element("class name", "random-button")

citate_button.click()
anecdote_button.click()

bot = tb.TeleBot(bot_token)
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Я мультизадачный бот!")


@bot.message_handler(regexp = r'/citate')
def citate_message(message):
    bot.send_message(message.chat.id, "Понял")
    citate_button.click()
    text = BeautifulSoup(driver_citate.page_source, features="lxml.parser")
    text = text.find("div", "citata")
    text = text.text
    print(text)
    bot.send_message(message.chat.id, text)
@bot.message_handler(regexp = r'/anecdote')
def anecdote_message(message):
    bot.send_message(message.chat.id, "Понял")
    anecdote_button.click()
    text = BeautifulSoup(driver_anecdote.page_source, features="lxml.parser")
    text = text.find("div", "anekdot")
    text = text.text
    print(text)
    bot.send_message(message.chat.id, text)
    
@bot.message_handler(regexp = r'/describe')
def describe_message(message):
    bot.send_message(message.chat.id, "Понял")
    text = citate_url, rifma_url,anecdote_url
    print(text)
    bot.send_message(message.chat.id, text)


bot.infinity_polling()
