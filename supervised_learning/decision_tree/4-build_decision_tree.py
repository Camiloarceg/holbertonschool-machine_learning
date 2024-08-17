#!/usr/bin/env python3
""" decisoon tree
"""

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
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.is_leaf = False
        self.is_root = is_root
        self.sub_population = None
        self.depth = depth
        self.lower = {}
        self.upper = {}

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

    def count_nodes_below(self, only_leaves=False):
        """
        Counts the number of nodes below this node in the tree.

        Args:
            only_leaves (bool): If True, only leaf nodes are counted.
                                Otherwise, all nodes are counted.

        Returns:
            int: The number of nodes below this node.
        """
        if only_leaves and not self.is_leaf:
            count = 0
        else:
            count = 1

        if self.left_child:
            count += self.left_child.count_nodes_below(only_leaves=only_leaves)
        if self.right_child:
            count += self.right_child.count_nodes_below(
                only_leaves=only_leaves)

        return count

    def left_child_add_prefix(self, text):
        """ adds a prefix to the left """
        lines = text.split("\n")
        new_text = "    +--" + lines[0] + "\n"
        for x in lines[1:]:
            new_text += ("    |  " + x) + "\n"
        return new_text

    def right_child_add_prefix(self, text):
        """ adds a prefix to the right """
        lines = text.split("\n")
        new_text = "    +--" + lines[0] + "\n"
        for x in lines[1:]:
            new_text += ("       " + x) + "\n"
        return new_text

    def __str__(self):
        """ creates the entire tree string """
        current = "root" if self.is_root else "-> node"
        result = \
            f"{current} [feature={self.feature}, threshold={self.threshold}]\n"
        if self.left_child:
            result += \
              self.left_child_add_prefix(str(self.left_child).strip())
        if self.right_child:
            result += \
              self.right_child_add_prefix(str(self.right_child).strip())
        return result

    def get_leaves_below(self):
        """
        Returns the list of all leaf nodes below (and including) this node.

        Returns:
            list: A list of leaf nodes in the tree.
        """
        if self.is_leaf:
            return [self]

        leaves = []
        if self.left_child:
            leaves.extend(self.left_child.get_leaves_below())
        if self.right_child:
            leaves.extend(self.right_child.get_leaves_below())

        return leaves

    def update_bounds_below(self):
        """
        Recursively compute and attach the lower and upper bounds dictionaries
        for each node.
        """
        if self.is_root:
            self.upper = {0: np.inf}
            self.lower = {0: -np.inf}

        if self.left_child:
            self.left_child.lower = self.lower.copy()
            self.left_child.upper = self.upper.copy()
            if self.feature is not None:
                self.left_child.upper[self.feature] = self.threshold

        if self.right_child:
            self.right_child.lower = self.lower.copy()
            self.right_child.upper = self.upper.copy()
            if self.feature is not None:
                self.right_child.lower[self.feature] = self.threshold

        for child in [self.left_child, self.right_child]:
            if child:
                child.update_bounds_below()


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

    def count_nodes_below(self, only_leaves=False):
        """ count nodes below
        """
        return 1

    def __str__(self):
        return (f"-> leaf [value={self.value}]")

    def get_leaves_below(self):
        """ return self as a list element
        """
        return [self]

    def update_bounds_below(self):
        """ update bounds below """
        pass


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

    def count_nodes(self, only_leaves=False):
        """ count nodes below
        """
        return self.root.count_nodes_below(only_leaves=only_leaves)

    def __str__(self):
        return self.root.__str__()

    def get_leaves(self):
        """ return self as a list element
        """
        return self.root.get_leaves_below()

    def update_bounds(self):
        """ update bounds """
        self.root.update_bounds_below()
