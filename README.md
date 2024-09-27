# Dog Walking App

## Описание

Приложение для управления заказами на выгул собак. Жильцы могут оформить заказы на выгул собак, указывая время и дату прогулки. Пётр и Антон могут одновременно выгуливать не более одного животного.

## Запуск приложения

1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   
2. Запуск приложения:
   ```bash
   uvicorn app.main:app --reload
