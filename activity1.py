try :
    num = int(input("enter your number : "))
    print(num)
except ValueError as ex:
    print("Exception: ",ex)
print("I am outside the try block")

