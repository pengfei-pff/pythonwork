#!/usr/bin/env python
# encoding: utf-8

class Tree(object):
    def __init__(self, label):
        self.value = label
        self.child = {}

    def add_child(self, label, relate):
        # self.child.append(Tree())
        self.child[label] = Tree(relate)

    def get_value(self):
        return self.value

    def get_child(self):
        return self.child


def travelsal(tree):
    li = [tree]
    while True:
        try:
            t = li.pop()
            print (t.get_value())
            child = t.get_child()
            if child:
                li.extend(child.values())
        except:
            break


def create_tree():
    root = Tree('root')
    root.add_child('c_key1', 'child_1')
    root.add_child('c_key2', 'child_2')
    print (root.get_child())
    travelsal(root)


def main():
    create_tree()

if __name__ == "__main__":
    main()

