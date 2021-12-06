import mysql.connector

class Db:
    connection = ""

    def __init__(self):
        self.connection = mysql.connector.connect(user='root',password='mysql',
                             host='localhost',
                             database='pizza')
    def save_pizza(self,pizza):
        if pizza.id > 0:
            try:
                cursor = self.connection.cursor()
                sql = ("UPDATE `pizza` SET `pizza_name`=%s,`price`=%s WHERE id = %s")
                cursor.execute(sql, (pizza.pizza_name,str(pizza.price),str(pizza.id)))
                self.connection.commit()
            except Exception as e:
                print(e)
        else:
            try:
                cursor = self.connection.cursor()
                sql = ("INSERT INTO `pizza`(`id`, `pizza_name`, `price`) VALUES (null,%s,%s)")
                cursor.execute(sql, (pizza.pizza_name,str(pizza.price)))
                self.connection.commit()
            except Exception as e:
                print(e)

    def select_pizza(self,id = 0):
        if id == 0:
            try:
                cursor = self.connection.cursor()
                sql = ("select * from `pizza`")
                cursor.execute(sql)
                for (id, pizza_name,price) in cursor:
                    print(id, pizza_name, price)
            except Exception as e:
                print(e)
        else:
            try:
                cursor = self.connection.cursor()
                sql = ("select * from `pizza` where id = %s")
                cursor.execute(sql,(id,))
                for (id, pizza_name,price) in cursor:
                    print(id, pizza_name, price)
            except Exception as e:
                print(e)

class Pizza:
    id = 0
    pizza_name = ""
    price = 0.00

    def __init__(self,name = "",price = 0,id = 0):
        self.id = id
        self.pizza_name = name
        self.price = price



p = Pizza("Afrt",1000,5)
db = Db()
db.save_pizza(p)
db.select_pizza()