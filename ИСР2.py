import urllib.request 
from xml.etree import ElementTree as ET
import json

def nerv(func):
  import functools
  import datetime 
  @functools.wraps(func) 
  def wrapper(calc):
      t = datetime.datetime.now()
      result = func(calc)
      t = datetime.datetime.now() - t

      with open('Результат.json', 'a') as fail:
            fail.write("\n")
            fail.write("Переводим " + str(calc) + " " + str(in_type) + " в " + str(convert_to) + "\n")
            fail.write("Результат: " + str(result) + " " + str(convert_to) +"\n\n")
            file.write(json.dumps(json_data, indent=4))
            
      return result
  return wrapper  

print ("Конвертер")
calc = float(input("Сумма для перевода: "))
in_type = input("Исходная валюта (RUB, USD, EUR): ")
convert_to = input("Конечная валюта (RUB, USD, EUR): ")

id_dollar = "R01235" #USD
id_euro = "R01239" #EUR

valuta = ET.parse(urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp")) #данные с сайта


def convert(calc):
  for line in valuta.findall('Valute'):
    id_v = line.get('ID')
    if id_v == id_dollar:
        rub1 = line.find('Value').text
    elif id_v == id_euro:
        rub2 = line.find('Value').text
       
  rub1 = float(rub1.replace(',', '.'))
  rub2 = float(rub2.replace(',', '.'))

  if in_type == "RUB":
    if convert_to == "RUB":
      result = float (calc)
    elif convert_to == "USD":
      result = float (calc) / rub1
    elif convert_to == "EUR":
      result = float (calc) / rub2
   
  elif in_type == "USD":  
    if convert_to == "RUB":
      result = float (calc) * rub1
    elif convert_to == "USD":
      result = float (calc)
    elif convert_to == "EUR":
      result = (float (calc) * rub1) / rub2


  elif in_type == "EUR":  
    if convert_to == "RUB":
      result = float (calc) * rub2
    elif convert_to == "USD":
      result = (float (calc) * rub2) / rub1
    elif convert_to == "EUR":
      result = float (calc)
  return result

result = convert(calc)

print (calc, in_type, " = ", result, convert_to)