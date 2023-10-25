# 1A
day_of_week = input("What day of the week is it?\n").lower()
if(day_of_week == "monday"):
    print(f"Today is {day_of_week}, time to get it in gear")
else:
    print(f"It's not Monday, it's {day_of_week}, so that's a win.")

# 1B
day_of_week = input("What day of the week is it?\n").lower()
weekdays = ["monday","tuesday,","wednesday","thursday"]
weekend = ["friday","saturday","sunday"]

if(day_of_week in weekdays):
    print(f"Today is {day_of_week}, time to get it in gear")
elif(day_of_week in weekend):
    print(f"It's not Monday, it's {day_of_week}, its the weekend that's a win.")

#1C

weekly_hours = int(input(f"How many hours do you work in a week?\n"))
hourly_rate = 50
weekly_pay = float(0)

if(weekly_hours <= 40):
    weekly_pay = hourly_rate * weekly_hours
elif(weekly_hours > 40):
    weekly_pay = (weekly_hours -40)* (hourly_rate *  1.5)+((40 * hourly_rate))
print(f"Your pay for the week including overtime is {weekly_pay}.")


#2A
i = 5
while i <= 15:
    print(i)
    i += 1
    

#2Ai
i = 0
while i <= 100:
    print(i)
    i += 2

#2Aii
i = 2
while i <= 1000000:
    print(i)
    i = i*i
   
    
#2Aii 
i = 100
print(i)
i -= 5


number = int(input("enter a number\n"))
for n in range(1,11):
    mult = n * number
    print(f"{number} * {n} = {mult}")

#2ii
for i in range(1,10):
    print(str(i)*i)
    
#cii
integer = int(input("Enter a positive integer\n"))
for n in range(integer,0,-1):
    print(n)
         
#ciii
integer = int(input("Enter a positive integer\n"))
for n in range(0,integer+1,1):
    print(n)

#ciii
integer = input("Enter a positive odd integer between 1 and 50\n")
while integer.isdigit() == False or int(integer) > 50 or int(integer) < 0 or int(integer) % 2 == 0:
    integer = input("INVALID ENTRY! Enter a positive odd integer between 1 and 50\n")
print(f"Number to skip is: {integer}\n")
for r in range(0,51):
    if( r == int(integer)):
        print(f"Yikes skipping number: {r}")
        continue
    elif(r % 2 != 0):
            print(f"Here is an odd number: {r}")
    
        
        

#3 Fizzbuzz
for r in range(1,101):
    if r % 3 == 0 and r % 5 == 0:
        print("FizzBuzz")
    elif r % 5 == 0:
        print("Buzz") 
    elif r %  3 == 0:
        print("Fizz")
    else:
        print(r)



   

#4
keep_going = "yes"
while keep_going == "yes":
    answer = int(input('Enter an integer: '))
    print(f'number | squared | cubed ')
    print(f'-------|-------|-------')
    for n in range(1,answer+1):
        print(f'{n:<7} |{n**2} |{n**3}')
    keep_going = input("Would you like to continue?")

    


# 5
grade = int(input("What score did you make on the test?\n"))
if grade in range(88,101):
        print("Your grade is A.")
elif grade in range(80,88):
    print("Your grade is B.")
elif grade in range(67,80):
    print("Your grade is C.")
elif grade in range(60,67):
    print("Your grade is D.")
elif grade in range(0,60):
    print("Your grade is F.")

while grade < 101:
    grade = int(input("If you want to continue, enter the score you made on the next test?\n"))
    if grade in range(88,101):
        print("Your grade is A.")
    elif grade in range(80,88):
        print("Your grade is B.")
    elif grade in range(67,80):
        print("Your grade is C.")
    elif grade in range(60,67):
        print("Your grade is D.")
    elif grade in range(0,60):
        print("Your grade is F.")

print("I guess you are done then, BYE")   

#6

books =[{"title":"insomnia","author":"s_king","genre":"horror"},
        {"title":"pet_semetary","author":"s_king","genre":"horror"},
        {"title":"the_mist","author":"s_king","genre":"horror"},
        {"title":"cloud_guardians","author":"g_bettwny","genre":"educational"},
         {"title":"the_talisman","author":"p_straub","genre":"thriller"}]

choice = input("Enter a genre of book you like\n")
for book in books:
    if choice == (book["genre"]):
        print(f"You like will like the book "+book["title"])
    
    else:
        pass
        
       



