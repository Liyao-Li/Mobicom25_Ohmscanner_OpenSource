# for filter data to obvious distribution distance between wifi play time and cellular play time
import numpy as np
import pandas as pd
from matplotlib.patches import Patch
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
##
##
##
##
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
    colors = [np.array([255, 46, 41]) / 255,np.array([0, 114, 189]) / 255,
              np.array([237, 177, 32]) / 255, np.array([119, 172, 48]) / 255,
              np.array([136, 137, 139]) / 255, np.array([100, 100, 100]) / 255]
    ##distance_differencial
if mode == 1:
    input_file = './data/diffirencialtag/distance/1.5m'
    dista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    distb = [0, 10, 20, 30]
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
    font = font
    for index, i in enumerate(dista):
        phase5, RSS5 = np.loadtxt(input_file + '/second-' + str(i) + '.txt', unpack=True)
        phase10, RSS10 = np.loadtxt(input_file + '/third-' + str(i) + '.txt', unpack=True)
        phase15, RSS15 = np.loadtxt(input_file + '/fourth-' + str(i) + '.txt', unpack=True)
        middle_phase5 = abs(phase5)
        middle_phase10 = abs(phase10)
        middle_phase15 = abs(phase15)
        if min(middle_phase5) > 4:
            middle_phase5 = middle_phase5 - np.pi * 2
        if min(middle_phase5) > 2:
            middle_phase5 = abs(middle_phase5 - np.pi)
        if min(middle_phase5) < 0:
            middle_phase5 = abs(middle_phase5)

        if min(middle_phase10) > 4:
            middle_phase10 = middle_phase10 - np.pi * 2
        if min(middle_phase10) > np.pi:
            middle_phase10 = abs(middle_phase10 - np.pi)
        if min(middle_phase10) < 0:
            middle_phase10 = abs(middle_phase10)

        if min(middle_phase15) > 4:
            middle_phase15 = middle_phase15 - np.pi * 2
        if min(middle_phase15) > np.pi:
            middle_phase15 = abs(middle_phase15 - np.pi)
        if min(middle_phase15) < 0:
            middle_phase15 = abs(middle_phase15)
        midpoints5.append(np.median(middle_phase5))
        midpoints10.append(np.median(middle_phase10))
        midpoints15.append(np.median(middle_phase15))

        all_phase5.append(middle_phase5)
        all_phase10.append(middle_phase10)
        all_phase15.append(middle_phase15)

    fig, ax = plt.subplots(figsize=(7, 5.5), sharex=True)  # 修改为1x4的布局
    wide = 0.5
    lindw = 2
    positions = np.arange(1, len(dista) + 1, 1)
    # 使用箱线图代替小提琴图
    parts5 = ax.boxplot(all_phase5, positions=positions, widths=wide, patch_artist=True,
                        showmeans=False, showfliers=False)
    line5 = ax.plot(positions, midpoints5, color=colors[0], marker='o', linestyle='-',
                    linewidth=lindw, markersize=6, label='1 m')
    parts10 = ax.boxplot(all_phase10, positions=positions, widths=wide, patch_artist=True,
                         showmeans=False, showfliers=False)
    line10 = ax.plot(positions, midpoints10, color=colors[1], marker='o', linestyle='-',
                     linewidth=lindw, markersize=6, label='1.5 m')
    parts15 = ax.boxplot(all_phase15, positions=positions, widths=wide, patch_artist=True,
                         showmeans=False, showfliers=False)
    line15 = ax.plot(positions, midpoints15, color=colors[2], marker='o', linestyle='-',
                     linewidth=lindw, markersize=6, label='2 m')

    for parts, color in zip([parts5, parts10, parts15], colors):  # parts15
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
    for parts in [parts5, parts10, parts15]:
        for mean in parts['means']:
            mean.set_markerfacecolor('r')
            mean.set_markeredgecolor('black')

    ax.set_ylim([0, np.pi])
    ax.grid()
    ax.grid(True)
    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_minor_locator(MultipleLocator(0.1))
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.xaxis.set_minor_locator(MultipleLocator(0.5))
    plt.subplots_adjust(left=0.146, right=0.996, top=0.99,
                        bottom=0.18)  # left=0.127, right=0.98, top=0.98, bottom=0.18
    ax.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='-', linewidth=0.75, alpha=0.3)
    ax.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)
    # print(gamma)
    print("α, β, γ, δ, ε")
    ax.set_ylabel('Phase of γ (radian)', fontsize=font + 4, fontname="Times New Roman",
                  color='black')  # Differential Phase(rad)
    ax.set_xlabel('Finger touch position', fontsize=font + 4, fontname="Times New Roman")
    ax.tick_params(labelsize=font, labelcolor="black", length=6, width=1,
                   direction="in")  # , labelfontfamily="Times New Roman")
    ax.tick_params(axis='y', labelsize=font + 1, labelcolor='black')
    ax.yaxis.set_label_coords(-0.08, 0.5)
    ax.xaxis.set_label_coords(0.5, -0.1)
    ax.spines['top'].set_linewidth(2)  # 上边框
    ax.spines['right'].set_linewidth(2)  # 右边框
    ax.spines['bottom'].set_linewidth(2)  # 下边框
    ax.spines['left'].set_linewidth(2)  # 左边框

    text = ['1', '', '3', '', '5', '', '7', '', '9']
    ax.set_xticks(positions[0:len(dista)])  # Ensure the number of ticks matches the length of your text
    ax.set_xticklabels(text)
    # legend
    handles_lines = [Line2D([0], [0], color=colors[0], linestyle='-', marker='o', label='Vertical phase'),
                     Line2D([0], [0], color=colors[1], linestyle='-', marker='o', label='Vertical RSS'),
                     Line2D([0], [0], color=colors[2], linestyle='-', marker='o', label='Vertical RSS')]
    ax.legend(handles=handles_lines, loc=(0.65, 0.6),
              labels=['0.5m', '1 m', '1.5m'],
              frameon=False, fontsize=font - 2, handlelength=0.8, ncol=1, handletextpad=0.1,
              labelspacing=0.2, columnspacing=0.2, borderpad=0.01)

    plt.savefig('./sec2_fig4_a.pdf', format='pdf')
    plt.show()
elif mode == 2:  ##distance_differencial
    input_file = './data/diffirencialtag/distance/1.5m'
    dista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    distb = [0, 10, 20, 30]
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
    font = font
    for index, i in enumerate(dista):
        phase5, RSS5 = np.loadtxt(input_file + '/rotate20-' + str(i) + '.txt', unpack=True)
        phase10, RSS10 = np.loadtxt(input_file + '/rotate40-' + str(i) + '.txt', unpack=True)
        phase15, RSS15 = np.loadtxt(input_file + '/third-' + str(i) + '.txt', unpack=True)
        phase20, RSS20 = np.loadtxt(input_file + '/rotate-40-' + str(i) + '.txt', unpack=True)

        middle_phase5 = abs(phase5)
        middle_phase10 = abs(phase10)
        middle_phase15 = abs(phase15)
        middle_phase20 = abs(phase20)
        midpoints5.append(np.median(middle_phase5))
        midpoints10.append(np.median(middle_phase10))
        midpoints15.append(np.median(middle_phase15))
        midpoints20.append(np.median(middle_phase20))

        all_phase5.append(middle_phase5)
        all_phase10.append(middle_phase10)
        all_phase15.append(middle_phase15)
        all_phase20.append(middle_phase20)
    fig, ax = plt.subplots(figsize=(6, 5.5), sharex=True)  # 修改为1x4的布局
    wide = 0.5
    lindw = 2
    positions = np.arange(1, len(dista) + 1, 1)

    # 使用箱线图代替小提琴图
    parts5 = ax.boxplot(all_phase5, positions=positions, widths=wide, patch_artist=True,
                        showmeans=False, showfliers=False)
    line5 = ax.plot(positions, midpoints5, color=colors[0], marker='o', linestyle='-',
                    linewidth=lindw, markersize=6, label='1 m')
    parts10 = ax.boxplot(all_phase10, positions=positions, widths=wide, patch_artist=True,
                         showmeans=False, showfliers=False)
    line10 = ax.plot(positions, midpoints10, color=colors[1], marker='o', linestyle='-',
                     linewidth=lindw, markersize=6, label='1.5 m')
    parts15 = ax.boxplot(all_phase15, positions=positions, widths=wide, patch_artist=True,
                         showmeans=False, showfliers=False)
    line15 = ax.plot(positions, midpoints15, color=colors[2], marker='o', linestyle='-',
                     linewidth=lindw, markersize=6, label='2 m')
    parts20 = ax.boxplot(all_phase20, positions=positions, widths=wide, patch_artist=True,
                         showmeans=False, showfliers=False)
    line20 = ax.plot(positions, midpoints20, color=colors[3], marker='o', linestyle='-',
                     linewidth=lindw, markersize=6, label='2 m')

    for parts, color in zip([parts5, parts10, parts15, parts20], colors):  # parts15
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
    for parts in [parts5, parts10, parts15, parts20]:
        for mean in parts['means']:
            mean.set_markerfacecolor('r')
            mean.set_markeredgecolor('black')

    ax.set_ylim([0, np.pi])
    ax.grid()
    ax.grid(True)
    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_minor_locator(MultipleLocator(0.1))
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.xaxis.set_minor_locator(MultipleLocator(0.5))
    plt.subplots_adjust(left=0.01, right=0.996, top=0.99,
                        bottom=0.18)  # left=0.127, right=0.98, top=0.98, bottom=0.18
    ax.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='-', linewidth=0.75, alpha=0.3)
    ax.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)

    ax.set_ylabel('γ phase (radian)', fontsize=font + 4, fontname="Times New Roman",
                  color='black')  # Differential Phase(rad)
    ax.set_xlabel('Finger touch position', fontsize=font + 4, fontname="Times New Roman")
    ax.tick_params(labelsize=font, labelcolor="black", length=6, width=1,
                   direction="in")  # , labelfontfamily="Times New Roman")
    ax.tick_params(axis='y', labelsize=font + 1, labelcolor='black')

    ax.yaxis.set_label_coords(-0.089, 0.45)
    ax.xaxis.set_label_coords(0.5, -0.1)
    ax.spines['top'].set_linewidth(2)  # 上边框
    ax.spines['right'].set_linewidth(2)  # 右边框
    ax.spines['bottom'].set_linewidth(2)  # 下边框
    ax.spines['left'].set_linewidth(2)  # 左边框
    text = ['1', '', '3', '', '5', '', '7', '', '9']
    ax.set_xticks(positions[0:len(dista)])  # Ensure the number of ticks matches the length of your text
    ax.set_xticklabels(text)
    # legend
    handles_lines = [Line2D([0], [0], color=colors[0], linestyle='-', marker='o', label='Vertical phase'),
                     Line2D([0], [0], color=colors[1], linestyle='-', marker='o', label='Vertical RSS'),
                     Line2D([0], [0], color=colors[2], linestyle='-', marker='o', label='Vertical RSS'),
                     Line2D([0], [0], color=colors[3], linestyle='-', marker='o', label='Vertical RSS')]
    ax.legend(handles=handles_lines, loc=(0.7, 0.2),
              labels=['H-20\u00B0', 'H-40\u00B0', 'V-20\u00B0', 'V-40\u00B0'],
              frameon=True, fontsize=font - 2, handlelength=0.6, ncol=1, handletextpad=0.1,
              labelspacing=0.1, columnspacing=0.2, borderpad=0.01)
    plt.savefig('./sec2_fig4_d.pdf', format='pdf')
    plt.show()
elif mode == 3:  ##angle_differencial
    input_file = './data/diffirencialtag/distance/1.5m'
    dista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    distb = [0, 10, 20, 30]
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
    font = font
    for index, i in enumerate(dista):
        phase5, RSS5 = np.loadtxt(input_file + '/angle20-' + str(i) + '.txt', unpack=True)
        phase10, RSS10 = np.loadtxt(input_file + '/angle40-' + str(i) + '.txt', unpack=True)
        phase15, RSS15 = np.loadtxt(input_file + '/angle60-' + str(i) + '.txt', unpack=True)
        middle_phase5 = abs(phase5)
        middle_phase10 = abs(phase10)
        middle_phase15 = abs(phase15)

        midpoints5.append(np.median(middle_phase5))
        midpoints10.append(np.median(middle_phase10))
        midpoints15.append(np.median(middle_phase15))

        all_phase5.append(middle_phase5)
        all_phase10.append(middle_phase10)
        all_phase15.append(middle_phase15)

    fig, ax = plt.subplots(figsize=(6, 5.5), sharex=True)  # 修改为1x4的布局
    wide = 0.5
    lindw = 2
    positions = np.arange(1, len(dista) + 1, 1)
    # 使用箱线图代替小提琴图
    parts5 = ax.boxplot(all_phase5, positions=positions, widths=wide, patch_artist=True,
                        showmeans=False, showfliers=False)
    line5 = ax.plot(positions, midpoints5, color=colors[0], marker='o', linestyle='-',
                    linewidth=lindw, markersize=6, label='1 m')
    parts10 = ax.boxplot(all_phase10, positions=positions, widths=wide, patch_artist=True,
                         showmeans=False, showfliers=False)
    line10 = ax.plot(positions, midpoints10, color=colors[1], marker='o', linestyle='-',
                     linewidth=lindw, markersize=6, label='1.5 m')
    parts15 = ax.boxplot(all_phase15, positions=positions, widths=wide, patch_artist=True,
                         showmeans=False, showfliers=False)
    line15 = ax.plot(positions, midpoints15, color=colors[2], marker='o', linestyle='-',
                     linewidth=lindw, markersize=6, label='2 m')

    for parts, color in zip([parts5, parts10, parts15], colors):  # parts15
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
    for parts in [parts5, parts10, parts15]:
        for mean in parts['means']:
            mean.set_markerfacecolor('r')
            mean.set_markeredgecolor('black')

    ax.set_ylim([0, np.pi])
    ax.grid()
    ax.grid(True)
    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_minor_locator(MultipleLocator(0.1))
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.xaxis.set_minor_locator(MultipleLocator(0.5))
    plt.subplots_adjust(left=0.01, right=0.996, top=0.99,
                        bottom=0.18)  # left=0.127, right=0.98, top=0.98, bottom=0.18
    ax.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='-', linewidth=0.75, alpha=0.3)
    ax.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)
    ax.set_ylabel('Ratio γ', fontsize=font + 4, fontname="Times New Roman",
                  color='black')  # Differential Phase(rad)
    ax.set_xlabel('Finger touch position', fontsize=font + 4, fontname="Times New Roman")
    ax.tick_params(labelsize=font, labelcolor="black", length=6, width=1,
                   direction="in")  # , labelfontfamily="Times New Roman")
    ax.tick_params(axis='y', labelsize=font + 1, labelcolor='black')
    ax.yaxis.set_label_coords(-0.089, 0.45)
    ax.xaxis.set_label_coords(0.5, -0.1)
    ax.spines['top'].set_linewidth(2)  # 上边框
    ax.spines['right'].set_linewidth(2)  # 右边框
    ax.spines['bottom'].set_linewidth(2)  # 下边框
    ax.spines['left'].set_linewidth(2)  # 左边框
    text = ['1', '', '3', '', '5', '', '7', '', '9']
    ax.set_xticks(positions[0:len(dista)])  # Ensure the number of ticks matches the length of your text
    ax.set_xticklabels(text)
    # legend
    handles_lines = [Line2D([0], [0], color=colors[0], linestyle='-', marker='o', label='Vertical phase'),
                     Line2D([0], [0], color=colors[1], linestyle='-', marker='o', label='Vertical RSS'),
                     Line2D([0], [0], color=colors[2], linestyle='-', marker='o', label='Vertical RSS')]
    ax.legend(handles=handles_lines, loc=(0.65, 0.58),
              labels=['20 \u00B0', '40 \u00B0', '60 \u00B0'],
              frameon=False, fontsize=font - 5, handlelength=0.8, ncol=1, handletextpad=0.1,
              labelspacing=0.2, columnspacing=0.2, borderpad=0.01)
    plt.savefig('./sec2_fig4_b.pdf', format='pdf')
    plt.show()
elif mode == 4:  ##height_differencial
    input_file = './data/diffirencialtag/distance/1.5m'
    dista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    distb = [0, 10, 20, 30]
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
    font = font
    for index, i in enumerate(dista):
        phase5, RSS5 = np.loadtxt(input_file + '/height60-' + str(i) + '.txt', unpack=True)
        phase10, RSS10 = np.loadtxt(input_file + '/height90-' + str(i) + '.txt', unpack=True)
        phase15, RSS15 = np.loadtxt(input_file + '/height150-' + str(i) + '.txt', unpack=True)
        middle_phase5 = abs(phase5)
        middle_phase10 = abs(phase10)
        middle_phase15 = abs(phase15)

        midpoints5.append(np.median(middle_phase5))
        midpoints10.append(np.median(middle_phase10))
        midpoints15.append(np.median(middle_phase15))

        all_phase5.append(middle_phase5)
        all_phase10.append(middle_phase10)
        all_phase15.append(middle_phase15)
    fig, ax = plt.subplots(figsize=(6, 5.5), sharex=True)  # 修改为1x4的布局
    wide = 0.5
    lindw = 2
    positions = np.arange(1, len(dista) + 1, 1)
    # 使用箱线图代替小提琴图
    parts5 = ax.boxplot(all_phase5, positions=positions, widths=wide, patch_artist=True,
                        showmeans=False, showfliers=False)
    line5 = ax.plot(positions, midpoints5, color=colors[0], marker='o', linestyle='-',
                    linewidth=lindw, markersize=6, label='1 m')
    parts10 = ax.boxplot(all_phase10, positions=positions, widths=wide, patch_artist=True,
                         showmeans=False, showfliers=False)
    line10 = ax.plot(positions, midpoints10, color=colors[1], marker='o', linestyle='-',
                     linewidth=lindw, markersize=6, label='1.5 m')
    parts15 = ax.boxplot(all_phase15, positions=positions, widths=wide, patch_artist=True,
                         showmeans=False, showfliers=False)
    line15 = ax.plot(positions, midpoints15, color=colors[2], marker='o', linestyle='-',
                     linewidth=lindw, markersize=6, label='2 m')

    for parts, color in zip([parts5, parts10, parts15], colors):  # parts15
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
    for parts in [parts5, parts10, parts15]:
        for mean in parts['means']:
            mean.set_markerfacecolor('r')
            mean.set_markeredgecolor('black')

    ax.set_ylim([0, np.pi])
    ax.grid()
    ax.grid(True)
    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_minor_locator(MultipleLocator(0.1))
    ax.xaxis.set_major_locator(MultipleLocator(1))
    # ax2.yaxis.set_major_locator(MultipleLocator(3))
    ax.xaxis.set_minor_locator(MultipleLocator(0.5))
    plt.subplots_adjust(left=0.01, right=0.996, top=0.99,
                        bottom=0.18)  # left=0.127, right=0.98, top=0.98, bottom=0.18
    ax.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='-', linewidth=0.75, alpha=0.3)
    ax.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)

    ax.set_ylabel('Ratio γ', fontsize=font + 4, fontname="Times New Roman",
                  color='black')  # Differential Phase(rad)
    ax.set_xlabel('Finger touch position', fontsize=font + 4, fontname="Times New Roman")
    ax.tick_params(labelsize=font, labelcolor="black", length=6, width=1,
                   direction="in")  # , labelfontfamily="Times New Roman")
    ax.tick_params(axis='y', labelsize=font + 1, labelcolor='black')
    ax.yaxis.set_label_coords(-0.089, 0.45)
    ax.xaxis.set_label_coords(0.5, -0.1)
    ax.spines['top'].set_linewidth(2)  # 上边框
    ax.spines['right'].set_linewidth(2)  # 右边框
    ax.spines['bottom'].set_linewidth(2)  # 下边框
    ax.spines['left'].set_linewidth(2)  # 左边框
    text = ['1', '', '3', '', '5', '', '7', '', '9']
    ax.set_xticks(positions[0:len(dista)])  # Ensure the number of ticks matches the length of your text
    ax.set_xticklabels(text)
    # legend
    handles_lines = [Line2D([0], [0], color=colors[0], linestyle='-', marker='o', label='Vertical phase'),
                     Line2D([0], [0], color=colors[1], linestyle='-', marker='o', label='Vertical RSS'),
                     Line2D([0], [0], color=colors[2], linestyle='-', marker='o', label='Vertical RSS')]
    ax.legend(handles=handles_lines, loc=(0.1, 0.83),
              labels=['0.3m', '1m', '1.5m'],
              frameon=False, fontsize=font - 2, handlelength=0.8, ncol=3, handletextpad=0.1,
              labelspacing=0.2, columnspacing=0.2, borderpad=0.01)
    plt.savefig('./sec2_fig4_c.pdf', format='pdf')
    plt.show()