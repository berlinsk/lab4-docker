import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="user",
    password="password",
    database="library_db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    inventory_number INT PRIMARY KEY,
    author VARCHAR(100),
    title VARCHAR(200),
    category ENUM('технічна', 'художня', 'економічна'),
    year INT,
    pages INT,
    price DECIMAL(10,2),
    type ENUM('посібник', 'книга', 'періодичне видання'),
    copies INT,
    max_days INT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Readers (
    ticket_number INT PRIMARY KEY,
    last_name VARCHAR(100),
    first_name VARCHAR(100),
    phone VARCHAR(20),
    address TEXT,
    course INT CHECK (course BETWEEN 1 AND 4),
    group_name VARCHAR(50)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Issues (
    issue_id INT PRIMARY KEY AUTO_INCREMENT,
    issue_date DATE,
    ticket_number INT,
    inventory_number INT,
    FOREIGN KEY (ticket_number) REFERENCES Readers(ticket_number) ON DELETE CASCADE,
    FOREIGN KEY (inventory_number) REFERENCES Books(inventory_number) ON DELETE CASCADE
)
""")

print("База даних і таблиці створено успішно.")
conn.commit()
cursor.close()
conn.close()