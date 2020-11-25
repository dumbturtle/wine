import pandas
from pprint import pprint
excel_data_df = pandas.read_excel('wine2.xlsx', sheet_name='Лист1', na_values=' ', keep_default_na=False, usecols=['Категория', 'Название', 'Сорт', 'Цена', 'Картинка'])
excel_data_df['dict'] = excel_data_df[['Название', 'Сорт', 'Цена', 'Картинка']].to_dict("records")
excel_data_df = excel_data_df[['Категория', 'dict']]
pprint(excel_data_df.groupby('Категория')['dict'].apply(list).to_dict())