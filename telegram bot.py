import telebot
import requests

token='5292724613:AAGPalKUF_-KJx_xogvkt7yj61kj0HsmICY'
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
  print(message)
  bot.send_message(message.chat.id,f"Привет ✌️{message.chat.first_name} , you send {message.text}")
  bot.send_message(message.chat.id, f'Привет ✌️{message.chat.first_name} , please enter currency')

@bot.message_handler(regexp=".*")
def any_message(message):
    print(message)

    # current exchange rate, base currency = USD
    exch_rates_response = requests.request('GET', 'https://freecurrencyapi.net/api/v2/latest?apikey=967f8e20-84de-11ec-bc3c-890057b0472e')
    exch_rates_json = exch_rates_response.json()
    if message.text == 'USD':
        bot.send_message(message.chat.id, '1')
    elif message.text not in exch_rates_json['data']:
        bot.send_message(message.chat.id, 'unknown currency')
    else:
        current_exch_rate = exch_rates_json['data'][message.text]
        bot.send_message(message.chat.id, current_exch_rate)

    # change of base currency
    # exch_rates_basecur_json  = requests.request('GET', 'https://freecurrencyapi.net/api/v2/latest?apikey=967f8e20-84de-11ec-bc3c-890057b0472e&base_currency=UAH').json()
    # current_exch_rate = exch_rates_basecur_json['data'][message.text]
    # bot.send_message(message.chat.id, current_exch_rate)

    # historical data
    # exch_rates_hist_json  = requests.request('GET', 'https://freecurrencyapi.net/api/v2/historical?apikey=967f8e20-84de-11ec-bc3c-890057b0472e&base_currency=USD&date_from=2021-12-25&date_to=2022-02-01').json()
    # for i in exch_rates_hist_json['data']:
    #     exch_rate = exch_rates_hist_json['data'][i][message.text]
    #     bot.send_message(message.chat.id, f"on {i} exchange rate was {exch_rate}")

bot.infinity_polling()
