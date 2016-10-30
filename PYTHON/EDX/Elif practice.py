user_response=input("Please enter a temperature in celsius: ")
Celsius=float(user_response)
Fahrenheit=((Celsius*9)/5)+32
print("The temperature is", Fahrenheit, "ºF")
if Fahrenheit<32:
    print("It is freezing")
elif Fahrenheit<50:
    print("It is chilly")
elif Fahrenheit<90:
    print("It is OK")
else:
    print("It is hot")

