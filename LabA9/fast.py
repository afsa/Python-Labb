#coding=latin1
'''
Created on 11 nov 2013

@author: MJ & YJ
'''
import time;

class WideSearch:
    
    def __init__(self):
        self.allWords = self.readFile();
        self.chars = "abcdefghijklmnoprstuvxyzåäö";
    
    def getChildren(self, parent):
        children = set();
        for i in range(3):
            for j in self.chars:
                temp = parent[0:i] + j + parent[i+1:3];
                if temp in self.allWords and temp not in self.used:
                    children.add(temp);
                    self.used.add(temp);
                    self.hierarchy[temp] = parent;
        return children;
    
    def search(self, start, target):
        self.target = None;
        self.used = set();
        self.hierarchy = {};
        
        if start not in self.allWords:
            print("Start not found");
        
        if start == target:
            print("Search completed in 0 jumps.")
            print(start);
        
        self.target = target;
        self.used.add(start);
        self.hierarchy[start] = None;
        
        nodes = set();
        nodes.add(start);
        
        while True:
            children = set();
            for word in nodes:
                tempChildren = self.getChildren(word);
                
                if target in tempChildren:
                    return self.getAnswer(self.target);
                children = children | tempChildren;
            nodes = children;
            children = set();
    
    def findLongest(self, target, more = False):
        self.used = set();
        self.hierarchy = {};
          
        self.used.add(target);
        self.hierarchy[target] = None;
        
        nodes = set();
        nodes.add(target);
        
        while True:
            children = set();
            for word in nodes:
                tempChildren = self.getChildren(word);
                children = children | tempChildren;
            
            if not children:
                if not more:
                    return self.getAnswer(nodes.pop(), True, True);
                else:
                    tempNodes = nodes;
                    temp = nodes.pop();
                    return self.getAnswer(temp, True, True), self.getLength(temp), tempNodes;
            
            nodes = children;
            children = set();
            
    def getLongestInList(self):
        longest = 0;
        longestHierarchy = None;
        usedTargets = set();
        for target in self.allWords:
            if target in usedTargets:
                continue;
            
            a,b,c = self.findLongest(target, True);
            usedTargets.add(target);
            
            if b > longest:
                longest = b;
                longestHierarchy = a;
        
        return longestHierarchy, longest;
        
    def readFile(self):
        f = open("word3.txt");
        return set(f.read().split("\n"));
    
    def getAnswer(self, word, first = True, invert = False):
        return ((" <- " if not invert else " -> ") if not first else "") + word + (self.getAnswer(self.hierarchy[word], False, invert) if self.hierarchy[word] else "");
    
    def getLength(self, word):
        return 1 + (self.getLength(self.hierarchy[word]) if self.hierarchy[word] else 0);
    
test = WideSearch();
print(test.search("dum", "vis"));
print(test.search("blå", "röd"));
print(test.search("fan", "gud"));

print(test.findLongest("bla"));
print(test.findLongest("vis"));

timestamp = time.time();
data = test.getLongestInList();
print("Maximum jumps", data[1])
print(data[0]);
print("It took", int(time.time() - timestamp), "s to run");
