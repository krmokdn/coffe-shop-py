# Convert given scenario to python code
# After python exam , you decided to quit school and open a coffee shop
# It turns out that business is really good and you are making more money than you could earn in a job.
# You are selling 3 different coffee Latte, Mocha and Ice Chocolate Mocha
# There are 3 different size for your coffees , Tall,Grande and Vetti
# Base prices for coffees are 3 TL, 4 TL and 10 TL
# Based on size, prices are multiplied by 1.25, 1.5 or 2
# If customer want to add sugar , it costs 1 TL
# Ask user to what would he/she want to buy, with the choice of size and if he/she wants sugar?
# P.S : Only enter valid inputs

coffe_type= int(input("Please write your coffe type(Latte(1),Mocha(2),Aysçokaboka(3)):"))



if coffe_type == 1 :
   base_price= 3

elif coffe_type == 2 :
    base_price = 4

elif coffe_type == 4 :
    base_price = 10

else:
    print("You typed wrong name")

print(base_price)

coffe_size = int(input("Please enter your coffe size(Tall(1),grande(2),vetti(3)):"))

if coffe_size == 1:
    baseprice2= base_price*1.25

elif coffe_size == 2:
    baseprice2 = base_price * 1.5

elif coffe_size == 3:
    baseprice2 = base_price * 2

else:
    print("You typed wrong name")

print("Your price is",baseprice2 )

sugar= int(input("Do you want sugar(Yes(1) or No(0)):"))

if sugar == 1:
   price = baseprice2 + 1

elif sugar == 0:
    baseprice2 = price

else:
    print("You typed wrong name")

print("Your last price is:",price)
