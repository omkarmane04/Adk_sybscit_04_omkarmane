import datetime
name =input("Hello! enter the name =")
age =int(input("enter the age ="))
year_now = datetime.datetime.now()
print("You will turn 100 in " + str(int(100-age) + int(year_now.year)))
               
 
