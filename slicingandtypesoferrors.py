#4. Design a program for a 'Student Resource Portal.' The program should ask for a username and a password.

#  If the username is admin and password is ad123, print Access Granted: Faculty Dashboard

#  If the username is student and password is st2026, print Access Granted: Notes and Practice Questions

#  For any other combination, print Invalid Credentials. Please try again.

uname=input("Enter Username: ")

pwd=input("Enter Password: ")

if uname=="admin" and pwd=="ad123":

    print("Access Granted: Faculty Dashboard")

elif uname=="student" and pwd=="st2026":

    print("Access Granted: Notes and Practice Questions")

else:

    print("Invalid Credentials. Please try again.")

#5.Write a Python program that calculates a customer's final bill based on their spending and membership status.

# The program should follow the exact logic shown in the flowchart.

amount=float(input("Enter Purchase Amount: "))

if amount>5000:

    member=input("Do you have membership (y/n): ").lower()

    if member=="y":

        discount=amount*0.20

        final_bill=amount-discount

        print(f"Final Amount={final_bill}")

        print(f"You Saved={discount}")

    else:

        print(f"Final Amount={amount}")

else:

    print(f"Final Amount={amount}")

#6.Create a Python program for a text-based adventure game called Magic Forest based on the given flowchart.

# The program should follow the exact logic shown in the flowchart.

msg="WELCOME TO THE MAGIC FOREST"

print(msg.center(100))

way=input("Choose Direction (North/South): ").lower()

if way=="north":

    print("Game Over!!!")

else:

    route=input("Cross the river(r) or Follow the path(p): ").lower()

    if route=="p":

        print("Cross The River")

        print("THE END")

    else:

        creature=input("Choose Fairy, Ogre or Elf: ").lower()

        if creature=="elf":

            print("Congratulations!!!")

            print("You Win")

        else:

            print("Game Over!!!")

            print("THE END")

#10.Write a Python program that calculates a person’s Body Mass Index and determines their weight category.

mass=float(input("Enter Your Weight: "))

height=float(input("Enter Your Height in meters: "))

bmi=mass/(height**2)

if bmi<18.5:

    print(f"Weight:{mass}")

    print(f"Height:{height}")

    print(f"BMI:{bmi}")

    print("Underweight")

elif bmi>=18.5 and bmi<=25:

    print(f"Weight:{mass}")

    print(f"Height:{height}")

    print(f"BMI:{bmi}")

    print("Normal Weight")

elif bmi>25 and bmi<=30:

    print(f"Weight:{mass}")

    print(f"Height:{height}")

    print(f"BMI:{bmi}")

    print("Overweight")

else:

    print(f"Weight:{mass}")

    print(f"Height:{height}")

    print(f"BMI:{bmi}")

    print("Obese")

#12.A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.

# Ask user for their salary and year of service and print the net bonus amount.

salary=float(input("Enter Your Salary: "))

service=int(input("Enter Years of Service: "))

if service>5:

    bonus=salary*0.05

    print(f"Your Net Bonus is: {bonus}")

else:

    print("No Bonus. Service year is less than 5 years.")

#16.A utility company charges different rates based on electricity usage.

units=int(input("Enter Units of Electricity Used: "))

if units<=100:

    total_cost=units*5

    print(f"The Cost of {units} units of electricity is Rs {total_cost}")

elif units>100 and units<=300:

    total_cost=((units-100)*8)+500

    print(f"The Cost of {units} units of electricity is Rs {total_cost}")

else:

    total_cost=((units-300)*10)+2100

    print(f"The Cost of {units} units of electricity is Rs {total_cost}")

#18. Write a Python program that takes a number as input, first checks if it is positive if yes then

# check whether it is even or odd.

num=int(input("Enter Your Number: "))

if num>0:

    if num%2==0:

        print("Positive Even Number")

    else:

        print("Positive Odd Number")

else:

    print("Negative Number")

#20. Create a weight conversion program.

earth_weight=float(input("Enter Your Earth Weight: "))

planet_no=int(input("Enter Planet Number from 1-7: "))

match planet_no:

    case 1:

        print("Weight on Mercury is:", earth_weight*0.38)

    case 2:

        print("Weight on Venus is:", earth_weight*0.91)

    case 3:

        print("Weight on Mars is:", earth_weight*0.38)

    case 4:

        print("Weight on Jupiter is:", earth_weight*2.53)

    case 5:

        print("Weight on Saturn is:", earth_weight*1.07)

    case 6:

        print("Weight on Uranus is:", earth_weight*0.89)

    case 7:

        print("Weight on Neptune is:", earth_weight*1.14)

    case _:

        print("Invalid Planet Number")

#21. WAP which accepts marks of four subjects and display total marks, percentage and grade.

eng=float(input("Enter Marks for English: "))

math=float(input("Enter Marks for Maths: "))

sci=float(input("Enter Marks for Science: "))

comp=float(input("Enter Marks for Computer: "))

grand_total=eng+math+sci+comp

percentage=grand_total/4

if percentage>70:

    print(f"Total Marks:{grand_total}")

    print(f"Percentage:{percentage}")

    print("Grade: Distinction")

elif percentage>60:

    print(f"Total Marks:{grand_total}")

    print(f"Percentage:{percentage}")

    print("Grade: First")

elif percentage>40:

    print(f"Total Marks:{grand_total}")

    print(f"Percentage:{percentage}")

    print("Grade: Pass")

else:

    print(f"Total Marks:{grand_total}")

    print(f"Percentage:{percentage}")

    print("Grade: Fail")

#21. Write a program that simulates the elevator's internal logic.

target_floor=int(input("Enter Desired Floor: "))

current_load=float(input("Enter Current Weight Load in Lift: "))

door_state=int(input("Enter Door Status\n1.Closed\n2.Open or Not Fully Closed\n: "))

if target_floor>=0 and target_floor<=10:

    if current_load<=500:

        if door_state==1:

            print("ACTIVATE ELEVATOR MOTION")

        else:

            print("WARNING: CLOSE THE DOOR")

    else:

        print("OVERWEIGHT: LIFT CANNOT MOVE")

else:

    print("INVALID FLOOR")