speed = int(input("Welcome, please insert speed:"))

if speed <= 0:
    print("invalid speed")
elif speed > 0 and speed <= 30:
    print("tpp slow")
elif speed > 30 and speed <= 120:
    print("good")
else:
    print("too fast")
