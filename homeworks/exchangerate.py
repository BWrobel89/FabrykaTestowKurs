import csv
import requests
import time
from datetime import datetime


# funkcja pytajaca uzykownika o kod waluty
def input_currency_code():
    curr = input("Podaj walute dla ktorej chcesz pobrac kurs sprzedazy: ")
    currency = curr.upper()
    return currency


requested_currency = input_currency_code()
exchange_url = f"http://api.nbp.pl/api/exchangerates/rates/a/{requested_currency}"
#Czy to dobrze aby wypisywac zmienne pomiedzy funkcjami? Funkcji i zmienne pisze w formacir text_text (czy jest to poprawne?Czy lepiej w przypadku ktorejs stosowac camelCase?)

# funkcja pobierajace sredni kurs waluty podanej przez uzytkownika
def read_currency_exchange_rate():
    currency_info = requests.get(exchange_url)
    rate_json = currency_info.json()
    exchange_rate = rate_json['rates'][0]['mid']
    print(f"Average exchange rate for {requested_currency} is {exchange_rate}")
    return exchange_rate


# funkcja mierzaca czas wykonania zapytania
def read_request_response_time():
    date = (datetime.now()).strftime("%d %b %Y, %H:%M:%S")
    start = time.time()
    currency_info = requests.get(exchange_url)
    stop = time.time()
    request_time = (stop - start) * 1000
    rounded_request_time = '{0:.2f}'.format(request_time)
    print(f"Date and time: {date}")
    print(f"Request total time {rounded_request_time} ms")
    print("------------------------------------------")
    return rounded_request_time
    #chcialam zwracac tu tez date, ale w CSV prezentuje sie to inaczej niz bym chciala i nie moglam tego podzielic, dlatego w funckji get_exchange_rate_looop() mamy powtorzenie zmiennej date

execution_time = 15
execution_end = time.time() + execution_time


# pobieranie kursu waluty przez okres 15 sekund
def get_exchange_rate_looop():
    with open("files/exchange_rates.csv", "w") as f:
        try:
            rate_writer = csv.writer(f)
            rate_writer.writerow(["Currency", "Rate", "'Date , Time'", "Request time[ms]"])
            while True:
                if time.time() < execution_end:
                    rate = requested_currency
                    exrate = read_currency_exchange_rate()
                    date = (datetime.now()).strftime('%d %b %Y, %H:%M:%S') # data i godzina zgadzaja sie z tymi wypisanymi printem in read_request_response_time(). Nie jestem przekonana do poprawnosci tego podejscia.
                    responsetime = read_request_response_time()
                    rate_writer.writerow([rate, exrate, date, responsetime])
                else:
                    break
            f.close()
        except:
            print("Oops, something went wrong! Try again later.")
#W pliku CSV mam dodatkowe puste linie, ale nie wiem z czego wynikaja. Nie udalo mi sie ich usunac. W githubie wygladaja ok (bez dodatkowych lini)

get_exchange_rate_looop()
