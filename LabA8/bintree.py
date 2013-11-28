import sys

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
    curr = tree.head;
    while(True):
      if curr.left and curr.left.data == data:
#        self.printtree(True, curr)
        return curr, 0;
      elif curr.right and curr.right.data == data:
        return curr, 1;
      elif data < curr.data:
        curr = curr.left;
      else:
        curr = curr.right;
    """
    if tree.head.left.data == data:
      return tree, 0;
    elif tree.head.right.data == data:
      return tree, 1;
    elif data < tree.head.data:
      self.find_node(data, tree.left);
    else:
      self.find_node(data, tree.right);
    """
        
  def delete_data(self, data):
    parent, pos = self.find_node(data, self);
    def alias():
      if not pos:
        return parent.left;
      else:
        return parent.right;
    #DEBUG
#    print(self.printtree(True, alias));
    #DEBUG
    if not pos:
      if not parent.left.left:
        parent.left = parent.left.right;
      elif not parent.left.right:
        parent.left = parent.left.left;
      else:
        curr = parent.left.left;
        while(True):
          if not curr.right:
            maximum = curr.data;
            self.delete_data(maximum);
            break;
          else:
            curr = curr.right;
        parent.left.data = maximum;
    else:
      if not parent.right.left:
        parent.right = parent.right.right;
      elif not parent.right.right:
        parent.right = parent.right.left;
      else:
        curr = parent.right.left;
        while(True):
          if not curr.right:
            maximum = curr.data;
            self.delete_data(maximum);
            break;
          else:
            curr = curr.right;
        parent.right.data = maximum;
      
  
