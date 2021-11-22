import csv
import requests
import time
from datetime import datetime


# funkcja pytajaca uzykownika o kod waluty
def input_currency_code():
    input_curr = input("Podaj walute dla ktorej chcesz pobrac kurs sprzedazy w PLN: ")
    currency = input_curr.upper()
    return currency
#nie obsluzylam konkretnego bledu gdy uzytkownik wpisze walute PLN, jest tylko generyczny

input_currency = input_currency_code()
exchange_url = f"http://api.nbp.pl/api/exchangerates/rates/a/{input_currency}"


# Czy to dobrze aby wypisywac zmienne pomiedzy funkcjami? Funkcje i zmienne pisze w formacie text_text (czy jest to poprawne?Czy lepiej w przypadku ktorejs stosowac camelCase?)

# funkcja pobierajace sredni kurs waluty podanej przez uzytkownika
def read_currency_exchange_rate():
    currency_info = requests.get(exchange_url)
    rate_json = currency_info.json()
    exchange_rate = rate_json['rates'][0]['mid']
    print(f"Average exchange rate for {input_currency} is {exchange_rate}")
    return exchange_rate


# funkcja mierzaca czas wykonania zapytania
def read_currency_request_response_time():
    date = (datetime.now()).strftime("%d %b %Y, %H:%M:%S")
    start = time.time()
    currency_info = requests.get(exchange_url)
    stop = time.time()
    request_time = (stop - start) * 1000
    rounded_request_time = '{0:.2f}'.format(request_time)
    print(f"Date and time: {date}")
    print(f"Request total time {rounded_request_time} ms")
    print("------------------------------------------")
    return [date, rounded_request_time]


# pobieranie kursu waluty przez minute (4 razy) w interwale 15 sekundowym
def get_exchange_rate_loop():
    with open("files/exchange_rates.csv", "w") as f:
        try:
            rate_writer = csv.writer(f)
            rate_writer.writerow(["Currency", "Rate", "Date", "Time", "Request time[ms]"])
            iteration = 0
            while True:
                if iteration < 4:
                    currency = input_currency
                    exrate = read_currency_exchange_rate()
                    exrate_data = read_currency_request_response_time()
                    date_and_time = exrate_data[0].split(",")
                    req_date = date_and_time[0]
                    req_time = date_and_time[1]
                    resp_time = exrate_data[1]
                    rate_writer.writerow([currency, exrate, req_date, req_time, resp_time])
                    iteration = iteration + 1
                    time.sleep(15)  # nie wiem czy to jest najbardziej efektywne ale dziala
                else:
                    break
            f.close()
        except:
            print("Oops, something went wrong! Try again later.")


# W pliku CSV mam dodatkowe puste linie, ale nie wiem z czego wynikaja. Nie udalo mi sie ich usunac. W githubie wygladaja ok (bez dodatkowych lini)

get_exchange_rate_loop()
