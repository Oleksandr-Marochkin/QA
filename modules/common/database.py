import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(
            r"C:\\Users\\USER\\aqa" + r"\\become_qa_auto.db"
        )
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id ={product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id ={product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
                products.description, orders.order_date \
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    # Individual:

    def update_product_qnt_by_name(self, name, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE name = '{name}'"
        self.cursor.execute(query)
        self.connection.commit()

    def insert_new_order(self, id, customer_id, product_id, order_date):
        query = f"INSERT OR REPLACE INTO orders (id, customer_id, product_id, order_date) \
            VALUES ({id}, {customer_id}, {product_id}, '{order_date}')"
        self.cursor.execute(query)
        self.connection.commit()

    def get_order_details(self, id):
        query = f"SELECT * FROM orders WHERE id = {id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_customer_name_by_order(self, id):
        query = f"SELECT orders.id, customers.name FROM orders \
            JOIN customers ON orders.customer_id = customers.id \
            WHERE orders.id = {id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_product_details_by_order(self, id):
        query = f"SELECT orders.id, products.name, products.description FROM orders \
            JOIN products ON orders.customer_id = products.id\
            WHERE orders.id = {id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_order_next_id(self):
        query = "SELECT MAX(id) FROM orders"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        next_id = result[0][0] + 1
        return next_id

    def insert_next_order(self, id, customer_id, product_id, order_date):
        query = f"INSERT INTO orders (id, customer_id, product_id, order_date) \
            VALUES ({id}, {customer_id}, {product_id}, '{order_date}')"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_order_by_id(self, id):
        query = f"DELETE FROM orders WHERE id = {id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_all_product_names(self):
        query = "SELECT name FROM products"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def get_product_quantity(self, name):
        query = f"SELECT quantity FROM products WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
