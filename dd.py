try:
    age=int(input("enter your age"))
except ValueError:
    print("Incorrect value")
if age %2==0:
    print("It is an even no.")
else:
    print("It is an odd no.")