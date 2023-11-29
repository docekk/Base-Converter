allCharList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = int(input("Number: "))
base = int(input("Base: ")) # 2-36
cycle = 0
highestPower = 0
poweredNumber = pow(base,cycle)
output = "Your Converted Number: "

while True: # Find Highest Power
    if poweredNumber > number:
        cycle -= 1
        highestPower=cycle
        break
    cycle += 1
    poweredNumber = pow(base,cycle)

while highestPower != -1: # Convert
    i = 0
    poweredNumber = pow(base,highestPower)
    
    if poweredNumber <= number:
        i = number // poweredNumber
        number -= poweredNumber * i

    output += str(allCharList[i])
    highestPower -= 1

print(output)