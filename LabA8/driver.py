import bintree

def uppgift_1():
    tree = bintree.Bintree()
    print(tree.height())     # bör ge 0
    print(tree.isempty())    # bör ge True
    tree.put('solen')
    print(tree.isempty())    # bör ge False
    print(tree.height())     # bör ge 1
    tree.put('går')
    tree.put('sin')
    tree.put('höga')
    tree.put('ban')
    tree.put('uppå')
    tree.put('himlarunden')
    tree.put('månen')
    tree.put('seglar')
    tree.put('som')
    tree.put('en')
    tree.put('svan')
    tree.put('uti')
    tree.put('midnattsstunden')
    print(tree.exists('visa')) 
    print(tree.exists('ban'))  
    print(tree.printtree())
    print(tree.height())   

def uppgift_2():
    tree = bintree.Bintree();
    the15ord = open("15ordu", encoding = 'utf-8');
    ordlst = the15ord.read().split('\n');
    for i in ordlst:
        tree.put(i);
        
    print(tree.height());
    print(tree.printtree());
# Lösning: Sortera listan sen lägga man in element i mitten först. D.v.s. Binär inlägg.

def uppgift_3():
    tree = bintree.Bintree();
    words = open("word3u", encoding = 'utf-8');
    ordlst = words.read().split('\n');
    for i in ordlst:
        if not tree.put(i):
            print (i, end=' ');
            
    print ();

def uppgift_4():
    swetree = bintree.Bintree();
    engtree = bintree.Bintree();
    swe = open("word3u", encoding = 'UTF-8');
    eng = open("englishu", encoding = 'UTF-8');
    swelst = swe.read().split('\n');
    englst = eng.read().split();
    
    for i in swelst:
        swetree.put(i);
        
    for i in englst:
        if swetree.exists(i) and not engtree.exists(i):
            print (i, end=' ');
            engtree.put(i);
            
    print ();

def extra_uppgift():
    def go_lr(root, dire):
        if not root:
            return None;
        else:
            if dire == 'l':
                while(True):
                    if not root.head.left:
                        return root.head;
                    else:
                        root = root.head.left;
            else:
                while(True):
                    if not root.head.right:
                        return root.head;
                    else:
                        root = root.head.right;
                        
    tree = bintree.Bintree();
    l = [23,3,1,4,2,3,1,41,3,34,12,3,1,3,1,1,11,2,4,3,33,12,3,23,2,23];
    tree.put_list(l);
    
    def max_tree(root):
        go_lr(root, 'r');

    def min_tree(root):
        go_lr(root, 'l');
        
    print (max_tree(tree));
    print (min_tree(tree));
    
def main():
    ctrl = input("Choose which question you want to check, 1-4. 5 for extra question: ");
    if ctrl == '1':
        uppgift_1();
    elif ctrl == '2':
        uppgift_2();
    elif ctrl == '3':
        uppgift_3();
    elif ctrl == '4':
        uppgift_4();
    elif ctrl == '5':
        extra_uppgift();
    else:
        print("There is no such a command.");
    print ();
    
if __name__=="__main__":
    while(True):
        main();
