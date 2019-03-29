#!/usr/bin/env python
# encoding: GBK

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/1/24 16:55
�й���������������������

https://blog.csdn.net/Bone_ACE/article/details/46718683
"""





class Node(object):
    """�ڵ���"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    """����"""
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, elem):
        """Ϊ�����ӽڵ�"""
        node = Node(elem)
        if self.root.elem == -1:  # ������ǿյģ���Ը��ڵ㸳ֵ
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]  # �˽���������û���롣
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)  # ����ý����������������˽�㶪����


    def front_digui(self, root):
        """���õݹ�ʵ�������������"""
        if root == None:
            return
        print root.elem,
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)


    def middle_digui(self, root):
        """���õݹ�ʵ�������������"""
        if root == None:
            return
        self.middle_digui(root.lchild)
        print root.elem,
        self.middle_digui(root.rchild)


    def later_digui(self, root):
        """���õݹ�ʵ�����ĺ������"""
        if root == None:
            return
        self.later_digui(root.lchild)
        self.later_digui(root.rchild)
        print root.elem,


    def front_stack(self, root):
        """���ö�ջʵ�������������"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:                     #�Ӹ��ڵ㿪ʼ��һֱ������������
                print node.elem,
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()            #while������ʾ��ǰ�ڵ�nodeΪ�գ���ǰһ���ڵ�û����������
            node = node.rchild                  #��ʼ�鿴����������


    def middle_stack(self, root):
        """���ö�ջʵ�������������"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:                     #�Ӹ��ڵ㿪ʼ��һֱ������������
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()            #while������ʾ��ǰ�ڵ�nodeΪ�գ���ǰһ���ڵ�û����������
            print node.elem,
            node = node.rchild                  #��ʼ�鿴����������


    def later_stack(self, root):
        """���ö�ջʵ�����ĺ������"""
        if root == None:
            return
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        while myStack1:                   #���whileѭ���Ĺ������ҳ�������������򣬴���myStack2����
            node = myStack1.pop()
            if node.lchild:
                myStack1.append(node.lchild)
            if node.rchild:
                myStack1.append(node.rchild)
            myStack2.append(node)
        while myStack2:                         #��myStack2�е�Ԫ�س�ջ����Ϊ�����������
            print myStack2.pop().elem,


    def level_queue(self, root):
        """���ö���ʵ�����Ĳ�α���"""
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print node.elem,
            if node.lchild != None:
                myQueue.append(node.lchild)
            if node.rchild != None:
                myQueue.append(node.rchild)


if __name__ == '__main__':
    """������"""
    elems = range(10)           #����ʮ��������Ϊ���ڵ�
    tree = Tree()          #�½�һ��������
    for elem in elems:
        tree.add(elem)           #����������Ľڵ�

    print '����ʵ�ֲ�α���:'
    tree.level_queue(tree.root)

    print '\n\n�ݹ�ʵ���������:'
    tree.front_digui(tree.root)
    print '\n�ݹ�ʵ���������:'
    tree.middle_digui(tree.root)
    print '\n�ݹ�ʵ�ֺ������:'
    tree.later_digui(tree.root)

    print '\n\n��ջʵ���������:'
    tree.front_stack(tree.root)
    print '\n��ջʵ���������:'
    tree.middle_stack(tree.root)
    print '\n��ջʵ�ֺ������:'
    tree.later_stack(tree.root)






















