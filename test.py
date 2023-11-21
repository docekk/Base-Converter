number = int(input())
base = 2
cycle = 0
poweredNumber = pow(base,cycle)
highestPower = 0
output = ""

while True:
    if poweredNumber > number:
        cycle -= 1
        highestPower=cycle
        break
    cycle += 1
    poweredNumber = pow(base,cycle)

while True:
    poweredNumber = pow(base,highestPower)

    if poweredNumber <= number:
        output += "1"
        number -= poweredNumber
    else:
        output += "0"
    
    highestPower -= 1
    if highestPower == -1:
        break

print(output)