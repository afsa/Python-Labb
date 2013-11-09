#coding=latin1
'''
Created on 8 nov 2013

@author: MJ & YJ
'''

from queue import Queue;
from random import randrange;

class RadixSort:
    buckets = [];
    
    def __init__(self, base = 10):
        self.base = base;
        self.createBuckets();
        
    def createBuckets(self):
        for i in range(self.base):
            self.buckets.insert(i, Queue());
        
    def sortQueue(self, numbers, n):
        for i in range(n):
            while numbers.hasNext():
                tempNr = numbers.get();
                
                selectedBucket = 0;
                
                if len(str(tempNr)) - 1 >= i:
                    selectedBucket = int(str(tempNr)[::-1][i]);
                    
                self.buckets[selectedBucket].put(tempNr);
            
            for j in range(self.base):
                while self.buckets[j].hasNext():
                    numbers.put(self.buckets[j].get());
        return numbers;
    
class SortFailedException(Exception):
    pass;
    
if __name__ == "__main__":
    try:
        m = int(input("M= "));
        n = int(input("N= "));
        print("Print sorted list? y/n");
        printList = input();
        
        queue = Queue();
        
        for _ in range(m):
            queue.put(randrange(0, 10**n));
         
        radixSort = RadixSort();
        sortedQueue = radixSort.sortQueue(queue, n);
        
        previous = 0;
        
        while sortedQueue.hasNext():
            temp = sortedQueue.get();            
            if previous > temp:
                raise SortFailedException;
            else:
                previous = temp;
                if printList == "y":
                    print(temp);
        
        print("Success");
    except(ValueError):
        print("Error! Input was not integers.");
    except(SortFailedException):
        print("Error! Sort failed!!!")