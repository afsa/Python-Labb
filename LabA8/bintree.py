import sys
import random

class TreeNode:
  data, left, right = None, None, None;

  def __init__ (self, data):
    self.data, self.left, self.right = data, None, None;

  def __str__ (self):
    return self.data;
    
class Bintree:
  head = None;
  
  def __init__ (self):
    self.head = None;

  def isempty(self):
    return not self.head;

  def exists(self, data, curr = None, ctrl = False):
    if not ctrl:
      return self.exists(data, self.head, True);
    elif not curr:
      return False;
    elif curr.data == data:
      return True;
    elif curr.data > data:
      return self.exists (data, curr.left, True);
    else:
      return self.exists (data, curr.right, True);

  def height(self, curr = None, ctrl = None):
    if not ctrl:
      return self.height(self.head, True);
    elif not curr:
      return 0;
    else:
      return (max (self.height(curr.left, True), self.height(curr.right, True) ) + 1);

  def put(self, data):
    if not self.head:
      self.head = TreeNode(data);
      return True;
    else:
      curr = self.head;
      while(True):
        if not curr:
          curr = TreeNode(data);
          return True;
        elif curr.data == data:
          return False;
        elif curr.data > data:
          if not curr.left:
            curr.left = TreeNode(data);
            return True;
          else:
            curr = curr.left;
        else:
          if not curr.right:
            curr.right = TreeNode(data);
            return True;
          else:
            curr = curr.right;

  def put_list(self, lst):
    for i in lst:
      self.put(i);
            
  def printtree(self, ctrl = False, curr = None):
    if not ctrl:
      re = self.printtree(True, self.head);
      return re;
    else:
      if curr and curr.data:
        ra = self.printtree(True, curr.left);
        if not ra: ra = [];
        rb = curr.data;
        rc = self.printtree(True, curr.right);
        if not rc: rc = [];
        return ra + [rb] + rc;

  def find_node(self, data, tree):
    curr = tree;
    while(True):
      type (curr.data)
      if curr.left and curr.left.data == data:
        return curr, 0;
      elif curr.right and curr.right.data == data:
        return curr, 1;
      elif data < curr.data:
        curr = curr.left;
      else:
        curr = curr.right;
        
  def delete_data(self, data):
    parent, pos = self.find_node(data, self.head);

    def s():
      if not pos:
        return parent.left;
      else:
        return parent.right;
      
    def give(ins):
      if not pos:
        parent.left = ins;
      else:
        parent.right = ins;

    def switch(first, pos1, second, pos2):
      if pos2 == 0:
        tmp = second.left.data;
      else:
        tmp = second.right.data;
      second.left = None;
      if pos1 == 0:
        first.left.data = tmp;
      else:
        first.right.data = tmp;

    def go_lr(root, dire):
      if not root:
        return None;
      else:
        if dire == 'l':
          while(True):
            if not root.left:
#              print ("in here", root.data)
              return root.data;
            else:
              root = root.left;
        else:
          while(True):
            if not root.right:
#              print ("in here", root.data)
              return root.data;
            else:
              root = root.right;
    
    def max_tree(root):
      return go_lr(root, 'r');

    def min_tree(root):
      return go_lr(root, 'l');
        
    if not s().left:
      give( s().right );
    elif not s().right:
      give( s().left );
    else:
      r = random.randrange(0,2);
      if r == 0:
        m = max_tree(s().left);
#        print ("m", m);
#        print ( self.exists(m, s().left, True))
        end, endpos = self.find_node (m, s());
        switch(parent, pos, end, endpos);
      else:
        m = min_tree(s().right);
#        print ("m", m);
#        print ( self.exists(m, s().left, True))
        end, endpos = self.find_node (m, s());
        switch(parent, pos, end, endpos);
