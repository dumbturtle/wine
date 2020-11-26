import datetime
import pandas
from collections import defaultdict
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader("."), autoescape=select_autoescape(["html", "xml"])
)

template = env.get_template("template.html")

# Расчет возраста
birthday_of_wine = 1920
current_year = datetime.datetime.now().year
age = current_year - birthday_of_wine

# Перечень вина


excel_data_df = pandas.read_excel(
    "wine2.xlsx",
    sheet_name="Лист1",
    na_values=" ",
    keep_default_na=False,
    usecols=["Категория", "Название", "Сорт", "Цена", "Картинка"],
)

dict_of_wines = defaultdict(list)
for data in excel_data_df.to_dict("records"):
    dict_of_wines[data["Категория"]].append(data)


rendered_page = template.render(
    age=age,
    wines=dict_of_wines,
)

with open("index.html", "w", encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler)
server.serve_forever()
