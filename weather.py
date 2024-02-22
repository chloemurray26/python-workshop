tempature = int(input("What's the tempature outside?    "))

if tempature > 80:
    print("It's too hot!")
    print("Stay inside.")
elif tempature < 60:
    print("It's too cold!")
    print("Stay inside.")
else:
    print("Enjoy the outdoors.")

weather = int(input("What the temperature outside?  "))
if weather > 80 or weather < 60:
    print("Stay inside.")
else:
    print("Enjoy the outdoors")