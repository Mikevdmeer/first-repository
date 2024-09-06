a=5
b=3
c=2

# if statement 1
if (a==6 and b==4 or c==2):
   print("De conditie is waar")
else: 
   print("De conditie is niet waar")    

# if statement 2
if (a==6 and (b==4 or c==2)):
   print("De conditie is waar")
else:
   print("De conditie is niet waar")


print("UITLEG: 1. Dit controleert voor 6 of 4 of 2, if statement 2 controleert voor 6 EN 4 of 2.")