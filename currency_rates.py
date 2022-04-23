import requests
from lxml import etree


def currency_rates(code):
    xml_response = etree.fromstring(requests.get("http://www.cbr.ru/scripts/XML_daily.asp").text.encode("1251"))
    curs_usd = xml_response.find("Valute[@ID='R01235']/Value").text
    curs_eur = xml_response.find("Valute[@ID='R01239']/Value").text
    curs_gbp = xml_response.find("Valute[@ID='R01035']/Value").text
    if code == 'USD':
        print(f"Один Американский доллар равен {curs_usd} рублей")
    if code == 'EUR':
        print(f"Один Евро равен {curs_eur} рублей")
    if code == 'GBP':
        print(f"Один Фунт стерлингов Соединенного королевства равен {curs_gbp} рублей")
    return code


if __name__ == '__main__':
    x = input('Введите код валаюты, чтобы узнать курс\n'
              'Для отображения курса доллара введите USD\n'
              'Для отображения курса евро введите EUR\n'
              'Для отображения курса фунта стерлинга введите GBP\n')
    currency_rates(x)
