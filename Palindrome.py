temp = int(input("Enter the number: "))
num = str(temp)
rev = 0
while (temp > 0):
    d = temp % 10
    rev = rev * 10 + d
    temp = temp // 10
if (num == rev):
    print("Number is palindrome.....")
    nl = len(num)
    if nl % 2 == 0:
        mid = int((nl / 2) - 1)
        pre = num[:mid + 1]
        last = num[:mid + 1][::-1]
        print("Previous Palindrome number is ", pre + last)
        num = num.replace(num[mid], str(int(num[mid]) + 1))
        pre = num[:mid + 1]
        last = num[:mid + 1][::-1]
        print("Next Palindrome number is ", pre + last)
    else:
        mid = int(nl / 2)
        pre = num[:mid]
        last = num[:mid][::-1]
        print("Previous Palindrome number is ", pre + num[mid] + last)
        num = num.replace(num[mid], str(int(num[mid]) + 1))
        pre = num[:mid]
        last = num[:mid][::-1]
        print("Next Palindrome number is ", pre + num[mid] + last)
else:
    print("Number is not palindrome.....")
    nl = len(num)
    if nl % 2 == 0:
        mid = int((nl / 2) - 1)
        pre = num[:mid + 1]
        last = num[:mid + 1][::-1]
        print("Previous Palindrome number is ", pre + last)
        num = num.replace(num[mid], str(int(num[mid]) + 1))
        pre = num[:mid + 1]
        last = num[:mid + 1][::-1]
        print("Next Palindrome number is ", pre + last)
    else:
        mid = int(nl / 2)
        pre = num[:mid]
        last = num[:mid][::-1]
        print("Previous Palindrome number is ", pre + num[mid] + last)
        num = num.replace(num[mid], str(int(num[mid]) + 1))
        pre = num[:mid]
        last = num[:mid][::-1]
        print("Next Palindrome number is ", pre + num[mid] + last)