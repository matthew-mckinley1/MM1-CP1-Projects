#Matthew McKinley Celsius to Fahrenheit

celsius = input("What celsius temperature do you want changed?")
celsius = int(celsius)
fahrenheit = float((celsius * 9/5)+32)
fahrenheit = str(fahrenheit)
celsius = str(celsius)
print("When it is "+celsius,"degrees celsius, it is "+fahrenheit,"degrees fahrenheit")