import requests
import time
from datetime import datetime

#funkcja pytajaca uzykownika o kod waluty
def input_currency_code():
    curr = input("Podaj walute dla ktorej chcesz pobrac kurs sprzedazy: ")
    currency = curr.upper()
    return (currency)

exchange_url = f"http://api.nbp.pl/api/exchangerates/rates/a/{input_currency_code()}"

#funkcja pobierajace sredni kurs waluty podanej przez uzytkownika
def read_currency_exchange_rate():
    try:
        currency_info = requests.get(exchange_url)
        rate_json = currency_info.json()
        exchange_rate = rate_json['rates'][0]['mid']
        print(
            f"Average exchange rate for today is {exchange_rate}")  # nie wiem jak przekazac tu tresc tj walute jaka wprowadzil uzytkownik 2 input_currency_code()
    except:
        print("Oops, something went wrong! Try again later.")

#funkcja mierzaca czas wykonania zapytania
def read_request_response_time():
    date = (datetime.now()).strftime("%d %b %Y, %H:%M:%S")
    start = time.time()
    currency_info = requests.get(exchange_url)
    stop = time.time()
    request_time_ms = (stop - start) * 1000
    print(f"Date and time: {date}")
    print("Request total time {0:.2f} ms".format(request_time_ms))
    print("------------------------------------------")


execution_time = 15
execution_end = time.time() + execution_time

#pobieranie kursu waluty przez okres 15 sekund
def get_exchange_rate_looop():
    while True:
        if time.time() < execution_end:
            read_currency_exchange_rate()
            read_request_response_time()
        else:
            break

get_exchange_rate_looop()
