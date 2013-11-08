#coding=latin1
'''
Created on 28 okt 2013

@author: MJ & YJ
'''

from queue import Queue

mening = input("Skriv en mening: ")

myq = Queue()
for ordet in mening.split():  # dela upp meningen i ord
    myq.put(ordet)            # och sätt in varje ord i kön

while not myq.isEmpty():      # alla köns element
    print(myq.get())          # skrivs ut

print()                       # tom rad
print(myq.get())              # None skrivs ut eftersom kön är tom