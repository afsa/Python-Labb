#coding=latin1
'''
Created on 1 okt 2013

@author: MJ and YJ
'''

class Queue():
    queue = [];
    
    def put(self, x):
        self.queue.append(x);
    
    def get(self):
        return self.queue.pop() if not self.isEmpty() else None;
    
    def isEmpty(self):
        return len(self.queue) == 0;