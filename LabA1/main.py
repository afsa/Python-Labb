#coding=latin1
'''
Created on 1 okt 2013

@author: MJ
'''

# Beräkna den kubiska summan av talen a och b
def calculateSum():
    print()
    a = input("Skriv talet A: ")
    b = input("Skriv talet B: ")
    
    if a.isdigit() and b.isdigit():
        print("Kubiksumma = ", int(a)**3 + int(b)**3)
    else:
        print("Error: Både A och B måste vara tal.")
        
# Hitta alla tal a och b sådana att den kubiska summan av a och b är n
def kubpar(n):
    pairs = []    
    a = 1
    while a**3 < n/2:
        foo = n - a**3
        bar = round((foo)**(1./3))
        if bar**3 == foo:
            pairs.append((a, bar))
        a += 1
    
    return pairs

def minRamanujan(m):
    output = []
    
    i = 0
    antal = 0
    
    while True:
        dummy = kubpar(i)
        
        if dummy:
            output.append((i, dummy))
            antal += 1
        
        if antal == m:
            break 
        
        i += 1
    
    return output
        

# Starta laborationen 
def main():
    print()
    start = input("Starta uppgift 1, 2 eller 3? ")
    if start.isdigit() and int(start) == 1:
        calculateSum()
    elif start.isdigit() and int(start) == 2:
        print()
        theSum = input("Skriv kubiksumman av två tal: ")
        if theSum.isdigit():
            print(kubpar(int(theSum)))
        else:
            print("Error: Summan måste vara ett tal.")  
    elif start.isdigit() and int(start) == 3:
        print()
        m = input("Hitta de m första Ramanujan tal. m= ")
        if m.isdigit():
            lists = minRamanujan(int(m))
            for foo in lists:
                print(foo)
        else:
            print("Error: Summan måste vara ett tal.")
    else:
        print("Error: Indata kan endast vara 1 eller 2")

if __name__ == "__main__":
    main() 