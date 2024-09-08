# for filter data to obvious distribution distance between wifi play time and cellular play time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import sys
import seaborn as sns
import matplotlib as mpl
import matplotlib.image as mpimg
from matplotlib.table import Table
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import os
import pandas as pd
import matplotlib.patches as patches
import math
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator
from scipy.stats import gaussian_kde
mpl.rcParams['font.family'] = 'Times New Roman'
## mode == 1 impact_angle.pdf
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
    fig_size = (8,6)
    if mode == 1:
        # 示例数据
        data = [0.33, 0.2, 0.37, 0.65, 0.91, 0.41, 0.48, 0.01, 0.73, 0.9]
        data2 = [1, 0.83, 0.84, 0.72, 0.92, 1, 0.8, 0.5, 0.81, 0.93]
        data3 = [0.933, 1, 1, 1, 0.9286, 1, 0.8095, 1, 1, 1]
        data5 = [0.9, 0.976, 1, 1, 0.9286, 1, 0.8, 0.8947, 1, 1]
        data4 = [0.082917317,0.01,0.096540332,0.101170047,0.001716069,0.103292553,0.139420314,0.096477543,0.000520021,0.163026521]
        print(np.mean(data4))
        print(np.mean(data5))
        print(np.mean(data5)-np.mean(data4))
        categories = ['Coke', 'Milk', 'Sesame\n  Oil', 'Soybean\n  Oil', 'Redbull', 'Salt', 'Sprite', 'Vinegar', 'Water',
                      'Wine']
        colors = [np.array([0, 114, 189]) / 255, np.array([255, 46, 41]) / 255,
                  np.array([237, 177, 32]) / 255, np.array([119, 172, 48]) / 255,
                  np.array([136, 137, 139]) / 255,np.array([100,100,100]) / 255]
        bar_width = 0.25
        index = np.arange(len(categories))

        # 创建图形和子图
        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(7, 2.8))
        edge_color = (0.5, 0.5, 0.5, 0.5)
        # 绘制下方的垂直条形图
        alp = 0.75
        ax2.bar(index, data4, bar_width, label='RF-EATS', hatch='/', color=colors[0], edgecolor=edge_color,alpha=alp)
        ax2.bar(index + bar_width, data5, bar_width, label='OhmScan', hatch='\\', color=colors[1], edgecolor=edge_color,alpha=alp)
        print(index)
        # 绘制上方的垂直条形图
        ax1.bar(index, data, bar_width, label='RF-EATS w/o VAE', color=colors[2], edgecolor=colors[5], alpha=alp)
        ax1.bar(index + bar_width, data2, bar_width, label='RF-EATS', hatch='/', color=colors[0], edgecolor=edge_color,alpha=alp)
        ax1.bar(index + 2 * bar_width, data3, bar_width, label='OhmScan', hatch='\\', color=colors[1], edgecolor=edge_color,alpha=alp)

        # 设置 x 轴的刻度标签为 categories
        ax1.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=True)
        ax1.set_xticks(index + bar_width)
        # 添加图例
        ax1.legend(loc=(0, 0.9), ncol=3, handlelength=1, frameon=False, fontsize=15, columnspacing=0.6,handletextpad=0.1)
        ax2.legend(loc=(0, 0.9), ncol=2, handlelength=1, frameon=False, fontsize=15, columnspacing=0.6,handletextpad=0.1)
        # ax2.legend(loc=(-0.01, -0.05), ncol=2, handlelength=1.2, frameon=False, fontsize=15, columnspacing=0.2)
        ax1.set_yticks([0,0.5,1], ['0', '0.5','1'])
        ax2.set_yticks([0,0.5,1], ['0', '0.5','1'])
        ax1.set_xticks([0.25, 1.25, 2.25, 3.25, 4.25, 5.25, 6.25, 7.25, 8.25, 9.25], ['1', '2', '3', '4', '5', '6', '7', '8', '9','10'])
        ax2.set_xticks([0.25, 1.25, 2.25, 3.25, 4.25, 5.25, 6.25, 7.25, 8.25, 9.25], ['1', '2', '3', '4', '5', '6', '7', '8', '9','10'])
        ax1.tick_params(axis='y', labelsize=17)
        ax1.tick_params(axis='x', labelsize=18)
        ax2.tick_params(axis='y', labelsize=17)
        ax2.tick_params(axis='x', labelsize=18)
        # 添加轴标签和标题
        ax1.set_ylabel('Accuracy',fontsize=17)
        ax2.set_ylabel('Accuracy',fontsize=17)
        ax2.set_xlabel('Liquid Index', fontsize=17)
        fig.subplots_adjust(left=0.09, right=0.782, top=0.924, bottom=0.174, hspace=0.6)
        ax1.set_ylim([0, 1])
        ax1.set_xlim([-0.25, 9.75])
        ax2.set_ylim([0, 1])
        ax2.set_xlim([-0.25, 9.75])
        ax1.yaxis.set_label_coords(-0.085, 0.5)
        ax2.yaxis.set_label_coords(-0.085, 0.5)
        ax2.xaxis.set_label_coords(0.5, -0.33)
        table_data = [
            [" "],
            [" 1 - Coke "],
            [" 2 - Milk "],
            [" 3 - Sesame Oil "],
            [" 4 - Soybean Oil "],
            [" 5 - Redbull "],
            [" 6 - Salt "],
            [" 7 - Sprite "],
            [" 8 - Vinegar "],
            [" 9 - Water "],
            ["10- Wine "]
        ]
        table = plt.table(cellText=table_data, colLabels=None, cellLoc='center', loc='right', bbox=[1, -0.4, 0.3, 3.1],
                          fontsize=font)
        table.auto_set_font_size(False)
        table.set_fontsize(15)
        plt.text(11.4, 2.5, "Liquid Index", fontsize=15, fontweight='bold', ha='center',
                 )
        # Adjust the appearance of the cells
        for key, cell in table.get_celld().items():
            # Remove vertical borders
            cell.visible_edges = ""

            # Set the text alignment to left
            cell._loc = 'left'
            cell.set_text_props(ha='left')

        line = Line2D([0.805,1], [0.96, 0.96], linewidth=2, color='black', transform=fig.transFigure)
        line1 = Line2D([0.805, 1], [0.87, 0.87], linewidth=1.5, color='black', transform=fig.transFigure)
        line2 = Line2D([0.805, 1], [0.06,0.06], linewidth=2, color='black', transform=fig.transFigure)

        fig.lines.append(line)
        fig.lines.append(line1)
        fig.lines.append(line2)
        plt.savefig('revistApp_rfeats_fig22.pdf', format='pdf')
        # plt.tight_layout()
        plt.show()