import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator
from matplotlib.lines import Line2D

# 设置调色板和字体
palette = pyplot.get_cmap('Set1')
font_size = 30
font_properties = FontProperties(family='Times New Roman', weight='normal', size=font_size)

# 定义颜色
red_rgb = (1, 0.2118, 0.1569)
blue_rgb = (0.09, 0.47, 0.72)
color_1 = np.array([0, 114, 189])/255
color_2 = np.array([217, 83, 25])/255
color_3 = np.array([237, 177, 32])/255
color_4 = np.array([77, 190, 238])/255
color_5 = np.array([119, 172, 48])/255
color_6 = np.array([126, 47, 142])/255
color_7 = np.array([255, 0, 0])/255

marsize = 28
line_width = 2

# 读取数据
power, chipimp = np.loadtxt('./data/chip_impedance.txt', unpack=True)
power2, antimp = np.loadtxt('./data/antenna_impedance.txt', unpack=True)

# 创建图表
fig, ax1 = plt.subplots(figsize=(5.3, 3.7))

# 绘制线和散点，并生成自定义图例
ax1.plot(power+1, chipimp, color=blue_rgb, linewidth=line_width)
ax1.scatter(power+1, chipimp, s=marsize, color=blue_rgb, marker='o')
ax1.plot(power2, antimp, color=red_rgb, linewidth=line_width)
ax1.scatter(power2, antimp, s=marsize+5, color=red_rgb, marker='s')

# 创建自定义图例
custom_legend = [
    Line2D([0], [0], color=red_rgb, lw=line_width, marker='s', markersize=8, label='Antenna'),
    Line2D([0], [0], color=blue_rgb, lw=line_width, marker='o', markersize=8, label='Chip')
]

# 设置图例
legend_properties = FontProperties(family='Times New Roman', weight='normal', size=font_size-2)
ax1.legend(handles=custom_legend, frameon=False,handlelength=1,
           prop=legend_properties, loc = (0.05,0.63),
           handletextpad=0.2, borderpad=0.1)

# 设置轴范围
ax1.set_ylim(71.6, 78.4)
ax1.set_xlim(-30, 0)

# 生成网格
ax1.grid(True, which='both', linestyle='-', color='gray', linewidth=1, alpha=0.5)
fig.tight_layout()

# 加粗边框
for spine in ax1.spines.values():
    spine.set_linewidth(1.5)

# 设置刻度标签字体
for label in ax1.get_xticklabels() + ax1.get_yticklabels():
    label.set_fontproperties(font_properties)

# 设置次要和主要刻度
ax1.xaxis.set_major_locator(MultipleLocator(10))
ax1.xaxis.set_minor_locator(MultipleLocator(1))
ax1.yaxis.set_major_locator(MultipleLocator(2))
ax1.yaxis.set_minor_locator(MultipleLocator(0.25))

# 设置网格样式
ax1.grid(which="major", color=(0.6, 0.6, 0.6), linestyle='-', linewidth=1, alpha=0.6)
ax1.grid(which="minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)
# ax1.legend(ncol=2, handletextpad=0.3, borderpad=0.1)

# 调整图表布局
fig.subplots_adjust(left=0.17, right=0.982, top=0.994, bottom=0.223)

# 设置轴标签
ax1.set_xlabel('Input power (dBm)', fontproperties=font_properties, color='black', size = font_size+2)
ax1.set_ylabel('Impedance (\u03A9)', fontproperties=font_properties, color='black')
# ax1.xaxis.set_label_coords(0.45, -0.18)
ax1.tick_params(labelsize=font_size, labelcolor="black", length=6, width=1,
                       direction="in")
ax1.spines['top'].set_linewidth(2)    # 上边框
ax1.spines['right'].set_linewidth(2)  # 右边框
ax1.spines['bottom'].set_linewidth(2) # 下边框
ax1.spines['left'].set_linewidth(2)   # 左边框
ax1.xaxis.set_label_coords(0.5, -0.145)
# 保存并显示图表
plt.savefig('sec3_fig11.pdf', format='pdf')
plt.show()
