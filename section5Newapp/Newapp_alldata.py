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
    colors = [np.array([255, 46, 41]) / 255, np.array([0, 114, 189]) / 255,
              np.array([237, 177, 32]) / 255, np.array([119, 172, 48]) / 255,
              np.array([136, 137, 139]) / 255, np.array([100, 100, 100]) / 255]
    fig_size = (8,6)
    if mode == 1:  ################################################################################# stall rate VS play time
        input_file = './data/protein/'
        dista = [1,2,3,4,5]
        all_phase5 = []
        midpoints = []
        maxpoints = []
        # phase5 = np.loadtxt(input_file + '/1.txt', unpack=True)
        # middle_phase5 = phase5[phase5 <= np.percentile(phase5, 95)]  #
        # midpoints.append(np.median(middle_phase5))
        # all_phase5.append(middle_phase5)
        for index, i in enumerate(dista):
            phase5= np.loadtxt(input_file + '/' + str(i) + '.txt', unpack=True)
            # middle_phase5 = abs(phase5)#*1000/(np.pi*0.003*0.003)
            middle_phase5 = phase5[phase5 <= np.percentile(phase5, 95)]
            midpoints.append(np.median(middle_phase5))
            all_phase5.append(middle_phase5)
        # 创建箱线图
        print(midpoints)
        fig, ax = plt.subplots(figsize=(7, 5.2), sharex=True)  # 修改为1x4的布局
        wide = 0.5
        lindw = 2
        positions = np.arange(1, len(dista) + 1, 1)
        all_data_combined = np.concatenate(all_phase5)
        positions_combined = [positions[-1] + 1]
        parts_combined = ax.violinplot(all_data_combined, positions=positions_combined, showmeans=True,
                                       showmedians=True, widths=0.4)
        print(np.median(all_data_combined))
        # line5 = ax.plot(positions, midpoints, color=colors[0], marker='o', linestyle='-',
        #                 linewidth=lindw, markersize=6, label='1 m',markerfacecolor ='black' ,markeredgecolor='black')
        line5 = ax.plot(positions, midpoints, color=colors[0], marker='o', linestyle='-',
                        linewidth=lindw, markersize=6, markerfacecolor='black', markeredgecolor='black', label='1 m', )
        ax.plot(positions[len(positions) - 1] + 1, np.median(all_data_combined), color=colors[0], marker='o',
                linestyle='-',
                linewidth=lindw, markersize=6, markerfacecolor='black', markeredgecolor='black', label='1 m')

        parts5 = ax.violinplot(all_phase5, positions=positions, showmeans=True, showmedians=True, widths=0.4)
        for j, pc in enumerate(parts5['bodies']):
            pc.set_facecolor(colors[0])
            pc.set_edgecolor(colors[5])
            pc.set_alpha(0.7)
        for j, pc in enumerate(parts_combined['bodies']):
            pc.set_facecolor(colors[1])
            pc.set_edgecolor(colors[5])
            pc.set_alpha(0.7)

        # Customize the rest of the parts (means, medians, etc.)
        for part_name in ['cbars', 'cmins', 'cmaxes', 'cmeans', 'cmedians']:
            if part_name in parts5:
                vp = parts5[part_name]
                vp.set_edgecolor(colors[5])
                vp.set_linewidth(1.5)
        ax.set_ylim([0, 2.6])
        ax.grid()
        ax.grid(True)
        ax.yaxis.set_major_locator(MultipleLocator(1))
        ax.yaxis.set_minor_locator(MultipleLocator(0.2))
        ax.xaxis.set_major_locator(MultipleLocator(1))
        # ax2.yaxis.set_major_locator(MultipleLocator(3))
        ax.xaxis.set_minor_locator(MultipleLocator(0.5))
        plt.subplots_adjust(left=0.115, right=0.996, top=0.99,
                            bottom=0.17)  # left=0.127, right=0.98, top=0.98, bottom=0.18
        ax.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='-', linewidth=0.75, alpha=0.3)
        ax.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)
        ax.set_ylabel('Detection error (wt%)', fontsize=font, fontname="Times New Roman", color='black')
        ax.set_xlabel('Orientation angle(\u00B0)', fontsize=font, fontname="Times New Roman")
        ax.tick_params(labelsize=font, labelcolor="black", length=6, width=1,
                       direction="in")  # , labelfontfamily="Times New Roman")
        ax.tick_params(axis='y', labelsize=font + 1, labelcolor='black')
        ax.spines['top'].set_linewidth(2)  # 上边框
        ax.spines['right'].set_linewidth(2)  # 右边框
        ax.spines['bottom'].set_linewidth(2)  # 下边框
        ax.spines['left'].set_linewidth(2)  # 左边框
        # ax.set_yticks([0, 0.2, 0.4])
        # ax.set_yticklabels([' 0', '0.7', '1.4'])
        # ax.set_yticklabels([0, 0.2, 0.4],  [' 0', '0.7', '1.4'])
        text = ['0','20', '40', '60', '80']
        ax.set_xticks(positions)  # Ensure the number of ticks matches the length of your text
        ax.set_xticklabels(text)
        lt = 0.4
        lp = 2
        ax.text(0.6, 2.4, 'Median error', fontsize=font-5,fontweight='bold',fontname = 'Arial', color='black',
                verticalalignment='center', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.1))
        ax.text(positions[1]-lt, lp, '0.83', fontsize=font-2, color='black', verticalalignment='center',
                fontname = 'Arial',bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[2]-lt, lp, '0.6', fontsize=font-2, color='black', verticalalignment='center',
                fontname = 'Arial',bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[3]-lt, lp, '0.59', fontsize=font-2, color='black', verticalalignment='center',
                fontname = 'Arial',bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[4]-lt, lp, '0.86', fontsize=font-2, color='black', verticalalignment='center',
                fontname = 'Arial',bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[0] - lt, lp, '0.86', fontsize=font - 2, color='black', verticalalignment='center',
                fontname='Arial', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[4]+1 - lt, lp, '0.65', fontsize=font - 2, color=colors[1], verticalalignment='center',
                fontname='Arial', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        # ax.text(positions[4] + 0.55, -0.15, 'Total', fontsize=font - 3, color='black', verticalalignment='center',
        #         )
        ax.text(positions[4] + 0.55, -0.28, 'Over\n  all', fontsize=font - 2, color='black', verticalalignment='center',
                )
        # ax.text(positions[4]-lt, lp, '0.18', fontsize=font-2, color='black', verticalalignment='center',fontname = 'Arial')
        ax.xaxis.set_label_coords(0.5, -0.1)
        plt.savefig('./newapp_fig24.pdf', format='pdf')
        plt.show()
    elif mode == 2:  ################################################################################# stall rate VS play time
        input_file = './data/lightdetect'
        dista = [50,100,150,200,250]
        all_phase5 = []
        midpoints = []
        maxpoints = []
        for index, i in enumerate(dista):
            phase5 = np.loadtxt(input_file + '/dis-error' + str(i) + '.txt', unpack=True)
            # middle_phase5 = abs(phase5)#*1000/(np.pi*0.003*0.003)
            # midpoints.append(np.median(middle_phase5))
            middle_phase5 = phase5[phase5 <= np.percentile(phase5, 95)]
            # maxpoints.append(np.percentile(middle_phase5, 80))
            midpoints.append(np.median(middle_phase5))
            all_phase5.append(middle_phase5)
        # 创建箱线图
        print(midpoints)
        fig, ax = plt.subplots(figsize=(7,4.4), sharex=True)  # 修改为1x4的布局
        wide = 0.5
        lindw = 2
        positions = np.arange(1, len(dista) + 1, 1)
        all_data_combined = np.concatenate(all_phase5)
        positions_combined = [positions[-1] + 1]
        parts_combined = ax.violinplot(all_data_combined, positions=positions_combined, showmeans=True,
                                       showmedians=True, widths=0.4)
        print(np.median(all_data_combined))
        parts5 = ax.violinplot(all_phase5, positions=positions, showmeans=True, showmedians=True, widths=0.4)
        line5 = ax.plot(positions, midpoints, color=colors[0], marker='o', linestyle='-',
                linewidth=lindw, markersize=6, markerfacecolor='black', markeredgecolor='black',label='1 m')
        ax.plot(positions[len(positions) - 1] + 1, np.median(all_data_combined), color=colors[0], marker='o',
                linestyle='-',
                linewidth=lindw, markersize=6, markerfacecolor='black', markeredgecolor='black', label='1 m')

        for j, pc in enumerate(parts5['bodies']):
            pc.set_facecolor(colors[0])
            pc.set_edgecolor(colors[5])
            pc.set_alpha(0.7)
        for j, pc in enumerate(parts_combined['bodies']):
            pc.set_facecolor(colors[1])
            pc.set_edgecolor(colors[5])
            pc.set_alpha(0.7)

        # Customize the rest of the parts (means, medians, etc.)
        for part_name in ['cbars', 'cmins', 'cmaxes', 'cmeans', 'cmedians']:
            if part_name in parts5:
                vp = parts5[part_name]
                vp.set_edgecolor(colors[5])
                vp.set_linewidth(1.5)

        ax.grid()
        ax.grid(True)
        ax.yaxis.set_major_locator(MultipleLocator(2))
        ax.yaxis.set_minor_locator(MultipleLocator(0.5))
        ax.xaxis.set_major_locator(MultipleLocator(1))
        # ax2.yaxis.set_major_locator(MultipleLocator(3))
        ax.xaxis.set_minor_locator(MultipleLocator(0.5))
        plt.subplots_adjust(left=0.115, right=0.996, top=0.99,
                            bottom=0.198)  # left=0.127, right=0.98, top=0.98, bottom=0.18
        ax.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='-', linewidth=0.75, alpha=0.3)
        ax.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)
        ax.set_ylabel('Exposure time error(s)', fontsize=font, fontname="Times New Roman", color='black')
        ax.set_xlabel('Distance (m)', fontsize=font, fontname="Times New Roman")
        ax.tick_params(labelsize=font, labelcolor="black", length=6, width=1,
                       direction="in")  # , labelfontfamily="Times New Roman")
        ax.tick_params(axis='y', labelsize=font + 1, labelcolor='black')
        ax.spines['top'].set_linewidth(2)  # 上边框
        ax.spines['right'].set_linewidth(2)  # 右边框
        ax.spines['bottom'].set_linewidth(2)  # 下边框
        ax.spines['left'].set_linewidth(2)  # 左边框

        ax.set_ylim([0, 6.3])
        # ax.set_yticks([0, 0.2, 0.4])
        # ax.set_yticklabels([' 0', '0.7', '1.4'])
        # ax.set_yticklabels([0, 0.2, 0.4],  [' 0', '0.7', '1.4'])
        text = ['0.5', '1', '1.5', '2','2.5']
        ax.set_xticks(positions)  # Ensure the number of ticks matches the length of your text
        ax.set_xticklabels(text)
        lt = 0.4
        lp = 3.5
        ax.text(0.6, 4.5, 'Median error', fontsize=font - 5, fontweight='bold', fontname='Arial', color='black',
                verticalalignment='center', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[0] - lt, lp, '1.31', fontsize=font - 2, color='black', verticalalignment='center',
                fontname='Arial', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[1] - lt, lp, '1.41', fontsize=font - 2, color='black', verticalalignment='center',
                fontname='Arial', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[2] - lt, lp, '2.3', fontsize=font - 2, color='black', verticalalignment='center',
                fontname='Arial', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[3] - lt, lp, '2.06', fontsize=font - 2, color='black', verticalalignment='center',
                fontname='Arial', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[4] - lt, lp, '2.10', fontsize=font - 2, color='black', verticalalignment='center',
                fontname='Arial', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[4] + 1 - lt, lp, '1.78', fontsize=font - 2, color=colors[1], verticalalignment='center',
                fontname='Arial', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[4] + 0.55, -0.84, 'Over\n  all', fontsize=font - 2, color='black', verticalalignment='center',
                )
        ax.yaxis.set_label_coords(-0.06, 0.4)
        ax.xaxis.set_label_coords(0.5, -0.12)
        plt.savefig('./newapp_fig26_a.pdf', format='pdf')
        plt.show()
    elif mode == 3:  ################################################################################# stall rate VS play time
        input_file = './data/lightdetect'
        dista = [0,20,40,60]
        all_phase5 = []
        midpoints = []
        maxpoints = []
        phase5 = np.loadtxt(input_file + '/dis-error50.txt', unpack=True)
        middle_phase5 = phase5[phase5<np.percentile(phase5, 95)]
        midpoints.append(np.median(middle_phase5))
        all_phase5.append(middle_phase5)
        for index, i in enumerate(dista):
            phase5= np.loadtxt(input_file + '/rotate-error' + str(i) + '.txt', unpack=True)
            middle_phase5 = phase5[phase5 <= np.percentile(phase5, 95)]
            midpoints.append(np.median(middle_phase5))
            all_phase5.append(middle_phase5)
        # 创建箱线图
        print(midpoints)
        fig, ax = plt.subplots(figsize=(7, 4.4), sharex=True)  # 修改为1x4的布局
        wide = 0.5
        lindw = 2
        positions = np.arange(1, len(dista) + 2, 1)
        all_data_combined = np.concatenate(all_phase5)
        positions_combined = [positions[-1] + 1]
        parts_combined = ax.violinplot(all_data_combined, positions=positions_combined, showmeans=True,
                                       showmedians=True, widths=0.4)
        print(np.median(all_data_combined))
        parts5 = ax.violinplot(all_phase5, positions=positions, showmeans=True, showmedians=True, widths=0.4)
        line5 = ax.plot(positions, midpoints, color=colors[0], marker='o', linestyle='-',
                linewidth=lindw, markersize=6,markerfacecolor='black', markeredgecolor='black', label='1 m')
        ax.plot(positions[len(positions) - 1] + 1, np.median(all_data_combined), color=colors[0], marker='o',
                linestyle='-',
                linewidth=lindw, markersize=6, markerfacecolor='black', markeredgecolor='black', label='1 m')

        for j, pc in enumerate(parts5['bodies']):
            pc.set_facecolor(colors[0])
            pc.set_edgecolor(colors[5])
            pc.set_alpha(0.7)
        for j, pc in enumerate(parts_combined['bodies']):
            pc.set_facecolor(colors[1])
            pc.set_edgecolor(colors[5])
            pc.set_alpha(0.7)

        # Customize the rest of the parts (means, medians, etc.)
        for part_name in ['cbars', 'cmins', 'cmaxes', 'cmeans', 'cmedians']:
            if part_name in parts5:
                vp = parts5[part_name]
                vp.set_edgecolor(colors[5])
                vp.set_linewidth(1.5)
        ax.grid()
        ax.grid(True)
        ax.yaxis.set_major_locator(MultipleLocator(2))
        ax.yaxis.set_minor_locator(MultipleLocator(0.5))
        ax.xaxis.set_major_locator(MultipleLocator(1))
        ax.xaxis.set_minor_locator(MultipleLocator(0.5))
        plt.subplots_adjust(left=0.115, right=0.996, top=0.99,
                            bottom=0.198)  # left=0.127, right=0.98, top=0.98, bottom=0.18
        ax.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='-', linewidth=0.75, alpha=0.3)
        ax.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)
        ax.set_ylabel('Exposure time error(s)', fontsize=font, fontname="Times New Roman", color='black')
        ax.set_xlabel('Orientation angle(\u00B0)', fontsize=font, fontname="Times New Roman")
        ax.tick_params(labelsize=font, labelcolor="black", length=6, width=1,
                       direction="in")  # , labelfontfamily="Times New Roman")
        ax.tick_params(axis='y', labelsize=font + 1, labelcolor='black')
        ax.spines['top'].set_linewidth(2)  # 上边框
        ax.spines['right'].set_linewidth(2)  # 右边框
        ax.spines['bottom'].set_linewidth(2)  # 下边框
        ax.spines['left'].set_linewidth(2)  # 左边框
        ax.set_ylim([0, 6.2])
        text = ['0','20', '40', '60', '80']
        ax.set_xticks(positions)  # Ensure the number of ticks matches the length of your text
        ax.set_xticklabels(text)
        lt = 0.4
        lp = 3.5
        ax.text(0.6, 4.5, 'Median error', fontsize=font-5,fontweight='bold',fontname = 'Arial', color='black',
                verticalalignment='center', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[0] - lt, lp, '1.3', fontsize=font - 2, color='black', verticalalignment='center',
                fontname='Arial', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[1]-lt, lp, '1.74', fontsize=font-2, color='black', verticalalignment='center',
                fontname = 'Arial',bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[2]-lt, lp, '1.42', fontsize=font-2, color='black', verticalalignment='center',
                fontname = 'Arial',bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[3]-lt, lp, '1.62', fontsize=font-2, color='black', verticalalignment='center',
                fontname = 'Arial',bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[4]-lt, lp, '1.74', fontsize=font-2, color='black', verticalalignment='center',
                fontname = 'Arial',bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[4] + 1 - lt, lp, '1.56', fontsize=font - 2, color=colors[1], verticalalignment='center',
                fontname='Arial', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[4] + 0.55, -0.84, 'Over\n  all', fontsize=font - 2, color='black', verticalalignment='center',
                )
        ax.yaxis.set_label_coords(-0.06, 0.4)
        ax.xaxis.set_label_coords(0.5, -0.12)
        plt.savefig('./newapp_fig26_b.pdf', format='pdf')
        plt.show()
    elif mode == 4:  ################################################################################# stall rate VS play time
        input_file = './data/Pressure/differentangle_distance'
        dista = [50,100,150,200,250]
        all_phase5 = []
        midpoints = []
        maxpoints = []
        for index, i in enumerate(dista):
            phase5= np.loadtxt(input_file + '/dis-error' + str(i) + '.txt', unpack=True)
            middle_phase5 = phase5[phase5<0.45]#*1000/(np.pi*0.003*0.003)

            maxpoints.append(np.percentile(middle_phase5, 80))
            midpoints.append(np.median(middle_phase5))
            all_phase5.append(middle_phase5)


        # 创建箱线图
        print(midpoints)
        fig, ax = plt.subplots(figsize=(7, 4.4))  # Create a single subplot
        wide = 0.5
        lindw = 2
        positions = np.arange(0, len(dista), 1)
        all_data_combined = np.concatenate(all_phase5)  # 将所有子集合并成一个整体
        print(np.median(all_data_combined))
        positions_combined = [positions[-1] + 1]  # 将其放在最后一个位置
        parts_combined = ax.violinplot(all_data_combined, positions=positions_combined, showmeans=True,
                                       showmedians=True, widths=0.4)
        print(positions[len(positions)-1]+1)
        # 在琴图上方添加折线图
        line5 = ax.plot(positions, midpoints, color=colors[0], marker='o', linestyle='-',
                        linewidth=lindw, markersize=6,markerfacecolor ='black' ,markeredgecolor='black', label='1 m')
        ax.plot(positions[len(positions)-1]+1, np.median(all_data_combined), color=colors[0], marker='o', linestyle='-',
                        linewidth=lindw, markersize=6, markerfacecolor='black', markeredgecolor='black', label='1 m')

        parts5 = ax.violinplot(all_phase5, positions=positions, showmeans=True, showmedians=True, widths=0.4)
        for j, pc in enumerate(parts5['bodies']):
            pc.set_facecolor(colors[0])
            pc.set_edgecolor(colors[5])
            pc.set_alpha(0.7)
        for j, pc in enumerate(parts_combined['bodies']):
            pc.set_facecolor(colors[1])
            pc.set_edgecolor(colors[5])
            pc.set_alpha(0.7)

        # Customize the rest of the parts (means, medians, etc.)
        for part_name in ['cbars', 'cmins', 'cmaxes', 'cmeans', 'cmedians']:
            if part_name in parts5:
                vp = parts5[part_name]
                vp.set_edgecolor(colors[5])
                vp.set_linewidth(1.5)
        # # Customizing the violins
        # for violin in ax.collections:  # This iterates over the violin parts
        #     violin.set_alpha(0.7)
        #     violin.set_edgecolor(colors[5])
        ax.set_ylim([0, 0.52])
        ax.grid()
        ax.grid(True)
        ax.yaxis.set_major_locator(MultipleLocator(0.2))
        ax.yaxis.set_minor_locator(MultipleLocator(0.05))
        ax.xaxis.set_major_locator(MultipleLocator(1))
        # ax2.yaxis.set_major_locator(MultipleLocator(3))
        ax.xaxis.set_minor_locator(MultipleLocator(0.5))
        plt.subplots_adjust(left=0.164, right=0.996, top=0.99,
                            bottom=0.187)  # left=0.127, right=0.98, top=0.98, bottom=0.18
        ax.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='-', linewidth=0.75, alpha=0.3)
        ax.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)
        ax.set_ylabel('Pressure error (kPa)', fontsize=font, fontname="Times New Roman", color='black')
        ax.set_xlabel('Distance (m)', fontsize=font, fontname="Times New Roman")
        ax.tick_params(labelsize=font, labelcolor="black", length=6, width=1,
                       direction="in")  # , labelfontfamily="Times New Roman")
        ax.tick_params(axis='y', labelsize=font + 1, labelcolor='black')
        ax.spines['top'].set_linewidth(2)  # 上边框
        ax.spines['right'].set_linewidth(2)  # 右边框
        ax.spines['bottom'].set_linewidth(2)  # 下边框
        ax.spines['left'].set_linewidth(2)  # 左边框
        ax.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5])
        ax.set_yticklabels([' 0', '0.3', '0.6', '0.9', '1.2', '1.5'])
        # ax.set_yticklabels([0, 0.2, 0.4],  [' 0', '0.7', '1.4'])
        text = ['0.5', '1', '1.5', '2', '2.5']
        ax.set_xticks(positions)  # Ensure the number of ticks matches the length of your text
        ax.set_xticklabels(text)
        lt = 0.45
        lp = 0.34
        # 0.53, 0.420, 0.47
        ax.text(-0.45, 0.41, 'Median error', fontsize=font-5,fontweight='bold',fontname = 'Arial',
                color='black', verticalalignment='center',bbox=dict(facecolor='white', alpha=0.8,
                                                                    edgecolor='none', pad=0.1))
        ax.text(positions[0]-lt, lp, '0.21', fontsize=font-2, color='black', verticalalignment='center',
                fontname = 'Arial',bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.1))
        ax.text(positions[1]-lt, lp, '0.3', fontsize=font-2, color='black', verticalalignment='center',
                fontname = 'Arial',bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[2]-lt, lp, '0.18', fontsize=font-2, color='black', verticalalignment='center',
                fontname = 'Arial',bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[3]-lt, lp, '0.21', fontsize=font-2, color='black', verticalalignment='center',
                fontname = 'Arial',bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[4]-lt, lp, '0.27', fontsize=font-2, color='black', verticalalignment='center',
                fontname = 'Arial',bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[4]+1 - lt, lp, '0.21', fontsize=font - 2, color=colors[1], verticalalignment='center',
                fontname='Arial', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[4] + 0.55, -0.07, 'Over\n  all', fontsize=font - 2, color='black', verticalalignment='center',
                )
        # ax.text(positions[4] + 0.55, -0.038, 'Total', fontsize=font - 1, color='black', verticalalignment='center',
        #         )
        ax.yaxis.set_label_coords(-0.12, 0.48)
        ax.xaxis.set_label_coords(0.5, -0.11)
        plt.savefig('./newapp_fig28_a.pdf', format='pdf')
        plt.show()
    elif mode == 5:  ################################################################################# stall rate VS play time
        input_file = './data/Pressure/differentangle_distance'
        dista = [0,20,40,60]
        all_phase5 = []
        midpoints = []
        maxpoints = []
        phase5 = np.loadtxt(input_file + '/dis-error50.txt', unpack=True)
        middle_phase5 = phase5[phase5 <= 0.4]
        midpoints.append(np.median(middle_phase5))
        all_phase5.append(middle_phase5)
        for index, i in enumerate(dista):
            phase5= np.loadtxt(input_file + '/rotate-error' + str(i) + '.txt', unpack=True)
            # middle_phase5 = abs(phase5)#*1000/(np.pi*0.003*0.003)
            middle_phase5 = phase5[phase5 <= 0.5]
            maxpoints.append(np.percentile(middle_phase5, 80))
            midpoints.append(np.median(middle_phase5))
            all_phase5.append(middle_phase5)

        k = np.array(midpoints)/(0.007*0.007*np.pi)/1000
        # 创建箱线图
        print(k)
        fig, ax = plt.subplots(figsize=(7, 4.4), sharex=True)  # 修改为1x4的布局
        wide = 0.5
        lindw = 2
        positions = np.arange(1, len(dista) + 2, 1)
        all_data_combined = np.concatenate(all_phase5)
        positions_combined = [positions[-1] + 1]
        parts_combined = ax.violinplot(all_data_combined, positions=positions_combined, showmeans=True,
                                       showmedians=True, widths=0.4)
        print(np.median(all_data_combined))
        line5 = ax.plot(positions, midpoints, color=colors[0], marker='o', linestyle='-',
                        linewidth=lindw, markersize=6, label='1 m',markerfacecolor ='black' ,markeredgecolor='black')
        ax.plot(positions[len(positions) - 1] + 1, np.median(all_data_combined), color=colors[0], marker='o',
                linestyle='-',
                linewidth=lindw, markersize=6, markerfacecolor='black', markeredgecolor='black', label='1 m')

        parts5 = ax.violinplot(all_phase5, positions=positions, showmeans=True, showmedians=True, widths=0.4)
        for j, pc in enumerate(parts5['bodies']):
            pc.set_facecolor(colors[0])
            pc.set_edgecolor(colors[5])
            pc.set_alpha(0.7)
        for j, pc in enumerate(parts_combined['bodies']):
            pc.set_facecolor(colors[1])
            pc.set_edgecolor(colors[5])
            pc.set_alpha(0.7)

        # Customize the rest of the parts (means, medians, etc.)
        for part_name in ['cbars', 'cmins', 'cmaxes', 'cmeans', 'cmedians']:
            if part_name in parts5:
                vp = parts5[part_name]
                vp.set_edgecolor(colors[5])
                vp.set_linewidth(1.5)

        ax.set_ylim([0, 0.52])
        ax.grid()
        ax.grid(True)
        ax.yaxis.set_major_locator(MultipleLocator(0.2))
        ax.yaxis.set_minor_locator(MultipleLocator(0.05))
        ax.xaxis.set_major_locator(MultipleLocator(1))
        # ax2.yaxis.set_major_locator(MultipleLocator(3))
        ax.xaxis.set_minor_locator(MultipleLocator(0.5))
        plt.subplots_adjust(left=0.164, right=0.996, top=0.99,
                            bottom=0.187)  # left=0.127, right=0.98, top=0.98, bottom=0.18
        ax.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='-', linewidth=0.75, alpha=0.3)
        ax.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)
        ax.set_ylabel('Pressure error(kPa)', fontsize=font, fontname="Times New Roman", color='black')
        ax.set_xlabel('Orientation angle(\u00B0)', fontsize=font, fontname="Times New Roman")
        ax.tick_params(labelsize=font, labelcolor="black", length=6, width=1,
                       direction="in")  # , labelfontfamily="Times New Roman")
        ax.tick_params(axis='y', labelsize=font + 1, labelcolor='black')
        ax.spines['top'].set_linewidth(2)  # 上边框
        ax.spines['right'].set_linewidth(2)  # 右边框
        ax.spines['bottom'].set_linewidth(2)  # 下边框
        ax.spines['left'].set_linewidth(2)  # 左边框
        ax.set_yticks([0,0.1, 0.2,0.3, 0.4,0.5])
        ax.set_yticklabels([' 0', '0.3','0.6','0.9', '1.2','1.5'])
        text = ['0','20', '40', '60', '80']
        ax.set_xticks(positions)  # Ensure the number of ticks matches the length of your text
        ax.set_xticklabels(text)
        lt = 0.45
        lp = 0.34
        ax.text(0.53, 0.42, 'Median error', fontsize=font-5,fontweight='bold',fontname = 'Arial', color='black', verticalalignment='center')
        ax.text(positions[0] - lt, lp, '0.21', fontsize=font - 2, color='black', verticalalignment='center',
                fontname='Arial',bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.1))
        ax.text(positions[1]-lt, lp, '0.21', fontsize=font-2, color='black', verticalalignment='center',
                fontname = 'Arial',bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[2]-lt, lp, '0.21', fontsize=font-2, color='black', verticalalignment='center',
                fontname = 'Arial',bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[3]-lt, lp, '0.21', fontsize=font-2, color='black', verticalalignment='center',
                fontname = 'Arial',bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[4]-lt, lp, '0.39', fontsize=font-2, color='black', verticalalignment='center',
                fontname = 'Arial',bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[4]+1 - lt, lp, '0.24', fontsize=font - 2, color=colors[1], verticalalignment='center',
                fontname='Arial', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[4] + 0.55, -0.07, 'Over\n  all', fontsize=font - 2, color='black', verticalalignment='center',
                )

        ax.yaxis.set_label_coords(-0.12, 0.49)
        ax.xaxis.set_label_coords(0.5, -0.11)
        plt.savefig('./newapp_fig28_b.pdf', format='pdf')
        plt.show()
    elif mode == 6:  ################################################################################# stall rate VS play time
        input_file = './data/temperature/温度'
        dista = [0,20,40,60]
        all_phase5 = []
        midpoints = []
        maxpoints = []
        phase5 = np.loadtxt(input_file + '/dis-error50.txt', unpack=True)
        middle_phase5 = phase5[phase5 <= np.percentile(phase5, 95)]  #
        midpoints.append(np.median(middle_phase5))
        all_phase5.append(middle_phase5)
        for index, i in enumerate(dista):
            phase5= np.loadtxt(input_file + '/error-' + str(i) + '.txt', unpack=True)
            # middle_phase5 = abs(phase5)#*1000/(np.pi*0.003*0.003)
            middle_phase5 = phase5[phase5 <= np.percentile(phase5, 95)]
            midpoints.append(np.median(middle_phase5))
            all_phase5.append(middle_phase5)
        # 创建箱线图
        print(midpoints)
        fig, ax = plt.subplots(figsize=(7, 4.4), sharex=True)  # 修改为1x4的布局
        wide = 0.5
        lindw = 2
        positions = np.arange(1, len(dista) + 2, 1)
        all_data_combined = np.concatenate(all_phase5)
        positions_combined = [positions[-1] + 1]
        parts_combined = ax.violinplot(all_data_combined, positions=positions_combined, showmeans=True,
                                       showmedians=True, widths=0.4)
        print(np.median(all_data_combined))
        # line5 = ax.plot(positions, midpoints, color=colors[0], marker='o', linestyle='-',
        #                 linewidth=lindw, markersize=6, label='1 m',markerfacecolor ='black' ,markeredgecolor='black')
        line5 = ax.plot(positions, midpoints, color=colors[0], marker='o', linestyle='-',
                        linewidth=lindw, markersize=6, markerfacecolor='black', markeredgecolor='black', label='1 m', )
        ax.plot(positions[len(positions) - 1] + 1, np.median(all_data_combined), color=colors[0], marker='o',
                linestyle='-',
                linewidth=lindw, markersize=6, markerfacecolor='black', markeredgecolor='black', label='1 m')

        parts5 = ax.violinplot(all_phase5, positions=positions, showmeans=True, showmedians=True, widths=0.4)
        for j, pc in enumerate(parts5['bodies']):
            pc.set_facecolor(colors[0])
            pc.set_edgecolor(colors[5])
            pc.set_alpha(0.7)
        for j, pc in enumerate(parts_combined['bodies']):
            pc.set_facecolor(colors[1])
            pc.set_edgecolor(colors[5])
            pc.set_alpha(0.7)

        # Customize the rest of the parts (means, medians, etc.)
        for part_name in ['cbars', 'cmins', 'cmaxes', 'cmeans', 'cmedians']:
            if part_name in parts5:
                vp = parts5[part_name]
                vp.set_edgecolor(colors[5])
                vp.set_linewidth(1.5)
        ax.set_ylim([0, 6.6])
        ax.grid()
        ax.grid(True)
        ax.yaxis.set_major_locator(MultipleLocator(2))
        ax.yaxis.set_minor_locator(MultipleLocator(0.5))
        ax.xaxis.set_major_locator(MultipleLocator(1))
        # ax2.yaxis.set_major_locator(MultipleLocator(3))
        ax.xaxis.set_minor_locator(MultipleLocator(0.5))
        plt.subplots_adjust(left=0.115, right=0.996, top=0.99,
                            bottom=0.187)  # left=0.127, right=0.98, top=0.98, bottom=0.18
        ax.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='-', linewidth=0.75, alpha=0.3)
        ax.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)
        ax.set_ylabel('Temperature error(\u00B0C)', fontsize=font, fontname="Times New Roman", color='black')
        ax.set_xlabel('Orientation angle(\u00B0)', fontsize=font, fontname="Times New Roman")
        ax.tick_params(labelsize=font, labelcolor="black", length=6, width=1,
                       direction="in")  # , labelfontfamily="Times New Roman")
        ax.tick_params(axis='y', labelsize=font + 1, labelcolor='black')
        ax.spines['top'].set_linewidth(2)  # 上边框
        ax.spines['right'].set_linewidth(2)  # 右边框
        ax.spines['bottom'].set_linewidth(2)  # 下边框
        ax.spines['left'].set_linewidth(2)  # 左边框
        text = ['0','20', '40', '60', '80']
        ax.set_xticks(positions)  # Ensure the number of ticks matches the length of your text
        ax.set_xticklabels(text)
        lt = 0.4
        lp = 4.2
        ax.text(0.6, 5.55, 'Median error', fontsize=font-5,fontweight='bold',fontname = 'Arial', color='black',
                verticalalignment='center', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.1))
        ax.text(positions[1]-lt, lp, '1.57', fontsize=font-2, color='black', verticalalignment='center',
                fontname = 'Arial',bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[2]-lt, lp, '1.74', fontsize=font-2, color='black', verticalalignment='center',
                fontname = 'Arial',bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[3]-lt, lp, '1.82', fontsize=font-2, color='black', verticalalignment='center',
                fontname = 'Arial',bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[4]-lt, lp, '1.78', fontsize=font-2, color='black', verticalalignment='center',
                fontname = 'Arial',bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[0] - lt, lp, '1.60', fontsize=font - 2, color='black', verticalalignment='center',
                fontname='Arial', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[4]+1 - lt, lp, '1.70', fontsize=font - 2, color=colors[1], verticalalignment='center',
                fontname='Arial', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        # ax.text(positions[4] + 0.55,-0.48, 'Total', fontsize=font, color='black', verticalalignment='center',
        #         )
        ax.text(positions[4] + 0.55, -0.84, 'Over\n  all', fontsize=font - 2, color='black', verticalalignment='center',
                )
        ax.yaxis.set_label_coords(-0.06, 0.41)
        ax.xaxis.set_label_coords(0.5, -0.11)
        # ax.text(positions[4]-lt, lp, '0.18', fontsize=font-2, color='black', verticalalignment='center',fontname = 'Arial')
        plt.savefig('./newapp_fig30_b.pdf', format='pdf')
        plt.show()
    elif mode == 7:  ################################################################################# stall rate VS play time
        input_file = './data/temperature/温度'
        dista = [50,100,150,200]
        all_phase5 = []
        midpoints = []
        maxpoints = []
        for index, i in enumerate(dista):
            phase5 = np.loadtxt(input_file + '/dis-error' + str(i) + '.txt', unpack=True)
            # middle_phase5 = abs(phase5)#*1000/(np.pi*0.003*0.003)
            middle_phase5 = phase5[phase5 <= np.percentile(phase5, 95)]
            midpoints.append(np.median(middle_phase5))
            all_phase5.append(middle_phase5)

        phase5 = np.loadtxt(input_file + '/error-80.txt', unpack=True)
        # middle_phase5 = abs(phase5)
        middle_phase5 = phase5[phase5 <= np.percentile(phase5, 95)]
        midpoints.append(np.median(middle_phase5))
        all_phase5.append(middle_phase5)
        # 创建箱线图
        print(midpoints)
        fig, ax = plt.subplots(figsize=(7, 4.4), sharex=True)  # 修改为1x4的布局
        wide = 0.5
        lindw = 2
        positions = np.arange(1, len(dista) + 2, 1)
        all_data_combined = np.concatenate(all_phase5)
        positions_combined = [positions[-1] + 1]
        parts_combined = ax.violinplot(all_data_combined, positions=positions_combined, showmeans=True,
                                       showmedians=True, widths=0.4)
        print(np.median(all_data_combined))
        parts5 = ax.violinplot(all_phase5, positions=positions, showmeans=True,
                               showmedians=True, widths=0.4)
        line5 = ax.plot(positions, midpoints, color=colors[0], marker='o', linestyle='-',
                        linewidth=lindw, markersize=6, markerfacecolor ='black' ,markeredgecolor='black',label='1 m',)
        ax.plot(positions[len(positions) - 1] + 1, np.median(all_data_combined), color=colors[0], marker='o',
                linestyle='-',
                linewidth=lindw, markersize=6, markerfacecolor='black', markeredgecolor='black', label='1 m')

        for j, pc in enumerate(parts5['bodies']):
            pc.set_facecolor(colors[0])
            pc.set_edgecolor(colors[5])
            pc.set_alpha(0.7)
        for j, pc in enumerate(parts_combined['bodies']):
            pc.set_facecolor(colors[1])
            pc.set_edgecolor(colors[5])
            pc.set_alpha(0.7)

        # Customize the rest of the parts (means, medians, etc.)
        for part_name in ['cbars', 'cmins', 'cmaxes', 'cmeans', 'cmedians']:
            if part_name in parts5:
                vp = parts5[part_name]
                vp.set_edgecolor(colors[5])
                vp.set_linewidth(1.5)

        ax.set_ylim([0, 6.6])
        ax.grid()
        ax.grid(True)
        ax.yaxis.set_major_locator(MultipleLocator(2))
        ax.yaxis.set_minor_locator(MultipleLocator(0.5))
        ax.xaxis.set_major_locator(MultipleLocator(1))
        # ax2.yaxis.set_major_locator(MultipleLocator(3))
        ax.xaxis.set_minor_locator(MultipleLocator(0.5))
        plt.subplots_adjust(left=0.115, right=0.996, top=0.99,
                            bottom=0.187)  # left=0.127, right=0.98, top=0.98, bottom=0.18
        ax.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='-', linewidth=0.75, alpha=0.3)
        ax.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)
        ax.set_ylabel('Temperature error(\u00B0C)', fontsize=font, fontname="Times New Roman", color='black')
        ax.set_xlabel('Distance (m)', fontsize=font, fontname="Times New Roman")
        ax.tick_params(labelsize=font, labelcolor="black", length=6, width=1,
                       direction="in")  # , labelfontfamily="Times New Roman")
        ax.tick_params(axis='y', labelsize=font + 1, labelcolor='black')
        ax.spines['top'].set_linewidth(2)  # 上边框
        ax.spines['right'].set_linewidth(2)  # 右边框
        ax.spines['bottom'].set_linewidth(2)  # 下边框
        ax.spines['left'].set_linewidth(2)  # 左边框
        # ax.set_yticks([0, 0.2, 0.4])
        # ax.set_yticklabels([' 0', '0.7', '1.4'])
        # ax.set_yticklabels([0, 0.2, 0.4],  [' 0', '0.7', '1.4'])
        text = ['0.5', '1', '1.5', '2','2.5']
        ax.set_xticks(positions)  # Ensure the number of ticks matches the length of your text
        ax.set_xticklabels(text)
        lt = 0.4
        lp = 4.2
        ax.text(0.6, 5.63, 'Median error', fontsize=font - 5, fontweight='bold', fontname='Arial', color='black',
                verticalalignment='center')#, bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.1))
        ax.text(positions[0] - lt, lp, '1.61', fontsize=font - 2, color='black', verticalalignment='center',
                fontname='Arial', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[1] - lt, lp, '1.61', fontsize=font - 2, color='black', verticalalignment='center',
                fontname='Arial', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[2] - lt, lp, '1.76', fontsize=font - 2, color='black', verticalalignment='center',
                fontname='Arial', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[3] - lt, lp, '1.47', fontsize=font - 2, color='black', verticalalignment='center',
                fontname='Arial', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[4] - lt, lp, '1.80', fontsize=font - 2, color='black', verticalalignment='center',
                fontname='Arial', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(positions[4] + 1 - lt, lp, '1.67', fontsize=font - 2, color=colors[1], verticalalignment='center',
                fontname='Arial', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        # ax.text(positions[4] + 0.55, -0.49, 'Total', fontsize=font, color='black', verticalalignment='center',
        #         )
        ax.text(positions[4] + 0.55, -0.84, 'Over\n  all', fontsize=font - 2, color='black', verticalalignment='center',
                )
        # ax.yaxis.set_label_coords(-0.06, 0.48)
        # ax.xaxis.set_label_coords(0.5, -0.1)
        ax.yaxis.set_label_coords(-0.06, 0.41)
        ax.xaxis.set_label_coords(0.5, -0.11)
        plt.savefig('./newapp_fig30_a.pdf', format='pdf')
        plt.show()



