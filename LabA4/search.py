#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time

ordlst = [];

def initial():
    sys.setrecursionlimit(30000);
    fil = open("ordlistau", encoding = 'utf-8');
    global ordlst
    ordlst = fil.read().split('\n');

def linear_search(en_ord, ordlst):
    if not ordlst:
        return False;
    elif en_ord == ordlst[0]:
        return True;
    else:
        return linear_search(en_ord, ordlst[1:]);

def linsok(lista, elem):
    print ("Ditt ord: " + elem);
    if linear_search(elem, lista):
        print (elem + " finns");
    else:
        print (elem + " finns inte");
        
def binary_search(en_ord, ordlst):
    l = len(ordlst)//2;
    if not ordlst:
        return False;
    elif en_ord == ordlst[l]:
        return True;
    elif en_ord < ordlst[l]:
        return binary_search(en_ord, ordlst[0:l]);
    else:
        return binary_search(en_ord, ordlst[l+1:]);
    
def docking(en_ord):
    return en_ord[2:] + en_ord[:2];

def reverse(en_ord):
    if en_ord == "":
        return "";
    else:
        return en_ord[-1:] + reverse(en_ord[:-1]);

def the_filter (lista, search_func, change_func):
    if not lista:
        return [];
    elif search_func(change_func(lista[0]), lista[1:]):
        lst = the_filter(lista[1:], search_func, change_func);
        return [(lista[0] ,change_func(lista[0]))] + lst;
    else:
        return the_filter(lista[1:], search_func, change_func);

def linparsok(lista):
    return the_filter (lista, linear_search, docking);

def binparsok(lista):
    return the_filter (lista, binary_search, docking);

def binrevsok(lista):
    return the_filter (lista, binary_search, reverse);

def create_card (var):
    card = []
    for i in range(var):
        card.append(i);
    return card

def rifflar(lst, card, times=1):
    tmp = [];
    l = len(lst);
    for i in range(l//2):
        tmp.append(lst[i]);
        tmp.append(lst[i+l//2]);
    if tmp == card: 
        return times;
    else:
        return rifflar(tmp, card, times+1);

def show_card(ordlst):
    c = create_card(52);
    return (rifflar(c, c));

def get_input(func):
    ord = input("Write the word you want to search: ");
    if func(ord, ordlst):
        print (ord + " exists");
    else:
        print (ord + " doesn't exist");

def test(ordlst):
    word = "abcde";
    ordet = "ajour";
    ordet2 = "banan";
    print (docking(word));
    print (reverse(word));
    linsok(ordlst, ordet);
    linsok(ordlst, ordet2);
    print (linparsok(ordlst));
    print (binparsok(ordlst));
    print (binrevsok(ordlst));
    return "Test complete";
        
def main():
    try:
        lst = [[linear_search, True], [binary_search, True], 
               [linparsok, False], [binparsok, False], [binrevsok, False],
               [show_card, False], [test, False]];
        print("Choose what do you want to do:");
        print("1. Search if a word exist with linear search")
        print("2. Search if a word exist with binary search")
        print("3. Find all the word-pairs with linear search")
        print("4. Find all the word-pairs with binary search")
        print("5. Find all the reverse word-pairs with binary search")
        print("6. Find card thing")
        print("7. Run the test")
        print("8. Quit")
        ctrl = int(input());
    except: 
        print("ERROR\nNaN")
    if ctrl == 8:
        return 1;
    elif lst[ctrl-1][1]:
        get_input(lst[ctrl-1][0]);
        return 0;
    else:
        print (lst[ctrl-1][0](ordlst));
        return 0;

if __name__ == "__main__":
    initial();
    while(1):
        if main():
            break;
