# for filter data to obvious distribution distance between wifi play time and cellular play time
import numpy as np
import pandas as pd
from matplotlib.patches import Patch
import matplotlib.pyplot as plt
import sys
import seaborn as sns
import matplotlib as mpl
# import statsmodels.api as sm
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator
from scipy.stats import gaussian_kde
from matplotlib.lines import Line2D
mpl.rcParams['font.family'] = 'Times New Roman'

if __name__ == "__main__":
    mode = int(sys.argv[1])
    # font = 25
    # labefont = 24
    font = 40
    lasize = 40
    linewides = 3
    red_rgb = (1, 0.2118, 0.1569)
    blue_rgb = (0.09, 0.47, 0.72)
    linestyles = ['-', '--', '-.', ':']
    color_1 = np.array([0, 114, 189]) / 255
    color_2 = np.array([217, 83, 25]) / 255
    color_3 = np.array([237, 177, 32]) / 255
    color_4 = np.array([77, 190, 238]) / 255
    color_5 = np.array([201, 92, 46]) / 255
    color_6 = np.array([48, 112, 183]) / 255
    color_7 = np.array([228, 179, 69]) / 255
    colors = [np.array([201, 92, 46]) / 255, np.array([48, 112, 183]) / 255, np.array([228, 179, 69]) / 255,
              np.array([5, 120, 5]) / 255, np.array([119, 172, 48]) / 255, np.array([126, 47, 142]) / 255,
              np.array([255, 0, 0]) / 255]
    if mode ==1:
        font = font -20
        # colors = [np.array([201, 92, 46]) / 255, np.array([48, 112, 183]) / 255, np.array([228, 179, 69]) / 255,
        #           np.array([5, 120, 5]) / 255, np.array([201, 92, 46]) / 255, np.array([48, 112, 183]) / 255, np.array([228, 179, 69]) / 255,
        #           np.array([5, 120, 5]) / 255]
        colors = [np.array([0, 114, 189]) / 255, np.array([217, 83, 25]) / 255,
                  np.array([237, 177, 32]) / 255, np.array([119, 172, 48]) / 255,np.array([118, 118, 118]) / 255,
                  np.array([0, 114, 189]) / 255, np.array([217, 83, 25]) / 255,
                  np.array([237, 177, 32]) / 255, np.array([119, 172, 48]) / 255,np.array([118, 118, 118]) / 255,]
        power0, SCdata0 = np.loadtxt('./data/default_RIO.txt', unpack=True)  # np.random.rand(20) * 2 * np.pi  # 角度
        power00, SCdata00 = np.loadtxt('./data/default_Dimsen.txt', unpack=True)

        power, SCdata = np.loadtxt('./data/Exp1_RIO.txt', unpack=True)  # np.random.rand(20) * 2 * np.pi  # 角度
        power2, SCdata2 = np.loadtxt('./data/Exp2_RIO.txt', unpack=True)
        power3, SCdata3 = np.loadtxt('./data/Exp3_RIO.txt', unpack=True)
        power4, SCdata4 = np.loadtxt('./data/Exp4_RIO.txt', unpack=True)

        power5, SCdata5 = np.loadtxt('./data/Exp1_Dimsens.txt', unpack=True)
        power6, SCdata6 = np.loadtxt('./data/Exp2_Dimsens.txt', unpack=True)
        power7, SCdata7 = np.loadtxt('./data/Exp3_Dimsens.txt', unpack=True)
        power8, SCdata8 = np.loadtxt('./data/Exp4_Dimsens.txt', unpack=True)

        RIO = abs(np.loadtxt('./data/RIO.txt', unpack=True, dtype=float))
        # Define colors and positions for violin plots
        colors = [np.array([0, 114, 189]) / 255, np.array([255, 46, 41]) / 255, np.array([100,100,100]) / 255]
        # positions = [[1, 9], [1, 9], [1,5], [1, 5],[1, 5]]
        line_width = 2
        # Create subplots
        fig, axes = plt.subplots(ncols=5, figsize=(9,2.5), sharey=True)#2.3
        axes[0].plot(power0, SCdata0, color=red_rgb, linewidth=line_width, linestyle='-', label='RIO')
        axes[1].plot(power, SCdata, color=red_rgb, linewidth=line_width, linestyle='-', label='RIO')
        axes[3].plot(power3, SCdata3, color=red_rgb, linewidth=line_width, linestyle='-', label='RIO')
        axes[4].plot(power4, SCdata4, color=red_rgb, linewidth=line_width, linestyle='-', label='RIO')

        axes[0].plot(power00, SCdata00, color=blue_rgb, linewidth=line_width, linestyle='-', label='OhmScan')
        axes[1].plot(power5, SCdata5, color=blue_rgb, linewidth=line_width, linestyle='-', label='OhmScan')
        axes[2].plot(power6, SCdata6, color=blue_rgb, linewidth=line_width, linestyle='-', label='OhmScan')
        axes[2].plot(power2, SCdata2, color=red_rgb, linewidth=line_width, linestyle='-', label='RIO')
        axes[3].plot(power7, SCdata7, color=blue_rgb, linewidth=line_width, linestyle='-', label='OhmScan')
        axes[4].plot(power8, SCdata8, color=blue_rgb, linewidth=line_width, linestyle='-', label='OhmScan')
        for i, ax in enumerate(axes):
            ax.set_xlim([0, 9.9])
            ax.set_ylim([0, 1])
            ax.yaxis.set_major_locator(MultipleLocator(1))
            ax.yaxis.set_minor_locator(MultipleLocator(0.1))
            ax.xaxis.set_major_locator(MultipleLocator(3))
            ax.xaxis.set_minor_locator(MultipleLocator(1))

            ax.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)
            ax.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)
            ax.tick_params(axis='y', labelsize=font)
            ax.tick_params(axis='x', labelsize=font)
            plt.subplots_adjust(left=0.06, right=0.998, top=0.886,
                                bottom=0.24)  # left=0.127, right=0.98, top=0.98, bottom=0.18
            if i == 0:
                ax.set_ylabel('CDF', fontsize=font, fontname="Times New Roman")
            ax.spines['top'].set_linewidth(1.8)
            ax.spines['right'].set_linewidth(1.8)
            ax.spines['bottom'].set_linewidth(1.8)
            ax.spines['left'].set_linewidth(1.8)
        axes[2].set_xlabel('Finger tracking error (cm)', fontsize=font, fontname="Times New Roman")
        axes[0].set_title('Static Empty Lab',size=font-1)
        axes[1].set_title('Static Office', size=font - 1)
        axes[2].set_title('Dynamic Office', size=font - 1)
        axes[3].set_title('Unstable Tag', size=font - 1)
        axes[4].set_title('Moving Tag', size=font - 1)
        ############################
        axes[2].xaxis.set_label_coords(0.5, -0.21)
        fontSC =font -2
        axes[0].text(6, 0.27, '0.96', fontsize=fontSC, color='black', verticalalignment='center')  # ,
        # bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        axes[0].text(6, 0.1, '0.75', fontsize=fontSC, color='black', verticalalignment='center')  # ,
        axes[0].text(4.1, 0.44, 'Median', fontsize=fontSC - 2, color='black', verticalalignment='center',
                     fontname="Arial", fontweight='bold')
        axes[0].plot([4, 9], [0.37, 0.37], color='gray', linewidth=line_width - 0.5)
        axes[0].plot([4, 9], [0.53, 0.53], color='gray', linewidth=line_width - 0.5)
        axes[0].plot([4.3, 5.3], [0.1, 0.1], color=blue_rgb, linewidth=line_width)
        axes[0].plot([4.3, 5.3], [0.27, 0.27], color=red_rgb, linewidth=line_width)
        axes[0].plot([4, 9], [0.02, 0.02], color='gray', linewidth=line_width - 0.5)

        ##############################
        axes[1].text(6, 0.27, '1.77', fontsize=fontSC, color='black', verticalalignment='center')  # ,
        # bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        axes[1].text(6, 0.1, '0.50', fontsize=fontSC, color='black', verticalalignment='center')  # ,
        # bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        axes[1].text(4.1, 0.44, 'Median', fontsize=fontSC - 2, color='black', verticalalignment='center',
                     fontname="Arial", fontweight='bold')
        axes[1].plot([4, 9], [0.37, 0.37], color='gray', linewidth=line_width - 0.5)
        axes[1].plot([4, 9], [0.53, 0.53], color='gray', linewidth=line_width - 0.5)
        axes[1].plot([4.3, 5.3], [0.1, 0.1], color=blue_rgb, linewidth=line_width)
        axes[1].plot([4.3, 5.3], [0.27, 0.27], color=red_rgb, linewidth=line_width)
        axes[1].plot([4, 9], [0.02, 0.02], color='gray', linewidth=line_width - 0.5)

        ##############################
        axes[2].text(6, 0.27, '1.78', fontsize=fontSC, color='black', verticalalignment='center')  # ,
        axes[2].text(6, 0.1, '0.64', fontsize=fontSC, color='black', verticalalignment='center')  # ,
        axes[2].text(4.1, 0.44, 'Median', fontsize=fontSC - 2, color='black', verticalalignment='center',
                     fontname="Arial", fontweight='bold')
        axes[2].plot([4, 9], [0.37, 0.37], color='gray', linewidth=line_width - 0.5)
        axes[2].plot([4, 9], [0.53, 0.53], color='gray', linewidth=line_width - 0.5)
        axes[2].plot([4.3, 5.3], [0.1, 0.1], color=blue_rgb, linewidth=line_width)
        axes[2].plot([4.3, 5.3], [0.27, 0.27], color=red_rgb, linewidth=line_width)
        axes[2].plot([4, 9], [0.02, 0.02], color='gray', linewidth=line_width - 0.5)

        ##############################
        axes[3].text(6, 0.27, '2.36', fontsize=fontSC, color='black', verticalalignment='center')  # ,
        # bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        axes[3].text(6, 0.1, '0.74', fontsize=fontSC, color='black', verticalalignment='center')  # ,
        axes[3].text(4.1, 0.44, 'Median', fontsize=fontSC - 2, color='black', verticalalignment='center',
                     fontname="Arial", fontweight='bold')
        # bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9),fontname="Arial",fontweight='bold')
        axes[3].plot([4, 9], [0.37, 0.37], color='gray', linewidth=line_width - 0.5)
        axes[3].plot([4, 9], [0.53, 0.53], color='gray', linewidth=line_width - 0.5)
        axes[3].plot([4.3, 5.3], [0.1, 0.1], color=blue_rgb, linewidth=line_width)
        axes[3].plot([4.3, 5.3], [0.27, 0.27], color=red_rgb, linewidth=line_width)
        axes[3].plot([4, 9], [0.02, 0.02], color='gray', linewidth=line_width - 0.5)

        ##############################
        axes[4].text(6, 0.27, '3.37', fontsize=fontSC, color='black', verticalalignment='center')#,
                     # bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        axes[4].text(6, 0.1, '0.90', fontsize=fontSC, color='black', verticalalignment='center')#,
                     # bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        axes[4].text(4.1, 0.44, 'Median', fontsize=fontSC - 2, color='black', verticalalignment='center',
                     fontname="Arial", fontweight='bold')
        # bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9),fontname="Arial",fontweight='bold')
        axes[4].plot([4, 9], [0.37, 0.37], color='gray', linewidth=line_width - 0.5)
        axes[4].plot([4, 9], [0.53, 0.53], color='gray', linewidth=line_width - 0.5)
        axes[4].plot([4.3, 5.3], [0.1, 0.1], color=blue_rgb, linewidth=line_width)
        axes[4].plot([4.3, 5.3], [0.27, 0.27], color=red_rgb, linewidth=line_width)
        axes[4].plot([4, 9], [0.02, 0.02], color='gray', linewidth=line_width - 0.5)
        legend = axes[0].legend(frameon=False, loc=(0.21, 0.52), fontsize=font - 1, handlelength=0.5, ncol=1,
                                handletextpad=0.1, borderpad=0.1, columnspacing=0,labelspacing=0.1)

        plt.subplots_adjust(wspace=0.1)
        plt.savefig('revistApp_fig16.pdf', format='pdf')
        plt.show()