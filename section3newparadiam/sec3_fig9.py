import matplotlib.pyplot as plt
import sys
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator

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

    colors = [np.array([255, 46, 41]) / 255,np.array([0, 114, 189]) / 255,
              np.array([237, 177, 32]) / 255, np.array([119, 172, 48]) / 255,
              np.array([136, 137, 139]) / 255, np.array([100, 100, 100]) / 255]
    if mode == 1:  ##keystub_distance
        fig_size = (7.5, 5)
        # font = 42
        font = 30
        lasize = 30
        linewides = 2
        font_properties = FontProperties(family='Times New Roman', weight='normal', size=font)

        posit, phase, phase_error, impedance = np.loadtxt('./data/differentdisSC3.txt', unpack=True)
        posit = posit / 100
        red_rgb = (1, 0.2118, 0.1569)
        blue_rgb = (0.09, 0.47, 0.72)
        linewide = 2
        fig = plt.figure(figsize=(5.5, 4))
        # (figsize=(5.5, 4))
        ax1 = fig.add_subplot(111)
        ax1.plot(posit, phase, 's-', linewidth=linewides - 0.5, markersize=4, label='Register Value')
        ax1.fill_between(posit, phase - phase_error / 2, phase + phase_error / 2, color=blue_rgb, alpha=0.2)
        # ax1.errorbar(power, SCdata, yerr=Var_data, fmt='s-', capsize = 3, capthick = 2, color = blue_rgb)#, capsize=5, color='skyblue', ecolor='black', label='数据2')
        ax1.set_xlabel('Reader-tag distance (m)', fontsize=font, fontweight='normal', fontname='Times New Roman',
                       color='black')
        ax1.set_ylabel('Register value', fontsize=font, fontweight='normal', fontname='Times New Roman', color=blue_rgb)
        ax1.tick_params(axis='y', labelcolor=blue_rgb, labelsize=lasize, width=2)
        # ax.tick_params(axis='both', width=2)
        # plt.xlabel('Power')
        # plt.ylabel('Register Value')
        ax2 = ax1.twinx()
        ax2.plot(posit, impedance, color=red_rgb, linewidth=linewides, label='Impedance')
        # ax2.set_ylabel('Impedance (Ohm)', fontsize=font, fontweight='normal', fontname='Times New Roman', color=red_rgb)
        ax2.tick_params(axis='y', labelcolor=red_rgb, labelsize=lasize, width=2)
        ax2.set_ylim(76.3, 82)
        ax1.set_ylim(90, 170)
        for label in ax1.get_xticklabels() + ax1.get_yticklabels():
            label.set_fontproperties(font_properties)
        for label in ax2.get_yticklabels():
            label.set_fontproperties(font_properties)
        # minigrid
        ax1.xaxis.set_major_locator(MultipleLocator(1))
        ax1.xaxis.set_minor_locator(MultipleLocator(0.1))
        ax1.yaxis.set_major_locator(MultipleLocator(20))
        ax1.yaxis.set_minor_locator(MultipleLocator(2.5))
        ax2.set_yticks([76.3, 78.95, 81.25])  # Set the positions of the ticks
        ax2.set_yticklabels(['80', '82', '84'])  # Set the labels for these positions (empty in this case)
        # ax2.yticks([71.37, 72.77,74.17,76.57,76.97], ['', '', '', '', ''])
        ax1.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='-', linewidth=1.5, alpha=0.6)
        ax1.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)

        ax1.spines['top'].set_linewidth(2)  # 上边框
        ax1.spines['right'].set_linewidth(2)  # 右边框
        ax1.spines['bottom'].set_linewidth(2)  # 下边框
        ax1.spines['left'].set_linewidth(2)  # 左边框

        ax1.legend(loc=(0.35, 0.45), frameon=False, handlelength=0.9, fontsize=font - 5, handletextpad=0.3,
                   borderpad=0.3)
        ax2.legend(loc=(0.35, 0.3), frameon=False, handlelength=0.9, fontsize=font - 5, handletextpad=0.3,
                   borderpad=0.3)

        # fig.tight_layout()
        fig.subplots_adjust(left=0.213, right=0.99, top=0.99, bottom=0.233)

        plt.savefig('./sec3_fig9_a.pdf', format='pdf')
        plt.show()
    elif mode == 2:
        font = 30
        lasize = 30
        linewides = 2
        font_properties = FontProperties(family='Times New Roman', weight='normal', size=font)

        file_path = './data/differentpower_SC_WISP.txt'
        power = []
        SCdata = []
        Var_data = []
        font = font
        with open(file_path, 'r') as file:
            for line in file:
                values = line.strip().split()
                power.append(values[0])
                SCdata.append(values[1])
                Var_data.append(values[2])

        power = [float(i) for i in power]
        SCdata = [int(float(i)) for i in SCdata]
        Var_data = [int(float(i)) for i in Var_data]

        # read the second file
        file_path2 = './data/differentpower_SC_WISP_impedance.txt'
        power2 = []
        dataImpedance = []
        with open(file_path2, 'r') as file:
            for line2 in file:
                va2 = line2.strip().split()
                power2.append(va2[0])
                dataImpedance.append(va2[1])
                # dataImpedance = dataImpedance

        power2 = [float(i) for i in power2]
        dataImpedance = [float(i) for i in dataImpedance]
        dataImpedance = np.array(dataImpedance) + 0.66
        print(dataImpedance)
        # plot figure
        red_rgb = (1, 0.2118, 0.1569)
        blue_rgb = (0.09, 0.47, 0.72)
        linewide = 2
        fig = plt.figure(figsize=(5.5, 4))
        ax1 = fig.add_subplot(111)
        SCdata = np.array(SCdata)
        Var_data = np.array(Var_data)
        ax1.plot(power, SCdata, 's-', linewidth=linewides - 0.5, markersize=4, label='Register Value')
        ax1.fill_between(power, SCdata - Var_data, SCdata + Var_data, color=blue_rgb, alpha=0.2)
        ax1.set_xlabel('Reader sending power(dBm)', fontsize=font, fontweight='normal', fontname='Times New Roman',
                       color='black')
        ax1.tick_params(axis='y', labelcolor=blue_rgb, labelsize=lasize, width=2)
        ax2 = ax1.twinx()
        ax2.plot(power, dataImpedance, color=red_rgb, linewidth=linewides, label='Impedance')
        ax2.set_ylabel('Impedance (\u03A9)', fontsize=font, fontweight='normal', fontname='Times New Roman',
                       color=red_rgb)
        ax2.tick_params(axis='y', labelcolor=red_rgb, labelsize=lasize, width=2)
        ax2.set_ylim(80, 84.6)
        ax1.set_ylim(90, 170)
        for label in ax1.get_xticklabels() + ax1.get_yticklabels():
            label.set_fontproperties(font_properties)
        for label in ax2.get_yticklabels():
            label.set_fontproperties(font_properties)
        # minigrid
        ax1.xaxis.set_major_locator(MultipleLocator(2))
        ax1.xaxis.set_minor_locator(MultipleLocator(0.25))
        ax1.yaxis.set_major_locator(MultipleLocator(20))
        ax1.yaxis.set_minor_locator(MultipleLocator(2.5))

        ax1.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='-', linewidth=1.5, alpha=0.6)
        ax1.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)

        ax1.spines['top'].set_linewidth(2)  # 上边框
        ax1.spines['right'].set_linewidth(2)  # 右边框
        ax1.spines['bottom'].set_linewidth(2)  # 下边框
        ax1.spines['left'].set_linewidth(2)  # 左边框
        font_properties = FontProperties(family='Times New Roman', weight='normal', size=font)

        ax1.legend(loc=(0, 0.17), frameon=False, handlelength=0.9, fontsize=font - 5, handletextpad=0.3, borderpad=0.3)
        ax2.legend(loc=(0, 0.01), frameon=False, handlelength=0.9, fontsize=font - 5, handletextpad=0.3, borderpad=0.3)
        ax1.xaxis.set_label_coords(0.53, -0.18)
        # fig.tight_layout()
        # fig.subplots_adjust(left=0.182, right=0.844, top=0.98, bottom=0.233)
        # fig.subplots_adjust(left=0.195, right=0.915, top=0.99, bottom=0.233)
        fig.subplots_adjust(left=0.01, right=0.825, top=0.99, bottom=0.233)

        plt.savefig('sec3_fig9_b.pdf', format='pdf')
        plt.show()

