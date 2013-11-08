#coding=latin1
'''
Created on 28 okt 2013

@author: MJ & YJ
'''

class WordPair():
    def __init__(self, word1 = None, word2 = None, minRight = 2):
        self.word1 = word1;
        self.word2 = word2;
        self.rightAnswers = 0;
        self.minRight = minRight;
    
    def __str__(self):
        return self.word1[0].upper() + self.word1[1:] + "?";
    
    def checkAnswer(self, test):
        verdict = self.word2.lower() == test.lower();
        if verdict:
            self.rightAnswers += 1;
        return True if self.rightAnswers == self.minRight else False, verdict;