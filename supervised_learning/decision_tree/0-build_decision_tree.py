#!/usr/bin/env python3

import numpy as np


class Node:
    """
    A class representing a node in a decision tree.

    Attributes:
        feature (int or None): The index of the feature used for
            splitting the data at this node.
        threshold (float or None): The threshold value for
            splitting the data at this node.
        left_child (Node or None): The left child node.
        right_child (Node or None): The right child node.
        is_root (bool): A flag indicating whether this node is the root
            of the tree.
        depth (int): The depth of this node in the tree.
        sub_population (numpy.ndarray or None): The subset of the data
            at this node.
        is_leaf (bool): A flag indicating whether this node is a leaf node.

    Methods:
        max_depth_below(): Returns the maximum depth of the tree below
            this node.
    """

    def __init__(self, feature=None, threshold=None, left_child=None,
                 right_child=None, is_root=False, depth=0):
        """ The constructor
        """
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.is_leaf = False
        self.is_root = is_root
        self.sub_population = None
        self.depth = depth

    def max_depth_below(self):
        """
        Returns the maximum depth of the tree below this node.

        Returns:
            int: The maximum depth of the tree below this node.
        """
        if self.left_child is None and self.right_child is None:
            return self.depth

        left_depth = (self.left_child.max_depth_below()
                      if self.left_child else self.depth)
        right_depth = (self.right_child.max_depth_below()
                       if self.right_child else self.depth)

        return max(left_depth, right_depth)


class Leaf(Node):
    """
    A class representing a leaf node in a decision tree.

    Attributes:
        value (float or int): The value associated with this leaf node.
        depth (int): The depth of this node in the tree.

    Methods:
        max_depth_below(): Returns the depth of this leaf node.
    """

    def __init__(self, value, depth=None):
        """ The constructor
        """
        super().__init__()
        self.value = value
        self.is_leaf = True
        self.depth = depth

    def max_depth_below(self):
        """
        Returns the depth of this leaf node.

        Returns:
            int: The depth of this leaf node.
        """
        return self.depth


class Decision_Tree:
    """
    A class representing a decision tree.

    Attributes:
        rng (numpy.random.Generator): A random number generator.
        root (Node): The root node of the decision tree.
        explanatory (numpy.ndarray or None): The explanatory variables
            (features) of the data.
        target (numpy.ndarray or None): The target variable (labels)
            of the data.
        max_depth (int): The maximum depth of the decision tree.
        min_pop (int): The minimum population size for splitting a node.
        split_criterion (str): The criterion used for splitting nodes.
        predict (callable or None): A function for making predictions
            using the decision tree.
    """

    def __init__(self, max_depth=10, min_pop=1, seed=0,
                 split_criterion="random", root=None):
        """ The constructor
        """
        self.rng = np.random.default_rng(seed)
        if root:
            self.root = root
        else:
            self.root = Node(is_root=True)
        self.explanatory = None
        self.target = None
        self.max_depth = max_depth
        self.min_pop = min_pop
        self.split_criterion = split_criterion
        self.predict = None

    def depth(self):
        """
        Returns the maximum depth of the decision tree.

        Returns:
            int: The maximum depth of the decision tree.
        """
        return self.root.max_depth_below()
