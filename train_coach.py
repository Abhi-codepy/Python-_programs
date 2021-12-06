def berth():
    seat = int(input("Please enter your seat number.. :- "))
    if seat > 0 and seat <=108:
        s = seat % 12
        if s == 0:
            print(seat-11,"Window Seat")
        elif s == 1:
            print(seat+11,"Window Seat")
        elif s == 6:
            print(seat+1,"Window Seat")
        elif s == 7:
            print(seat-1,"Window Seat")
        elif s == 2:
            print(seat+9,"Middle Seat")
        elif s == 5:
            print(seat+3,"Middle Seat")
        elif s == 8:
            print(seat-3,"Middle Seat")
        elif s == 11:
            print(seat-9,"Middle Seat")
        elif s == 3:
            print(seat+7,"Aisle Seat")
        elif s == 4:
            print(seat+5,"Aisle Seat")
        elif s == 9:
            print(seat-5,"Aisle Seat")
        elif s == 10:
            print(seat-7,"Aisle Seat")
        else:
            print("Invalid seat number")
berth()