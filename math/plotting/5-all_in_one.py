#!/usr/bin/env python3
""" all in one
"""
from matplotlib import gridspec
import numpy as np
import matplotlib.pyplot as plt

def all_in_one():
    """ all in one plots
    """

    y0 = np.arange(0, 11) ** 3

    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
    y1 += 180

    x2 = np.arange(0, 28651, 5730)
    r2 = np.log(0.5)
    t2 = 5730
    y2 = np.exp((r2 / t2) * x2)

    x3 = np.arange(0, 21000, 1000)
    r3 = np.log(0.5)
    t31 = 5730
    t32 = 1600
    y31 = np.exp((r3 / t31) * x3)
    y32 = np.exp((r3 / t32) * x3)

    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)

    bins = np.arange(0, 110, 10)

    # Create a figure and set up a 3x2 grid layout with the last plot spanning two columns
    fig = plt.figure(figsize=(12, 8))
    gs = gridspec.GridSpec(3, 2, width_ratios=[1, 1])
    
    # Subplot 1: Line Plot
    ax0 = plt.subplot(gs[0, 0])
    ax0.plot(np.arange(0, 11), y0, color='red')
    ax0.set_xlim(0, 10)
    ax0.set_yticks(np.arange(0, 1001, 500))

    # Subplot 2: Scatter Plot
    ax1 = plt.subplot(gs[0, 1])
    ax1.scatter(x1, y1, c='magenta')
    ax1.set_title("Men's Height vs Weight", fontsize='x-small')
    ax1.set_xlabel('Height (in)', fontsize='x-small')
    ax1.set_ylabel('Weight (lbs)', fontsize='x-small')
    ax1.set_yticks(np.arange(170, 191, 10))
    ax1.set_xticks(np.arange(60, 81, 10))

    # Subplot 3: Exponential Decay
    ax2 = plt.subplot(gs[1, 0])
    ax2.plot(x2, y2)
    ax2.set_title('Exponential Decay of C-14', fontsize='x-small')
    ax2.set_xlabel('Time (years)', fontsize='x-small')
    ax2.set_ylabel('Fraction Remaining', fontsize='x-small')
    ax2.set_yscale('log')
    ax2.set_xlim([0, 28650])
    ax2.set_xticks(np.arange(0, 20001, 10000))

    # Subplot 4: Two Decays
    ax3 = plt.subplot(gs[1, 1])
    ax3.plot(x3, y31, 'r--', label="C-14")
    ax3.plot(x3, y32, 'g-', label="Ra-226")
    ax3.set_title('Exponential Decay of Radioactive Elements', fontsize='x-small')
    ax3.set_xlabel('Time (years)', fontsize='x-small')
    ax3.set_ylabel('Fraction Remaining', fontsize='x-small')
    ax3.set_xlim(0, 20000)
    ax3.set_ylim(0, 1)
    ax3.legend(fontsize='x-small')
    ax3.set_xticks(np.arange(0, 20001, 5000))
    ax3.set_yticks(np.arange(0, 1.1, 0.5))

    # Subplot 5: Histogram (spanning two columns)
    ax4 = plt.subplot(gs[2, :])
    ax4.hist(student_grades, bins=bins, edgecolor='black')
    ax4.set_title('Project A', fontsize='x-small')
    ax4.set_xlabel('Grades', fontsize='x-small')
    ax4.set_ylabel('Number of Students', fontsize='x-small')
    ax4.set_xlim([0, 100])
    ax4.set_ylim([0, 30])
    ax4.set_xticks(np.arange(0, 101, 10))
    ax4.set_yticks(np.arange(0, 31, 10))

    # Overall figure title
    fig.suptitle('All in One', fontsize='large', y=0.95)

    # Adjust layout to fit all subplots
    plt.tight_layout(rect=[0, 0, 1, 0.95])

    # Show the figure
    plt.show()
