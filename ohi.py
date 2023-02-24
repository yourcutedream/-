import telebot
from telebot import types
import openpyxl

wb = openpyxl.reader.excel.load_workbook(filename="102.xlsx")
sheet=wb.active


TOKEN = '5752244568:AAEAJ1LiLXMxFXoDZq9tZ_rIiv2wCPE1Zg8'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True) #создание новых кнопок
    item1 = types.KeyboardButton('Расписание')
    item2 = types.KeyboardButton('Мотиватор')

    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Приветствую, Хомосапиенс! Что Вам угодно?', parse_mode='Markdown', reply_markup=markup)#ответ бота

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Мотиватор':
        bot.send_message(message.from_user.id, 'Иди работай!!!', parse_mode='Markdown')
    elif message.text == 'Расписание':
       bot.send_message(message.from_user.id, "Привет, какой класс тебя интересует?")
       bot.register_next_step_handler(message,klass)
    else:
        bot.send_message(message.from_user.id, "Чтобы получить уроки, напиши: Расписание")


def klass(message):
    if (message.text == "10а") or (message.text == '10А') or (message.text == '10 А') or (message.text == '10 а'):
        bot.send_message(message.from_user.id, "Какой день недели?(формат две буквы)")
        bot.register_next_step_handler(message,raspis);
    elif (message.text == "10б") or (message.text == '10Б') or (message.text == '10 Б') or (message.text == '10 б'):
        bot.send_message(message.from_user.id, "Какой день недели?(формат две буквы)")
        bot.register_next_step_handler(message,raspis1);
    elif (message.text == "5а") or (message.text == '5А') or (message.text == '5 А') or (message.text == '5 а'):
        bot.send_message(message.from_user.id, "Какой день недели?(формат две буквы)")
        bot.register_next_step_handler(message,raspis2);
    elif (message.text == "4а") or (message.text == '4А') or (message.text == '4 а') or (message.text == '4 А'):
        bot.send_message(message.from_user.id, "Какой день недели?(формат две буквы)")
        bot.register_next_step_handler(message,raspis3);
    elif (message.text == "5б") or (message.text == '5Б') or (message.text == '5 Б') or (message.text == '5 б'):
        bot.send_message(message.from_user.id, "Какой день недели?(формат две буквы)")
        bot.register_next_step_handler(message,raspis4);
    elif (message.text == "3а") or (message.text == '3А') or (message.text == '3 а') or (message.text == '4 А'):
        bot.send_message(message.from_user.id, "Какой день недели?(формат две буквы)")
        bot.register_next_step_handler(message,raspis5);
    elif (message.text == "6а") or (message.text == '6А') or (message.text == '6 А') or (message.text == '6 а'):
        bot.send_message(message.from_user.id, "Какой день недели?(формат две буквы)")
        bot.register_next_step_handler(message,raspis6);
    elif (message.text == "7а") or (message.text == '7А') or (message.text == '7 А') or (message.text == '7 а'):
        bot.send_message(message.from_user.id, "Какой день недели?(формат две буквы)")
        bot.register_next_step_handler(message,raspis7);
    elif (message.text == "8а") or (message.text == '8А') or (message.text == '8 А') or (message.text == '8 а'):
        bot.send_message(message.from_user.id, "Какой день недели?(формат две буквы)")
        bot.register_next_step_handler(message,raspis8);
    elif (message.text == "9а") or (message.text == '9А') or (message.text == '9 А') or (message.text == '9 а'):
        bot.send_message(message.from_user.id, "Какой день недели?(формат две буквы)")
        bot.register_next_step_handler(message,raspis9);
    elif (message.text == "11а") or (message.text == '11А') or (message.text == '11 А') or (message.text == '11 а'):
        bot.send_message(message.from_user.id, "Какой день недели?(формат две буквы)")
        bot.register_next_step_handler(message,raspis10);
    else:
        bot.send_message(message.from_user.id, "Неверный формат")


def raspis(message):
    if (message.text == "Пн") or (message.text == 'пн') :
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+1][0].value))
            
   # else:
        #bot.send_message(message.from_user.id, "Неверный формат");
    if (message.text == "Вт") or (message.text.strip() == 'вт'):
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+1][1].value))
                
    if (message.text == "Ср") or (message.text.strip() == 'ср'):
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+1][2].value))
                
    if (message.text == "Чт") or (message.text.strip() == 'чт'):
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+1][3].value))
    
    if (message.text == "Пт") or (message.text.strip() == 'пт'):
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+1][4].value))


def raspis1(message):
    if (message.text == "Пн") or (message.text == 'пн') :
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+13][0].value))
            
   # else:
        #bot.send_message(message.from_user.id, "Неверный формат");
    if (message.text == "Вт") or (message.text.strip() == 'вт'):
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+13][1].value))
                
    if (message.text == "Ср") or (message.text.strip() == 'ср'):
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+13][2].value))
                
    if (message.text == "Чт") or (message.text.strip() == 'чт'):
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+13][3].value))
    
    if (message.text == "Пт") or (message.text.strip() == 'пт'):
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+13][4].value))
    

def raspis2(message):
    if (message.text == "Пн") or (message.text == 'пн') :
            for i in range(1,8):
                bot.send_message(message.chat.id,(sheet[i+25][0].value))
            
   # else:
        #bot.send_message(message.from_user.id, "Неверный формат");
    if (message.text == "Вт") or (message.text.strip() == 'вт'):
            for i in range(1,8):
                bot.send_message(message.chat.id,(sheet[i+25][1].value))
                
    if (message.text == "Ср") or (message.text.strip() == 'ср'):
            for i in range(1,8):
                bot.send_message(message.chat.id,(sheet[i+25][2].value))
                
    if (message.text == "Чт") or (message.text.strip() == 'чт'):
            for i in range(1,8):
                bot.send_message(message.chat.id,(sheet[i+25][3].value))
    
    if (message.text == "Пт") or (message.text.strip() == 'пт'):
            for i in range(1,8):
                bot.send_message(message.chat.id,(sheet[i+25][4].value))
                
                
def raspis3(message):
    if (message.text == "Пн") or (message.text == 'пн') :
            for i in range(1,8):
                bot.send_message(message.chat.id,(sheet[i+25][0].value))
            
   # else:
        #bot.send_message(message.from_user.id, "Неверный формат");
    if (message.text == "Вт") or (message.text.strip() == 'вт'):
            for i in range(1,8):
                bot.send_message(message.chat.id,(sheet[i+49][1].value))
                
    if (message.text == "Ср") or (message.text.strip() == 'ср'):
            for i in range(1,8):
                bot.send_message(message.chat.id,(sheet[i+49][2].value))
                
    if (message.text == "Чт") or (message.text.strip() == 'чт'):
            for i in range(1,8):
                bot.send_message(message.chat.id,(sheet[i+49][3].value))
    
    if (message.text == "Пт") or (message.text.strip() == 'пт'):
            for i in range(1,8):
                bot.send_message(message.chat.id,(sheet[i+49][4].value))            

def raspis4(message):
    if (message.text == "Пн") or (message.text == 'пн') :
            for i in range(1,8):
                bot.send_message(message.chat.id,(sheet[i+37][0].value))
            
   # else:
        #bot.send_message(message.from_user.id, "Неверный формат");
    if (message.text == "Вт") or (message.text.strip() == 'вт'):
            for i in range(1,8):
                bot.send_message(message.chat.id,(sheet[i+37][1].value))
                
    if (message.text == "Ср") or (message.text.strip() == 'ср'):
            for i in range(1,8):
                bot.send_message(message.chat.id,(sheet[i+37][2].value))
                
    if (message.text == "Чт") or (message.text.strip() == 'чт'):
            for i in range(1,8):
                bot.send_message(message.chat.id,(sheet[i+37][3].value))
    
    if (message.text == "Пт") or (message.text.strip() == 'пт'):
            for i in range(1,8):
                bot.send_message(message.chat.id,(sheet[i+37][4].value))

def raspis5(message):
    if (message.text == "Пн") or (message.text == 'пн') :
            for i in range(1,8):
                bot.send_message(message.chat.id,(sheet[i+61][0].value))
            
   # else:
        #bot.send_message(message.from_user.id, "Неверный формат");
    if (message.text == "Вт") or (message.text.strip() == 'вт'):
            for i in range(1,8):
                bot.send_message(message.chat.id,(sheet[i+61][1].value))
                
    if (message.text == "Ср") or (message.text.strip() == 'ср'):
            for i in range(1,8):
                bot.send_message(message.chat.id,(sheet[i+61][2].value))
                
    if (message.text == "Чт") or (message.text.strip() == 'чт'):
            for i in range(1,8):
                bot.send_message(message.chat.id,(sheet[i+61][3].value))
    
    if (message.text == "Пт") or (message.text.strip() == 'пт'):
            for i in range(1,8):
                bot.send_message(message.chat.id,(sheet[i+61][4].value))

def raspis6(message):
    if (message.text == "Пн") or (message.text == 'пн') :
            for i in range(1,8):
                bot.send_message(message.chat.id,(sheet[i+73][0].value))
            
   # else:
        #bot.send_message(message.from_user.id, "Неверный формат");
    if (message.text == "Вт") or (message.text.strip() == 'вт'):
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+73][1].value))
                
    if (message.text == "Ср") or (message.text.strip() == 'ср'):
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+73][2].value))
                
    if (message.text == "Чт") or (message.text.strip() == 'чт'):
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+73][3].value))
    
    if (message.text == "Пт") or (message.text.strip() == 'пт'):
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+73][4].value))

def raspis7(message):
    if (message.text == "Пн") or (message.text == 'пн') :
            for i in range(1,8):
                bot.send_message(message.chat.id,(sheet[i+85][0].value))
            
   # else:
        #bot.send_message(message.from_user.id, "Неверный формат");
    if (message.text == "Вт") or (message.text.strip() == 'вт'):
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+85][1].value))
                
    if (message.text == "Ср") or (message.text.strip() == 'ср'):
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+85][2].value))
                
    if (message.text == "Чт") or (message.text.strip() == 'чт'):
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+85][3].value))
    
    if (message.text == "Пт") or (message.text.strip() == 'пт'):
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+85][4].value))

def raspis8(message):
    if (message.text == "Пн") or (message.text == 'пн') :
            for i in range(1,8):
                bot.send_message(message.chat.id,(sheet[i+97][0].value))
            
   # else:
        #bot.send_message(message.from_user.id, "Неверный формат");
    if (message.text == "Вт") or (message.text.strip() == 'вт'):
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+97][1].value))
                
    if (message.text == "Ср") or (message.text.strip() == 'ср'):
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+97][2].value))
                
    if (message.text == "Чт") or (message.text.strip() == 'чт'):
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+97][3].value))
    
    if (message.text == "Пт") or (message.text.strip() == 'пт'):
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+97][4].value))

def raspis9(message):
    if (message.text == "Пн") or (message.text == 'пн') :
            for i in range(1,8):
                bot.send_message(message.chat.id,(sheet[i+109][0].value))
            
   # else:
        #bot.send_message(message.from_user.id, "Неверный формат");
    if (message.text == "Вт") or (message.text.strip() == 'вт'):
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+109][1].value))
                
    if (message.text == "Ср") or (message.text.strip() == 'ср'):
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+109][2].value))
                
    if (message.text == "Чт") or (message.text.strip() == 'чт'):
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+109][3].value))
    
    if (message.text == "Пт") or (message.text.strip() == 'пт'):
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+109][4].value))

def raspis10(message):
    if (message.text == "Пн") or (message.text == 'пн') :
            for i in range(1,8):
                bot.send_message(message.chat.id,(sheet[i+121][0].value))
            
   # else:
        #bot.send_message(message.from_user.id, "Неверный формат");
    if (message.text == "Вт") or (message.text.strip() == 'вт'):
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+121][1].value))
                
    if (message.text == "Ср") or (message.text.strip() == 'ср'):
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+121][2].value))
                
    if (message.text == "Чт") or (message.text.strip() == 'чт'):
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+121][3].value))
    
    if (message.text == "Пт") or (message.text.strip() == 'пт'):
            for i in range(1,9):
                bot.send_message(message.chat.id,(sheet[i+121][4].value))

    
bot.polling(none_stop=True, interval=0)
