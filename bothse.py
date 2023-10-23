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
    def handle_text(m):
    elif m.text == "привет":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("к категориям")
        markup.add(back)        
        bot.send_media_group(m.chat.id,[telebot.types.InputMediaPhoto("https://sun9-53.userapi.com/impg/aCiTgRIXkL667WoudqGaMmu5q6lYWwnhRmiQNA/ElWFTwkechc.jpg?size=604x604&quality=95&sign=5a8b24d096041f4095bb7e11d5ad269f&type=album "), telebot.types.InputMediaPhoto("https://sun9-72.userapi.com/impg/XA-Xa7aFgDe5tN-xJ8CbGQgJMbdwR3Pf5IpbFA/MsAfD9exmGw.jpg?size=265x253&quality=95&sign=3df7f677291b9f8befa89a440a0c30df&type=album "),telebot.types.InputMediaPhoto("https://sun9-76.userapi.com/impg/qbm3bK1UFMoWWKkZttnQ3Ba0QOzeOPDgORG0Eg/avSSOCIroaw.jpg?size=736x742&quality=96&sign=031d4eaab79d0d817f838ca79edbc3e4&type=album "),telebot.types.InputMediaPhoto("https://sun9-61.userapi.com/impg/iuXP1k09V7NqIXFIdrYVbhANlm4mmPOXObX0QQ/vGM786VL7nA.jpg?size=1280x1280&quality=96&sign=a87203ec25133eb9f2c582802570ea30&type=album "),telebot.types.InputMediaPhoto("https://sun9-27.userapi.com/impg/fWq9ZmhFfDEdtyxjuND2lQrQSTbd0P6skjuq2w/qCumULmx988.jpg?size=240x320&quality=96&sign=669ca518e50f5b8f917a37ed8a7a85a1&type=album "),telebot.types.InputMediaPhoto("https://sun9-5.userapi.com/impg/w0Njafua3z53sBYWb4HPtpCdkTJT3HNcLweZFg/rhLvnMj2kRI.jpg?size=604x604&quality=96&sign=83874e44d25fe9d9ef4afbae4218a90f&type=album "),telebot.types.InputMediaPhoto("https://sun9-36.userapi.com/impg/olb0LjEf0c76ECknE-sYFC73HeHgRNU24ukIWg/aikQrSCFL08.jpg?size=1280x1280&quality=96&sign=93afe025914047f28c01e83b0d16b247&type=album "),telebot.types.InputMediaPhoto("https://sun9-5.userapi.com/impg/_WSU4dVEvWDvQ1pRV4YivjwkgxRlDjBaN9E-Vg/0liu-ICWR30.jpg?size=735x794&quality=96&sign=3ca5ed617863f43a0b8e66576466b734&type=album "),telebot.types.InputMediaPhoto("https://sun9-41.userapi.com/impg/0tdPItkyr6UYHtV_HU38kd4Q5smEnVvD1f05_A/Mo23i0Xbvhs.jpg?size=480x360&quality=96&sign=d68e1e19f78f00cf5eff53a6fff2bda7&type=album "),telebot.types.InputMediaPhoto("https://sun9-37.userapi.com/impg/dXNyCBSdcQmw5hyurEQnhw9wsFJEisFRilR6Sw/z7ZXoBWSpyM.jpg?size=700x577&quality=96&sign=5db4d121a236d3b94afb4c84d8a0ed76&type=album ")])
        bot.send_message(m.chat.id, text="можешь посмотреть другие категории картинок", reply_markup=markup)
    elif m.text == "споки":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("к категориям")
        markup.add(back)  
        bot.send_media_group(m.chat.id,[telebot.types.InputMediaPhoto("https://sun9-68.userapi.com/impg/qFtSpYy3UCu2p70TJFaotWrKQyjeqYHjNa7RaQ/OM91Jni6XAA.jpg?size=735x490&quality=95&sign=4aea3fbfe38a377e3d28985c78e00d19&type=album "), telebot.types.InputMediaPhoto("https://sun9-14.userapi.com/impg/_0cg_RdsIEqtMvDbb98nW85OLlNy2oXXCwLcsw/7nH9u5sA_pw.jpg?size=736x736&quality=95&sign=7165520980286973c717bb600085430d&type=album "),telebot.types.InputMediaPhoto("https://sun9-41.userapi.com/impg/j8WeqWBgnnhKG72-a910SjWEYq8yrK9hBT7-KA/kVQBGQWb0hU.jpg?size=736x736&quality=95&sign=4380d3949e754adf99590dd0ca088724&type=album "),telebot.types.InputMediaPhoto("https://sun9-77.userapi.com/impg/oJk0i6Juxevlqrj_uKpkZCGHkCvjq9iuJlhPdA/-234_dACKa4.jpg?size=802x1000&quality=95&sign=4e9a17ea35026ea36750b3dcce47be37&type=album "),telebot.types.InputMediaPhoto("https://sun9-11.userapi.com/impg/QbJyTsrZsor7mB-FVvEiEsoeZOW8FyV1rYW-FQ/V-n-G7PQUrw.jpg?size=800x800&quality=95&sign=8913842e46e91697ac51dfbbf7b28834&type=album "),telebot.types.InputMediaPhoto("https://sun9-14.userapi.com/impg/xNDUIR6F6UErS1rj3CRsxUCZT5ug4O7GiR5MQA/ptNtLGzsUZc.jpg?size=736x523&quality=95&sign=6c70590a49d860c7020fae828cd2396e&type=album "),telebot.types.InputMediaPhoto("https://sun9-14.userapi.com/impg/HyL93AexZOSP9h0Sg7nrVsiGfa_R_mnyhwQ1_w/bw0_FZoQBsg.jpg?size=533x416&quality=95&sign=80d88ba2d5b61771b66ed05fbf0ee4e1&type=album "),telebot.types.InputMediaPhoto("https://sun9-54.userapi.com/impg/g6QBkd6duMZ38Gah5guRVHouLndptATmObqxqw/BCthWVwhT6s.jpg?size=736x736&quality=95&sign=d5fee318c15a6f50df90c90d2fc406ad&type=album "),telebot.types.InputMediaPhoto("https://sun9-41.userapi.com/impg/kTKejsxwTo0-mHXf_PaQTGIDESs29AMFBGDf4w/NoM7_FIXJd0.jpg?size=720x946&quality=95&sign=1c792dd750a2dc3ea3a87b10730d3411&type=album "),telebot.types.InputMediaPhoto("https://sun9-68.userapi.com/impg/UpFmqW2mNlSRuSR335y4HyOzF2EMLoZ1UhffFQ/y7ruAQs8ttw.jpg?size=736x736&quality=95&sign=fd616f6d768ed0e44547b6f3bc1dde8f&type=album ")])
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
    elif m.text == "ругань":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("к категориям")
        markup.add(back) 
        bot.send_media_group(m.chat.id,[telebot.types.InputMediaPhoto("https://sun9-1.userapi.com/impg/pQmVaCyelXqz83oaLyDG--sOAjKUzQN0qYU_dA/UQSfhHmx2oc.jpg?size=1472x1472&quality=95&sign=c1ed1f536cb30f64c9b02aadef9de56b&type=album"), telebot.types.InputMediaPhoto("https://sun9-56.userapi.com/impg/9O_Di8hb9K8YrFrC1Ua6IiRgJaVxVbHYAbQRIg/TmJ3Frc3zfg.jpg?size=782x782&quality=95&sign=ab989ee508c2e63372ec519b62923495&type=album"), telebot.types.InputMediaPhoto("https://sun9-63.userapi.com/impg/Umx3HMt3sbjO8myOBykmWbayaDWoFJ9yJmr87Q/PVZm6Du7yvw.jpg?size=720x658&quality=95&sign=24b93e17e84eb6aa484eb03500c8066e&type=album"),telebot.types.InputMediaPhoto("https://sun9-32.userapi.com/impg/frkFRcbmzDMSjZmxj4hIlLpQgt7wCVftducQMQ/FZiH9yQVqpg.jpg?size=749x755&quality=95&sign=4f622875e5faaf1e9830848fd0688f73&type=album"),telebot.types.InputMediaPhoto("https://sun9-71.userapi.com/impg/MgD_jKst-3SFViZG6JBVMa-ja8aCS1JXJWKdCw/DMd0xwl02SU.jpg?size=451x438&quality=95&sign=a1a8d4d454869c36e4dde063e9bc7f86&type=album"),telebot.types.InputMediaPhoto("https://sun9-64.userapi.com/impg/UryNt57r5ZlZ7j2YyMVeuVDM0tnf6TNqAihxsQ/ZyLqR7eX19M.jpg?size=600x600&quality=95&sign=b1fba58e551dd091740bbc36e5f9c040&type=album"),telebot.types.InputMediaPhoto("https://sun9-32.userapi.com/impg/iBLZmJLRWg1ko5Ui5VO3yQCdSgu_1zqzF7EYKQ/SqIfGJXvaJE.jpg?size=720x720&quality=95&sign=36ac3570c2f444f93b1d42877e2f147e&type=album"), telebot.types.InputMediaPhoto("https://sun9-35.userapi.com/impg/lXbB7NAg9s1G8bcTkxGrfBDQhD0WHgCbiPSHAw/3hUROijzRng.jpg?size=736x736&quality=95&sign=ebe821cd768c059728fc000ce925216c&type=album"), telebot.types.InputMediaPhoto("https://sun9-50.userapi.com/impg/wLWojs8IfvePhKpV0MvhESntAKdK6VnJ_JAFAg/GY5HvJyDIkc.jpg?size=453x604&quality=95&sign=4930dfe328d4e494e7b9d25fe057d8ae&type=album"), telebot.types.InputMediaPhoto("https://sun9-23.userapi.com/impg/g3lDXfbotmMVDaVwizuKgl1ga4xfFjjzThNz-w/QGtTzbpZYcQ.jpg?size=584x585&quality=95&sign=f72d5ac5823d3a71a2bed8daeb5caeac&type=album")])
        bot.send_message(m.chat.id, text="можешь посмотреть другие категории картинок", reply_markup=markup)
    elif m.text == "твоему крашу":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("к категориям")
        markup.add(back) 
        bot.send_media_group(m.chat.id,[telebot.types.InputMediaPhoto("https://sun9-3.userapi.com/impg/JcrkRVBczdNMSnTb6CccnFpfpHdTJ-cNf7qV4Q/hwtfi7o1Cfw.jpg?size=736x736&quality=95&sign=049cb427400ca1f3cec1895e65e37b45&type=album"), telebot.types.InputMediaPhoto("https://sun9-69.userapi.com/impg/OdyIdHPCwjXHg_XOK56-eyiNAt2rM1CUO8_Kjw/jIQBBjven1Q.jpg?size=736x736&quality=95&sign=7135486f1cb68abd48ff960bbb3080db&type=album"),telebot.types.InputMediaPhoto("https://sun9-70.userapi.com/impg/XCD-ntzxsgQfXuF_-xz8wBzcNw_Zuq7w37i9dw/75JA18tPEDU.jpg?size=730x728&quality=95&sign=21562c880961423e0ba865f7d9e46dc9&type=album"),telebot.types.InputMediaPhoto("https://sun9-77.userapi.com/impg/iG4qVK2Fs4MbhYE5TXRHEiHt8w3GdLtvyeUSwA/VQgIwr7gTDw.jpg?size=748x465&quality=95&sign=b9f583a969c06a2086359fd7cb80d2a0&type=album"),telebot.types.InputMediaPhoto("https://sun9-44.userapi.com/impg/zH-8bzxPlAdfyeEA22YJSKS_Dp7IyBfVhNV2qg/FuAQVTdlhh8.jpg?size=720x475&quality=95&sign=7be4375f3b310a3d841707af2458ff4c&type=album"),telebot.types.InputMediaPhoto("https://sun9-72.userapi.com/impg/BAn0bdLBCFmJJnzogC76P_r59tDUZPifVnATYA/U5L3CVx-Ibw.jpg?size=474x480&quality=95&sign=f34df9476a8213ddf2f01b524470e9eb&type=album"),telebot.types.InputMediaPhoto("https://sun9-57.userapi.com/impg/p0zKtaKzBE1llLv84R06T2OSD-mCC_soXB42tA/Zx33jBhbsug.jpg?size=582x577&quality=95&sign=f301fff0b7a662f233da31d04b4a1e9f&type=album"),telebot.types.InputMediaPhoto("https://sun9-57.userapi.com/impg/M_jxajwr0i8eJrrbbJjIEwWth48ekRXtJSIaOQ/F5UFOaYW9Jk.jpg?size=440x649&quality=95&sign=94aff1614dc1d9d026d6169c8f73574b&type=album"),telebot.types.InputMediaPhoto("https://sun9-62.userapi.com/impg/RR5hVpquTbIpspOBE5T-DpzYtVenkxYKc2v0xw/TyI9Yl7KyMc.jpg?size=736x719&quality=95&sign=ee7448b0e2accb4a20cac84da54a457c&type=album"),telebot.types.InputMediaPhoto("https://sun9-65.userapi.com/impg/53DDs3tn7Z6mVSAEXopxepHiM27LWxz6yaWALQ/vpCBT1ipg9I.jpg?size=593x593&quality=95&sign=d9ab83714fbf9fa7df1fa194d5ed1f6d&type=album")])
        bot.send_message(m.chat.id, text="можешь посмотреть другие категории картинок", reply_markup=markup)    
    if m.text == "сэд муд":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("к категориям")
        markup.add(back)
        bot.send_media_group(m.chat.id,[telebot.types.InputMediaPhoto("https://sun9-58.userapi.com/impg/9e3dfUP3UGHnRGBUWFdgxMRofbOtQVylPRc5Qw/53zq93EfAZY.jpg?size=736x724&quality=95&sign=145038ee5a2153f444cbe5867257790a&type=album"),
        telebot.types.InputMediaPhoto("https://sun9-23.userapi.com/impg/3Ig2RvRoQDcs95SVtimEll-XlSriuVNqO-a-kQ/flPCL7Jvpm4.jpg?size=442x338&quality=95&sign=799ae6902b4c310899b481583086a298&type=album")])
        bot.send_message(m.chat.id, text="можешь посмотреть другие категории картинок", reply_markup=markup)
    elif m.text == "хсе мемы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("к категориям")
        markup.add(back)
        bot.send_media_group(m.chat.id,[telebot.types.InputMediaPhoto("https://sun9-78.userapi.com/impg/R5YB3O5uVa5uVzORco3nV2xAKNFAf94n760UiA/2XTvIRUFYI0.jpg?size=1080x411&quality=95&sign=963f37d63e139098d99a611eebea1e46&type=album"),telebot.types.InputMediaPhoto("https://sun9-57.userapi.com/impg/hFNTZ1R5UsUiAEW_UTowGfaqsm05SSJwhwu9xw/dEmKFfT7GKY.jpg?size=1242x774&quality=95&sign=408b23e065c9eda15685cfbe4465d6e1&type=album"), telebot.types.InputMediaPhoto("https://sun9-45.userapi.com/impg/mkzsYOfE5Frvd-f2WN8dIE_9g3IORIHnC1Q7Rw/2MKJ22Xxtj4.jpg?size=1280x864&quality=95&sign=f9f9c93903604ca675b9207507dacd79&type=album"),
        telebot.types.InputMediaPhoto("https://sun9-71.userapi.com/impg/FJLqs2ggPAcqxcFMB8vGzldzYQFRbZEd1S7FWg/8qJnxLp2W70.jpg?size=598x648&quality=95&sign=e3d79c3bdc1b97d88a2ba9a603ee5dff&type=album")])
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
