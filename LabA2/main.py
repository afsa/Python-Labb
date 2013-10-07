#coding=latin1
'''
Created on 1 okt 2013

@author: MJ
'''

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
    numbers = []
    
    for i in range(2, n):
        numbers.append(i)
    
    for number in numbers:
        if number**2 > n:
            break
        
        for checkNumber in numbers:
            if checkNumber != number and checkNumber%number == 0:
                numbers.remove(checkNumber)
    
    return numbers

print(getPrimes(10000))
    