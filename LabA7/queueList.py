#coding=latin1
'''
Created on 1 okt 2013

@author: MJ and YJ
'''

class Queue():
        
    def __init__(self):
        self.queue = [];
    
    def put(self, x):
        self.queue.append(x);
    
    def get(self):
        return self.queue.pop(0) if not self.isEmpty() else None;
    
    def isEmpty(self):
        return len(self.queue) == 0;
    
    def hasNext(self):
        return len(self.queue) != 0;