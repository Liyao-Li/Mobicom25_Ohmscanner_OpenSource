import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator
import matplotlib as mpl
# for filter data to obvious distribution distance between wifi play time and cellular play time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import sys
from matplotlib.font_manager import FontProperties
# 数据
font_size = 38
font_properties = FontProperties(family='Times New Roman', weight='normal', size=font_size)
mpl.rcParams['font.family'] = 'Times New Roman'
if __name__ == "__main__":
    mode = int(sys.argv[1])
    # font = 25
    # labefont = 24
    font = 34
    lasize = 40
    linewides = 2
    red_rgb = (1, 0.2118, 0.1569)
    blue_rgb = (0.09, 0.47, 0.72)
    linestyles = ['-', '--', '-.', ':']
    if mode == 1:
        a = [0.825, 0.825, 0.9, 0.9, 0.9125, 0.9125, 0.95, 0.95, 0.9625, 0.9625, 0.975, 0.975, 0.975, 0.975, 0.975,
             0.975, 0.9875, 0.9875, 0.9875, 0.9875]
        b = [0.88, 0.9, 0.91, 0.91, 0.92, 0.93, 0.93, 0.93, 0.95, 0.97, 0.97, 0.98, 1, 1, 1, 1, 1, 1, 1, 1]
        c = [0.6375, 0.65, 0.675, 0.6875, 0.7, 0.7, 0.7125, 0.7125, 0.7125, 0.725, 0.7375, 0.7375, 0.7375, 0.775, 0.775,
             0.7875, 0.7875, 0.8125, 0.8125, 0.8375]
        d = [0.608333333, 0.616666667, 0.666666667, 0.75, 0.733333333, 0.583333333, 0.633333333, 0.666666667,
             0.708333333, 0.741666667, 0.741666667, 0.7, 0.75, 0.741666667, 0.758333333, 0.658333333, 0.741666667, 0.7,
             0.791666667, 0.8]

        a = sorted(a, reverse=False)
        b = sorted(b, reverse=False)
        c = sorted(c, reverse=False)
        d = sorted(d, reverse=False)

        a = np.array(a) * 100
        b = np.array(b) * 100
        c = np.array(c) * 100
        d = np.array(d) * 100
        plt.rcParams['font.family'] = 'Times New Roman'
        # 创建图形
        # plt.figure(figsize=(7, 4.81))  # (7, 5)
        plt.figure(figsize=(5, 6))  # (7, 5)
        position = np.linspace(0, 1, 20)
        # position[19] = 1
        print(position)
        # 绘制每一条数据线
        # print(d[:,0])
        # pp = [87.96,88.01,90.07,90.64,91.10,92.03,92.37,95.12,95.90,97.01,98,98.76,99.63,99.63,99.63]
        for i in range(len(d)):
            plt.plot([d[i], max(a[i], b[i], c[i])], [position[i], position[i]], color='black', linestyle='--',
                     linewidth=1)
        marsize = 10

        plt.plot(a, position, 'o', color=[175 / 255, 72 / 255, 20 / 255], linewidth=2,
                 markersize=marsize, label='OhmScan-16')
        plt.plot(b, position, 'v', color=[175 / 255, 72 / 255, 20 / 255], linewidth=1.5,
                 markersize=marsize, label='OhmScan-12')
        plt.plot(d, position, '-*', color=[99 / 255, 99 / 255, 102 / 255], linewidth=2,
                 markersize=marsize, label='Keystub-12')
        plt.plot(c, position, 's', color=[50 / 255, 113 / 255, 182 / 255], linewidth=1.5,
                 markersize=marsize, label='Keystub-8')

        plt.subplots_adjust(left=0.01, right=0.983, top=0.993, bottom=0.214)

        # plt.subplots_adjust(left=0.17, right=0.99, top=0.993, bottom=0.214)
        plt.xlabel('Detect accuracy (%)', fontproperties=font_properties, color='black', size=font_size + 3)
        plt.ylabel('CDF', fontproperties=font_properties, color='black')
        legend_properties = FontProperties(family='Times New Roman', weight='normal', size=27)
        plt.legend(prop=legend_properties, frameon=False, handlelength=0.7, ncol=1, loc=(-0.01, 0.653),
                   labelspacing=0.1, handletextpad=0.1, columnspacing=0.4, borderpad=0.1)
        plt.ylim(0, 1)
        plt.xlim(53, 101)
        # 添加标签和图例
        ax = plt.gca()
        ax.xaxis.set_major_locator(MultipleLocator(10))
        ax.xaxis.set_minor_locator(MultipleLocator(1))
        ax.yaxis.set_major_locator(MultipleLocator(0.2))
        ax.yaxis.set_minor_locator(MultipleLocator(0.04))

        ax.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='-', linewidth=1, alpha=0.6)
        ax.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)

        plt.tick_params(axis='both', which='major', labelsize=font_size)

        plt.grid(True)
        plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1], ['0 ', '0.2', '0.4', '0.6', '0.8', ' '])
        plt.xticks([60, 70, 80, 90, 100], ['60', '70', '80', '90', '100   '])

        ax.spines['top'].set_linewidth(2)  # 上边框
        ax.spines['right'].set_linewidth(2)  # 右边框
        ax.spines['bottom'].set_linewidth(2)  # 下边框
        ax.spines['left'].set_linewidth(2)  # 左边框
        ax.xaxis.set_label_coords(0.5, -0.14)
        ax.yaxis.set_label_coords(-0.127, 0.5)

        ax.text(51, 0.91, '1', fontsize=font_size, ha='right', fontname="Times New Roman")  # 标注坐标

        plt.savefig('revistApp_fig19_c.pdf', format='pdf')
        # 显示图形
        plt.show()
    elif mode == 2:
        a = [0.93,0.95,0.97,0.97,0.98,0.93,0.95,0.98,0.97,0.98,0.97,0.98,1,1,1,1,1,1,1,1]
        b = [0.98,	0.98,	0.97,	0.97,	0.98,	0.95,	0.95,	0.98,	0.97,	0.98,	0.97,	1,	1,	1,	1,	1,	1,	1,	1,	1]
        c = [0.76,	0.8,	0.83,	0.84,	0.86,	0.9,	0.9,	0.91,	0.93,	0.93,	0.94,	0.94,	0.94,	0.94,	0.96,	0.96,	0.96,	0.97,	0.98,	0.98]
        d = [0.73,	0.75,	0.8,	0.82,	0.84,	0.86,	0.88,	0.88,	0.89,	0.9,	0.9,	0.92,	0.92,	0.92,	0.93	,0.93,	0.95,	0.95,	0.97,	0.97]

        a = sorted(a, reverse=False)
        b = sorted(b, reverse=False)
        c = sorted(c, reverse=False)
        d = sorted(d, reverse=False)

        a = np.array(a) * 100
        b = np.array(b) * 100
        c = np.array(c) * 100
        d = np.array(d) * 100
        plt.rcParams['font.family'] = 'Times New Roman'
        # 创建图形
        plt.figure(figsize=(6, 6))  # (7, 5)
        position = np.linspace(0, 1, 20)
        # position[19] = 1
        print(position)
        # 绘制每一条数据线
        # print(d[:,0])
        # pp = [87.96,88.01,90.07,90.64,91.10,92.03,92.37,95.12,95.90,97.01,98,98.76,99.63,99.63,99.63]
        for i in range(len(d)):
            plt.plot([d[i], max(a[i], b[i], c[i])], [position[i], position[i]], color='black', linestyle='--',
                     linewidth=1)
        marsize = 10

        plt.plot(a, position, 'o', color=[175 / 255, 72 / 255, 20 / 255], linewidth=2,
                 markersize=marsize, label='OhmScan-16')
        plt.plot(b, position, 'v', color=[175 / 255, 72 / 255, 20 / 255], linewidth=1.5,
                 markersize=marsize, label='OhmScan-12')
        plt.plot(d, position, '-*', color=[99 / 255, 99 / 255, 102 / 255], linewidth=2,
                 markersize=marsize, label='Keystub-12')
        plt.plot(c, position, 's', color=[50 / 255, 113 / 255, 182 / 255], linewidth=1.5,
                 markersize=marsize, label='Keystub-8')

        # plt.subplots_adjust(left=0.17, right=0.99, top=0.993, bottom=0.214)

        plt.subplots_adjust(left=0.21, right=0.983, top=0.993, bottom=0.214)
        plt.xlabel('Detect accuracy (%)', fontproperties=font_properties, color='black', size=font_size + 3)
        plt.ylabel('CDF across positions', fontproperties=font_properties, color='black')
        legend_properties = FontProperties(family='Times New Roman', weight='normal', size=27)
        plt.legend(prop=legend_properties, frameon=False, handlelength=0.7, ncol=1, loc=(0, 0.64),
                   labelspacing=0.2, handletextpad=0.2, columnspacing=0.4, borderpad=0.1)
        plt.ylim(0, 1)
        plt.xlim(53, 101)
        # 添加标签和图例
        ax = plt.gca()
        ax.xaxis.set_major_locator(MultipleLocator(10))
        ax.xaxis.set_minor_locator(MultipleLocator(1))
        ax.yaxis.set_major_locator(MultipleLocator(0.2))
        ax.yaxis.set_minor_locator(MultipleLocator(0.04))

        ax.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='-', linewidth=1, alpha=0.6)
        ax.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)

        plt.tick_params(axis='both', which='major', labelsize=font_size)

        plt.grid(True)
        plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1], ['0 ', '0.2', '0.4', '0.6', '0.8', ''])
        plt.xticks([60, 70, 80, 90, 100], ['60', '70', '80', '90', '100   '])

        ax.spines['top'].set_linewidth(2)  # 上边框
        ax.spines['right'].set_linewidth(2)  # 右边框
        ax.spines['bottom'].set_linewidth(2)  # 下边框
        ax.spines['left'].set_linewidth(2)  # 左边框
        ax.xaxis.set_label_coords(0.5, -0.14)
        ax.yaxis.set_label_coords(-0.165, 0.5)

        ax.text(51, 0.91, '1', fontsize=font_size, ha='right', fontname="Times New Roman")  # 标注坐标

        plt.savefig('revistApp_fig19_b.pdf', format='pdf')
        # 显示图形
        plt.show()
    elif mode == 3:##扁长
        a = [0.825, 0.825, 0.9, 0.9, 0.9125, 0.9125, 0.95, 0.95, 0.9625, 0.9625, 0.975, 0.975, 0.975, 0.975, 0.975,
             0.975, 0.9875, 0.9875, 0.9875, 0.9875]
        b = [0.88, 0.9, 0.91, 0.91, 0.92, 0.93, 0.93, 0.93, 0.95, 0.97, 0.97, 0.98, 1, 1, 1, 1, 1, 1, 1, 1]
        c = [0.6375, 0.65, 0.675, 0.6875, 0.7, 0.7, 0.7125, 0.7125, 0.7125, 0.725, 0.7375, 0.7375, 0.7375, 0.775, 0.775,
             0.7875, 0.7875, 0.8125, 0.8125, 0.8375]
        d = [0.608333333, 0.616666667, 0.666666667, 0.75, 0.733333333, 0.583333333, 0.633333333, 0.666666667,
             0.708333333, 0.741666667, 0.741666667, 0.7, 0.75, 0.741666667, 0.758333333, 0.658333333, 0.741666667, 0.7,
             0.791666667, 0.8]

        a = sorted(a, reverse=False)
        b = sorted(b, reverse=False)
        c = sorted(c, reverse=False)
        d = sorted(d, reverse=False)

        a = np.array(a) * 100
        b = np.array(b) * 100
        c = np.array(c) * 100
        d = np.array(d) * 100
        plt.rcParams['font.family'] = 'Times New Roman'
        # 创建图形
        # plt.figure(figsize=(7, 4.81))  # (7, 5)
        plt.figure(figsize=(5.8, 5))  # (7, 5)
        position = np.linspace(0, 1, 20)
        # position[19] = 1
        print(position)
        # 绘制每一条数据线
        for i in range(len(d)):
            plt.plot([d[i], max(a[i], b[i], c[i])], [position[i], position[i]], color='black', linestyle='--',
                     linewidth=1)
        # 添加最后一个点的水平线max(a[i,0],b[i,0],c[i,0])]
        marsize = 10

        plt.plot(a, position, 'o', color=[175 / 255, 72 / 255, 20 / 255], linewidth=2,
                 markersize=marsize, label='OhmScan-16')
        plt.plot(b, position, 'v', color=[175 / 255, 72 / 255, 20 / 255], linewidth=1.5,
                 markersize=marsize, label='OhmScan-12')
        plt.plot(d, position, '-*', color=[99 / 255, 99 / 255, 102 / 255], linewidth=2,
                 markersize=marsize, label='Keystub-12')
        plt.plot(c, position, 's', color=[50 / 255, 113 / 255, 182 / 255], linewidth=1.5,
                 markersize=marsize, label='Keystub-8')

        plt.subplots_adjust(left=0.03, right=0.976, top=0.993, bottom=0.214)

        plt.xlabel('Detect accuracy (%)', fontproperties=font_properties, color='black', size=font_size + 3)
        plt.ylabel('CDF', fontproperties=font_properties, color='black')
        legend_properties = FontProperties(family='Times New Roman', weight='normal', size=27)
        plt.legend(prop=legend_properties, frameon=False, handlelength=0.7, ncol=1, loc=(0, 0.55),
                   labelspacing=0.1, handletextpad=0.1, columnspacing=0.4, borderpad=0.1)
        plt.ylim(0, 1)
        plt.xlim(50, 101)
        # 添加标签和图例
        ax = plt.gca()
        ax.xaxis.set_major_locator(MultipleLocator(10))
        ax.xaxis.set_minor_locator(MultipleLocator(1))
        ax.yaxis.set_major_locator(MultipleLocator(0.2))
        ax.yaxis.set_minor_locator(MultipleLocator(0.04))

        ax.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='-', linewidth=1, alpha=0.6)
        ax.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)

        plt.tick_params(axis='both', which='major', labelsize=font_size)

        plt.grid(True)
        plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1], [' ', '', '', '', '', ' '])
        plt.xticks([50,60, 70, 80, 90, 100], [' 50','60', '70', '80', '90', '100  '])

        ax.spines['top'].set_linewidth(2)  # 上边框
        ax.spines['right'].set_linewidth(2)  # 右边框
        ax.spines['bottom'].set_linewidth(2)  # 下边框
        ax.spines['left'].set_linewidth(2)  # 左边框
        ax.xaxis.set_label_coords(0.5, -0.14)
        ax.yaxis.set_label_coords(-0.127, 0.5)

        # ax.text(51, 0.91, '1', fontsize=font_size, ha='right', fontname="Times New Roman")  # 标注坐标

        plt.savefig('revistApp_fig19_c.pdf', format='pdf')
        # 显示图形
        plt.show()
    elif mode == 4:
        a = [0.93,0.95,0.97,0.97,0.98,0.93,0.95,0.98,0.97,0.98,0.97,0.98,1,1,1,1,1,1,1,1]
        b = [0.98,	0.98,	0.97,	0.97,	0.98,	0.95,	0.95,	0.98,	0.97,	0.98,	0.97,	1,	1,	1,	1,	1,	1,	1,	1,	1]
        c = [0.76,	0.8,	0.83,	0.84,	0.86,	0.9,	0.9,	0.91,	0.93,	0.93,	0.94,	0.94,	0.94,	0.94,	0.96,	0.96,	0.96,	0.97,	0.98,	0.98]
        d = [0.73,	0.75,	0.8,	0.82,	0.84,	0.86,	0.88,	0.88,	0.89,	0.9,	0.9,	0.92,	0.92,	0.92,	0.93	,0.93,	0.95,	0.95,	0.97,	0.97]

        a = sorted(a, reverse=False)
        b = sorted(b, reverse=False)
        c = sorted(c, reverse=False)
        d = sorted(d, reverse=False)

        a = np.array(a) * 100
        b = np.array(b) * 100
        c = np.array(c) * 100
        d = np.array(d) * 100
        plt.rcParams['font.family'] = 'Times New Roman'
        # 创建图形
        plt.figure(figsize=(7, 5))  # (7, 5)
        position = np.linspace(0, 1, 20)
        # position[19] = 1
        print(position)
        # 绘制每一条数据线
        for i in range(len(d)):
            plt.plot([d[i], max(a[i], b[i], c[i])], [position[i], position[i]], color='black', linestyle='--',
                     linewidth=1)
        # 添加最后一个点的水平线max(a[i,0],b[i,0],c[i,0])]
        marsize = 10

        plt.plot(a, position, 'o', color=[175 / 255, 72 / 255, 20 / 255], linewidth=2,
                 markersize=marsize, label='OhmScan-16')
        plt.plot(b, position, 'v', color=[175 / 255, 72 / 255, 20 / 255], linewidth=1.5,
                 markersize=marsize, label='OhmScan-12')
        plt.plot(d, position, '-*', color=[99 / 255, 99 / 255, 102 / 255], linewidth=2,
                 markersize=marsize, label='Keystub-12')
        plt.plot(c, position, 's', color=[50 / 255, 113 / 255, 182 / 255], linewidth=1.5,
                 markersize=marsize, label='Keystub-8')

        plt.subplots_adjust(left=0.21, right=0.983, top=0.993, bottom=0.214)
        plt.xlabel('Detect accuracy (%)', fontproperties=font_properties, color='black', size=font_size + 3)
        plt.ylabel('CDF across positions', fontproperties=font_properties, color='black')
        legend_properties = FontProperties(family='Times New Roman', weight='normal', size=27)
        plt.legend(prop=legend_properties, frameon=False, handlelength=0.7, ncol=1, loc=(0, 0.55),
                   labelspacing=0.2, handletextpad=0.2, columnspacing=0.4, borderpad=0.1)
        plt.ylim(0, 1)
        plt.xlim(50, 101)
        # 添加标签和图例
        ax = plt.gca()
        ax.xaxis.set_major_locator(MultipleLocator(10))
        ax.xaxis.set_minor_locator(MultipleLocator(1))
        ax.yaxis.set_major_locator(MultipleLocator(0.2))
        ax.yaxis.set_minor_locator(MultipleLocator(0.04))

        ax.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='-', linewidth=1, alpha=0.6)
        ax.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)

        plt.tick_params(axis='both', which='major', labelsize=font_size)

        plt.grid(True)
        plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1], ['0 ', '0.2', '0.4', '0.6', '0.8', ''])
        plt.xticks([50,60, 70, 80, 90, 100], [' 50','60', '70', '80', '90', '100   '])

        ax.spines['top'].set_linewidth(2)  # 上边框
        ax.spines['right'].set_linewidth(2)  # 右边框
        ax.spines['bottom'].set_linewidth(2)  # 下边框
        ax.spines['left'].set_linewidth(2)  # 左边框
        ax.xaxis.set_label_coords(0.5, -0.14)
        ax.yaxis.set_label_coords(-0.177, 0.43)

        ax.text(48, 0.91, '1', fontsize=font_size, ha='right', fontname="Times New Roman")  # 标注坐标

        plt.savefig('revistApp_fig19_b.pdf', format='pdf')
        # 显示图形
        plt.show()
    