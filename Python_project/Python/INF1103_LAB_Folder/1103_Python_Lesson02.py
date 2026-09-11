for i in range(10):
    trafficlightcolour = input("Enter the traffic light colour (red, yellow, green): ").strip().lower() 
    if trafficlightcolour == "green":
        print("Go")
    elif trafficlightcolour == "yellow":
        print("Slow down")
    elif trafficlightcolour == "red":
        print("Stop")
    print(i)