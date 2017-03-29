#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import random
from telebot import types
import time
import datetime
import os
import threading
import urllib2
from bs4 import BeautifulSoup
import requests
from bs4 import *



TOKEN = '315919476:AAF7LcDtNpl2AP8GJuizGlrh0rAqfOJxock'
pole = 0
bot = telebot.TeleBot(TOKEN)
now = datetime.datetime.now()
def boton(messages):
    for msg in messages:
        user = msg.from_user.username
        cid = msg.chat.id
        if msg.text == '!kvothe':
            bot.reply_to(msg, "el que te pone to palote")
        elif msg.text == '!audio':
            rndvoice = random.choice([open('./audio/voz1.ogg', 'rb'), open('./audio/iscdildo.ogg', 'rb'), open('./audio/laslolis.ogg', 'rb'), open('./audio/megustan.ogg', 'rb')])
            bot.send_voice(cid, rndvoice)
            bot.send_voice(cid, "FILEID")
        elif msg.text == '!petada':
            petada = open('./audio/petada.ogg', 'rb')
            bot.send_voice(cid, petada)
            bot.send_voice(cid, "FILEID")
        elif msg.text == '@JuanmaHL':
            bot.reply_to(msg, "Mi creador <3")
        elif msg.text == '!boton':
            bot.reply_to(msg, user + " es subnormal")
        elif msg.text == '!ayuda':
            with open("ayuda.txt", mode="r") as ayuda:
              bot.reply_to(msg, ayuda)
        elif msg.text == '!dildo':
            url = "http://seguimientochinapost.com/result_china.php?order_no=RJ011020672CN"
            r = requests.get(url)
            html_content = r.text
            soup = BeautifulSoup(html_content, "html.parser")
            tabla = soup.findAll("table")
            for tr in tabla[2].findAll("tr"):
                for col in tr.findAll("td"):
                    bot.reply_to(msg, col.getText())
@bot.message_handler(commands=['historia'])
def resp_pole(msg):
    user = msg.from_user.username
    rnd1 = random.choice(["empezo a escribir un libro sobre zoofilia", "se aficiono al parchis online", "estaba tranquilamente en la jurisdiccion del surtidor"])
    rnd2 = random.choice(["cuando vio a willyrex", "cuando encontro su dignidad", "mientras salvaba el mundo de Salvador Raya"])
    rnd3 = random.choice(["y vio la oportunidad de tirarle la red", "y fue secuestrado por Nestor para su club de virgenes", "y se fue a tomar por culo"])
    bot.reply_to(msg, user + " " + rnd1 + ", " + rnd2 + ", " + rnd3)

@bot.message_handler(commands=['pole'])
def resp_pole(msg):
    bot.reply_to(msg, "A la proxima te baneo payaso")

@bot.message_handler(commands=['chiste'])
def chiste(msg):
  with open("chistes.txt", mode="r") as myFile:
    lines = myFile.readlines()

  random.shuffle(lines)
  bot.reply_to(msg, lines)

bot.set_update_listener(boton)
bot.polling(none_stop=True)
