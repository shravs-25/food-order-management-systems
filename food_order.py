import mysql.connector
from datetime import date

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="YOUR_PASSWORD",
  database="food_order_db"
)
cursor = db.cursor()

def show_menu():
    print("\n--- MENU ---")
    cursor.execute("SELECT item_id, item_name, price FROM menu_items")
    for row in cursor.fetchall():
        print(f"{row[0]}. {row[1]} - Rs.{row[2]}")

def place_order():
    show_menu()
    item_id = int(input("Item ID ivvu: "))
    qty = int(input("Quantity: "))
    cursor.execute("SELECT price FROM menu_items WHERE item_id=%s", (item_id,))
    price = cursor.fetchone()[0]
    total = price * qty
    cursor.execute("INSERT INTO orders (user_id, item_id, quantity, total_price, order_date) VALUES (1, %s, %s, %s, %s)", (item_id, qty, total, date.today()))
    db.commit()
    print(f"Order Success! Total: Rs.{total}")

def view_orders():
    print("\n--- MY ORDERS ---")
    cursor.execute("SELECT o.order_id, m.item_name, o.quantity, o.total_price, o.order_date FROM orders o JOIN menu_items m ON o.item_id=m.item_id")
    for row in cursor.fetchall():
        print(row)

while True:
    print("\n1. Menu Chudu\n2. Order Chey\n3. Orders Chudu\n4. Exit")
    ch = input("Choice: ")
    if ch == '1': show_menu()
    elif ch == '2': place_order()
    elif ch == '3': view_orders()
    else: break