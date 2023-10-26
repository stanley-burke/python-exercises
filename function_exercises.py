# Print statements in methods are to verify output

#1
def is_two(n):
    if n ==2 or n == int(2):
        print("True")
        return True
    else:
        print("False")
        return False
is_two(2)


#2
def is_vowel(vowel):
    if vowel.lower() in ["a","e","i","o","u"]:
        print("True")
        return True
    else:
        print("False")
        return False
is_vowel("w")

#3
def is_consonant(const):
    if const.lower() in ["b","c","d","f","g","h","j",
                         "k","l","m","n","p","q","r","s",
                         "t","v","w","x","y","z"]:
        print("True")
        return True
    else:
        print("False")
        return False

is_consonant("y")

#4
def capitalizer(word):
    if word[0] in ["b","c","d","f","g","h","j",
                "k","l","m","n","p","q","r","s",
                "t","v","w","x","y","z"]:
        print(str.capitalize(word))

capitalizer("superhuman")


#5
def calculate_tip(tip, bill):
    tip = float(tip)
    bill = float(bill)
    total_tip = tip * bill
    print(f"amount to tip is: {total_tip}")
    return tip * bill

calculate_tip(.05,100)


#6
def apply_discount(price,disc_per):
    price = float(price)
    disc_per = float(disc_per) * price
    total_amount = price - disc_per
    print(f"Discounted price is: {total_amount}")
    return price

apply_discount(100,.05)

#7
def handle_commas(n):
 if ","  in n:
     n = n.replace(",","")
     print(n)
     return(n)

handle_commas("1,000,000")


#8
def get_letter_grade(grade):
    grade = int(grade)
    if grade in range(88,101):
        print("Your grade is A.")
        return "A"
    elif grade in range(80,88):
        print("Your grade is B.")
        return "B"
    elif grade in range(67,80):
        print("Your grade is C.")
        return "C"
    elif grade in range(60,67):
        print("Your grade is D.")
        return "D"
    elif grade in range(0,60):
        print("Your grade is F.")
        return "F"
    
get_letter_grade(99)


#9
def remove_vowels(word):
    vowels = ["a","e","i","o","u"]
    remove = [w for w in word if w not in vowels]
    new_word= "".join(remove)
    print(new_word)
    return(new_word)  
       
        

remove_vowels("supercallfrajaeeeee")


#10
def normalize_name(name):
    alph = ["a","b","c","d","e","f","g","h","i","j",
                "k","l","m","n","o","p","q","r","s",
                "t","u","v","w","x","y","z"]
       
    while name[0].lower() not in alph:
        name = name.replace(name[0],"")
    
    name = name.lower()
    name = name.replace(" ","_")
    name = name.strip()
    print(name)
    return(name)

normalize_name("%$$$$Stanley Burke")

#11
numbys = [1,2,3,4]       
def cumulative_sum(a):
    total = 0
    listy = []
    for n in numbys:
        total += n
        listy.append(total)
    print(listy)
    return listy
        

cumulative_sum(numbys)