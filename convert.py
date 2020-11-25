from collections import defaultdict
from pprint import pprint

import pandas

excel_data_df = pandas.read_excel(
    "wine2.xlsx",
    sheet_name="Лист1",
    na_values=" ",
    keep_default_na=False,
    usecols=["Категория", "Название", "Сорт", "Цена", "Картинка"],
)
wine_dict = defaultdict(list)
for data in excel_data_df.to_dict("records"):
    wine_dict[data["Категория"]].append(data)
pprint(wine_dict)
