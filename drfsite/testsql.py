# # import sqlite3
# #
# # def update_sqlite_table():
# #     try:
# #         sqlite_connection = sqlite3.connect('db.sqlite3')
# #         cursor = sqlite_connection.cursor()
# #         print("Подключен к SQLite")
# #
# #         sql_update_query = """Update auth_user set is_staff = 1 where id = 8"""
# #         sql_update_query = """Update auth_user set is_superuser = 1 where id = 8"""
# #         cursor.execute(sql_update_query)
# #         sqlite_connection.commit()
# #         print("Запись успешно обновлена")
# #         cursor.close()
# #
# #     except sqlite3.Error as error:
# #         print("Ошибка при работе с SQLite", error)
# #     finally:
# #         if sqlite_connection:
# #             sqlite_connection.close()
# #             print("Соединение с SQLite закрыто")
# #
# # update_sqlite_table()
#
#
import sqlite3
#
# def read_sqlite_table(records):
#     try:
#         sqlite_connection = sqlite3.connect('db.sqlite3')
#         cursor = sqlite_connection.cursor()
#         print("Подключен к SQLite")
#
#         sqlite_select_query = """SELECT * from auth_user"""
#         cursor.execute(sqlite_select_query)
#         records = cursor.fetchall()
#         print("Всего строк:  ", len(records))
#         print("Вывод каждой строки")
#         login = 'root'
#         name = []
#         for row in records:
#             print("ID:", row[0])
#             print("Админ?:", row[3])
#             print("Имя:", row[4], end="\n\n")
#             if row[3] == 1:
#                 name.append(str(row[4]))
#
#         print(name)
#
#         if login in name:
#             print("OOOH YEAH")
#
#         cursor.close()
#
#     except sqlite3.Error as error:
#         print("Ошибка при работе с SQLite", error)
#     finally:
#         if sqlite_connection:
#             sqlite_connection.close()
#             print("Соединение с SQLite закрыто")
#
# read_sqlite_table(1)