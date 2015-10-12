#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python implementation of Huffman Coding

"""
__author__ =  'Ismael Taboada'
__version__=  '1.0'

from heapq import heappush, heappop, heapify
from graphviz import Digraph


class HuffmanCoding(object):
    """docstring for HuffmanCoding"""

    def __init__(self):
        super(HuffmanCoding, self).__init__()
        self.tree = []

    def encode(self,symb2freq):
        """Huffman encode the given dict mapping symbols to weights

        :param symb2freq: dictionary of frecuencies
        """
        heap = [(wt,sym) for sym, wt in symb2freq.items()]
        heapify(heap)
        while len(heap) > 1:
            lo = heappop(heap)
            hi = heappop(heap)
            heappush(heap, (lo[0]+hi[0],[lo,hi]))
        self.tree = heap[0]

    def tree_to_graph(self,tree=None,n="",comment="Huffman Coding",formatin="png"):
        """Based on the Huffman Coding it create a graph with graphviz library

        :param comment: graph comment
        :param formatin: graph format
        :param n: temporal huffman coding path to leaf
        """
        if not tree:
            tree=self.tree

        dot = Digraph(comment=comment, format=formatin)

        left = n+"0"

        right = n+"1"
        # Each node has the symbol frecuency
        dot.node(n,str(tree[0])+","\
            # Symbol value if it is a leaf
            +str(tree[1])+";\n"\
            # Symbol code if it is a leaf
            +n if not isinstance(tree[1],list) else str(tree[0]))
        if (isinstance(tree[1],list)):
            self.tree_to_graph(tree[1][0],left)
            self.tree_to_graph(tree[1][1],right)
            try:
                dot.edge(n,left,label='0')
                dot.edge(n,right,label='1')
            except Exception as e:
                print n, "error"
                raise

        return dot

    def tree_to_table(self,tree=None,n=""):
        """Extracts from Huffman coding tree the symbols, giving a tables with the rows:
         Symbol, frecuency, Coding

        :param n: temporal coding path to leaf
         """
        if not tree:
            tree = self.tree

        if not isinstance(tree[1],list):
            return [[tree[1],tree[0],n]]
        else:
            leaf=[]
            # left subtree
            leaf.extend(self.tree_to_table(tree[1][0],n+"0"))
            # right subtree
            leaf.extend(self.tree_to_table(tree[1][1],n+"1"))
            return leaf
