# print("Wellcome to roller coaster")
# bill=0
# height=int(input("Input your height! "))
# if height >= 120:
#     print("You can ride the roller coaster")
#     age=int(input("Enter your age: "))
#     if age<12:
#         bill=5
#         print(f"Your bill is {bill}.")
#     elif age<=18:
#         bill=7
#         print(f"Your bill is {bill}")
#     elif age>=45 and age<=55:
#         bill=0
#         print("You can ride!")
#     else:
#         bill=7
#         print(f"BILL{bill}")
# else:
#     print("Sorry! You can't ride")  

# Even and odd number program
# for x in range(5):
#     Number=int(input("Enter a number: "))
#     if Number%2==0:
#         print("Your given number is even number")
#     else:
#         print("Your given number is odd number")



bill=0
print("Wellcome to python pizza ")
size=input("Size of your pizza? ")
peproni=input("Do you want to add peproni reply in yes or no: ")
extra_cheez=input("Do you want extra cheez? ")

if size=="S":
    bill+=15
elif size=="M":
    bill+=20 
else:
    bill+=25

if peproni=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3

if extra_cheez=="Y":
    bill+=1

print(f"final bill  is {bill}")

           






