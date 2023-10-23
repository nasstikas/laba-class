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
        bot.send_media_group(m.chat.id,[telebot.types.InputMediaPhoto("https://sun9-11.userapi.com/impg/zoLxhxzHaps298SSv1YEQCn8lICIkZLS9N8g1A/HknEsxdpgIg.jpg?size=736x733&quality=95&sign=35e7d6e39c07dad92cbdbfd98b34187c&type=album"), telebot.types.InputMediaPhoto("https://sun9-10.userapi.com/impg/vFIn9jof3VEtRXtRbps-3NvLWW0_BOTPjJTPNA/tiA3Tn_MW3E.jpg?size=735x683&quality=95&sign=d3aadad4251e729da5f37c03f6614438&type=album"), telebot.types.InputMediaPhoto("https://sun9-34.userapi.com/impg/WhMI9LiLqKxoRndXGUxOijW0-31sMPMOvq-nDA/NQ2meLLcEfs.jpg?size=438x576&quality=95&sign=e4c84cfc828476fb2d8a5553248d1378&type=album"), telebot.types.InputMediaPhoto("https://sun9-66.userapi.com/impg/u2-v4ib6dg4aW2qGoOOqojB4B4xcjlCgBgdpuw/G3_EaCQyYWo.jpg?size=700x700&quality=95&sign=486652dc569fbc6e7b1664ab8954a91e&type=album"), telebot.types.InputMediaPhoto("https://sun9-77.userapi.com/impg/1V0a-lgahlr7MkN-GAdcneWU2VUQwDslD2hNZA/aCyCfEt4b4Y.jpg?size=604x403&quality=95&sign=64f955954dc230ba93ee2690a8ea51cc&type=album"), telebot.types.InputMediaPhoto("https://sun9-29.userapi.com/impg/CCwSry64BycQEZ67tXzPUDMskzXXKajE3BCLCw/7RuZ7Ox1ZEc.jpg?size=604x604&quality=95&sign=b87c3fd79bac3c47d2ec01b9b64b1817&type=album"), telebot.types.InputMediaPhoto("https://sun9-66.userapi.com/impg/QpL74tBds9RJ62pBTghBZJicaBBoSlpyE-CUDQ/sb56fMusdkM.jpg?size=672x576&quality=95&sign=b7229869d35d17c14cb98e43068cb8fa&type=album"), telebot.types.InputMediaPhoto("https://sun9-13.userapi.com/impg/a8TM5AfuwbTO6KNYNP66Vm7J--xjzzz2d9wpUA/VR2jCRl4fKM.jpg?size=735x489&quality=95&sign=9947fc4084b49ad6cb84c878b99540e1&type=album")])
        bot.send_message(m.chat.id, text="можешь посмотреть другие категории картинок", reply_markup=markup)

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
        
    elif m.text == "сэд муд":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("к категориям")
        markup.add(back)
        bot.send_media_group(m.chat.id,[telebot.types.InputMediaPhoto("https://sun9-48.userapi.com/impg/p9TlbzMRjl190hQqMBgWSWC2cDimbDSK_H5PWg/lbiFnyBiMpk.jpg?size=736x735&quality=95&sign=1e2cda3c9b9a16c05259f77ce05c4ef0&type=album"), telebot.types.InputMediaPhoto("https://sun9-63.userapi.com/impg/8zkTwbs4s1ZI3fMCCy_42tN_NDS7y0FEGjI29w/HEEdi11rahI.jpg?size=447x511&quality=95&sign=81a4301a10a63ad4f01ad4f7bc0d2d5b&type=album"), telebot.types.InputMediaPhoto("https://sun9-14.userapi.com/impg/XgEJ0qv0D_T19dhmChSqFziDjpAuCWinTVF-Cw/3N7p4KPhR_c.jpg?size=735x570&quality=95&sign=2741684a394dbfad063d2fffb42f564c&type=album"),telebot.types.InputMediaPhoto("https://sun9-57.userapi.com/impg/4FYBJDtGaeHLzNPk3ouwyy6IuklUEPg9jnmuZg/xty6K8igsT8.jpg?size=650x492&quality=95&sign=bf82522380d7e6e3dc1332164d0a567d&type=album"), telebot.types.InputMediaPhoto("https://sun9-33.userapi.com/impg/qWjfoV52QIrUHOBZGEZaEcFwSLQrfFAG7w0r0w/wAQuQTInHbU.jpg?size=735x461&quality=95&sign=3831d4bcc5a3c31a638e2ebec46e81bc&type=album"), telebot.types.InputMediaPhoto("https://sun9-52.userapi.com/impg/98c3Z3EqNoKhZA5-lPdEwZLvtfFqNrwgD9t7fg/56aOwJjTfBA.jpg?size=736x733&quality=95&sign=583aa5ed0c8fefbbaf7aef0555469437&type=album"),telebot.types.InputMediaPhoto("https://sun9-1.userapi.com/impg/tGz6EIUL8KWpIU4LKSWo7aVPHgsj3vvquilAMg/F1ZJzGC4bXg.jpg?size=1280x960&quality=95&sign=a5e83ce67e2f44d47715100b1019eae7&type=album"), telebot.types.InputMediaPhoto("https://sun9-58.userapi.com/impg/Nf-6jXSBQPfQJWUcUA2A-vmBdM6ZaBytHgKPhA/6urW80PGbsY.jpg?size=604x494&quality=95&sign=01b1e9422af71adab7ca796b97dc04c9&type=album"), telebot.types.InputMediaPhoto("https://sun9-80.userapi.com/impg/8RVDx8Fjs0oQf-ZJ_1OklyWMhbJiGRxD_4OQ6Q/XpbAkT1j5_c.jpg?size=735x599&quality=95&sign=e83193710d806f987c10e9a6db436422&type=album")])
        bot.send_message(m.chat.id, text="можешь посмотреть другие категории картинок", reply_markup=markup)
        
    elif m.text == "хсе мемы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("к категориям")
        markup.add(back)
        bot.send_media_group(m.chat.id, [telebot.types.InputMediaPhoto("https://sun9-18.userapi.com/impg/aHfbT_AAfBm-gE6ZsHDagFCJ7rAeLipqJaDm_Q/TvARCScaphY.jpg?size=1280x1280&quality=95&sign=12a4794a868f4309d337dd43703ff19a&type=album"), telebot.types.InputMediaPhoto("https://sun9-71.userapi.com/impg/y0a9MkPwnJ92S97k0Y4LNrOXg10kc_tll2nOJA/2ostrBtM7JQ.jpg?size=799x1280&quality=95&sign=444fdd5f2790d2affe3b0546f91e2b65&type=album"), telebot.types.InputMediaPhoto("https://sun9-61.userapi.com/impg/XK7X6CE2uOTfUaO58A3ipbeVhZh14FkIXT367w/LDAJOkyUETM.jpg?size=750x518&quality=95&sign=2a4c453dcc0fe7f2f330089a5a6334db&type=album"), telebot.types.InputMediaPhoto ("https://sun9-16.userapi.com/impg/jZKp0vWnbA3WIs8pjVdx3TnfGxKaE5vfUw4_dA/eBuAEUHv8II.jpg?size=640x702&quality=95&sign=44a4924a14c6638841d6817f9523d223&type=album"),telebot.types.InputMediaPhoto("https://sun9-46.userapi.com/impg/JXfHWuGqnxiICmU5s_k450t3WK6NacyqCFTfuQ/lXGG8xGOFeU.jpg?size=828x912&quality=95&sign=59ec2d7f1185211888fac80073c55edc&type=album"), telebot.types.InputMediaPhoto("https://sun9-22.userapi.com/impg/L7fyO1RIjtDf6-etY3NhW28ua8LDNr5a_drtUA/g2---lFRHP8.jpg?size=828x558&quality=95&sign=a3c392238d3ca25d16b47217a61f6c1a&type=album"), telebot.types.InputMediaPhoto("https://sun9-76.userapi.com/impg/biAmEneUZ_mwW_04jQReTTJWaYaNDGKCUqBaiw/NxuK0DV7vPI.jpg?size=828x376&quality=95&sign=96a1d856923f636e63c45dea3e3c8e44&type=album"), telebot.types.InputMediaPhoto("https://sun59-1.userapi.com/impg/e4kx-Mqb2XAKrfNuo9Y1bv4FXru2a9j4uqAdIw/Ur0S39n_bcg.jpg?size=827x873&quality=95&sign=691a7edeb4ddfc9b4fa8654e4ade3ceb&type=album"), telebot.types.InputMediaPhoto("https://sun9-33.userapi.com/impg/h1LeHF0ne8uzoG1SU88vVGoudmCFytwPHehapA/ASvPCH8EIjI.jpg?size=750x742&quality=95&sign=d1c7af4033811155f1c567dedfad1cab&type=album")])
        bot.send_message(m.chat.id, text="можешь посмотреть другие категории картинок", reply_markup=markup)   

    elif m.text == "бабуле":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("с днем рождения")
        btn2 = types.KeyboardButton("с новым годом")
        btn3 = types.KeyboardButton("другие праздники")
        markup.add(btn1, btn2, btn3)
        bot.send_message(m.chat.id, text="выбери подкатегорию солнце)", reply_markup=markup) 
        
    elif m.text == "с днем рождения":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("к категориям")
        markup.add(back)         
        bot.send_media_group(m.chat.id,[telebot.types.InputMediaPhoto("https://sun9-34.userapi.com/impg/naLumnnEnZ4M-zoyWjoXkJe-UJTNAK2dU_i6Rg/-jxfbeoqbhU.jpg?size=888x888&quality=95&sign=5d86bfc89ccd2d4a436689219160077c&type=album"), telebot.types.InputMediaPhoto("https://sun9-14.userapi.com/impg/8cBs3PhlOl5W72aF9WTPmOiqQZtVixPuQ4jc8w/g9TX-bETo6M.jpg?size=700x934&quality=95&sign=4ea8620c5fe60501e9c53669c98e86a9&type=album"), telebot.types.InputMediaPhoto("https://sun9-21.userapi.com/impg/JMZvXwLN-ZISZZIGL3yNuT3GQ9IjWrkZzr-HfA/Bumh5JTblq0.jpg?size=588x700&quality=95&sign=7ea00f5762d2540f0661eaae87633459&type=album"), telebot.types.InputMediaPhoto("https://sun9-37.userapi.com/impg/JeVV9jWoNIZ7P9zgKh5pNagQKZ0Cno1CDCpMSg/UKJcn4Veag0.jpg?size=604x604&quality=95&sign=d20ba3523b540b8ac3c587387d1ae852&type=album"), telebot.types.InputMediaPhoto("https://sun9-7.userapi.com/impg/sa6ZSGnkWt_B_moSIxQIdpA-3aM1CHGEjJNkzA/8Yf--peeQ_g.jpg?size=640x400&quality=95&sign=bd99538cbbe360045eaafb8ea8b8e01e&type=album"), telebot.types.InputMediaPhoto("https://sun9-63.userapi.com/impg/B3ySkMEmSnAuEdR6m2oMTES5x1MrcI0WbbpPuA/Bn24s79vHl0.jpg?size=750x750&quality=95&sign=ef7ad1513f764e88721d825d4cb18823&type=album"), telebot.types.InputMediaPhoto("https://sun9-67.userapi.com/impg/9_wMIfT2EbrN2YF4jOeodFtoGWbI_7cvWcGlLA/Y2yhhIKjYZ8.jpg?size=1280x1280&quality=95&sign=a1d68311211d088bca2788a255ea7b56&type=album"), telebot.types.InputMediaPhoto("https://sun9-79.userapi.com/impg/gIGTJwEyssSUpys0n4TfwC7OBLtr26K-irMnzw/8tywqbtTbW4.jpg?size=563x673&quality=95&sign=54865e716bad233a2a1690c1c672798c&type=album"),])
        bot.send_message(m.chat.id, text="можешь посмотреть другие категории картинок", reply_markup=markup)
          
    elif m.text == "с новым годом":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("к категориям")
        markup.add(back)         
        bot.send_media_group(m.chat.id,[telebot.types.InputMediaPhoto("https://sun9-78.userapi.com/impg/ZYqRFbcoOA1UvmoAO4mgas4DPXccCkSkq9paEQ/q0V5v7B1tYc.jpg?size=300x300&quality=95&sign=0602d8b79b493edbadd67ec6bb94262d&type=album"), telebot.types.InputMediaPhoto("https://sun9-65.userapi.com/impg/fT4r--1jmUKHx_p0P9bCoBVwVNNnTN9pe8COow/BJ33Pc8xp9w.jpg?size=354x500&quality=95&sign=d610a65c68022814cff7387165889e36&type=album"), telebot.types.InputMediaPhoto("https://sun9-77.userapi.com/impg/_uot0hl0ZEw9SUqNBCNgK0bEheP8zz9ugs8Xjg/I5jYBh8Jdes.jpg?size=604x604&quality=95&sign=f4e16a2dde2cd343218c2943babeb579&type=album"), telebot.types.InputMediaPhoto("https://sun9-28.userapi.com/impg/DOPuHiAwpvoj8CY-lXaX8WiYl68lfto00qCDgA/L41NN2cXptQ.jpg?size=1200x1200&quality=95&sign=36660417f66819380bb11771168b07d0&type=album"), telebot.types.InputMediaPhoto("https://sun9-43.userapi.com/impg/Kywc2LI8nqNCHQlHVH2wdUsIBzGN3TiCJ25Hrg/FezLSIoDLag.jpg?size=650x650&quality=95&sign=84ff97924926c57ee848d909a8b311eb&type=album"), telebot.types.InputMediaPhoto("https://sun9-40.userapi.com/impg/eoSzxueJMmfdjdGYcD0owmrMwt_4ZLzjtWCdsA/uug4aGA19PI.jpg?size=736x736&quality=95&sign=fc2ea14ffa272f23460c36f7c224b454&type=album"), telebot.types.InputMediaPhoto("https://sun9-77.userapi.com/impg/vQAjfRFj7uryGKH-5F7P5QMpR-gfBTzm2Ys8Ng/swegnvr18pM.jpg?size=800x800&quality=95&sign=1a358af08f6b2188c1bea9c4c68daae5&type=album")])
        bot.send_message(m.chat.id, text="можешь посмотреть другие категории картинок", reply_markup=markup)  
        
    elif m.text == "другие праздники":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("к категориям")
        markup.add(back)         
        bot.send_media_group(m.chat.id,[telebot.types.InputMediaPhoto("https://sun9-38.userapi.com/impg/fD3eGpkEqV7qsIekZBSWfDCOkb4SMEFN8haLCQ/z011GmRQbxE.jpg?size=320x320&quality=95&sign=ae6b8f4a392efc0339ed4d7b56faa3ca&type=album"), telebot.types.InputMediaPhoto("https://sun9-3.userapi.com/impg/Z89EraQF5eGqvl110dK3jL1UC1nnv14KwXreAQ/oztGDuetbbg.jpg?size=604x604&quality=95&sign=4dfc6cc06792da74eca6ad98f721dc3d&type=album"), telebot.types.InputMediaPhoto("https://sun9-8.userapi.com/impg/59goVlFPw59zakIrs-igr8EG2snbokeWGVsfSw/X47nRIjTj58.jpg?size=440x385&quality=95&sign=23c609db85d2f6c5c5556e31c40e8762&type=album"), telebot.types.InputMediaPhoto("https://sun9-56.userapi.com/impg/D9DsliierFKxygjfnBD3YCEMdSi6ZqJVPKYALQ/dR0dQJYhlOM.jpg?size=604x604&quality=95&sign=7213212a30f6aa07fdf74b6345866ed2&type=album"), telebot.types.InputMediaPhoto("https://sun9-14.userapi.com/impg/N4Wzfr_jagQIrakWEiVbPFAL3MtZEgiH_p1VyA/hQHwZo3utKA.jpg?size=320x320&quality=95&sign=e3053386b70626e8c5f4a33d1e66acfc&type=album"), telebot.types.InputMediaPhoto("https://sun9-65.userapi.com/impg/rl39cUHCFm7so1WuCSOdBYwh24KTVs0eobk4cw/qzjkBazbNrk.jpg?size=736x736&quality=95&sign=331518f5ad402fb30d746e162e8840f1&type=album"), telebot.types.InputMediaPhoto("https://sun9-39.userapi.com/impg/KbyrDS1bMciOSicw9WYyvvjL-q2cIGCQImDa7w/inwJ7aXUOds.jpg?size=1280x1280&quality=95&sign=851cc58e6cf258b57360902ff8b8a149&type=album"), telebot.types.InputMediaPhoto("https://sun9-16.userapi.com/impg/di7e0sTnVWzIJ9tGNcUcDeBCOasZ8SaVA1QkwA/oiugtZWd-XY.jpg?size=600x600&quality=95&sign=3167df3edb2c0081be96c952504852f1&type=album"), telebot.types.InputMediaPhoto("https://sun9-45.userapi.com/impg/8APBvbmSwMwXZLlgqRIkGk4RAZvQkJcL6JtSPg/x2rHqj-5A6k.jpg?size=604x604&quality=95&sign=d94c70a132967eeddee790114f14ac62&type=album")])
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
        bot.send_message(m.chat.id, text="меню", reply_markup=markup)
        
    else:
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
        bot.send_message(m.chat.id, text="я не знаю такой команды(((\nвыбери категорию картинок", reply_markup=markup)

bot.polling(none_stop=True, interval=0)