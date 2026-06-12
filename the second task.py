temperature = float(input("enter the temperature in celsius: "))
if temperature >= 30:
    print("It's a hot day. Stay hydrated!")
elif temperature >= 20 and temperature <= 29:
    print("It's a warm day. Enjoy the weather!")
elif temperature >= 10 and temperature <= 19:
    print("It's a cool day. Wear a jacket!")
elif temperature < 10:
    print("It's a cold day. Stay warm!")