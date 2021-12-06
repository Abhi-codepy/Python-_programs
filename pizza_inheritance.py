class item:

    def __init__(self,name="",price = 0,qty = 0):
        self.name = name
        self.price = price
        self.qty = qty

class pizza(item):

    def __init__(self,id="",name="",size="",price=0,qty = 0):
        super(pizza,self).__init__(name,price,qty)
        self.id = id
        self.size = size
        self.p_tot = self.price * self.qty

    def get_total(self):
        return self.p_tot

    def __repr__(self):
        super(pizza,self).__repr__()
        data = ""
        data += ("------------------------DOMINOS------------------------------")+ "\n"
        data += ("ORDER ID ".ljust(20) +       "          :   " + str(self.id.ljust(50))) + "\n"
        data += ("PIZZA NAME ".ljust(20) +     "          :   " + str(self.name.ljust(50))) + "\n"
        data += ("PIZZA PRICE ".ljust(20) +    "          :   " + str(self.price).ljust(50)) + "\n"
        data += ("PIZZA SIZE ".ljust(20) +     "          :   " + str(self.size.ljust(50))) + "\n"
        data += ("NO. OF PIZZA'S ".ljust(20) + "          :   " + str(self.qty).ljust(50)) + "\n"
        data += ("PIZZA TOTAL    ".ljust(20) + "          :   " + str(self.p_tot).ljust(50))
        return data

class toppings(item):

    def __init__(self,name="", price=0,qty = 0):
        super(toppings, self).__init__(name, price, qty)
        self.t_tot = self.price * self.qty

    def get_total(self):
        return self.t_tot

    def __repr__(self):
        super(toppings, self).__repr__()
        data = ""
        data += ("-"*61)+ "\n"
        data += ("TOPPING NAME ".ljust(20) +     "          :   " + str(self.name.ljust(50))) + "\n"
        data += ("TOPPING PRICE ".ljust(20) +    "          :   " + str(self.price).ljust(50)) + "\n"
        data += ("NO. OF TOPPING'S ".ljust(20) + "          :   " + str(self.qty).ljust(50)) + "\n"
        data += ("TOPPING TOTAL    ".ljust(20) + "          :   " + str(self.t_tot).ljust(50))
        return data

class drinks(item):

    def __init__(self,name="",size="", price=0, qty = 0 ):
        super(drinks, self).__init__(name, price, qty)
        self.size = size
        self.d_tot = self.price * self.qty

    def get_total(self):
        return self.d_tot

    def __repr__(self):
        super(drinks, self).__repr__()
        data = ""
        data += ("-"*61)+ "\n"
        data += ("DRINK NAME ".ljust(20) +     "          :   " + str(self.name.ljust(50))) + "\n"
        data += ("DRINK SIZE ".ljust(20) + "          :   " + str(self.size.ljust(50))) + "\n"
        data += ("DRINK PRICE ".ljust(20) +     "          :   " + str(self.price).ljust(50)) + "\n"
        data += ("NO. OF DRINK'S ".ljust(20) + "          :   " + str(self.qty).ljust(50)) + "\n"
        data += ("DRINK TOTAL ".ljust(20) + "          :   " + str(self.d_tot).ljust(50))
        return data

class Order:
    totalOrder = 0
    def bill(self,pizza = "",topping = "",drink = ""):
        self.pizza = pizza
        self.topping = topping
        self.drink = drink

    def bill_bool(self):
        if bool(self.pizza):
            self.totalOrder += self.pizza.get_total()
        if bool(self.topping):
            self.totalOrder += self.topping.get_total()
        if bool(self.drink):
            self.totalOrder += self.drink.get_total()

    def display(self):
        self.gst = (18 * self.totalOrder) / 100
        self.T_bill = self.gst + self.totalOrder
        print("-"*61)
        print("BILL".ljust(20) + "          :   " + str(self.totalOrder).ljust(50))
        print("GST 18%".ljust(20) + "          : "+ " +"+ str(self.gst).ljust(50))
        print("TOTAL BILL".ljust(20) + "          :   " + str(self.T_bill).ljust(50))
        print("------------------------THANK YOU------------------------------")

pz = pizza(input("Enter Order id:- "),input("Enter pizza name:- "),input("Select size:- "),int(input("Enter price:- ")),int(input("Enter quantity:- ")))
top = toppings(input("Enter toppings:- "),int(input("Enter price:- ")),int(input("Enter quantity:- ")))
dr = drinks(input("Enter drinks:- "),input("Select size:- "),int(input("Enter price:- ")),int(input("Enter quantity:- ")))
orderD = Order()
orderD.bill(pz,top,dr)
print(pz)
print(top)
print(dr)
orderD.bill_bool()
orderD.display()