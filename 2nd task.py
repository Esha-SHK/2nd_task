# nested if 1st program

age = 25
country = "USA"
if country == "USA":
    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote yet")
else:
    print("Eligibility criteria may vary by country")

# nested if 2nd program    

age = 30
member = True
if age > 18:
    if member:
        print("Ticket price is $12.")
    else:
        print("Ticket price is $20.")
else:
    if member:
        print("Ticket price is $8.")
    else:
        print("Ticket price is $10.")


# for loop 1st program        

colors=["Red,Green,Yellow,Purple,Black"]
for color in colors:
   print(color)
   for i in color:
      print(i,end=", ")


# for loop 2nd program      

for table in range(15):
    if(table==10):
          break
    print("4*",table+1,"=",4*(table+1)) 
