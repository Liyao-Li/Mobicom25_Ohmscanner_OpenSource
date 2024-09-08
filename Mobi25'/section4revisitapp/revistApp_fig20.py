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
    if mode ==1:
        # Adjusting paths, filenames, and font
        input_file = './data/button/readingRate/distance/'
        dista = [1,2,3,4,5]
        # distb = [0, 20, 40, 60, 90]  # X
        # distc = [-60, -40, -20, 20, 40]  # Y
        # distd = [0, 20, 40]  # Z
        all_phase5 = []

        # # Load data into all_phase5
        # for i in distb:
        #     phase5 = np.loadtxt(input_file + 'dis_0830/' + str(i) + '-RR.txt', unpack=True)
        #     all_phase5.append(phase5)

        for i in dista:
            phase5 = np.loadtxt(input_file + str(i) + '.txt', unpack=True)
            all_phase5.append(phase5)
        # print(all_phase5)
        all_phase5 = np.array(all_phase5)+8

        # 转置矩阵，使得横轴为距离，纵轴为按钮索引
        all_phase5 = all_phase5.T
        column_sums = np.sum(all_phase5, axis=0)/16+1
        g = sns.JointGrid(data=all_phase5, height=7, ratio=3)
        print(column_sums)
        # 绘制直方图在顶部
        bar_width = 0.5  # 控制柱形条的宽度
        # height_scaling = 0.8  # 控制柱形条的高度缩放比例
        g.ax_marg_x.bar(np.arange(0.5, len(column_sums)+0.5), column_sums, color=colors[1], width=bar_width)

        g.ax_marg_x.tick_params(axis='y', labelsize=10, labelcolor="black")
        # g.ax_marg_x.spines['left'].set_visible(True)  # 显示左侧的 spine，如果被隐藏了

        # 设置 y 轴标签并调整显示位置
        g.ax_marg_x.tick_params(labelsize=font-3, labelcolor="black", length=6, width=1, direction="in")
        g.ax_marg_x.text(-1.5,-1, ' Avg.rate', fontsize=font-6, color='black',rotation = 90)
        # g.ax_marg_x.text(-0.7, 14, '15 ', fontsize=font - 6, color='black')
        g.ax_marg_x.set_ylim([0, 22])
        g.ax_marg_x.set_yticks(np.arange(0, 21, 10))
        g.ax_marg_x.spines['left'].set_visible(True)  # 确保左侧脊柱可见
        g.ax_marg_x.yaxis.set_ticks_position('left')  # 在左侧显示刻度线
        g.ax_marg_x.tick_params(axis='y', which='both', length=6, width=1, color='black', direction='in',
                                labelsize=25, labelcolor='black')
        g.ax_marg_x.set_ylabel('Reading\nRates', fontsize=12, fontname="Times New Roman", color='black', labelpad=10)
        g.ax_marg_x.yaxis.set_label_coords(-0.15, 0.5)  # 手动调整 y 轴标签的位置

        # 显示直方图的 x 轴和 y 轴
        g.ax_marg_x.spines['left'].set_visible(True)
        g.ax_marg_x.spines['bottom'].set_visible(True)
        g.ax_marg_x.spines['left'].set_linewidth(2)
        g.ax_marg_x.spines['bottom'].set_linewidth(2)
        g.ax_marg_y.set_visible(False)  # 直接隐藏整个右边直方图

        # 绘制热力图在中心
        sns.heatmap(all_phase5, annot=False, cmap="GnBu", cbar=False, ax=g.ax_joint, vmin=0, vmax=20)
        g.ax_joint.set_xlabel('Distance (m)', fontsize=font, fontname="Times New Roman", color='black')
        g.ax_joint.set_ylabel('Button index', fontsize=font, fontname="Times New Roman")
        g.ax_joint.tick_params(axis='x',labelsize=font-2, labelcolor="black", length=6, width=1, direction="in")
        g.ax_joint.tick_params(axis='y',labelsize=font - 4, labelcolor="black", length=6, width=1, direction="in",rotation = 0,pad=5)

        # 调整 y 轴的刻度标签并旋转 90 度
        plt.subplots_adjust(hspace=0.05)  # 调整热力图和直方图之间的间距
        plt.subplots_adjust(left=0.163, right=0.85, top=0.967, bottom=0.162)
        g.ax_joint.set_xticks([0.5, 1.5, 2.5, 3.5, 4.5], ['1','2', '3', '4', '5'])
        g.ax_joint.set_yticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5,15.5],
                              ['', '2 ', '', '4 ', '', '6 ', '', '8 ', ' ', '10', '', '12','','14','','16'])
        for spine in g.ax_joint.spines.values():
            spine.set_visible(True)
            spine.set_linewidth(2)
        plt.savefig('./revistApp_fig20_a.pdf', format='pdf')
        plt.show()
    elif mode == 2:
        # Adjusting paths, filenames, and font
        input_file = './data/button/readingRate/X/'
        dista = [0, 20, 40, 60, 90]  # X
        all_phase5 = []

        # Load data into all_phase5
        for i in dista:
            phase5 = np.loadtxt(input_file + str(i) + '.txt', unpack=True)
            all_phase5.append(phase5)

        all_phase5 = np.array(all_phase5)+8
        print(all_phase5)
        # 转置矩阵，使得横轴为距离，纵轴为按钮索引
        all_phase5 = all_phase5.T
        column_sums = np.sum(all_phase5, axis=0)/16+1
        g = sns.JointGrid(data=all_phase5, height=7, ratio=3)

        # 绘制直方图在顶部
        bar_width = 0.5  # 控制柱形条的宽度
        # height_scaling = 0.8  # 控制柱形条的高度缩放比例
        g.ax_marg_x.bar(np.arange(0.5, len(column_sums) + 0.5), column_sums, color=colors[1],
                        width=bar_width)

        g.ax_marg_x.tick_params(axis='y', labelsize=10, labelcolor="black")

        # 设置 y 轴标签并调整显示位置
        g.ax_marg_x.set_ylabel('Reading\nRates', fontsize=12, fontname="Times New Roman", color='black', labelpad=10)
        g.ax_marg_x.yaxis.set_label_coords(-0.15, 0.5)  # 手动调整 y 轴标签的位置
        g.ax_marg_x.tick_params(labelsize=font - 3, labelcolor="black", length=6, width=1, direction="in")
        g.ax_marg_x.text(-1.5,0, ' Avg. Rate', fontsize=font - 6, color='black', rotation=90)
        # g.ax_marg_x.set_ylim([0, 22])
        # g.ax_marg_x.set_yticks(np.arange(0, 21, 10))
        # g.ax_marg_x.spines['left'].set_visible(True)  # 确保左侧脊柱可见

        # 显示直方图的 x 轴和 y 轴
        g.ax_marg_x.spines['left'].set_visible(True)
        g.ax_marg_x.spines['bottom'].set_visible(True)
        g.ax_marg_x.spines['left'].set_linewidth(2)
        g.ax_marg_x.spines['bottom'].set_linewidth(2)
        g.ax_marg_y.set_visible(False)  # 直接隐藏整个右边直方图
        # g.ax_marg_x.set_ylim([0,20])
        g.ax_marg_x.set_ylim([0, 22])
        g.ax_marg_x.set_yticks(np.arange(0, 21, 10))
        g.ax_marg_x.spines['left'].set_visible(True)  # 确保左侧脊柱可见
        g.ax_marg_x.yaxis.set_ticks_position('left')  # 在左侧显示刻度线
        g.ax_marg_x.tick_params(axis='y', which='both', length=6, width=1, color='black', direction='in',
                                labelsize=25, labelcolor='black')

        # 绘制热力图在中心
        sns.heatmap(all_phase5, annot=False, cmap="GnBu", cbar=False, ax=g.ax_joint, vmin=0, vmax=20)
        g.ax_joint.set_xlabel('X-axis orient(\u00B0)', fontsize=font, fontname="Times New Roman", color='black')
        g.ax_joint.set_ylabel('Button index', fontsize=font, fontname="Times New Roman")
        g.ax_joint.tick_params(axis='x', labelsize=font - 2, labelcolor="black", length=6, width=1, direction="in")
        g.ax_joint.tick_params(axis='y', labelsize=font - 4, labelcolor="black", length=6, width=1, direction="in",
                               rotation=0, pad=5)

        # 调整 y 轴的刻度标签并旋转 90 度
        plt.subplots_adjust(hspace=0.05)  # 调整热力图和直方图之间的间距
        plt.subplots_adjust(left=0.007, right=0.702, top=0.967, bottom=0.162)
        g.ax_joint.set_xticks([0.5, 1.5, 2.5, 3.5, 4.5], ['0', '20', '40', '60', '90'])
        g.ax_joint.set_yticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5],
                              ['', '2 ', '', '4 ', '', '6 ', '', '8 ', ' ', '10', '', '12', '', '14', '', '16'])
        for spine in g.ax_joint.spines.values():
            spine.set_visible(True)
            spine.set_linewidth(2)
        plt.savefig('./revistApp_fig20_b.pdf', format='pdf')
        plt.show()
    elif mode == 3:
        # Adjusting paths, filenames, and font
        input_file = './data/button/readingRate/Y/'
        dista = [-90,-60,-30, 30, 60, 90]  # X
        all_phase5 = []

        # Load data into all_phase5
        for i in dista:
            phase5 = np.loadtxt(input_file + str(i) + '.txt', unpack=True)
            all_phase5.append(phase5)

        all_phase5 = np.array(all_phase5)+8
        print(all_phase5)
        # 转置矩阵，使得横轴为距离，纵轴为按钮索引
        all_phase5 = all_phase5.T
        column_sums = np.sum(all_phase5, axis=0)/16+1
        g = sns.JointGrid(data=all_phase5, height=7, ratio=3)

        # 绘制直方图在顶部
        bar_width = 0.5  # 控制柱形条的宽度
        height_scaling = 0.8  # 控制柱形条的高度缩放比例
        g.ax_marg_x.bar(np.arange(0.5, len(column_sums) + 0.5), column_sums, color=colors[1],
                        width=bar_width)

        g.ax_marg_x.tick_params(axis='y', labelsize=10, labelcolor="black")
        # g.ax_marg_x.spines['left'].set_visible(True)  # 显示左侧的 spine，如果被隐藏了

        # 设置 y 轴标签并调整显示位置
        g.ax_marg_x.set_ylabel('Reading\nRates', fontsize=12, fontname="Times New Roman", color='black', labelpad=10)
        g.ax_marg_x.yaxis.set_label_coords(-0.15, 0.5)  # 手动调整 y 轴标签的位置
        g.ax_marg_x.tick_params(labelsize=font - 3, labelcolor="black", length=6, width=1, direction="in")
        g.ax_marg_x.text(-1.5, 0.3, ' Avg. Rate', fontsize=font - 6, color='black', rotation=90)
        # 显示直方图的 x 轴和 y 轴
        g.ax_marg_x.spines['left'].set_visible(True)
        g.ax_marg_x.spines['bottom'].set_visible(True)
        g.ax_marg_x.spines['left'].set_linewidth(2)
        g.ax_marg_x.spines['bottom'].set_linewidth(2)
        g.ax_marg_y.set_visible(False)  # 直接隐藏整个右边直方图
        g.ax_marg_x.set_ylim([0, 22])
        g.ax_marg_x.set_yticks(np.arange(0, 21, 10))
        g.ax_marg_x.spines['left'].set_visible(True)  # 确保左侧脊柱可见
        g.ax_marg_x.yaxis.set_ticks_position('left')  # 在左侧显示刻度线
        g.ax_marg_x.tick_params(axis='y', which='both', length=6, width=1, color='black', direction='in',
                                labelsize=25, labelcolor='black')

        # 绘制热力图在中心

        sns.heatmap(all_phase5, annot=False, cmap="GnBu", cbar=False, ax=g.ax_joint, vmin=0, vmax=20)
        g.ax_joint.set_xlabel('Y-axis orient(\u00B0)', fontsize=font, fontname="Times New Roman", color='black')
        g.ax_joint.set_ylabel('Button Index', fontsize=font, fontname="Times New Roman")
        g.ax_joint.tick_params(axis='x', labelsize=font - 4, labelcolor="black", length=6, width=1, direction="in")
        g.ax_joint.tick_params(axis='y', labelsize=font - 4, labelcolor="black", length=6, width=1, direction="in",
                               rotation=0, pad=5)

        # 调整 y 轴的刻度标签并旋转 90 度
        plt.subplots_adjust(hspace=0.05)  # 调整热力图和直方图之间的间距
        plt.subplots_adjust(left=0.007, right=0.7, top=0.967, bottom=0.162)
        g.ax_joint.set_xticks([0.5, 1.5, 2.5, 3.5, 4.5,5.5], ['-90', '-60', '-30', '30','60', '90'])
        g.ax_joint.set_yticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5],
                              ['', '2 ', '', '4 ', '', '6 ', '', '8 ', ' ', '10', '', '12', '', '14', '', '16'])
        for spine in g.ax_joint.spines.values():
            spine.set_visible(True)
            spine.set_linewidth(2)
        plt.savefig('./revistApp_fig20_c.pdf', format='pdf')
        plt.show()
    elif mode == 4:
        # Adjusting paths, filenames, and font
        input_file = './data/button/readingRate/Z/'
        dista = [0, 20, 40, 60, 90]  # X
        all_phase5 = []
        # phase5 = np.loadtxt(input_file + '/dis/150-RR.txt', unpack=True)
        # all_phase5.append(phase5)

        # Load data into all_phase5
        # phase5 = []
        for i in dista:
            phase5 = np.loadtxt(input_file + str(i) + '.txt', unpack=True)
            all_phase5.append(phase5)
            print(str(i))
        all_phase5 = np.array(all_phase5)+8
        print(all_phase5)
        # 转置矩阵，使得横轴为距离，纵轴为按钮索引
        all_phase5 = all_phase5.T
        column_sums = np.sum(all_phase5, axis=0)/16
        g = sns.JointGrid(data=all_phase5, height=7, ratio=3)

        # 绘制直方图在顶部
        bar_width = 0.5  # 控制柱形条的宽度
        height_scaling = 0.8  # 控制柱形条的高度缩放比例
        g.ax_marg_x.bar(np.arange(0.5, len(column_sums) + 0.5), column_sums, color=colors[1],
                        width=bar_width)

        g.ax_marg_x.tick_params(axis='y', labelsize=10, labelcolor="black")

        # 设置 y 轴标签并调整显示位置
        g.ax_marg_x.set_ylabel('Reading\nRates', fontsize=12, fontname="Times New Roman", color='black', labelpad=10)
        g.ax_marg_x.yaxis.set_label_coords(-0.15, 0.5)  # 手动调整 y 轴标签的位置
        g.ax_marg_x.tick_params(labelsize=font - 3, labelcolor="black", length=2, width=1, direction="in")
        g.ax_marg_x.text(-1.5, 0.3, ' Avg. Rate', fontsize=font - 6, color='black', rotation=90)
        # 显示直方图的 x 轴和 y 轴
        g.ax_marg_x.spines['left'].set_visible(True)
        g.ax_marg_x.spines['bottom'].set_visible(True)
        g.ax_marg_x.spines['left'].set_linewidth(2)
        g.ax_marg_x.spines['bottom'].set_linewidth(2)
        g.ax_marg_y.set_visible(False)  # 直接隐藏整个右边直方图
        g.ax_marg_x.set_ylim([0, 22])
        g.ax_marg_x.set_yticks(np.arange(0, 21, 10))
        g.ax_marg_x.spines['left'].set_visible(True)  # 确保左侧脊柱可见
        g.ax_marg_x.yaxis.set_ticks_position('left')  # 在左侧显示刻度线
        g.ax_marg_x.tick_params(axis='y', which='both', length=6, width=1, color='black', direction='in',
                                labelsize=25, labelcolor='black')

        # 绘制热力图在中心
        sns.heatmap(all_phase5, annot=False, cmap="GnBu", cbar=False, ax=g.ax_joint, vmin=0, vmax=20)
        g.ax_joint.set_xlabel('Z-axis orient(\u00B0)', fontsize=font, fontname="Times New Roman", color='black')
        g.ax_joint.set_ylabel('Button Index', fontsize=font, fontname="Times New Roman")
        g.ax_joint.tick_params(axis='x', labelsize=font - 2, labelcolor="black", length=6, width=1, direction="in")
        g.ax_joint.tick_params(axis='y', labelsize=font - 4, labelcolor="black", length=6, width=1, direction="in",
                               rotation=0, pad=5)
        g.ax_marg_x.set_xlim(0, len(dista)-1)  # Set to match the number of data points
        g.ax_joint.set_xlim(0, len(dista))  # Match with the bar plot above

        # 调整 y 轴的刻度标签并旋转 90 度
        plt.subplots_adjust(hspace=0.05)  # 调整热力图和直方图之间的间距
        plt.subplots_adjust(left=0.005, right=0.7, top=0.967, bottom=0.162)
        g.ax_joint.set_xticks([0.5, 1.5, 2.5,3.5,4.5], ['0', '20', '40', '60', '90'])
        g.ax_joint.set_yticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5],
                              ['', '2 ', '', '4 ', '', '6 ', '', '8 ', ' ', '10', '', '12', '', '14', '', '16'])

        divider = make_axes_locatable(g.ax_marg_y)
        cax = divider.append_axes("left", size="3%", pad=-5)  # Adjust size and padding of the colorbar
        #
        # # Create the colorbar with specific limits
        norm = plt.Normalize(vmin=0, vmax=20)  # Set colorbar normalization range
        cbar = plt.colorbar(g.ax_joint.collections[0], cax=cax, cmap="Blues", norm=norm)
        cbar.ax.tick_params(labelsize=font-8)
        cbar.set_ticks([0, 5, 10, 15, 20])  # Positions of the ticks
        cbar.set_ticklabels(['0', '5', '10', '15', '20'])
        # cbar.set_ticks([0, 5, 10,15,20],['0', '10', '20', '30', '40'])
        cbar.set_label('Reading rate', fontsize=font, fontname="Times New Roman")
        cbar.ax.set_position([0.90, 0.16, 0.1, 0.6])

        for spine in g.ax_joint.spines.values():
            spine.set_visible(True)
            spine.set_linewidth(2)
        plt.savefig('./revistApp_fig20_d.pdf', format='pdf')
        plt.show()