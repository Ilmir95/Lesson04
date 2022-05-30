import requests
from decimal import *
def currency_rates(val):
    val = val.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    if val not in response:
        return None
    rub = response[response.find('<Value>', response.find(val)) + 7:response.find('</Value>', response.find(val))]
    return f"{Decimal(rub.replace(',', '.'))}"
print(currency_rates('USD'))
print(currency_rates('EUR'))
print(currency_rates('eur'))