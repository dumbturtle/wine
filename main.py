import argparse
import datetime
import os
import sys
from collections import defaultdict
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape

parser = argparse.ArgumentParser(
    description='Сайт по продаже вина'
)
env = Environment(
    loader=FileSystemLoader("."), autoescape=select_autoescape(["html", "xml"])
)

template = env.get_template("template.html")

birthday_of_wine_shop = 1920
current_year = datetime.datetime.now().year
shop_age = current_year - birthday_of_wine_shop

parser.add_argument('filename', help='File name of wine description.', nargs='?', default='default_description.xlsx')
args = parser.parse_args()
filename = args.filename

if not os.path.exists(filename):
    sys.exit('File with descriptions is not found!')

wine_descriptions_form_file = pandas.read_excel(
    filename,
    sheet_name="Лист1",
    na_values=" ",
    keep_default_na=False,
    usecols=["Категория", "Название", "Сорт", "Цена", "Картинка", "Акция"],
)

wine_descriptions = defaultdict(list)
for description in wine_descriptions_form_file.to_dict("records"):
    wine_descriptions[description["Категория"]].append(description)

rendered_page = template.render(
    shop_age=shop_age,
    wine_descriptions=wine_descriptions,
)

with open("index.html", "w", encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler)
server.serve_forever()
