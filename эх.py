import telebot
import threading
from time import sleep

TOKEN = '5752244568:AAEAJ1LiLXMxFXoDZq9tZ_rIiv2wCPE1Zg8'
bot = telebot.TeleBot(TOKEN)
delay=5
name='это будущее напоминание(введи)'
ids = []
stop=0
     
@bot.message_handler(commands=['nap'])
def starting(message):
  global stop
  stop=0
  sent_msg = bot.send_message(message.chat.id, 'Введите время в секундах:\n\n(10 минут - 600 сек\n1 час - 3600 сек\n3 часа - 10800 сек\n5 часов - 18000 сек)')
  bot.register_next_step_handler(sent_msg, start_message)
  
def start_message(message):
  global ids
  global delay
  id = message.from_user.id
  ids.append(id)
  delay = int(message.text)
  sent_msg2 = bot.send_message(message.chat.id, 'Введите напоминание:')
  bot.register_next_step_handler(sent_msg2, come_message)

def come_message(message):
  global name
  name=message.text
  bot.send_message(ids[0], 'Вы создали напоминание!')
  bot.register_next_step_handler(name, send_reminder)
  
  
def send_reminder():
  global ids
  global stop
  while True:
    if stop==1:
        break
    for id in ids:
        bot.send_message(id, name)
        sleep(delay)

@bot.message_handler(commands=['stop'])
def stopping(message):
    global stop
    stop=1

t = threading.Thread(target=send_reminder)
t.start()

while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except:
        sleep(10)
