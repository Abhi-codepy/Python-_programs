import os
import datetime

files = os.walk(r"C:\Users\ABHISHEK SINGH\PycharmProjects\Project2\Train")
length = 0
for (root,d,file) in files:
    length = len(file)
    break
try:
    x = datetime.datetime.now()
    f = open(r"Train\Ticket_"+str(length+1)+"_"+str(x.date())+".txt","w")
    c_name = input("Enter customer name: ")
    t_name = input("Enter Train name: ")
    t_num = int(input("Enter Train no: "))
    s_point = input("Enter Starting point: ")
    e_point = input("Enter Ending point: ")
    dis = int(input("Enter Total Distance: "))
    s_class = input("Enter class: ")
    s_coach = input("Enter coach: ")
    seat = int(input("Enter no. of seats: "))
    s_price = int(input("Enter ticket price: "))
    total = s_price * seat
    gst = (18 * total) / 100
    f_price = gst + total
    def train(**op):
        sym = "|"
        if (op.get("sym")):
            sym = op.get("sym")
        f.write("\n")
        f.write("DATE :- " + str(x.date()) + "\n")
        f.write("TIME :- " + str(x.time()) + "\n")
        f.write("\n")
        f.write("-" * 84+"\n")
        f.write(sym + "CUSTOMER DETAILS".center(82) + sym+"\n")
        f.write("*" * 84+"\n")
        f.write(sym + " CUSTOMER NAME         :  ".ljust(20) + c_name.ljust(56) + sym+"\n")
        f.write(sym + " TRAIN N0. / NAME      :  ".ljust(20) + str(t_num).ljust(6) + " / ".ljust(2) + t_name.ljust(47) + sym+"\n")
        f.write(sym + " FROM                  :  ".ljust(20) + s_point.ljust(56) + sym+"\n")
        f.write(sym + " TO                    :  ".ljust(20) + e_point.ljust(56) + sym+"\n")
        f.write(sym + " TOTAL DISTANCE        :  ".ljust(20) + str(dis).ljust(56) + sym+"\n")
        f.write(sym + " CLASS                 :  ".ljust(20) + s_class.ljust(56) + sym+"\n")
        f.write(sym + " COACH                 :  ".ljust(20) + s_coach.ljust(56) + sym+"\n")
        if seat <= 5:
            f.write("*" * 84+"\n")
            f.write(sym + " TICKET FARE ".center(82) + sym+"\n")
            f.write("-" * 84+"\n")
            f.write(sym + " PRICE                 :  ".ljust(20) + " " + str(s_price).ljust(55) + sym+"\n")
            f.write(sym + " NO. OF SEATS          :  ".ljust(20) + " " + str(seat).ljust(55) + sym+"\n")
            f.write(sym + " TOTAL                 :  ".ljust(20) + " " + str(total).ljust(55) + sym+"\n")
            f.write(sym + " GST 18%               :  ".ljust(20) + "+" + str(gst).ljust(55) + sym+"\n")
            f.write(sym + "--------".rjust(33)+"          ".rjust(49)+sym+"\n")
            f.write(sym + " TOTAL FARE            :  ".ljust(20) + " " + str(f_price).ljust(55) + sym+"\n")
            f.write("-" * 84+"\n")
        elif seat > 5 and seat <= 10:
            s5 = (f_price * 10) / 100
            f5_price = f_price - s5
            f.write("*" * 84+"\n")
            f.write(sym + " TICKET FARE ".center(82) + sym+"\n")
            f.write("_" * 84+"\n")
            f.write(sym + " PRICE                 :  ".ljust(20) + " " + str(s_price).ljust(55) + sym+"\n")
            f.write(sym + " NO. OF SEATS          :  ".ljust(20) + " " + str(seat).ljust(55) + sym+"\n")
            f.write(sym + " TOTAL                 :  ".ljust(20) + " " + str(total).ljust(55) + sym+"\n")
            f.write(sym + " GST 18%               :  ".ljust(20) + "+" + str(gst).ljust(55) + sym+"\n")
            f.write(sym + " 10% OFF COUPON        :  ".ljust(20) + "-" + str(s5).ljust(55) + sym+"\n")
            f.write(sym + "--------".rjust(33) + "          ".rjust(49) + sym+"\n")
            f.write(sym + " TOTAL FARE            :  ".ljust(20) + " " + str(f5_price).ljust(55) + sym+"\n")
            f.write("-" * 84+"\n")
        else:
            s6 = (f_price * 30) / 100
            f6_price = f_price - s6
            f.write("-" * 84+"\n")
            f.write(sym + " TICKET FARE ".center(82) + sym+"\n")
            f.write("*" * 84+"\n")
            f.write(sym + " PRICE                 :  ".ljust(20) + " " + str(s_price).ljust(55) + sym+"\n")
            f.write(sym + " NO. OF SEATS          :  ".ljust(20) + " " + str(seat).ljust(55) + sym+"\n")
            f.write(sym + " TOTAL                 :  ".ljust(20) + " " + str(total).ljust(55) + sym+"\n")
            f.write(sym + " GST 18%               :  ".ljust(20) + "+" + str(gst).ljust(55) + sym+"\n")
            f.write(sym + " 30% OFF COUPON        :  ".ljust(20) + "-" + str(s6).ljust(55) + sym+"\n")
            f.write(sym + "--------".rjust(33) + "          ".rjust(49) + sym+"\n")
            f.write(sym + " TOTAL FARE            :  ".ljust(20) + " " + str(f6_price).ljust(55) + sym+"\n")
            f.write("-" * 84+"\n")
    train()
except Exception as e:
    print(e)