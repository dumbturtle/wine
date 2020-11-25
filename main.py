import datetime
import pandas
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

#Расчет возраста
birthday_of_wine = 1920
current_year = datetime.datetime.now().year
age = current_year - birthday_of_wine

#Перечень вина
excel_data_df = pandas.read_excel('wine.xlsx', sheet_name='Лист1', usecols=['Название', 'Сорт', 'Цена', 'Картинка'])
dict_of_wines = excel_data_df.to_dict(orient='records')

rendered_page = template.render(
    age = age,
    wines = dict_of_wines,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
