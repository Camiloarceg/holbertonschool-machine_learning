#!/usr/bin/env python3
""" bars
"""
import numpy as np
import matplotlib.pyplot as plt

def bars():
    """ plot of stacked bars
    """
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4,3))
    plt.figure(figsize=(6.4, 4.8))

    labels = ['Farrah', 'Fred', 'Felicia']
    fruit_types = ['apples', 'bananas', 'oranges', 'peaches']
    colors = {
        'apples': 'red',
        'bananas': 'yellow',
        'oranges': '#ff8000',
        'peaches': '#ffe5b4'
    }
    
    bar_width = 0.5

    bottom = np.zeros(fruit.shape[1])
    for i, fruit_type in enumerate(fruit_types):
        plt.bar(labels, fruit[i], bar_width, label=fruit_type, color=colors[fruit_type], bottom=bottom)
        bottom += fruit[i]

    plt.ylabel('Quantity of Fruit')
    plt.title('Number of Fruit per Person')
    plt.ylim(0, 80)
    plt.yticks(np.arange(0, 81, 10))
    
    plt.legend()

    plt.show()
