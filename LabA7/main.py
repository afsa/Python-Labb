#coding=latin1
'''
Created on 28 okt 2013

@author: MJ & YJ
'''

from queue import Queue

mening = input("Skriv en mening: ")

myq = Queue()
for ordet in mening.split():  # dela upp meningen i ord
    myq.put(ordet)            # och s�tt in varje ord i k�n

while not myq.isEmpty():      # alla k�ns element
    print(myq.get())          # skrivs ut

print()                       # tom rad
print(myq.get())              # None skrivs ut eftersom k�n �r tom