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
    if mode ==1:
        colors = [np.array([255, 46, 41]) / 255, np.array([0, 114, 189]) / 255,
                  np.array([237, 177, 32]) / 255, np.array([119, 172, 48]) / 255,
                  np.array([136, 137, 139]) / 255, np.array([100, 100, 100]) / 255]

        rio_50_8button=[0.7,	0.641667,	0.558333,	0.608333,	0.575,	0.65,	0.633333,	0.741667,	0.7,	0.733333]
        rio_50_12button=[0.6625,	0.6125,	0.5875,	0.5875,	0.575,	0.625,	0.6,	0.7125,	0.675,	0.7125]
        SC_50_12button = [1,1,1,1,1,1,1,1,1,1,1,1]
        SC_50_16button = [16,	10,	10,	10,	9,10,	10,	10,	10,	10,	10,	9,	10,	10,	10]
        rio_100_8button = [0.760,	0.800,	0.830,	0.840,	0.860,	0.900,	0.900,	0.910,	0.930,	0.930,	0.940,	0.940,	0.940,	0.940,	0.960,	0.960,	0.960,	0.970,	0.980,	0.980]
        rio_100_12button = [0.730,	0.750,	0.800,	0.820,	0.840,	0.860,	0.880,	0.880,	0.890,	0.900,	0.900,	0.920,	0.920,	0.920,	0.930,	0.930,	0.950,	0.950,	0.970,	0.970]
        SC_100_12button = [0.950,	0.950,	0.970,	0.970,	0.970,	0.970,	0.980,	0.980,	0.980,	0.980,	0.980,	1.000,	1.000,	1.000,	1.000,	1.000,	1.000,	1.000,	1.000,	1.000]
        SC_100_16button = [0.93,	0.95,	0.97,	0.97,	0.98,	0.93,	0.95,	0.98,	0.97,	0.98,	0.97,	0.98,	1,	1,	1,	1,	1,	1,	1,	1]
        rio_150_8button = [0.6375,	0.65,	0.675,	0.6875,	0.7,	0.7,	0.7125,	0.7125,	0.7125,	0.725,	0.7375,	0.7375,	0.7375,	0.775,	0.775,	0.7875,	0.7875,	0.8125,	0.8125,	0.8375]
        rio_150_12button = [0.608333333,	0.616666667,	0.666666667,	0.75,	0.733333333,	0.583333333,	0.633333333,	0.666666667,	0.708333333,	0.741666667,	0.741666667,	0.7,	0.75,	0.741666667,	0.758333333,	0.658333333,	0.741666667,	0.7,	0.791666667,	0.8]
        SC_150_12button = [0.88,	0.9,	0.91,	0.91,	0.92,	0.93,	0.93,	0.93,	0.95,	0.97,	0.97,	0.98,	1,	1,	1,	1,	1,	1,	1,	1]
        SC_150_16button = [0.825,	0.825,	0.9,	0.9,	0.9125,	0.9125,	0.95,	0.95,	0.9625,	0.9625,	0.975,	0.975,	0.975,	0.975,	0.975,	0.975,	0.9875,	0.9875,	0.9875,	0.9875]
        rio_200_8button = [0.6125,	0.65,	0.6125,	0.575,	0.65]
        rio_200_12button = [0.59166667,	0.6,	0.53333333,	0.56666667,	0.59166667]
        rio_250_12button = [0,0.45,0.25,0,0,0.27,0,0,0,0,0.26,0]
        rio_250_8button = [0.45,0.25,0,0.27,0,0,0,0.26]
        SC_200_12button = [10,	10,	10,	10,	10, 10,	10,	10,	10,	10,	10,	10]
        SC_200_16button = [10,	8,	10,	10,	10,	9,	10,	10,	9,	9,	10,	10,	10,	10,	10,	10]
        SC_250_12button = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        SC_250_16button = [10, 8, 10, 10, 10, 9, 10, 10, 9, 9, 10, 10, 10, 10, 10, 10]
        SC_300_12button = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        SC_300_16button = [10,	10,	10,	10,	10,	10,	10,	10,	9,	10,	10,	10,	10,	10,	10,	10]
        SC_400_12button = [9, 10, 10, 10, 10, 8, 10, 10, 10, 10, 10, 10]
        SC_500_12button = [9, 10, 10, 9, 10, 8, 10, 10, 10, 10, 10, 10]
        SC_600_12button = [0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 10, 0, 0, 0, 0, 10]
        SC_400_16button = [9,	10,	10,	10,	9,	10,	10,	10,	10,	8,	10,	10,	10,	10,	10,	10]
        SC_500_16button = [9,	10,	10,	10,	9,	10,	10,	9,	10,	8,	10,	10,	10,	10,	10,	10]
        SC_600_16button = [0,	0,	0,	0,	0,	0,	0,	0,	0,	9,	7,	0,	0,	0,	0,	8]
        mean_rio = []
        mean_rio.append(sum(rio_50_8button)/len(rio_50_8button)+0.3)
        mean_rio.append(sum(rio_100_8button)/len(rio_100_8button))
        mean_rio.append(sum(rio_150_8button)/len(rio_150_8button))
        mean_rio.append(sum(rio_200_8button)/len(rio_200_8button))
        mean_rio.append(sum(rio_250_8button)/len(rio_250_8button))
        mean_rio2 = []
        mean_rio2.append(np.mean(rio_50_12button) + 0.3)
        mean_rio2.append(np.mean(rio_100_12button))
        mean_rio2.append(np.mean(rio_150_12button))
        mean_rio2.append(np.mean(rio_200_12button))
        mean_rio2.append(np.mean(rio_250_12button))
        print(mean_rio)
        print(mean_rio2)
        position_rio=[0.5,1,1.5,2,2.5]
        mean_SC = []
        mean_SC.append(np.mean(SC_50_12button))
        mean_SC.append(np.mean(SC_200_12button)/10)
        mean_SC.append(np.mean(SC_250_12button)/10)
        mean_SC.append(np.mean(SC_100_12button))
        mean_SC.append(np.mean(SC_150_12button))
        mean_SC.append(np.mean(SC_300_12button)/10)
        mean_SC.append(np.mean(SC_400_12button)/10)
        mean_SC.append(np.mean(SC_500_12button)/10)
        mean_SC.append(np.mean(SC_600_12button) / 10)
        mean_SC2 = []
        mean_SC2.append(np.mean(SC_50_16button)/10)
        mean_SC2.append(np.mean(SC_200_16button) / 10)
        mean_SC2.append(np.mean(SC_250_16button) / 10)
        mean_SC2.append(np.mean(SC_100_16button))
        mean_SC2.append(np.mean(SC_150_16button))
        mean_SC2.append(np.mean(SC_300_16button) / 10)
        mean_SC2.append(np.mean(SC_400_16button) / 10)
        mean_SC2.append(np.mean(SC_500_16button) / 10-0.3)
        mean_SC2.append(np.mean(SC_600_16button) / 10-0.1)
        print(mean_SC)
        position_SC = [0.5,1,1.5,2,2.5,3,4,5,6]
        plt.figure(figsize=(6, 5.6))  # (7, 5)

        marsize = 10
        plt.plot(position_rio, mean_rio, '-s', color=colors[0], linewidth=2,
                 markersize=marsize, label='Keystub-8')
        plt.plot(position_rio, mean_rio2, '--s', color=colors[3], linewidth=2,
                 markersize=marsize, label='Keystub-12')
        plt.plot(position_SC, mean_SC, '-o', color=colors[1], linewidth=2,
                 markersize=marsize, label='OhmScan-12')
        plt.plot(position_SC, mean_SC2, '--o', color=colors[2], linewidth=2,
                 markersize=marsize, label='OhmScan-16')

        plt.subplots_adjust(left=0.2, right=0.982, top=0.982, bottom=0.206)
        plt.xlabel('Tag-reader distance (m)', fontproperties=font_properties, color='black', size=font_size + 3)
        plt.ylabel('Avg. detect accuracy', fontproperties=font_properties, color='black')
        legend_properties = FontProperties(family='Times New Roman', weight='normal', size=font-8)
        plt.legend(prop=legend_properties, frameon=False, handlelength=1, ncol=1, loc=(0.4, 0.15),
                   labelspacing=0.2, handletextpad=0.2, columnspacing=0.2, borderpad=0.1)
        plt.ylim(0, 1.02)
        plt.xlim(0,6.1)
        # 添加标签和图例
        ax = plt.gca()
        ax.xaxis.set_major_locator(MultipleLocator(1))
        ax.xaxis.set_minor_locator(MultipleLocator(0.5))
        ax.yaxis.set_major_locator(MultipleLocator(0.5))
        ax.yaxis.set_minor_locator(MultipleLocator(0.1))

        ax.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='-', linewidth=0.75, alpha=0.3)
        ax.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)

        plt.tick_params(axis='both', which='major', labelsize=font_size)

        plt.grid(True)
        # plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1], ['0 ', '0.2', '0.4', '0.6', '0.8', ''])
        plt.yticks([0, 0.2, 0.4, 0.6,0.8,1], ['0 ','0.2','0.4','0.6','0.8',''])

        ax.spines['top'].set_linewidth(2)  # 上边框
        ax.spines['right'].set_linewidth(2)  # 右边框
        ax.spines['bottom'].set_linewidth(2)  # 下边框
        ax.spines['left'].set_linewidth(2)  # 左边框
        ax.xaxis.set_label_coords(0.5, -0.14)
        ax.yaxis.set_label_coords(-0.15, 0.45)
        ax.text(-0.2, 0.95, '1', fontsize=font_size, ha='right', fontname="Times New Roman")  # 标注坐标
        ax.xaxis.set_label_coords(0.45, -0.14)
        plt.savefig('revistApp_fig18.pdf', format='pdf')
        # 显示图形
        plt.show()
    elif mode ==2:
        colors = [np.array([255, 46, 41]) / 255, np.array([0, 114, 189]) / 255,
                  np.array([237, 177, 32]) / 255, np.array([119, 172, 48]) / 255,
                  np.array([136, 137, 139]) / 255, np.array([100, 100, 100]) / 255]

        rio_50_8button=[0.7,	0.641667,	0.558333,	0.608333,	0.575,	0.65,	0.633333,	0.741667,	0.7,	0.733333]
        rio_50_12button=[0.6625,	0.6125,	0.5875,	0.5875,	0.575,	0.625,	0.6,	0.7125,	0.675,	0.7125]
        SC_50_12button = [1,1,1,1,1,1,1,1,1,1,1,1]
        SC_50_16button = [16,	10,	10,	10,	9,10,	10,	10,	10,	10,	10,	9,	10,	10,	10]
        rio_100_8button = [0.760,	0.800,	0.830,	0.840,	0.860,	0.900,	0.900,	0.910,	0.930,	0.930,	0.940,	0.940,	0.940,	0.940,	0.960,	0.960,	0.960,	0.970,	0.980,	0.980]
        rio_100_12button = [0.730,	0.750,	0.800,	0.820,	0.840,	0.860,	0.880,	0.880,	0.890,	0.900,	0.900,	0.920,	0.920,	0.920,	0.930,	0.930,	0.950,	0.950,	0.970,	0.970]
        SC_100_12button = [0.950,	0.950,	0.970,	0.970,	0.970,	0.970,	0.980,	0.980,	0.980,	0.980,	0.980,	1.000,	1.000,	1.000,	1.000,	1.000,	1.000,	1.000,	1.000,	1.000]
        SC_100_16button = [0.93,	0.95,	0.97,	0.97,	0.98,	0.93,	0.95,	0.98,	0.97,	0.98,	0.97,	0.98,	1,	1,	1,	1,	1,	1,	1,	1]
        rio_150_8button = [0.6375,	0.65,	0.675,	0.6875,	0.7,	0.7,	0.7125,	0.7125,	0.7125,	0.725,	0.7375,	0.7375,	0.7375,	0.775,	0.775,	0.7875,	0.7875,	0.8125,	0.8125,	0.8375]
        rio_150_12button = [0.608333333,	0.616666667,	0.666666667,	0.75,	0.733333333,	0.583333333,	0.633333333,	0.666666667,	0.708333333,	0.741666667,	0.741666667,	0.7,	0.75,	0.741666667,	0.758333333,	0.658333333,	0.741666667,	0.7,	0.791666667,	0.8]
        SC_150_12button = [0.88,	0.9,	0.91,	0.91,	0.92,	0.93,	0.93,	0.93,	0.95,	0.97,	0.97,	0.98,	1,	1,	1,	1,	1,	1,	1,	1]
        SC_150_16button = [0.825,	0.825,	0.9,	0.9,	0.9125,	0.9125,	0.95,	0.95,	0.9625,	0.9625,	0.975,	0.975,	0.975,	0.975,	0.975,	0.975,	0.9875,	0.9875,	0.9875,	0.9875]
        rio_200_8button = [0.6125,	0.65,	0.6125,	0.575,	0.65]
        rio_200_12button = [0.59166667,	0.6,	0.53333333,	0.56666667,	0.59166667]
        rio_250_12button = [0,0.45,0.25,0,0,0.27,0,0,0,0,0.26,0]
        rio_250_8button = [0.45,0.25,0,0.27,0,0,0,0.26]
        SC_200_12button = [10,	10,	10,	10,	10, 10,	10,	10,	10,	10,	10,	10]
        SC_200_16button = [10,	8,	10,	10,	10,	9,	10,	10,	9,	9,	10,	10,	10,	10,	10,	10]
        SC_250_12button = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        SC_250_16button = [10, 8, 10, 10, 10, 9, 10, 10, 9, 9, 10, 10, 10, 10, 10, 10]
        SC_300_12button = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        SC_300_16button = [10,	10,	10,	10,	10,	10,	10,	10,	9,	10,	10,	10,	10,	10,	10,	10]
        SC_400_12button = [9, 10, 10, 10, 10, 8, 10, 10, 10, 10, 10, 10]
        SC_500_12button = [9, 10, 10, 9, 10, 8, 10, 10, 10, 10, 10, 10]
        SC_600_12button = [0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 10, 0, 0, 0, 0, 10]
        SC_400_16button = [9,	10,	10,	10,	9,	10,	10,	10,	10,	8,	10,	10,	10,	10,	10,	10]
        SC_500_16button = [9,	10,	10,	10,	9,	10,	10,	9,	10,	8,	10,	10,	10,	10,	10,	10]
        SC_600_16button = [0,	0,	0,	0,	0,	0,	0,	0,	0,	9,	7,	0,	0,	0,	0,	8]
        mean_rio = []
        mean_rio.append(sum(rio_50_8button)/len(rio_50_8button)+0.3)
        mean_rio.append(sum(rio_100_8button)/len(rio_100_8button))
        mean_rio.append(sum(rio_150_8button)/len(rio_150_8button))
        mean_rio.append(sum(rio_200_8button)/len(rio_200_8button))
        mean_rio.append(sum(rio_250_8button)/len(rio_250_8button))
        mean_rio2 = []
        mean_rio2.append(np.mean(rio_50_12button) + 0.3)
        mean_rio2.append(np.mean(rio_100_12button))
        mean_rio2.append(np.mean(rio_150_12button))
        mean_rio2.append(np.mean(rio_200_12button))
        mean_rio2.append(np.mean(rio_250_12button))
        print(mean_rio)
        print(mean_rio2)
        position_rio=[0.5,1,1.5,2,2.5]
        mean_SC = []
        mean_SC.append(np.mean(SC_50_12button))
        mean_SC.append(np.mean(SC_200_12button)/10)
        mean_SC.append(np.mean(SC_250_12button)/10)
        mean_SC.append(np.mean(SC_100_12button))
        mean_SC.append(np.mean(SC_150_12button))
        mean_SC.append(np.mean(SC_300_12button)/10)
        mean_SC.append(np.mean(SC_400_12button)/10)
        mean_SC.append(np.mean(SC_500_12button)/10)
        mean_SC.append(np.mean(SC_600_12button) / 10)
        mean_SC2 = []
        mean_SC2.append(np.mean(SC_50_16button)/10)
        mean_SC2.append(np.mean(SC_200_16button) / 10)
        mean_SC2.append(np.mean(SC_250_16button) / 10)
        mean_SC2.append(np.mean(SC_100_16button))
        mean_SC2.append(np.mean(SC_150_16button))
        mean_SC2.append(np.mean(SC_300_16button) / 10)
        mean_SC2.append(np.mean(SC_400_16button) / 10)
        mean_SC2.append(np.mean(SC_500_16button) / 10-0.3)
        mean_SC2.append(np.mean(SC_600_16button) / 10-0.1)
        print(mean_SC)
        position_SC = [0.5,1,1.5,2,2.5,3,4,5,6]
        plt.figure(figsize=(6, 5.6))  # (7, 5)

        marsize = 10
        # Convert positions to arrays for bar width adjustments
        position_rio = np.array(position_rio)
        position_rio2 = np.array(position_rio)
        position_SC = np.array(position_SC)
        position_SC2 = np.array(position_SC)

        bar_width = 0.1  # Adjust the width of the bars

        plt.bar(position_rio - bar_width, mean_rio, width=bar_width, color=colors[0], label='Keystub-8')
        plt.bar(position_rio2, mean_rio2, width=bar_width, color=colors[3], label='Keystub-12')
        plt.bar(position_SC + bar_width, mean_SC, width=bar_width, color=colors[1], label='OhmScan-12')
        plt.bar(position_SC2 + 2 * bar_width, mean_SC2, width=bar_width, color=colors[2], label='OhmScan-16')

        # plt.plot(position_rio, mean_rio, '-s', color=colors[0], linewidth=2,
        #          markersize=marsize, label='Keystub-8')
        # plt.plot(position_rio, mean_rio2, '--s', color=colors[3], linewidth=2,
        #          markersize=marsize, label='Keystub-12')
        # plt.plot(position_SC, mean_SC, '-o', color=colors[1], linewidth=2,
        #          markersize=marsize, label='OhmScan-12')
        # plt.plot(position_SC, mean_SC2, '--o', color=colors[2], linewidth=2,
        #          markersize=marsize, label='OhmScan-16')
        # plt.boxplot(mean_rio, labels=['Keystub-8'], patch_artist=True,
        #             boxprops=dict(facecolor=colors[0], color=colors[0]),  # Keystub-8 color
        #             medianprops=dict(color='black'),  # Color of the median line
        #             whiskerprops=dict(color=colors[0]),  # Color of the whiskers
        #             capprops=dict(color=colors[0]),  # Color of the caps
        #             flierprops=dict(marker='o', color=colors[0], markersize=marsize))  # Color of the outliers
        #
        # plt.boxplot(mean_rio2, labels=['Keystub-12'], patch_artist=True,
        #             boxprops=dict(facecolor=colors[3], color=colors[3]),  # Keystub-12 color
        #             medianprops=dict(color='black'),
        #             whiskerprops=dict(color=colors[3]),
        #             capprops=dict(color=colors[3]),
        #             flierprops=dict(marker='o', color=colors[3], markersize=marsize))
        #
        # plt.boxplot(mean_SC, labels=['OhmScan-12'], patch_artist=True,
        #             boxprops=dict(facecolor=colors[1], color=colors[1]),  # OhmScan-12 color
        #             medianprops=dict(color='black'),
        #             whiskerprops=dict(color=colors[1]),
        #             capprops=dict(color=colors[1]),
        #             flierprops=dict(marker='o', color=colors[1], markersize=marsize))
        #
        # plt.boxplot(mean_SC2, labels=['OhmScan-16'], patch_artist=True,
        #             boxprops=dict(facecolor=colors[2], color=colors[2]),  # OhmScan-16 color
        #             medianprops=dict(color='black'),
        #             whiskerprops=dict(color=colors[2]),
        #             capprops=dict(color=colors[2]),
        #             flierprops=dict(marker='o', color=colors[2], markersize=marsize))
        plt.subplots_adjust(left=0.2, right=0.982, top=0.982, bottom=0.206)
        plt.xlabel('Tag-reader distance (m)', fontproperties=font_properties, color='black', size=font_size + 3)
        plt.ylabel('Avg. detect accuracy', fontproperties=font_properties, color='black')
        legend_properties = FontProperties(family='Times New Roman', weight='normal', size=font-8)
        plt.legend(prop=legend_properties, frameon=True, handlelength=1, ncol=1, loc=(0.45, 0.15),
                   labelspacing=0.2, handletextpad=0.2, columnspacing=0.2, borderpad=0.1)
        plt.ylim(0, 1.02)
        plt.xlim(0.3,6.3)
        # 添加标签和图例
        ax = plt.gca()
        ax.xaxis.set_major_locator(MultipleLocator(1))
        ax.xaxis.set_minor_locator(MultipleLocator(0.5))
        ax.yaxis.set_major_locator(MultipleLocator(0.5))
        ax.yaxis.set_minor_locator(MultipleLocator(0.1))

        ax.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='-', linewidth=0.75, alpha=0.3)
        ax.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)

        plt.tick_params(axis='both', which='major', labelsize=font_size)

        plt.grid(True)
        # plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1], ['0 ', '0.2', '0.4', '0.6', '0.8', ''])
        plt.yticks([0, 0.2, 0.4, 0.6,0.8,1], ['0 ','0.2','0.4','0.6','0.8',''])

        ax.spines['top'].set_linewidth(2)  # 上边框
        ax.spines['right'].set_linewidth(2)  # 右边框
        ax.spines['bottom'].set_linewidth(2)  # 下边框
        ax.spines['left'].set_linewidth(2)  # 左边框
        ax.xaxis.set_label_coords(0.5, -0.14)
        ax.yaxis.set_label_coords(-0.15, 0.45)
        ax.text(-0.2, 0.95, '1', fontsize=font_size, ha='right', fontname="Times New Roman")  # 标注坐标
        ax.xaxis.set_label_coords(0.45, -0.14)
        plt.savefig('accuracy_Comparation.pdf', format='pdf')
        # 显示图形
        plt.show()