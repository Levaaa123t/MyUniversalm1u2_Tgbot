from config import token
import telebot
import time
from random import choice


API_TOKEN = token

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, """\
Привет, я телеграм бот! Я повторяю написанные тобой сообщения и выполняю некоторые команды, напиши /help для информации\
""")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, """\
У меня есть такие команды: /quote; /fact; /stupid_fact\
""")

@bot.message_handler(commands=['quote'])
def quote(message):
    quotes = choice(["Счастье — это не нечто готовое. Счастье зависит только от ваших действий", 
                     "Не так важно то, что вы получите, достигнув своих целей, как то, кем вы станете, сделав это.",
                     'Вы никогда не пересечёте океан, если не наберётесь мужества потерять берег из виду.',
                     'Начинайте делать всё, что вы можете сделать, и даже то, о чём можете хотя бы мечтать. В смелости — гений, сила и магия.'
                     ])
    bot.reply_to(message, f'Ваша цитата дня: {quotes}')

@bot.message_handler(commands=['fact'])
def fact(message):
    facts = choice(['Осьминоги имеют три сердца. Два из них прокачивают кровь через жабры, а третье — по всему телу. Когда осьминог плавает, одно из сердец перестает работать, что делает плавание для него утомительным.',
                    'Скорость света в алмазе в 2,5 раза медленнее, чем в вакууме. Алмазы настолько плотные, что замедляют свет, проходящий через них.',
                    'Бананы — это ягоды, а вот клубника — нет. В ботаническом смысле ягода — это плод с семенами внутри, что подходит для бананов, но не для клубники, чьи семена расположены снаружи.',
                    'Самая большая пещера в мире — Сон Дунг во Вьетнаме. В ней может поместиться целый квартал с небоскрёбами, а внутри есть собственные реки и леса!'
                    ])
    bot.reply_to(message, f'Интересный факт: {facts}')
@bot.message_handler(commands=['stupid_fact'])
def stupid_fact(message):
    stupid_facts = choice(['Мыши не любят сыр. Поп-культура нас обманывала! На самом деле мыши предпочитают сладости, как орехи или фрукты.',
                           'Примерно через 2,3 миллиарда лет, на Земле скорее всего что-то произойдет.',
                           'Если бы вы кричали на арбуз 8 лет, 7 месяцев и 6 дней, то скорее всего ничего бы не произошло',
                           'Ленивцы слишком ленивы, чтобы ходить в туалет. Они делают это раз в неделю, и для них это настоящее событие!'
                           ])
    bot.reply_to(message,f'Глупый факт: {stupid_facts}')
@bot.message_handler(content_types=['text'])
def usmessage(message):
    if message.text == 'Привет' or 'привет':
        bot.reply_to(message, """\
        Привет👋, напиши команду /help чтобы посмотреть мои команды. \
        """)

    




@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)



    


bot.infinity_polling()