user_response=input("Please enter a temperature in celsius: ")
Celsius=float(user_response)
Fahrenheit=((Celsius*9)/5)+32
print(Fahrenheit)
if Fahrenheit>90:
    print("It is hot")
else:
    print("It is not hot")
   
