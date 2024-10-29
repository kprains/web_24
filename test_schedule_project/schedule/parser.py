# import requests
# from bs4 import BeautifulSoup
# import sqlite3
#
#
# # Создание базы данных и таблицы
# def create_database():
#     conn = sqlite3.connect('schedule.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS schedule (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             group_name TEXT,
#             subject TEXT,
#             time TEXT,
#             teacher TEXT
#         )
#     ''')
#     conn.commit()
#     conn.close()
#
#
# # Очистка базы данных
# def clear_database():
#     conn = sqlite3.connect('schedule.db')
#     cursor = conn.cursor()
#     cursor.execute('DELETE FROM schedule')
#     conn.commit()
#     conn.close()
#
#
# # Вставка расписания в базу данных
# def insert_schedule(group_name, subject, time, teacher):
#     conn = sqlite3.connect('schedule.db')
#     cursor = conn.cursor()
#     cursor.execute('INSERT INTO schedule (group_name, subject, time, teacher) VALUES (?, ?, ?, ?)',
#                    (group_name, subject, time, teacher))
#     conn.commit()
#     conn.close()
#
#
# # Получение расписания через POST-запрос
# def fetch_schedule(group_name):
#     url = 'https://vvsu.ru/timetable/'  # Замените на правильный URL
#     payload = {'group': group_name}  # Параметры, которые нужно отправить
#
#     # Отправляем POST-запрос
#     response = requests.post(url, data=payload)
#
#     if response.status_code == 200:
#         return response.text  # Возвращает HTML-страницу
#     else:
#         print("Ошибка при получении расписания:", response.status_code)
#         return None
#
#
# # Парсинг расписания из HTML
# def parse_schedule(html, group_name):
#     soup = BeautifulSoup(html, 'html.parser')
#
#     # Измените селекторы в зависимости от структуры HTML
#     for item in soup.select('.schedule-item'):
#         subject = item.select_one('.subject').text.strip()
#         time = item.select_one('.time').text.strip()
#         teacher = item.select_one('.teacher').text.strip()
#
#         insert_schedule(group_name, subject, time, teacher)
#
#
# # Проверка содержимого базы данных
# def fetch_all_schedule():
#     conn = sqlite3.connect('schedule.db')
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM schedule')
#     rows = cursor.fetchall()
#     conn.close()
#     return rows
#
#
# # Основная функция
# def main():
#     create_database()
#     clear_database()
#
#     group_name = input("Введите название группы: ")
#     html = fetch_schedule(group_name)
#
#     if html:
#         parse_schedule(html, group_name)
#         print("Расписание успешно загружено в базу данных.")
#
#         # Проверка данных в базе данных
#         print("Содержимое базы данных:")
#         schedule_records = fetch_all_schedule()
#         for record in schedule_records:
#             print(record)
#
#
# if __name__ == "__main__":
#     main()
