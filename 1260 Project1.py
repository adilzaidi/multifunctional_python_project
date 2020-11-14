import math
import random

#created by Adil

def prob1():
    repeat=1
    while repeat==1:
        b=int(input("Enter the deposit amount: "))
        r=int(input("Enter the interest rate in % : "))
        r_actual=r/100
        n=int(input("Enter the year (to see the balance): "))
        x=(1+r_actual)**n
        balance=b*x
        print(balance)
        user_inp=int(input("Do you want to re_run the program (1)Yes (0) No: "))
        if user_inp == 0:
            break
        else:
            repeat=1
prob1()

def prob2():
    repeat=1
    while repeat==1:
        a=int(input("Please enter the a value: "))
        b=int(input("Please enter the b value: "))
        c=int(input("Please enter the c value: "))
        inside_sqrt=((b**2)-(4*a*c))
        denomiter=2*a
        neg_b= -1*b
        sqrt_val= math.sqrt(inside_sqrt)
        x_pos=((neg_b + sqrt_val)/denomiter)
        x_neg=((neg_b - sqrt_val)/denomiter)
        print("x values: ",x_pos,",",x_neg)
        user_inp=int(input("Do you want to re_run the program (1)Yes (0) No: "))
        if user_inp == 0:
            break
        else:
            repeat=1
prob2()

def prob3():
    repeat=1
    while repeat==1:
        system=input("Would you like to use (M)Metric or (E)English system: ")
        if system == 'E':
            h_english=float(input("Please enter height in inches: "))
            w_english=float(input("Please enter weight in pounds: "))
            BMI=(w_english/(h_english**2))*703
        elif system == 'M':
            h_metric=float(input("Please enter height in meters: "))
            w_metric=float(input("Please enter weight in kilograms: "))
            BMI=(w_metric/(h_metric**2))
        else:
            print("Invalid, input")
        if BMI <= 24:
            print("Normal BMI")
            print("BMI: ",BMI)
        elif BMI >= 25 and BMI <= 29:
            print("OVERWEIGHT BMI")
            print("BMI: ",BMI)
        elif BMI >= 30 and BMI <= 39:
            print("OBESE")
            print("BMI: ",BMI)
        elif BMI > 40:
            print("EXTREME OBESITY")
            print("BMI: ",BMI)
        user_inp=int(input("Do you want to re_run the program (1)Yes (0) No: "))
        if user_inp == 0:
            break
        else:
            repeat=1
prob3()

def prob4():
    play_again=1
    while play_again > 0:
        num1=['Rock', 'Scissors','Paper']
        comps_choice=random.choice(num1)
        user_choice=input("Enter Rock, Scissors, Paper: ")
        if comps_choice == user_choice:
            print("Tie")
        elif user_choice == 'Rock' and comps_choice == 'Scissors':
            print("Computer chooses Scissors")
            print("User Won")
        elif user_choice == 'Rock' and comps_choice == 'Paper':
            print("Computer chooses Paper")
            print("Computer Won")
        elif user_choice == 'Scissors' and comps_choice == 'Rock':
            print("Computer chooses Rock")
            print("Computer Won")
        elif user_choice == 'Scissors' and comps_choice == 'Paper':
            print("Computer chooses Paper")
            print("User Won")
        elif user_choice == 'Paper' and comps_choice == 'Rock':
            print("Computer chooses Rock")
            print("User Won")
        elif user_choice == 'Paper' and comps_choice == 'Scissors':
            print("Computer chooses Scissor")
            print("Computer Won")
        p=int(input("Do you want to play again (1) Yes (0) No: "))
        if p==0:
            break
        else:
            play_again+=play_again
prob4()
    
        
        
        
        

            
        
    