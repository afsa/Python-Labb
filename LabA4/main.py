#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

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
        return the_filter(lista[1:], search_func, change_func );

def linparsok(lista):
    return the_filter (lista, linear_search, docking);

def binparsok(lista):
    return the_filter (lista, binary_search, docking);

def binrevsok(lista):
    return the_filter (lista, binary_search, reverse);
    
def test():
    word = "abcde";
    ordet = "ajour";
    ordet2 = "banan";
    print (docking(word));
    print (reverse(word));
    initial();
    linsok(ordlst, ordet);
    linsok(ordlst, ordet2);
    print (linparsok(ordlst));
    print (binparsok(ordlst));
    print (binrevsok(ordlst));

test();