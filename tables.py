
def tables(num):
    for i in range(1, 11):
        print(f"{num} X {i} = {num*i}")

def names(char):
    for i in char:
        print(f"{char} is my name")

print("1.tables \n2.name")

option = int(input("Enter a option>>"))

if option == 1:
    num = int(input("Enter a number>>  "))
else:
    char = str(input("Enter a name>>   "))

if option == 1:
    tables(num)
elif option == 2:
    names(char)
    pass
else:
    print("Invalid option , Try again")