#1
rule1=int(input("entr your age:"))
rule2=int(input("enter your height in cm:"))
if rule1>=12 and rule2>=140:
    print("you can ride the roller coaster")
else :
    print("you are not allowed to ride a roller coaster")



#3
number=int(input("enter a number:"))
match number:
    case 1:
        print("spring")
    case 2:
        print("summer")
    case 3:
        print("autumn")
    case 4:
        print("winter")
    case _:
        print("invalid number")

#2
number=int(input("enter a number from 1-3:"))
match number:
    case 1:
        print("red")
    case 2:
        print("yellow")
    case 3:
        print("green")
    case _:
        print("given number is invalid")
        
#5
age=int(input("enter your age:"))
monthly_income=int(input("enter your monthly income:"))
credit=int(input("enter your credit:"))
if not age>21 and age<60:
    print("age should be between 21 to 60")
elif not monthly_income>=30000:
    print("monthly income should be atleast 30000")
elif not credit>=700:
    print("credit should be atleast 700")
else:
    print("loan access")

#4
username=input("enter username:")
password=input("enter password:")
if username=="admin" and password=="pass123":
    print("login sucessfully")
elif not username=="admin":
    print("wrong username")
elif not password=="pass123":
    print("wrong password")

#6
age=int(input("enter age:"))
membership_card=input("do you have membership card? (yes/no)= ")
if age<12 and membership_card=="yes":
    print("the ticket is free")
elif age>12 and age<60 and membership_card=="yes":
    print("the ticket price is 150")
elif age>12 and age<60 and membership_card=="no":
    print("the ticket is 200")
elif age>60 and membership_card=="yes":
    print("the ticket price is 100")
else:
    print("please enter valid age and membership card")

#7
salary=int(input("enter your salary:"))
year=int(input("enter your year of service:"))
if year>5:
    print(f'your net bonus is {salary*0.05}')

#8
radius=float(input("enter the radius:"))
area=3.14*radius*radius
if radius>0:
    print(f'the area of circle is {area}')
elif radius==0:
    print("the radius of circle is 0")
else:
    print("invalid input!rradius cannot be negative")

#9
age=int(input("enter your age:"))
gender=input("enter your gender?(m/f) ")
if age>=18 and age<30 and gender=="m":
    print("your wage is 700")
elif age>=18 and age<30 and gender=="f":
    print("your wage is 750")
elif age>=30 and age<=40 and gender=="m":
    print("your wage is 800")
elif age>=30 and age<=40 and gender=="f":
    print("your wage is 850")
else:
    print("invalid input")

#10
number=int(input("enter a number:"))
if number%3==0 and number%5==0:
    print("fizz buzz".title())
elif number%3==0 or  number%5==0:
    print("fizz".capitalize())
elif number%5==0 or number%3==0:
    print("buzz".capitalize())
elif number%3!=0 and number%5!=0:
    print(f'the value is {number%3:.2f},{number%5:.2f}')
    




   




