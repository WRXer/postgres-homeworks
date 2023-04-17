"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


#connect to db подключение к бд
conn = psycopg2.connect(host="localhost", database="north", user="postgres", password="777Nokia13")

try:
    with conn:
        with conn.cursor() as cur:    #create cursor
            with open("north_data/employees_data.csv", encoding='utf-8') as outfile:    #for employees
                reader = csv.reader(outfile, delimiter=",")    # Создаем объект Reader, указываем символ-разделитель ","
                next(reader)  # пропускаем первую строку с заголовками
                for row in reader:    # Считывание данных из CSV файла
                    cur.execute("INSERT INTO employees VALUES (default, %s, %s, %s, %s, %s)", row)

            with open("north_data/customers_data.csv", encoding='utf-8') as outfile:    #for customers
                reader = csv.reader(outfile, delimiter=",")  # Создаем объект Reader, указываем символ-разделитель ","
                next(reader)  # пропускаем первую строку с заголовками
                for row in reader:  # Считывание данных из CSV файла
                    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", row)

            with open("north_data/orders_data.csv", encoding='utf-8') as outfile:    #for orders
                reader = csv.reader(outfile, delimiter=",")  # Создаем объект Reader, указываем символ-разделитель ","
                next(reader)  # пропускаем первую строку с заголовками
                for row in reader:  # Считывание данных из CSV файла
                    cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", row)



finally:
    conn.close()    #close connection to db закрываем соединение