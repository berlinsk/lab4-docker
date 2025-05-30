import mysql.connector
from datetime import date

conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="user",
    password="password",
    database="library_db"
)
cursor = conn.cursor()

# Книги (14 штук)
books = [
    (1, "Андрухович Ю.", "Московіада", "художня", 2003, 180, 85.00, "книга", 2, 14),
    (2, "Коваленко В.", "Економіка для всіх", "економічна", 2010, 220, 120.00, "посібник", 3, 21),
    (3, "Стельмах І.", "Основи SQL", "технічна", 2022, 310, 200.00, "посібник", 2, 14),
    (4, "Ліна К.", "Поезія душі", "художня", 2005, 120, 55.00, "книга", 1, 10),
    (5, "Гончар О.", "Фінансова грамотність", "економічна", 2015, 160, 90.00, "посібник", 4, 30),
    (6, "Сергійчук В.", "Технології Python", "технічна", 2021, 280, 150.00, "посібник", 2, 14),
    (7, "Гудзь П.", "Веб-розробка", "технічна", 2020, 270, 180.00, "посібник", 2, 14),
    (8, "Іваненко Т.", "Маркетинг", "економічна", 2012, 230, 130.00, "книга", 2, 21),
    (9, "Карпенко Л.", "Світ у віршах", "художня", 2001, 100, 45.00, "періодичне видання", 5, 7),
    (10, "Остроградський М.", "Аналітика", "технічна", 2000, 300, 210.00, "книга", 2, 21),
    (11, "Малишко А.", "Економічні реформи", "економічна", 2018, 190, 110.00, "посібник", 3, 14),
    (12, "Тарас Ш.", "Народні думи", "художня", 1999, 150, 60.00, "періодичне видання", 2, 7),
    (13, "Котляревський І.", "Енеїда", "художня", 2016, 210, 75.00, "книга", 2, 14),
    (14, "Кучер І.", "Java для початківців", "технічна", 2023, 340, 250.00, "посібник", 3, 21)
]

cursor.executemany("""
INSERT INTO Books VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
""", books)

# Читачі (9 штук)
readers = [
    (101, "Іванов", "Петро", "0671234567", "Київ, вул. Лесі", 2, "ІП-21"),
    (102, "Петренко", "Ольга", "0679876543", "Львів, вул. Шевченка", 1, "ЕК-11"),
    (103, "Сидоренко", "Ірина", "0503456789", "Одеса, вул. Франка", 3, "ІП-31"),
    (104, "Мельник", "Андрій", "0932345678", "Харків, вул. Грушевського", 4, "ЕК-41"),
    (105, "Коваль", "Марія", "0501239876", "Полтава, вул. Довженка", 2, "ХУ-21"),
    (106, "Гнатюк", "Оксана", "0739871234", "Київ, вул. Січових", 1, "ХУ-11"),
    (107, "Романюк", "Тарас", "0668765432", "Луцьк, вул. Лесі", 3, "ІП-32"),
    (108, "Заболотна", "Юлія", "0974567890", "Рівне, вул. Драгоманова", 4, "ЕК-42"),
    (109, "Бондаренко", "Ігор", "0937894561", "Житомир, вул. Садова", 2, "ІП-22")
]

cursor.executemany("""
INSERT INTO Readers VALUES (%s, %s, %s, %s, %s, %s, %s)
""", readers)

# Видачі (11 штук)
issues = [
    (date(2024, 2, 1), 101, 2),
    (date(2024, 2, 3), 102, 3),
    (date(2024, 2, 5), 103, 5),
    (date(2024, 2, 7), 104, 6),
    (date(2024, 2, 9), 105, 8),
    (date(2024, 2, 11), 106, 1),
    (date(2024, 2, 13), 107, 14),
    (date(2024, 2, 15), 108, 11),
    (date(2024, 2, 17), 109, 12),
    (date(2024, 2, 19), 101, 4),
    (date(2024, 2, 21), 103, 7)
]

cursor.executemany("""
INSERT INTO Issues (issue_date, ticket_number, inventory_number)
VALUES (%s, %s, %s)
""", issues)

conn.commit()
cursor.close()
conn.close()

print("Таблиці заповнено даними.")