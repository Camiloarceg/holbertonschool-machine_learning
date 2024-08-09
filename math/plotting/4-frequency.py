#!/usr/bin/env python3
""" frequency
"""
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """ Histogram plot example
    """

    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    plt.hist(student_grades, bins=10, edgecolor='black')
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')
    plt.show()
