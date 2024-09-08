# for filter data to obvious distribution distance between wifi play time and cellular play time
# for filter data to obvious distribution distance between wifi play time and cellular play time
import numpy as np
import pandas as pd
from matplotlib.patches import Patch
import matplotlib.pyplot as plt
import sys
import seaborn as sns
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator
from matplotlib.lines import Line2D
mpl.rcParams['font.family'] = 'Times New Roman'
## mode == 1 single tag finger touch positon _different distances
## mode == 2 single tag finger touch positon _different orientations
if __name__ == "__main__":
    mode = int(sys.argv[1])
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
    colors = [np.array([255, 46, 41]) / 255,np.array([0, 114, 189]) / 255,
              np.array([237, 177, 32]) / 255, np.array([119, 172, 48]) / 255,
              np.array([136, 137, 139]) / 255, np.array([100, 100, 100]) / 255]
    if mode == 1:##keystub_pitch
        input_file = './data/dogbone'
        dista = [1,2,3,4,5,6,7,8,9]
        distb = [0,10,20,30]
        all_phase5 = []
        all_phase15 = []
        all_phase20 = []
        all_phase10 = []
        all_RSS5 = []
        all_RSS15 = []
        all_RSS20 = []
        all_RSS10 = []
        midpoints5 = []
        midpoints10 = []
        midpoints15 = []
        midpoints20 = []
        midpointsRSS5 = []
        midpointsRSS10 = []
        midpointsRSS15 = []
        midpointsRSS20 = []
        font = font -4
        for index, i in enumerate(dista):
            phase5, RSS5 = np.loadtxt(input_file + '/rote0-' + str(i) + '.txt', unpack=True)
            phase10, RSS10 = np.loadtxt(input_file + '/dis1-' + str(i) + '.txt', unpack=True)
            phase15, RSS15 = np.loadtxt(input_file + '/dis2-' + str(i) + '.txt', unpack=True)
            middle_phase5 = abs(phase5)
            middle_phase10 = abs(phase10)
            middle_phase15 = abs(phase15)
            if min(middle_phase5) > 4:
                middle_phase5 = middle_phase5-np.pi*2
            if min(middle_phase5) > 2:
                middle_phase5 = abs(middle_phase5-np.pi)
            if min(middle_phase5) < 0:
                middle_phase5 = abs(middle_phase5)

            if min(middle_phase10) > 4:
                middle_phase10 = middle_phase10-np.pi*2
            if min(middle_phase10) > np.pi:
                middle_phase10 = abs(middle_phase10-np.pi)
            if min(middle_phase10) < 0:
                middle_phase10 = abs(middle_phase10)

            if min(middle_phase15) > 4:
                middle_phase15 = middle_phase15-np.pi*2
            if min(middle_phase15) > np.pi:
                middle_phase15 = abs(middle_phase15-np.pi)
            if min(middle_phase15) < 0:
                middle_phase15 = abs(middle_phase15)

            midpoints5.append(np.mean(middle_phase5))
            midpoints10.append(np.mean(middle_phase10))
            midpoints15.append(np.mean(middle_phase15))

            all_phase5.append(middle_phase5)
            all_phase10.append(middle_phase10)
            all_phase15.append(middle_phase15)

        fig, ax = plt.subplots(figsize=(6.5, 4), sharex=True)  # 修改为1x4的布局
        wide = 0.5
        lindw = 2
        positions = np.arange(1, len(dista) + 1, 1)
        # print(all_phase10)
        print(len(all_phase10))
        print(len(positions))
        # 使用箱线图代替小提琴图
        parts5 = ax.boxplot(all_phase5, positions=positions[0:len(dista)], widths=wide, patch_artist=True,
                             showmeans=False, showfliers=False)
        line5 = ax.plot(positions[0:len(dista)], midpoints5, color=colors[0], marker='o', linestyle='-',
                         linewidth=lindw, markersize=6, label='1 m')
        parts10 = ax.boxplot(all_phase10, positions=positions[0:len(dista)+1], widths=wide, patch_artist=True,
                             showmeans=False, showfliers=False)
        line10 = ax.plot(positions[0:len(dista)], midpoints10, color=colors[1], marker='o', linestyle='-',
                         linewidth=lindw, markersize=6, label='1.5 m')
        parts15 = ax.boxplot(all_phase15, positions=positions[0:len(dista)], widths=wide, patch_artist=True,
                             showmeans=False, showfliers=False)
        line15 = ax.plot(positions[0:len(dista)], midpoints15, color=colors[2], marker='o', linestyle='-',
                         linewidth=lindw, markersize=6, label='2 m')


        for parts, color in zip([parts5,parts10,parts15], colors):  # parts15
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
        for parts in [parts5,parts10,parts15]:
            for mean in parts['means']:
                mean.set_markerfacecolor('r')
                mean.set_markeredgecolor('black')

        ax.set_ylim([0, np.pi+0.05])
        ax.grid()
        ax.grid(True)
        ax.yaxis.set_major_locator(MultipleLocator(1))
        ax.yaxis.set_minor_locator(MultipleLocator(0.1))
        ax.xaxis.set_major_locator(MultipleLocator(1))
        ax.xaxis.set_minor_locator(MultipleLocator(0.5))
        plt.subplots_adjust(left=0.146, right=0.996, top=0.98,
                            bottom=0.207)  # left=0.127, right=0.98, top=0.98, bottom=0.18
        ax.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='-', linewidth=0.75, alpha=0.3)
        ax.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)
        ax.set_ylabel('Phase (radian)', fontsize=font, fontname="Times New Roman",color = 'black')
        ax.set_xlabel('Finger touch position', fontsize=font, fontname="Times New Roman")
        ax.tick_params(labelsize=font, labelcolor="black", length=6, width=1,
                       direction="in")  # , labelfontfamily="Times New Roman")
        ax.tick_params(axis='y', labelsize=font, labelcolor='black')
        ax.yaxis.set_label_coords(-0.09, 0.5)
        ax.xaxis.set_label_coords(0.5, -0.12)
        ax.spines['top'].set_linewidth(2)  # 上边框
        ax.spines['right'].set_linewidth(2)  # 右边框
        ax.spines['bottom'].set_linewidth(2)  # 下边框
        ax.spines['left'].set_linewidth(2)  # 左边框
        text = ['1','','3','','5','','7','','9']
        ax.set_xticks(positions[0:len(dista)])  # Ensure the number of ticks matches the length of your text
        ax.set_xticklabels(text)
        #legend
        handles_lines = [Line2D([0], [0], color=colors[1], linestyle='-', marker='o', label='Vertical phase'),
                         Line2D([0], [0], color=colors[0], linestyle='-', marker='o', label='Vertical RSS'),
                         Line2D([0], [0], color=colors[2], linestyle='-', marker='o', label='Vertical RSS')]
        ax.legend(handles=handles_lines, loc=(0.22, 0.87),
                  labels=['0.5 m', '1 m','1.5 m'],
                  frameon=False, fontsize=font - 5, handlelength=0.7, ncol=3, handletextpad=0.1,
                  labelspacing=0, columnspacing=0.5,borderpad=0.01)
        plt.savefig('./sec2_fig2_b.pdf', format='pdf')
        plt.show()
    elif mode == 2:##keystub_pitch
        input_file = './data/dogbone'
        dista = [1,2,3,4,5,6,7,8,9]
        distb = [0,10,20,30]
        all_phase5 = []
        all_phase15 = []
        all_phase20 = []
        all_phase10 = []
        all_RSS5 = []
        all_RSS15 = []
        all_RSS20 = []
        all_RSS10 = []
        midpoints5 = []
        midpoints10 = []
        midpoints15 = []
        midpoints20 = []
        midpointsRSS5 = []
        midpointsRSS10 = []
        midpointsRSS15 = []
        midpointsRSS20 = []
        font = font -4
        for index, i in enumerate(dista):
            phase5, RSS5 = np.loadtxt(input_file + '/rote0-' + str(i) + '.txt', unpack=True)
            phase10, RSS10 = np.loadtxt(input_file + '/rote40-' + str(i) + '.txt', unpack=True)
            phase15, RSS15 = np.loadtxt(input_file + '/rote80-' + str(i) + '.txt', unpack=True)
            middle_phase5 = abs(phase5)
            middle_phase10 = abs(phase10)
            middle_phase15 = abs(phase15)
            if min(middle_phase5) > 4:
                middle_phase5 = middle_phase5-np.pi*2
            if min(middle_phase5) > 2:
                middle_phase5 = abs(middle_phase5-np.pi)
            if min(middle_phase5) < 0:
                middle_phase5 = abs(middle_phase5)

            if min(middle_phase10) > 4:
                middle_phase10 = middle_phase10-np.pi*2
            if min(middle_phase10) > np.pi:
                middle_phase10 = abs(middle_phase10-np.pi)
            if min(middle_phase10) < 0:
                middle_phase10 = abs(middle_phase10)

            if min(middle_phase15) > 4:
                middle_phase15 = middle_phase15-np.pi*2
            if min(middle_phase15) > np.pi:
                middle_phase15 = abs(middle_phase15-np.pi)
            if min(middle_phase15) < 0:
                middle_phase15 = abs(middle_phase15)

            midpoints5.append(np.mean(middle_phase5))
            midpoints10.append(np.mean(middle_phase10))
            midpoints15.append(np.mean(middle_phase15))

            all_phase5.append(middle_phase5)
            all_phase10.append(middle_phase10)
            all_phase15.append(middle_phase15)
        fig, ax = plt.subplots(figsize=(6.5, 4), sharex=True)  # 修改为1x4的布局
        wide = 0.5
        lindw = 2
        positions = np.arange(1, len(dista) + 1, 1)
        # print(all_phase10)
        print(len(all_phase10))
        print(len(positions))
        # 使用箱线图代替小提琴图
        parts5 = ax.boxplot(all_phase5, positions=positions[0:len(dista)], widths=wide, patch_artist=True,
                             showmeans=False, showfliers=False)
        line5 = ax.plot(positions[0:len(dista)], midpoints5, color=colors[0], marker='o', linestyle='-',
                         linewidth=lindw, markersize=6, label='1 m')
        parts10 = ax.boxplot(all_phase10, positions=positions[0:len(dista)+1], widths=wide, patch_artist=True,
                             showmeans=False, showfliers=False)
        line10 = ax.plot(positions[0:len(dista)], midpoints10, color=colors[1], marker='o', linestyle='-',
                         linewidth=lindw, markersize=6, label='1.5 m')
        parts15 = ax.boxplot(all_phase15, positions=positions[0:len(dista)], widths=wide, patch_artist=True,
                             showmeans=False, showfliers=False)
        line15 = ax.plot(positions[0:len(dista)], midpoints15, color=colors[2], marker='o', linestyle='-',
                         linewidth=lindw, markersize=6, label='2 m')


        for parts, color in zip([parts5,parts10,parts15], colors):  # parts15
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
        for parts in [parts5,parts10,parts15]:
            for mean in parts['means']:
                mean.set_markerfacecolor('r')
                mean.set_markeredgecolor('black')

        ax.set_ylim([0, np.pi+0.05])
        ax.grid()
        ax.grid(True)
        ax.yaxis.set_major_locator(MultipleLocator(1))
        ax.yaxis.set_minor_locator(MultipleLocator(0.1))
        ax.xaxis.set_major_locator(MultipleLocator(1))
        ax.xaxis.set_minor_locator(MultipleLocator(0.5))
        plt.subplots_adjust(left=0.146, right=0.996, top=0.99,
                            bottom=0.21)  # left=0.127, right=0.98, top=0.98, bottom=0.18
        ax.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='-', linewidth=0.75, alpha=0.3)
        ax.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)
        ax.set_ylabel('Phase (radian)', fontsize=font, fontname="Times New Roman",color = 'black')
        ax.set_xlabel('Finger touch position', fontsize=font, fontname="Times New Roman")
        ax.tick_params(labelsize=font, labelcolor="black", length=6, width=1,
                       direction="in")  # , labelfontfamily="Times New Roman")
        ax.tick_params(axis='y', labelsize=font, labelcolor='black')
        ax.yaxis.set_label_coords(-0.09, 0.5)
        ax.xaxis.set_label_coords(0.5, -0.12)
        ax.spines['top'].set_linewidth(2)  # 上边框
        ax.spines['right'].set_linewidth(2)  # 右边框
        ax.spines['bottom'].set_linewidth(2)  # 下边框
        ax.spines['left'].set_linewidth(2)  # 左边框
        text = ['1',' ','3','','5','','7','','9']
        ax.set_xticks(positions[0:len(dista)])  # Ensure the number of ticks matches the length of your text
        ax.set_xticklabels(text)
        #legend
        handles_lines = [Line2D([0], [0], color=colors[0], linestyle='-', marker='o', label='Vertical phase'),
                         Line2D([0], [0], color=colors[1], linestyle='-', marker='o', label='Vertical RSS'),
                         Line2D([0], [0], color=colors[2], linestyle='-', marker='o', label='Vertical RSS')]
        ax.legend(handles=handles_lines, loc=(0.01, -0),
                  labels=['0\u00B0', '40\u00B0','80\u00B0'],
                  frameon=False, fontsize=font - 5, handlelength=0.7, ncol=3, handletextpad=0.1,
                  labelspacing=0.2, columnspacing=0.2,borderpad=0.01)
        plt.savefig('./sec2_fig2_c.pdf', format='pdf')
        plt.show()