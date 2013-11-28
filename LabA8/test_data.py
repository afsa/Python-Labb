import bintree

t = bintree.Bintree();

l = [12,3,332,22,3,31,4,31,4,1,3,2];

t.put_list(l);

t.delete_data(2);
print(t.printtree());
t.delete_data(3);
print(t.printtree());
t.delete_data(22);
print(t.printtree());
