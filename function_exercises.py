# Print statements in functions are to verify output


#1 takes a number and determines if divisble by two
def is_two(n):
    if n ==2 or n == int(2) or n == 2.0:
        #print("True")
        return True
    else:
        #print("False")
        return False
is_two(2)


#2 takes a string and determines 
def is_vowel(vowel):
    if type(vowel) == str:
        if len(vowel.lower()) == 1 and vowel.lower() in ["a","e","i","o","u"]:
            #print("True")
            return True
        else:
            #print("False")
            return False
        
        return True
    else:
        #print("False")
        return False
    
    
        
is_vowel("a")

#3
def is_consonant(const):
    if type(const) == str:
        if const.lower() in ["b","c","d","f","g","h","j",
                            "k","l","m","n","p","q","r","s",
                            "t","v","w","x","y","z"]:
            #print("True")
            return True
        else:
            #print("False")
            return False
    else:
        return False

#is_consonant("4")

#4
def capitalizer(word):
    if type(word) == str:
        if word[0] in ["b","c","d","f","g","h","j",
                    "k","l","m","n","p","q","r","s",
                    "t","v","w","x","y","z"]:
            print(str.capitalize(word))
            return str.capitalize(word)
    else:
        return False

#capitalizer("superhuman")


#5
def calculate_tip(tip, bill):
    tip = float(tip)
    bill = float(bill)
    total_tip = float(tip * bill)
    #print(f"amount to tip is: ${total_tip}")
    return tip * bill

# calculate_tip(.2 ,70)


#6 
def apply_discount(price,disc_per):
    price = float(price)
    disc_per = float(disc_per) 
    total_amount = (1 - disc_per)*(price)
    #print(f"Discounted price is: {total_amount}")
    return price

#apply_discount(120,.2)

#7
def handle_commas(n): 
    if type(n) == str:
        if ","  in n:
            n = n.replace(",","")
            #print(n)
            return(n)
        else:
            return False
    else:
        return False

#handle_commas("1,000,000")


#8 # fix
def get_letter_grade(grade):
    if type(grade) == int:
        if grade in range(88,101):
            #print("Your grade is A.")
            return "A"
        elif grade in range(80,88):
            #print("Your grade is B.")
            return "B"
        elif grade in range(67,80):
            #print("Your grade is C.")
            return "C"
        elif grade in range(60,67):
            #print("Your grade is D.")
            return "D"
        elif grade in range(0,60):
            #print("Your grade is F.")
            return "F"
    
#get_letter_grade(99)

#9
def remove_vowels(word): # list comprehension
    vowels = ["a","e","i","o","u"]
    remove_list = [w for w in word if w not in vowels]
    new_word= "".join(remove_list)
    #print(new_word)
    return(new_word)  

    # vs adding to remove (Instructor Notes)
    # remove = []
    # for letter in word:
    #     if letter not in vowels: # if letter is not a vowel add to empty list
    #         remove.append(letter)
    # remove_vowels('yeah')

# remove_vowels("supercallfrajaeeeee")


#10 -- fix
# def normalize_name(name):
#     alph = ["a","b","c","d","e","f","g","h","i","j",
#                 "k","l","m","n","o","p","q","r","s",
#                 "t","u","v","w","x","y","z"]
    
#     numby = range(1,100000000)  
#     while name[0].lower() not in alph:
#         name = name.replace(name[0],"")

#     while len(name.lower()) not in numby:
#         name = name.replace(name,"")
#     name = name.lower()
#     name = name.strip()
#     name = name.replace(" ","_")
#     print(name)
#     return(name)

def normalize_name(somestr):
    new_string = ''
    somestr = somestr.strip().lower()
    for char in somestr:
        if char.isalpha() or char == ' ':
                 new_string+= char 
    
        fix = new_string.strip().replace(' ', '_') 
    print(fix)
    return fix

#normalize_name("%$$$$Stanley#$$%())) Burke")

#11 
numbys = [1,2,3,4]       
def cumulative_sum(a):
    total = 0
    listy = []
    for n in numbys:
        total += n
        listy.append(total)
    #print(listy)
    return listy
        

# cumulative_sum(numbys)

#split(":") can split 10:45 at  ":" for example  10:00 would be [10,00]

