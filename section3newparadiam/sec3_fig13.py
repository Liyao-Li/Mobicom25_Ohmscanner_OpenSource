import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib import pyplot
import matplotlib as mpl
import sys
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator
font_size = 32
font_properties = FontProperties(family='Times New Roman', weight='normal', size=font_size)

mpl.rcParams['font.family'] = 'Times New Roman'
#fig13 a Different scenarios
#fig13 b Impedance error.
##Comparison between OhmScan and VNA
# measured impedance in different environments.
if __name__ == "__main__":
    mode = int(sys.argv[1])
    red_rgb = (1, 0.2118, 0.1569)
    blue_rgb = (0.09, 0.47, 0.72)
    size_fig = (10, 6.5)
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
    if mode == 1:  ##keystub_distance

        stable_zchipnew = np.loadtxt('./data/stable_zchipnew.txt')
        stable_zvna = np.loadtxt('./data/stable_zvna.txt')
        movement1_zchipnew = np.loadtxt('./data/movement1_zchipnew.txt')
        movement1_zvna = np.loadtxt('./data/movement1_zvna.txt')

        stable_zchipnew_real, stable_zchipnew_imag = stable_zchipnew[:, 0], stable_zchipnew[:, 1]
        movement1_zchipnew_real, movement1_zchipnew_imag = movement1_zchipnew[:, 0], movement1_zchipnew[:, 1]

        stable_zchipnew_abs = np.abs(stable_zchipnew_real + 1j * stable_zchipnew_imag)
        movement1_zchipnew_abs = np.abs(movement1_zchipnew_real + 1j * movement1_zchipnew_imag)

        stable_zvna_real = np.abs(stable_zvna[:, 1])
        movement1_zvna_real = np.abs(movement1_zvna[:, 1])

        stable_zvna_error = np.abs(stable_zchipnew_abs - stable_zvna_real) / 2
        movement1_zvna_error = np.abs(movement1_zchipnew_abs - movement1_zvna_real) / 2

        red_rgb = (1, 0.2118, 0.1569)
        blue_rgb = (0.09, 0.47, 0.72)
        line_width = 2
        font_properties = {'family': 'Times New Roman', 'weight': 'normal', 'size': 30}

        fig, ax1 = plt.subplots(figsize=(5.8, 4))
        # ax1.plot([59, 91.05], [59, 91.05], '--', color='gray', linewidth=1, label='Ground Truth')  # Ground Truth line
        ax1.plot(stable_zvna_real, stable_zchipnew_abs, '-', linewidth=line_width, color=red_rgb,
                 label='Static Multipath')
        ax1.plot(movement1_zvna_real, movement1_zchipnew_abs, '-', linewidth=line_width, color=blue_rgb,
                 label='Dynamic Multipath')

        for x, y, yerr in zip(stable_zvna_real, stable_zchipnew_abs, stable_zvna_error):
            ax1.errorbar(x, y, yerr=yerr, fmt='s', color=red_rgb, linewidth=1.5, markersize=1, alpha=0.7)
            ax1.plot([x - 0.2, x + 0.2], [y + yerr, y + yerr], color=red_rgb, linewidth=1.5)
            ax1.plot([x - 0.2, x + 0.2], [y - yerr, y - yerr], color=red_rgb, linewidth=1.5)

        for x, y, yerr in zip(movement1_zvna_real, movement1_zchipnew_abs, movement1_zvna_error):
            ax1.errorbar(x, y, yerr=yerr, fmt='s', markersize=1, color=blue_rgb, linewidth=1.5, alpha=0.7)
            ax1.plot([x - 0.2, x + 0.2], [y + yerr, y + yerr], color=blue_rgb, linewidth=1.5)
            ax1.plot([x - 0.2, x + 0.2], [y - yerr, y - yerr], color=blue_rgb, linewidth=1.5)
        plt.subplots_adjust(left=0.24, right=0.99, top=0.986, bottom=0.199)
        plt.xlabel('VNA measured impedance(\u03A9)', fontsize=30, fontdict=font_properties)
        plt.ylabel('OhmScan measured \n impedance (\u03A9)', fontsize=30, fontdict=font_properties)
        ax1.xaxis.set_label_coords(0.43, -0.13)
        img = mpimg.imread('./image/Picture1.png')  # 读取图片
        img2 = mpimg.imread('./image/tag22.png')  # 读取图片
        print(len(movement1_zvna_real))
        print(len(stable_zvna_real))
        imagebox = OffsetImage(img, zoom=0.32)  # 设置图片的缩放比例
        imagebox2 = OffsetImage(img2, zoom=0.25)
        # 设置图片的位置 (0, 0) 为图形的左下角，(1, 1) 为右上角
        ab = AnnotationBbox(imagebox, (0.75, 0.32),  # 设置图片的中心位置
                            xycoords='axes fraction',  # 使用坐标轴的比例作为参考坐标
                            frameon=False)  # 是否绘制边框
        ax1.add_artist(ab)
        ab2 = AnnotationBbox(imagebox2, (0.24, 0.71),  # 设置图片的中心位置
                             xycoords='axes fraction',  # 使用坐标轴的比例作为参考坐标
                             frameon=False)  # 是否绘制边框
        ax1.add_artist(ab2)
        ax1.text(80, 74, 'Ex. Ant 1', fontsize=25, color='black', verticalalignment='center',
                 fontname="Times New Roman")
        ax1.text(63, 88, 'Ex. Ant 2', fontsize=25, color='black', verticalalignment='center',
                 fontname="Times New Roman")
        ax1.annotate('',
                     xy=(0.53, 0.5),
                     xytext=(0.75, 0.32),
                     xycoords='axes fraction',
                     textcoords='axes fraction',
                     arrowprops=dict(facecolor='black', arrowstyle='->', linewidth=2),
                     fontsize=26, color='black', ha='center', va='center', fontname="Times New Roman",
                     bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0'))
        ax1.annotate('',
                     xy=(0.1, 0.1),
                     xytext=(0.25, 0.68),
                     xycoords='axes fraction',
                     textcoords='axes fraction',
                     arrowprops=dict(facecolor='black', arrowstyle='->', linewidth=2),
                     fontsize=26, color='black', ha='center', va='center', fontname="Times New Roman",
                     bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0'))

        plt.xlim([58, 92.05])
        plt.ylim([58, 93.05])

        for spine in ax1.spines.values():
            spine.set_linewidth(1.5)
        for label in ax1.get_xticklabels() + ax1.get_yticklabels():
            label.set_fontproperties(font_properties)

        ax1.xaxis.set_major_locator(MultipleLocator(10))
        ax1.xaxis.set_minor_locator(MultipleLocator(2))
        ax1.yaxis.set_major_locator(MultipleLocator(10))
        ax1.yaxis.set_minor_locator(MultipleLocator(2))

        ax1.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='-', linewidth=0.75, alpha=0.6)
        ax1.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)
        # 设置图例
        legend_properties = FontProperties(family='Times New Roman', weight='normal', size=25)
        ax1.legend(prop=legend_properties, loc=(0.25, -0.03), frameon=False,
                   handlelength=0.7, labelspacing=0.1, handletextpad=0.2)  # bbox_to_anchor=(0.23,0.385)
        # ax1.legend(prop=legend_properties, loc = 'upper left', bbox_to_anchor=(-0.025,1.02))
        plt.gca().tick_params(axis='both', which='major', labelsize=30)

        # ax1.imshow(img, extent=[1, 3, 1, 3], aspect='auto', alpha=0.6)

        # 加粗边框
        for spine in ax1.spines.values():
            spine.set_linewidth(2)

        plt.savefig('sec3_fig13_a.pdf', format='pdf')
        plt.show()
    elif mode ==2:
        font = 25
        labefont = 24
        rate_5G = []
        rate_5G_min = []
        rate_wifi = []
        rate_wifi_min = []
        stall_5G_rate=[]
        stall_wifi_rate = []
        data1 = 2  # 对应第几列的数据？
        data2 = 6
        font = 30
        labefont = 30
        red_rgb = (1, 0.2118, 0.1569)
        blue_rgb = (0.09, 0.47, 0.72)
        fig_size = (8,6)
        # linestyles = ['-', '--', '-.', ':']
        linelengths=2.5
        xdata,ydata = np.loadtxt('./data/stable_cdf.txt', unpack=True)
        x_mobe,y_move = np.loadtxt('./data/move_cdf.txt', unpack=True)
        fig, ax = plt.subplots(figsize=(5.4,3.9))#(5.8, 4)

        ax.plot(xdata,ydata,  label="Static Multipath", linewidth=linelengths, color=red_rgb,
                    linestyle=linestyles[0])
        ax.plot(x_mobe,y_move, label="Dynamic Multipath", linewidth=linelengths, color=blue_rgb,
                          linestyle=linestyles[0])
        # sns.kdeplot(rate_wifi, cumulative=True, label=" WiFi", linewidth=linelengths, color=color_7,
        #             linestyle=linestyles[2], ax=ax)
        ax.set(xlim=(0, 2))
        ax.set(ylim=(0, 1))
        ax.legend(loc=(0.2,-0.03),frameon=False, fontsize=font-4, ncol=1,
                  # handlelength=1, handletextpad=0.3, borderpad=0.3,
                  handlelength=0.7,labelspacing=0.1,handletextpad=0.2)
        ax.grid(True)
        ax.xaxis.set_major_locator(MultipleLocator(0.5))
        ax.xaxis.set_minor_locator(MultipleLocator(0.1))
        ax.yaxis.set_major_locator(MultipleLocator(0.2))
        ax.yaxis.set_minor_locator(MultipleLocator(0.05))
        plt.subplots_adjust(left=0.19, right=0.982, top=0.99, bottom=0.207)
        ax.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='-', linewidth=0.75, alpha=0.6)
        ax.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)
        # ax.set_xscale('log')
        ax.set_xlabel('Impedance error (\u03A9)', fontsize=font+2, fontname="Times New Roman")
        ax.set_ylabel('CDF', fontsize=font+2, fontname="Times New Roman")
        ax.tick_params(labelsize=labefont, labelcolor="black", length=6, width=1,
                       direction="in")  # , labelfontfamily="Times New Roman")
        # ax.plot([1, 1.69], [0.5, 0.5], 'r*', markersize=35)
        # # ax.plot(1.69,0.5, 'r*', markersize=35)0.122366	0.500000 move0.118166	0.500000
        # ax.text(0.8, 0.6, '0.44', fontsize=font, color='red', verticalalignment='center')
        # ax.annotate('★*', xy=(0.44, 0.5), xytext=(0.44, 0.5),color='red',markersize=35)
                    ##arrowprops=dict(arrowstyle="wedge,tail_width=0.7", color='red', lw=2))
        # ax.annotate('★', xy=(0.44, 0.5), xytext=(0.44, 0.5),
        #             textcoords='data', ha='center', fontsize=35, color='red', weight='bold')
        # ax.plot([0, 15], [0.5, 0.5], '--', color='black', linewidth=linelengths-1)
        ax.text(1.05, 0.72, 'Median', fontsize=font, color='black', verticalalignment='center',fontname = 'Arial')
        ax.plot([1, 1.7], [0.8, 0.8], color='gray', linewidth=linelengths - 0.5)
        ax.plot([1, 1.7], [0.65, 0.65], color='gray', linewidth=linelengths - 0.5)
        ax.plot([1.05, 1.2], [0.57, 0.57], color=red_rgb, linewidth=linelengths)
        ax.plot([1.05, 1.2], [0.45, 0.45], color=blue_rgb, linewidth=linelengths)
        ax.plot([1, 1.7], [0.4, 0.4], color='gray', linewidth=linelengths - 0.5)
        ax.text(1.28, 0.57, '0.118', fontsize=font, color='black', verticalalignment='center')  # ,
        # bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.9))
        ax.text(1.28, 0.45, '0.122', fontsize=font, color='black', verticalalignment='center')  # ,
        plt.xticks([0, 0.5, 1, 1.5, 2], ['0', '0.5', '1', '1.5', '2'])
        plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1], ['0 ', '0.2', '0.4', '0.6', '0.8', ' '])
        ax.text(-0.2, 0.95, '1', fontsize=font, color='black', verticalalignment='center')  # ,
        ax.spines['top'].set_linewidth(2)  # 上边框
        ax.spines['right'].set_linewidth(2)  # 右边框
        ax.spines['bottom'].set_linewidth(2)  # 下边框
        ax.spines['left'].set_linewidth(2)  # 左边框
        ax.xaxis.set_label_coords(0.5, -0.13)
        plt.savefig('sec3_fig13_b.pdf', format='pdf')
        plt.show()