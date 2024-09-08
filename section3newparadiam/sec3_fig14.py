# for filter data to obvious distribution distance between wifi play time and cellular play time
import numpy as np
import pandas as pd
from matplotlib.patches import Patch
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.pyplot as plt
import sys
import seaborn as sns
import matplotlib as mpl
import statsmodels.api as sm
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator
from scipy.stats import gaussian_kde
from matplotlib.lines import Line2D
mpl.rcParams['font.family'] = 'Times New Roman'
## mode == 1 impact_angle.pdf
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
    # colors = [np.array([201, 92, 46]) / 255, np.array([48, 112, 183]) / 255, np.array([228, 179, 69]) / 255,
    #           np.array([5, 120, 5]) / 255, np.array([119, 172, 48]) / 255, np.array([126, 47, 142]) / 255,
    #           np.array([255, 0, 0]) / 255]
    colors = [np.array([255, 46, 41]) / 255, np.array([0, 114, 189]) / 255,
              np.array([237, 177, 32]) / 255, np.array([119, 172, 48]) / 255,
              np.array([136, 137, 139]) / 255, np.array([100, 100, 100]) / 255]
    if mode == 1:##keystub_distance
        input_file = './data/button/SCdata/distance/'
        dista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]#50

        all_phase5 = []
        all_phase6 = []
        all_phase12 = []
        all_phase15 = []
        all_phase20 = []
        all_phase10 = []
        midpoints5 = []
        midpoints10 = []
        midpoints12 = []
        midpoints15 = []
        midpoints6 = []
        font = font+7
        for index, i in enumerate(dista):
            phase5 = np.loadtxt(input_file + '1-'+str(i) + '.txt', unpack=True)
            middle_phase5 = abs(phase5)
            midpoints5.append(np.median(middle_phase5))
            all_phase5.append(middle_phase5)

            phase6 = np.loadtxt(input_file + '2-' + str(i) + '.txt', unpack=True)
            middle_phase6 = abs(phase6)
            midpoints6.append(np.median(middle_phase6))
            all_phase6.append(middle_phase6)

            phase10 = np.loadtxt(input_file + '3-'+str(i) + '.txt', unpack=True)
            middle_phase10 = abs(phase10)
            midpoints10.append(np.median(middle_phase10))
            all_phase10.append(middle_phase10)

            phase12 = np.loadtxt(input_file + '4-' + str(i) + '.txt', unpack=True)
            middle_phase12 = abs(phase12)
            midpoints12.append(np.median(middle_phase12))
            all_phase12.append(middle_phase12)

            phase15 = np.loadtxt(input_file + '5-' + str(i) + '.txt', unpack=True)
            middle_phase15 = abs(phase15)
            midpoints15.append(np.median(middle_phase15))
            all_phase15.append(middle_phase15)



        fig, ax = plt.subplots(figsize=(7.5,5.9), sharex=True)  # 修改为1x4的布局
        wide = 0.5
        lindw = 2
        positions = np.arange(1, 16+ 1, 1)
        # 使用箱线图代替小提琴图
        parts5 = ax.boxplot(all_phase5, positions=dista, widths=wide, patch_artist=True,
                             showmeans=False, showfliers=False)
        line5 = ax.plot(dista, midpoints5, color=colors[0], marker='o', linestyle='-',
                         linewidth=lindw, markersize=6, label='1 m')
        parts6 = ax.boxplot(all_phase6, positions=dista, widths=wide, patch_artist=True,
                            showmeans=False, showfliers=False)
        line6 = ax.plot(dista, midpoints6, color=colors[1], marker='o', linestyle='-',
                        linewidth=lindw, markersize=6, label='2 m')
            # raise ValueError("List of boxplot statistics and `positions` values must have the same length")

        parts10 = ax.boxplot(all_phase10, positions=dista, widths=wide, patch_artist=True,
                             showmeans=False, showfliers=False)
        line10 = ax.plot(dista, midpoints10, color=colors[2], marker='o', linestyle='-',
                         linewidth=lindw, markersize=6, label='3 m')
        parts12 = ax.boxplot(all_phase12, positions=dista, widths=wide, patch_artist=True,
                             showmeans=False, showfliers=False)
        line12 = ax.plot(dista, midpoints12, color=colors[3], marker='o', linestyle='-',
                         linewidth=lindw, markersize=6, label='4 m')
        parts15 = ax.boxplot(all_phase15, positions=dista, widths=wide, patch_artist=True,
                             showmeans=False, showfliers=False)
        line15 = ax.plot(dista, midpoints15, color=colors[4], marker='o', linestyle='-',
                         linewidth=lindw, markersize=6, label='5 m')


        for parts, color in zip([parts5,parts6,parts10,parts12,parts15], colors):  # parts15
            for box in parts['boxes']:
                box.set_facecolor(color)
                box.set_edgecolor('gray')
                box.set_alpha(0.7)
            for whisker in parts['whiskers']:
                whisker.set_color(colors[5])
            for cap in parts['caps']:
                cap.set_color(colors[5])
            for median in parts['medians']:
                median.set_color(colors[5])

        # 隐藏箱线图中的均值点，或者使用 `showmeans=True` 来显示
        for parts in [parts5,parts6,parts10,parts12,parts15]:
            for mean in parts['means']:
                mean.set_markerfacecolor('r')
                mean.set_markeredgecolor('black')

        ax.grid()
        ax.grid(True)
        ax.set_xlim([0, len(positions)+1])
        ax.yaxis.set_major_locator(MultipleLocator(100))
        ax.yaxis.set_minor_locator(MultipleLocator(20))
        ax.xaxis.set_major_locator(MultipleLocator(1))
        ax.xaxis.set_minor_locator(MultipleLocator(0.5))
        plt.subplots_adjust(left=0.27, right=0.996, top=0.982,
                            bottom=0.202)  # left=0.127, right=0.98, top=0.98, bottom=0.18
        ax.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='-', linewidth=0.75, alpha=0.3)
        ax.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)
        ax.set_ylabel('Register value', fontsize=font+4, fontname="Times New Roman",
                      color='black')  # Differential Phase(rad)
        ax.set_xlabel('Button index', fontsize = font + 4, fontname = "Times New Roman")
        ax.tick_params(labelsize=font, labelcolor="black", length=6, width=1,
                       direction="in")  # , labelfontfamily="Times New Roman")
        ax.tick_params(axis='y', labelsize=font + 1, labelcolor='black')
        ax.yaxis.set_label_coords(-0.25, 0.5)
        # ax.xaxis.set_label_coords(0.5, -0.3)
        ax.spines['top'].set_linewidth(3)  # 上边框
        ax.spines['right'].set_linewidth(3)  # 右边框
        ax.spines['bottom'].set_linewidth(3)  # 下边框
        ax.spines['left'].set_linewidth(3)  # 左边框
        # arr = np.concatenate(([0], positions))
        ar = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        text = ['0','','2','','4','','6','','8','','10','','12','','14','','16']
        ax.set_xticks(ar)  # Ensure the number of ticks matches the length of your text
        ax.set_xticklabels(text)
        ax.xaxis.set_label_coords(0.5, -0.15)
        kr = [0,100,200,300,400,500]
        text2 = ['0   ', '100 ','200 ','300 ','400 ','500 ']
        ax.set_yticks(kr)  # Ensure the number of ticks matches the length of your text
        ax.set_yticklabels(text2)

        #legend
        handles_lines = [Line2D([0], [0], color=colors[0], linestyle='-', marker='o'),
                         Line2D([0], [0], color=colors[1], linestyle='-', marker='o'),
                         Line2D([0], [0], color=colors[2], linestyle='-', marker='o'),
                         Line2D([0], [0], color=colors[3], linestyle='-', marker='o'),
                         Line2D([0], [0], color=colors[4], linestyle='-', marker='o')]
        ax.legend(handles=handles_lines, loc=(0.43, 0.54),#(0.44, 0.55)
                  labels=['1 m','2 m', '3 m','4 m','5 m'],
                  frameon=False, fontsize=font, handlelength=0.6, ncol=2, handletextpad=0.1,
                  labelspacing=0.2, columnspacing=0.2,borderpad=0.01)
        plt.savefig('./sec3_fig14_a.pdf', format='pdf')
        plt.show()
    elif mode == 2:##Keystub-RotationX
        input_file = './data/button/SCdata/X/'
        dista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]  # 50

        all_phase5 = []
        all_phase6 = []
        all_phase12 = []
        all_phase15 = []
        all_phase20 = []
        all_phase10 = []
        midpoints5 = []
        midpoints10 = []
        midpoints12 = []
        midpoints15 = []
        midpoints6 = []
        font = font + 10
        for index, i in enumerate(dista):
            phase5 = np.loadtxt(input_file + '0-' + str(i) + '.txt', unpack=True)
            middle_phase5 = abs(phase5)
            midpoints5.append(np.median(middle_phase5))
            all_phase5.append(middle_phase5)

            phase6 = np.loadtxt(input_file + '20-' + str(i) + '.txt', unpack=True)
            middle_phase6 = abs(phase6)
            midpoints6.append(np.median(middle_phase6))
            all_phase6.append(middle_phase6)

            phase10 = np.loadtxt(input_file + '40-' + str(i) + '.txt', unpack=True)
            middle_phase10 = abs(phase10)
            midpoints10.append(np.median(middle_phase10))
            all_phase10.append(middle_phase10)

            phase12 = np.loadtxt(input_file + '60-' + str(i) + '.txt', unpack=True)
            middle_phase12 = abs(phase12)
            midpoints12.append(np.median(middle_phase12))
            all_phase12.append(middle_phase12)

            phase15 = np.loadtxt(input_file + '90-' + str(i) + '.txt', unpack=True)
            middle_phase15 = abs(phase15)
            midpoints15.append(np.median(middle_phase15))
            all_phase15.append(middle_phase15)

        fig, ax = plt.subplots(figsize=(6, 6.3), sharex=True)  # 修改为1x4的布局
        wide = 0.5
        lindw = 2
        positions = np.arange(1, 16 + 1, 1)
        # 使用箱线图代替小提琴图
        parts5 = ax.boxplot(all_phase5, positions=dista, widths=wide, patch_artist=True,
                            showmeans=False, showfliers=False)
        line5 = ax.plot(dista, midpoints5, color=colors[0], marker='o', linestyle='-',
                        linewidth=lindw, markersize=6, label='1 m')
        parts6 = ax.boxplot(all_phase6, positions=dista, widths=wide, patch_artist=True,
                            showmeans=False, showfliers=False)
        line6 = ax.plot(dista, midpoints6, color=colors[1], marker='o', linestyle='-',
                        linewidth=lindw, markersize=6, label='2 m')

        parts10 = ax.boxplot(all_phase10, positions=dista, widths=wide, patch_artist=True,
                             showmeans=False, showfliers=False)
        line10 = ax.plot(dista, midpoints10, color=colors[2], marker='o', linestyle='-',
                         linewidth=lindw, markersize=6, label='3 m')
        parts12 = ax.boxplot(all_phase12, positions=dista, widths=wide, patch_artist=True,
                             showmeans=False, showfliers=False)
        line12 = ax.plot(dista, midpoints12, color=colors[3], marker='o', linestyle='-',
                         linewidth=lindw, markersize=6, label='4 m')
        parts15 = ax.boxplot(all_phase15, positions=dista, widths=wide, patch_artist=True,
                             showmeans=False, showfliers=False)
        line15 = ax.plot(dista, midpoints15, color=colors[4], marker='o', linestyle='-',
                         linewidth=lindw, markersize=6, label='5 m')

        for parts, color in zip([parts5, parts6, parts10, parts12, parts15], colors):  # parts15
            for box in parts['boxes']:
                box.set_facecolor(color)
                box.set_edgecolor('gray')
                box.set_alpha(0.7)
            for whisker in parts['whiskers']:
                whisker.set_color(colors[5])
            for cap in parts['caps']:
                cap.set_color(colors[5])
            for median in parts['medians']:
                median.set_color(colors[5])

        # 隐藏箱线图中的均值点，或者使用 `showmeans=True` 来显示
        for parts in [parts5, parts6, parts10, parts12, parts15]:
            for mean in parts['means']:
                mean.set_markerfacecolor('r')
                mean.set_markeredgecolor('black')

        ax.set_xlim([0.75, len(positions)+0.5])
        ax.grid()
        ax.grid(True)
        ax.yaxis.set_major_locator(MultipleLocator(100))
        ax.yaxis.set_minor_locator(MultipleLocator(20))
        ax.xaxis.set_major_locator(MultipleLocator(1))
        ax.xaxis.set_minor_locator(MultipleLocator(0.5))
        # ax2.set_yticks(np.arange(0, 20, 6.36),['0','','','19'])
        plt.subplots_adjust(left=0.012, right=0.99, top=0.99,
                            bottom=0.207)  # left=0.127, right=0.98, top=0.98, bottom=0.18
        ax.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='-', linewidth=0.75, alpha=0.3)
        ax.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)
        ax.set_ylabel('Ratio γ', fontsize=font + 4, fontname="Times New Roman",
                      color='black')  # Differential Phase(rad)
        ax.set_xlabel('Button index', fontsize=font + 4, fontname="Times New Roman")
        ax.tick_params(labelsize=font, labelcolor="black", length=6, width=1,
                       direction="in")  # , labelfontfamily="Times New Roman")
        ax.tick_params(axis='y', labelsize=font + 1, labelcolor='black')
        ax.yaxis.set_label_coords(-0.06, 0.45)
        ax.xaxis.set_label_coords(0.5, -0.11)
        ax.spines['top'].set_linewidth(3)  # 上边框
        ax.spines['right'].set_linewidth(3)  # 右边框
        ax.spines['bottom'].set_linewidth(3)  # 下边框
        ax.spines['left'].set_linewidth(3)  # 左边框
        ar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        text = [' 0', '', '2', '', '4', '', '6', '', '8', '', '10', '', '12', '', '14', '', '16 ']
        ax.set_xticks(ar)  # Ensure the number of ticks matches the length of your text
        ax.set_xticklabels(text)
        #legend
        handles_lines = [Line2D([0], [0], color=colors[0], linestyle='-', marker='o'),
                         Line2D([0], [0], color=colors[1], linestyle='-', marker='o'),
                         Line2D([0], [0], color=colors[2], linestyle='-', marker='o'),
                         Line2D([0], [0], color=colors[3], linestyle='-', marker='o'),
                         Line2D([0], [0], color=colors[4], linestyle='-', marker='o')]
        ax.legend(handles=handles_lines, loc=(0.47, 0.56),#(0.265, 0.72),
                  labels=['0\u00B0','20\u00B0', '40\u00B0','60\u00B0','90\u00B0'],
                  frameon=False, fontsize=font-3, handlelength=0.7, ncol=2, handletextpad=0.1,
                  labelspacing=0.2, columnspacing=0.01,borderpad=0.01)
        ax.xaxis.set_label_coords(0.5, -0.15)
        plt.savefig('./sec3_fig14_b.pdf', format='pdf')
        plt.show()
    elif mode == 3:  ##Keystub-RotationY
        input_file = './data/button/SCdata/Y/'
        dista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]  # 50
        all_phase5 = []
        all_phase6 = []
        all_phase12 = []
        all_phase15 = []
        all_phase20 = []
        all_phase21 = []
        all_phase10 = []
        midpoints5 = []
        midpoints10 = []
        midpoints12 = []
        midpoints15 = []
        midpoints20 = []
        midpoints6 = []
        font = font + 10
        for index, i in enumerate(dista):
            phase5 = np.loadtxt(input_file + '-90-' + str(i) + '.txt', unpack=True)
            middle_phase5 = abs(phase5)
            midpoints5.append(np.median(middle_phase5))
            all_phase5.append(middle_phase5)

            phase6 = np.loadtxt(input_file + '-60-' + str(i) + '.txt', unpack=True)
            middle_phase6 = abs(phase6)
            midpoints6.append(np.median(middle_phase6))
            all_phase6.append(middle_phase6)

            phase10 = np.loadtxt(input_file + '-30-' + str(i) + '.txt', unpack=True)
            middle_phase10 = abs(phase10)
            midpoints10.append(np.median(middle_phase10))
            all_phase10.append(middle_phase10)

            phase12 = np.loadtxt(input_file + '30-' + str(i) + '.txt', unpack=True)
            middle_phase12 = abs(phase12)
            midpoints12.append(np.median(middle_phase12))
            all_phase12.append(middle_phase12)

            phase15 = np.loadtxt(input_file + '60-' + str(i) + '.txt', unpack=True)
            middle_phase15 = abs(phase15)
            midpoints15.append(np.median(middle_phase15))
            all_phase15.append(middle_phase15)

            phase20 = np.loadtxt(input_file + '90-' + str(i) + '.txt', unpack=True)
            middle_phase20 = abs(phase20)
            midpoints20.append(np.median(middle_phase20))
            all_phase20.append(middle_phase20)

        fig, ax = plt.subplots(figsize=(6, 6.3), sharex=True)  # 修改为1x4的布局
        wide = 0.5
        lindw = 2
        positions = np.arange(1, 16 + 1, 1)
        # 使用箱线图代替小提琴图
        parts5 = ax.boxplot(all_phase5, positions=dista, widths=wide, patch_artist=True,
                            showmeans=False, showfliers=False)
        line5 = ax.plot(dista, midpoints5, color=colors[0], marker='o', linestyle='-',
                        linewidth=lindw, markersize=6, label='1 m')
        parts6 = ax.boxplot(all_phase6, positions=dista, widths=wide, patch_artist=True,
                            showmeans=False, showfliers=False)
        line6 = ax.plot(dista, midpoints6, color=colors[1], marker='o', linestyle='-',
                        linewidth=lindw, markersize=6, label='2 m')
        parts10 = ax.boxplot(all_phase10, positions=dista, widths=wide, patch_artist=True,
                             showmeans=False, showfliers=False)
        line10 = ax.plot(dista, midpoints10, color=colors[2], marker='o', linestyle='-',
                         linewidth=lindw, markersize=6, label='3 m')
        parts12 = ax.boxplot(all_phase12, positions=dista, widths=wide, patch_artist=True,
                             showmeans=False, showfliers=False)
        line12 = ax.plot(dista, midpoints12, color=colors[3], marker='o', linestyle='-',
                         linewidth=lindw, markersize=6, label='4 m')
        parts15 = ax.boxplot(all_phase15, positions=dista, widths=wide, patch_artist=True,
                             showmeans=False, showfliers=False)
        line15 = ax.plot(dista, midpoints15, color=colors[4], marker='o', linestyle='-',
                         linewidth=lindw, markersize=6, label='5 m')
        parts20 = ax.boxplot(all_phase20, positions=dista, widths=wide, patch_artist=True,
                             showmeans=False, showfliers=False)
        line20 = ax.plot(dista, midpoints20, color=colors[5], marker='o', linestyle='-',
                         linewidth=lindw, markersize=6, label='6 m')

        for parts, color in zip([parts5, parts6, parts10, parts12, parts15,parts20], colors):  # parts15
            for box in parts['boxes']:
                box.set_facecolor(color)
                box.set_edgecolor('gray')
                box.set_alpha(0.7)
            for whisker in parts['whiskers']:
                whisker.set_color(colors[5])
            for cap in parts['caps']:
                cap.set_color(colors[5])
            for median in parts['medians']:
                median.set_color(colors[5])

        # 隐藏箱线图中的均值点，或者使用 `showmeans=True` 来显示
        for parts in [parts5, parts6, parts10, parts12, parts15,parts20]:
            for mean in parts['means']:
                mean.set_markerfacecolor('r')
                mean.set_markeredgecolor('black')

        ax.set_xlim([0.75, len(positions) + 0.5])
        ax.grid()
        ax.grid(True)
        ax.yaxis.set_major_locator(MultipleLocator(100))
        ax.yaxis.set_minor_locator(MultipleLocator(20))
        ax.xaxis.set_major_locator(MultipleLocator(1))
        ax.xaxis.set_minor_locator(MultipleLocator(0.5))
        # ax2.set_yticks(np.arange(0, 20, 6.36),['0','','','19'])
        plt.subplots_adjust(left=0.012, right=0.99, top=0.99,
                            bottom=0.207)  # left=0.127, right=0.98, top=0.98, bottom=0.18
        ax.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='-', linewidth=0.75, alpha=0.3)
        ax.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)
        ax.set_ylabel('Ratio γ', fontsize=font + 4, fontname="Times New Roman",
                      color='black')  # Differential Phase(rad)
        ax.set_xlabel('Button index', fontsize=font + 4, fontname="Times New Roman")
        ax.tick_params(labelsize=font, labelcolor="black", length=6, width=1,
                       direction="in")  # , labelfontfamily="Times New Roman")
        ax.tick_params(axis='y', labelsize=font + 1, labelcolor='black')
        ax.yaxis.set_label_coords(-0.06, 0.45)
        ax.xaxis.set_label_coords(0.5, -0.11)
        ax.spines['top'].set_linewidth(3)  # 上边框
        ax.spines['right'].set_linewidth(3)  # 右边框
        ax.spines['bottom'].set_linewidth(3)  # 下边框
        ax.spines['left'].set_linewidth(3)  # 左边框
        ar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        text = [' 0', '', '2', '', '4', '', '6', '', '8', '', '10', '', '12', '', '14', '', '16 ']
        ax.set_xticks(ar)  # Ensure the number of ticks matches the length of your text
        ax.set_xticklabels(text)
        # legend
        handles_lines = [Line2D([0], [0], color=colors[0], linestyle='-', marker='o'),
                         Line2D([0], [0], color=colors[1], linestyle='-', marker='o'),
                         Line2D([0], [0], color=colors[2], linestyle='-', marker='o'),
                         Line2D([0], [0], color=colors[3], linestyle='-', marker='o'),
                         Line2D([0], [0], color=colors[4], linestyle='-', marker='o'),
                         Line2D([0], [0], color=colors[5], linestyle='-', marker='o')]
        ax.legend(handles=handles_lines, loc=(0.47, 0.56),#(0.45, 0.578),
                  labels=['-90\u00B0', '-60\u00B0', '-30\u00B0', '30\u00B0', '60\u00B0', '90\u00B0'],
                  frameon=False, fontsize=font - 3, handlelength=0.7, ncol=2, handletextpad=0.1,
                  labelspacing=0.2, columnspacing=0.01, borderpad=0.01)
        ax.xaxis.set_label_coords(0.5, -0.15)
        plt.savefig('./sec3_fig14_c.pdf', format='pdf')
        plt.show()
    elif mode == 4:##Keystub-RotationZ
        input_file = './data/button/SCdata/Z/'
        dista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]  # 50

        all_phase5 = []
        all_phase6 = []
        all_phase12 = []
        all_phase15 = []
        all_phase20 = []
        all_phase10 = []
        midpoints5 = []
        midpoints10 = []
        midpoints12 = []
        midpoints15 = []
        midpoints6 = []
        font = font + 10
        for index, i in enumerate(dista):
            phase5 = np.loadtxt(input_file + '0-' + str(i) + '.txt', unpack=True)
            middle_phase5 = abs(phase5)
            midpoints5.append(np.median(middle_phase5))
            all_phase5.append(middle_phase5)

            phase6 = np.loadtxt(input_file + '20-' + str(i) + '.txt', unpack=True)
            middle_phase6 = abs(phase6)
            midpoints6.append(np.median(middle_phase6))
            all_phase6.append(middle_phase6)

            phase10 = np.loadtxt(input_file + '40-' + str(i) + '.txt', unpack=True)
            middle_phase10 = abs(phase10)
            midpoints10.append(np.median(middle_phase10))
            all_phase10.append(middle_phase10)

            phase12 = np.loadtxt(input_file + '60-' + str(i) + '.txt', unpack=True)
            middle_phase12 = abs(phase12)
            midpoints12.append(np.median(middle_phase12))
            all_phase12.append(middle_phase12)

            phase15 = np.loadtxt(input_file + '90-' + str(i) + '.txt', unpack=True)
            middle_phase15 = abs(phase15)
            midpoints15.append(np.median(middle_phase15))
            all_phase15.append(middle_phase15)

        fig, ax = plt.subplots(figsize=(6, 6.3), sharex=True)  # 修改为1x4的布局
        wide = 0.5
        lindw = 2
        positions = np.arange(1, 16 + 1, 1)
        # 使用箱线图代替小提琴图
        parts5 = ax.boxplot(all_phase5, positions=dista, widths=wide, patch_artist=True,
                            showmeans=False, showfliers=False)
        line5 = ax.plot(dista, midpoints5, color=colors[0], marker='o', linestyle='-',
                        linewidth=lindw, markersize=6, label='1 m')
        parts6 = ax.boxplot(all_phase6, positions=dista, widths=wide, patch_artist=True,
                            showmeans=False, showfliers=False)
        line6 = ax.plot(dista, midpoints6, color=colors[1], marker='o', linestyle='-',
                        linewidth=lindw, markersize=6, label='2 m')
        # raise ValueError("List of boxplot statistics and `positions` values must have the same length")

        parts10 = ax.boxplot(all_phase10, positions=dista, widths=wide, patch_artist=True,
                             showmeans=False, showfliers=False)
        line10 = ax.plot(dista, midpoints10, color=colors[2], marker='o', linestyle='-',
                         linewidth=lindw, markersize=6, label='3 m')
        parts12 = ax.boxplot(all_phase12, positions=dista, widths=wide, patch_artist=True,
                             showmeans=False, showfliers=False)
        line12 = ax.plot(dista, midpoints12, color=colors[3], marker='o', linestyle='-',
                         linewidth=lindw, markersize=6, label='4 m')
        parts15 = ax.boxplot(all_phase15, positions=dista, widths=wide, patch_artist=True,
                             showmeans=False, showfliers=False)
        line15 = ax.plot(dista, midpoints15, color=colors[4], marker='o', linestyle='-',
                         linewidth=lindw, markersize=6, label='5 m')

        for parts, color in zip([parts5, parts6, parts10, parts12, parts15], colors):  # parts15
            for box in parts['boxes']:
                box.set_facecolor(color)
                box.set_edgecolor('gray')
                box.set_alpha(0.7)
            for whisker in parts['whiskers']:
                whisker.set_color(colors[5])
            for cap in parts['caps']:
                cap.set_color(colors[5])
            for median in parts['medians']:
                median.set_color(colors[5])

        # 隐藏箱线图中的均值点，或者使用 `showmeans=True` 来显示
        for parts in [parts5, parts6, parts10, parts12, parts15]:
            for mean in parts['means']:
                mean.set_markerfacecolor('r')
                mean.set_markeredgecolor('black')

        ax.set_xlim([0.75, len(positions)+0.5])
        # ax.set_ylim([0, np.pi])
        # ax.set_ylim([0, 1.99])
        # ax2.set_ylim([0, 20])
        ax.grid()
        ax.grid(True)
        ax.yaxis.set_major_locator(MultipleLocator(100))
        ax.yaxis.set_minor_locator(MultipleLocator(20))
        ax.xaxis.set_major_locator(MultipleLocator(1))
        ax.xaxis.set_minor_locator(MultipleLocator(0.5))
        # ax2.set_yticks(np.arange(0, 20, 6.36),['0','','','19'])
        plt.subplots_adjust(left=0.012, right=0.99, top=0.99,
                            bottom=0.207)  # left=0.127, right=0.98, top=0.98, bottom=0.18
        ax.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='-', linewidth=0.75, alpha=0.3)
        ax.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)
        ax.set_ylabel('Ratio γ', fontsize=font + 4, fontname="Times New Roman",
                      color='black')  # Differential Phase(rad)
        ax.set_xlabel('Button index', fontsize=font + 4, fontname="Times New Roman")
        ax.tick_params(labelsize=font, labelcolor="black", length=6, width=1,
                       direction="in")  # , labelfontfamily="Times New Roman")
        ax.tick_params(axis='y', labelsize=font + 1, labelcolor='black')
        ax.yaxis.set_label_coords(-0.06, 0.45)
        ax.xaxis.set_label_coords(0.5, -0.11)
        ax.spines['top'].set_linewidth(3)  # 上边框
        ax.spines['right'].set_linewidth(3)  # 右边框
        ax.spines['bottom'].set_linewidth(3)  # 下边框
        ax.spines['left'].set_linewidth(3)  # 左边框
        ar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        text = [' 0', '', '2', '', '4', '', '6', '', '8', '', '10', '', '12', '', '14', '', '16 ']
        ax.set_xticks(ar)  # Ensure the number of ticks matches the length of your text
        ax.set_xticklabels(text)
        #legend
        handles_lines = [Line2D([0], [0], color=colors[0], linestyle='-', marker='o'),
                         Line2D([0], [0], color=colors[1], linestyle='-', marker='o'),
                         Line2D([0], [0], color=colors[2], linestyle='-', marker='o'),
                         Line2D([0], [0], color=colors[3], linestyle='-', marker='o'),
                         Line2D([0], [0], color=colors[4], linestyle='-', marker='o')]
        ax.legend(handles=handles_lines, loc=(0.47, 0.56),#(0.265, 0.72),
                  labels=['0\u00B0','20\u00B0', '40\u00B0','60\u00B0','90\u00B0'],
                  frameon=False, fontsize=font-3, handlelength=0.7, ncol=2, handletextpad=0.1,
                  labelspacing=0.2, columnspacing=0.01,borderpad=0.01)
        ax.xaxis.set_label_coords(0.5, -0.15)
        plt.savefig('./sec3_fig14_d.pdf', format='pdf')
        plt.show()