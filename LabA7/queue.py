#coding=latin1
'''
Created on 8 nov 2013

@author: MJ & YJ
'''

class Queue:    
    def __init__(self):
        self.first = None;
        self.last = None;
    
    def isEmpty(self):
        return True if self.first == None else False;
    
    def hasNext(self):
        return True if self.first != None else False;
    
    def get(self):
        if self.hasNext():
            temp = self.first.getValue();
            self.first = self.first.getNext()
            return temp;
        return None;
    
    def put(self, obj):
        tempObj = QueueItem(obj);
        if self.last != None:
            self.last.setNext(tempObj);
        
        if self.first == None:
            self.first = tempObj;
                        
        self.last = tempObj;
        
class QueueItem:
    def __init__(self, item = None, nextItem = None):
        self.item = item;
        self.nextItem = nextItem;
        
    def getValue(self):
        return self.item;
        
    def getNext(self):
        return self.nextItem;
        
    def setNext(self, obj):
        self.nextItem = obj;
        
        