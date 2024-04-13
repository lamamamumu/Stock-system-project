import json

class Strok:
    def __init__(self):
        self.customers = {}
        self.products = []
        self.orders = []

    def add_customer(self, name, address, phone):
        customer_id = len(self.customers) + 1
        customer = {
            "id": customer_id,
            "name": name,
            "address": address,
            "phone": phone
        }
        self.customers[customer_id] = customer

    def add_product(self, name, price, quantity):
        product_id = len(self.products) + 1
        product = {
            "id": product_id,
            "name": name,
            "price": price,
            "quantity": quantity
        }
        self.products.append(product)

    def create_order(self, customer_id, product_id, quantity):
        order_id = len(self.orders) + 1
        product = None
        for p in self.products:
            if p["id"] == product_id:
                product = p
                break
        if product is not None:
            if product["quantity"] >= quantity: 
                order = {
                    "id": order_id,
                    "customer_id": customer_id,
                    "product_id": product["id"],
                    "quantity": quantity
                }
                self.orders.append(order)
                
                product["quantity"] -= quantity
            else:
                print(f"สต็อกของสินค้ารหัส {product_id} ไม่เพียงพอ")
        else:
            print(f"ไม่พบสินค้าที่มีรหัส {product_id}")

    def load_data(self, file_name):
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
                self.customers = data.get('customers', {})
                self.products = data.get('products', [])
                self.orders = data.get('orders', [])
        except FileNotFoundError:
            print(f"ไม่พบไฟล์ {file_name} จะใช้ข้อมูลว่างเริ่มต้น")

    def save_data(self, file_name):
        data = {
            'customers': self.customers,
            'products': self.products,
            'orders': self.orders
        }
        with open(file_name, 'w') as file:
            json.dump(data, file)

    def add_orders(self, num_customers):
        for customer_id in range(1, num_customers + 1):
            product_id = int(input(f"รหัสสินค้าสำหรับลูกค้า {customer_id}: "))
            quantity = int(input(f"จำนวนสินค้าสำหรับลูกค้า {customer_id}: "))
            self.create_order(customer_id, product_id, quantity)

    def show_all_data(self):
        print("ลูกค้าทั้งหมด:")
        for customer in self.customers.values():
            print(customer)

        print("สินค้าทั้งหมด:")
        for product in self.products:
            print(product)

        print("รายการสั่งซื้อทั้งหมด:")
        for order in self.orders:
            print(order)

    def save_stock_data(self):
        with open('stock_data.txt', 'w') as file:
            file.write("ลูกค้าทั้งหมด:\n")
            for customer in self.customers.values():
                file.write(str(customer) + '\n')

            file.write("\nสินค้าทั้งหมด:\n")
            for product in self.products:
                file.write(str(product) + '\n')

            file.write("\nรายการสั่งซื้อทั้งหมด:\n")
            for order in self.orders:
                file.write(str(order) + '\n')

    def reset_data(self):
        self.customers = {}
        self.products = []
        self.orders = []

strok = Strok()
strok.load_data('strok_data.json')

num_products = int(input("ป้อนจำนวนสินค้าที่ต้องการเพิ่ม: "))
for _ in range(num_products):

    name = input("ชื่อสินค้า: ")
    price = float(input("ราคา: "))
    quantity = int(input("จำนวน: "))
    strok.add_product(name, price, quantity)

num_customers = int(input("ป้อนจำนวนลูกค้าที่ต้องการเพิ่ม: "))
for _ in range(num_customers):
    name = input("ชื่อลูกค้า: ")
    address = input("ที่อยู่: ")
    phone = int(input("หมายเลขโทรศัพท์: "))
    strok.add_customer(name, address, phone)

strok.add_orders(num_customers)

command1 = input("ป้อนคำสั่ง reset หรือไม่ No reset (เพื่อรีเซตข้อมูล): ")
if command1.lower() == "reset":
    strok.reset_data()

command2 = input("ป้อนคำสั่ง show หรือไม่ No show (เพื่อรีเซตข้อมูล): ")
if command2.lower() == "show":
    strok.show_all_data()
    strok.save_stock_data()

strok.save_data('strok_data.json')

print('--------------------------------------------\n'
      'ไฟล์จะแสดงอยู่ที่หน้า Desktop \n'
      '--------------------------------------------\n')