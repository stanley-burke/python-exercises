print(type(99.9))
print("False")
print(type(False))
print(type('0'))
print(type(0))
print(type(True))
print(type('True'))
print(type([{}]))
print(type({'a':[]}))
# print(type([])
      
# -- 2
# 
# What data type would best represent the following?

# A term or phrase typed into a search box - string
# Whether or not a user is logged in - boolean
# A discount amount to apply to a user's shopping cart - float
# Whether or not a coupon code is valid - boolean
# An email address typed into a registration form - string
# The price of a product - float
# The email addresses collected from a registration form - list
# Information about applicants to Codeup's data science program - dictionary
# 
# '1' + 2 = concat error

# 6 % 4 = 2

# type(6 % 4) = 2

# type(type(6 % 4)) = int

# '3 + 4 is ' + 3 + 4 = error

# 0 < 0 = False

# 'False' == False = False

# True == 'True' = False

# 5 >= -5 True

# True or "42" = True

# 6 % 5  1 = True

# 5 < 4 and 1 == 1 = False

# 'codeup' == 'codeup' and 'codeup' == 'Codeup' = False

# 4 >= 0 and 1 !== '1' error

# 6 % 3 == 0 True

# 5 % 2 != 0 True

# [1] + 2 cant concat int to list

# [1] + [2] [1,2]

# [1] * 2 [1,1]

# [1] * [2] cant multiply lists

# [] + [] == [] True

# {} + {} cant concat dictionaries

# 4. You have rented some movies for your kids:

# The Little Mermaid for 3 days
# Brother Bear for 5 days
# Hercules for 1 day
# If the daily fee to rent a movie is 3 dollars, how much will you have to pay? $27

mermaid = 3
brother_bear = 5
hercules = 1
fees = 3
print((mermaid*fees)+(brother_bear*fees)+ (hercules*fees))

# 5. Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook.

# They pay you the following hourly rates:

# Google: 400 dollars
# Amazon: 380 dollars
# Facebook: 350 dollars
# This week you worked: 10 hours for Facebook, 6 hours for Google, and 4 hours for Amazon.

# How much will you receive in payment for this week? $7,420
google = 400
amazon = 380
facebook = 350
f_hours = 10
a_hours = 4
g_hours = 6
print((google*g_hours)+(facebook*f_hours)+(amazon*a_hours))

# 6. A student can be enrolled in a class only if the class is not full and the class schedule does not conflict with her current schedule.
not_full = True
no_conflict = True
not_full and no_conflict

# 7. A product offer can be applied only if a customer buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.
items_bought = 5
items_bought >= 2
offer_expired = False
if_premium = True

print((items_bought and offer_expired )or if_premium)

# 8. Use the following code to follow the instructions below:


# username = 'codeup'
# password = 'notastrongpassword'
# Create a variable that holds a boolean value for each of the following conditions:

# The password must be at least 5 characters
# The username must be no more than 20 characters
# The password must not be the same as the username
# Bonus Neither the username or password can start nor end with whitespace
username = 'codeup'
password = 'notastrongpassword'
pass_def = (int(len(password )) > 5 and int(len(username)) < 20 and password != username and password == str.strip(password) 
            and username == str.strip(username))

if(pass_def):
    print("This password meets all standards.")
else:
    print("This password is not up to par!")




