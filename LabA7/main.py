#coding=latin1
'''
Created on 28 okt 2013

@author: MJ & YJ
'''

from queue import Queue;
from wordPair import WordPair;

class Glosor:
    
    def __init__(self, file):
        self.queue = Queue();
        self.createQueue(self.readFile(file));
        self.errors = 0;
    
    def start(self):
        self.executeQueue();        
    
    def readFile(self, file):
        f = open(file);
        return f.read().split("\n");
    
    def createQueue(self, inputList):
        listLength = len(inputList);
        
        start = 0;
        
        if listLength % 2 == 1:
            print(inputList[0]);
            start = 1;
        
        for i in range(start, listLength, 2):
            newWordElement = WordPair(inputList[i], inputList[i+1]);
            self.queue.put(newWordElement);
    
    def executeQueue(self):
        while self.queue.hasNext():
            words = self.queue.get();
            print(words);
            answer = input();
            isFinished, rightAnswer = words.checkAnswer(answer);
            
            if not isFinished:
                self.queue.put(words);
                
            if rightAnswer:
                print("Rätt svar!");
            else:
                self.errors += 1;
                print("Fel svar...")
        print("Glosförhör avslutat, du hade", self.errors, "fel.");

if __name__ == "__main__":
    glosor = Glosor("glosor.txt");
    glosor.start()