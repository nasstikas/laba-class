import telebot
from telebot import types

token = '6734969287:AAFbb1CPxBdrMKlwg5dIXu0ZJUs4Ji1Rdq8'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("привет")
    btn2 = types.KeyboardButton("кд чд")
    btn3 = types.KeyboardButton("хсе мемы")
    btn4 = types.KeyboardButton("бабуле")
    btn5 = types.KeyboardButton("сэд муд")
    btn6 = types.KeyboardButton("твоему крашу")
    btn7 = types.KeyboardButton("ругань")
    btn8 = types.KeyboardButton("споки")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)    
    bot.send_message(m.chat.id, 'приветик, {0.first_name}! здесь ты можешь найти картинки на любой случай жизни.\nвыбери, картинка какой категории тебе нужна'.format(m.from_user), reply_markup=markup)    
    
@bot.message_handler(content_types=["text","stiker"])
def handle_text(m):
    if m.text == "кд чд":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("к категориям")
        markup.add(back)        
        bot.send_media_group(m.chat.id,[telebot.types.InputMediaPhoto("https://sun9-1.userapi.com/impg/eMsPGcNKOtOhJiUeNTuNS0vraAKtNVQUTh488Q/1YplOw1qLHI.jpg?size=1080x1243&quality=96&sign=b27c58f3c55544894fbfcf4d2f2f52eb&type=album"), telebot.types.InputMediaPhoto("https://sun9-62.userapi.com/impg/7Ml_a-RLUnf-yinS1dEaDF2cYQ1RjFmMeK9zWQ/zMGR71kUSzM.jpg?size=286x267&quality=95&sign=95238d7b8a6c1e468467401b47b9c317&type=album")])
        bot.send_message(m.chat.id, text="можешь посмотреть другие категории картинок", reply_markup=markup)
        
        
    elif m.text == "бабуле":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("с днем рождения")
        btn2 = types.KeyboardButton("с новым годом")
        btn3 = types.KeyboardButton("другие праздники")
        markup.add(btn1, btn2, btn3)
        bot.send_message(m.chat.id, text="выбери подкатегорию солнце)", reply_markup=markup) 
        
    elif m.text == "":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("к категориям")
        markup.add(back)         
        bot.send_media_group(m.chat.id,[telebot.types.InputMediaPhoto(""), telebot.types.InputMediaPhoto(""), telebot.types.InputMediaPhoto(""), telebot.types.InputMediaPhoto(""), telebot.types.InputMediaPhoto(""), telebot.types.InputMediaPhoto("")])
        bot.send_message(m.chat.id, text="можешь посмотреть другие категории картинок", reply_markup=markup)
          
    elif m.text == "":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("к категориям")
        markup.add(back)         
        bot.send_media_group(m.chat.id,[telebot.types.InputMediaPhoto(""), telebot.types.InputMediaPhoto(""), telebot.types.InputMediaPhoto(""), telebot.types.InputMediaPhoto(""), telebot.types.InputMediaPhoto(""), telebot.types.InputMediaPhoto("")])
        bot.send_message(m.chat.id, text="можешь посмотреть другие категории картинок", reply_markup=markup)  
        
    elif m.text == "":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("к категориям")
        markup.add(back)         
        bot.send_media_group(m.chat.id,[telebot.types.InputMediaPhoto(""), telebot.types.InputMediaPhoto(""), telebot.types.InputMediaPhoto(""), telebot.types.InputMediaPhoto(""), telebot.types.InputMediaPhoto(""), telebot.types.InputMediaPhoto("")])
        bot.send_message(m.chat.id, text="можешь посмотреть другие категории картинок", reply_markup=markup)    
        
    elif (m.text == "к категориям"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("привет")
        btn2 = types.KeyboardButton("кд чд")
        btn3 = types.KeyboardButton("хсе мемы")
        btn4 = types.KeyboardButton("бабуле")
        btn5 = types.KeyboardButton("сэд муд")
        btn6 = types.KeyboardButton("твоему крашу")
        btn7 = types.KeyboardButton("ругань")
        btn8 = types.KeyboardButton("споки")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8) 
        bot.send_message(m.chat.id, text="менюшка", reply_markup=markup)

bot.polling(none_stop=True, interval=0)