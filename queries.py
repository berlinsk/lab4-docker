import mysql.connector
from tabulate import tabulate
from datetime import timedelta

conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="user",
    password="password",
    database="library_db"
)
cursor = conn.cursor()

def run_query(description, sql, params=None):
    print(f"\n--- {description} ---")
    cursor.execute(sql, params or ())
    results = cursor.fetchall()
    headers = [i[0] for i in cursor.description]
    print(tabulate(results, headers=headers, tablefmt="grid"))

# 1. Книги після 2001 року (алфавіт)
run_query(
    "Книги, видані після 2001 року (відсортовано за назвою)",
    "SELECT * FROM Books WHERE year > 2001 ORDER BY title"
)

# 2. Кількість книг кожного виду
run_query(
    "Кількість книг кожного виду",
    "SELECT type, COUNT(*) as count FROM Books GROUP BY type"
)

# 3. Читачі, які брали посібники
run_query(
    "Читачі, які брали посібники",
    """
    SELECT DISTINCT Readers.last_name, Readers.first_name
    FROM Readers
    JOIN Issues ON Readers.ticket_number = Issues.ticket_number
    JOIN Books ON Issues.inventory_number = Books.inventory_number
    WHERE Books.type = 'посібник'
    ORDER BY Readers.last_name
    """
)

# 4. Книги за розділом
category = input("\nВведіть розділ для пошуку книг: ").strip()
run_query(
    f"Книги за розділом '{category}'",
    "SELECT * FROM Books WHERE category = %s", (category,)
)

# 5. Кінцевий термін повернення книг
run_query(
    "Кінцевий термін повернення книг",
    """
    SELECT Books.title, Readers.last_name, Issues.issue_date,
           DATE_ADD(Issues.issue_date, INTERVAL Books.max_days DAY) AS return_deadline
    FROM Issues
    JOIN Books ON Issues.inventory_number = Books.inventory_number
    JOIN Readers ON Issues.ticket_number = Readers.ticket_number
    """
)

# 6. Перехресний запит: кількість типів у кожному розділі
run_query(
    "Кількість типів книг у кожному розділі",
    """
    SELECT category, type, COUNT(*) as count
    FROM Books
    GROUP BY category, type
    """
)

cursor.close()
conn.close()