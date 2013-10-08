#coding=latin1
'''
Created on 1 okt 2013

@author: MJ
'''
import time

# Bygg en sträng med utseende av en kub
def getRect(marginLeft, height, width, char):
    output = ""
    
    for _ in range(height):
        output += marginLeft * " " + width * char + "\n"
        
    return output

# Bygg en sträng med utseende av en ram
def getFrame(height, width, border):
    output = ""
    
    for i in range(height):
        if i >= border and i < (height - border):
            output += border * "*" +  (width - 2 * border) * " "  + border * "*" + "\n"
        else:
            output += width * "*" + "\n"
    
    return output

# Bygg en sträng med utseende av nedåtvänd triangel
def getDSTriangle(marginLeft, base):
    output = ""
    
    if base%2 == 0:
        base += 1
    
    for i in range(base//2 + 1):
        output += (marginLeft + i) * " " + (base - 2 * i) * "*" + "\n"
        
    return output

# Bygg en sträng med utseende av uppåtvänd triangel
def getUSTriangle(marginLeft, base):
    output = ""
    
    if base%2 == 0:
        base += 1
    
    for i in range(base//2 + 1):
        output += (marginLeft + base//2 - i) * " " + (2 * i + 1) * "*" + "\n"
    
    return output
    
# Bygg en sträng med utseende av en romb    
def getDiamond(marginLeft, base):
    return getUSTriangle(marginLeft, base) + getDSTriangle(marginLeft + 1, base - 2)

# Hitta alla printal p < n
def getPrimes(n):
    numbers = {}
    
    for i in range(2, n):
        numbers[i] = True
    
    for number in numbers:
        if number**2 > n:
            break
        
        if not numbers[number]:
            continue
        
        for checkNumber in range(number**2, n, number):
            numbers[checkNumber] = False
                
    primes = []
    
    for isPrime in numbers:
        if numbers[isPrime]:
            primes.append(isPrime)
    
    return primes

# Starta laborationen 
def main():
    print()
    start = input("Starta uppgift 1, 2, 3, 4, 5 eller 6? ")
    if start.isdigit() and int(start) < 7 and int(start) > 0:
        start = int(start)
        if start == 1:
            margin = input("Marginal till vänster: ")
            height = input("Antal rader: ")
            width = input("Antal kolumner: ")
            char = input("Tecken: ")
            if margin.isdigit() and height.isdigit() and width.isdigit():
                print(getRect(int(margin), int(height), int(width), char))
            else:
                print("Error: Marginal, rader och kolumner måste vara tal")
        
        if start == 2:
            border = input("Tjocklek på ram: ")
            height = input("Antal rader: ")
            width = input("Antal kolumner: ")
            if border.isdigit() and height.isdigit() and width.isdigit():
                print(getFrame(int(height), int(width), int(border)))
            else:
                print("Error: Tjocklek på ram, rader och kolumner måste vara tal")
        
        if start == 3:
            margin = input("Marginal: ")
            base = input("Bas: ")
            if base.isdigit() and margin.isdigit():
                print(getDSTriangle(int(margin), int(base)))
            else:
                print("Error: Marginal och bas måste vara tal")
                
        if start == 4:
            margin = input("Marginal: ")
            base = input("Bas: ")
            if base.isdigit() and margin.isdigit():
                print(getUSTriangle(int(margin), int(base)))
            else:
                print("Error: Marginal och bas måste vara tal")
                
        if start == 5:
            margin = input("Marginal: ")
            base = input("Bas: ")
            if base.isdigit() and margin.isdigit():
                print(getDiamond(int(margin), int(base)))
            else:
                print("Error: Marginal och bas måste vara tal")
                
        if start == 6:
            n = input("Hitta primtal mindre än: ")
            if n.isdigit():
                print(getPrimes(int(n)))
            else:
                print("Error: Gränsen till störtsa primtal måste vara ett tal")
    else:
        print("Error: Indata kan endast vara 1 till 6")

if __name__ == "__main__":
    main()