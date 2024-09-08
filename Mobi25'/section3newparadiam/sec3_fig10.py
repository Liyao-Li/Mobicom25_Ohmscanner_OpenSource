import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.lines import Line2D
# plt.style.use('seaborn-whitegrid')
import matplotlib as mpl
mpl.rcParams['font.family'] = 'Times New Roman'
palette = pyplot.get_cmap('Set1')
# font1 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 30}
font_size = 32
font_properties = FontProperties(family='Times New Roman', weight='normal', size=font_size)

red_rgb = (1, 0.2118, 0.1569)
blue_rgb = (0.09, 0.47, 0.72)
color_1 = np.array([0, 114, 189])/255
color_2 = np.array([217, 83, 25])/255
color_3 = np.array([237, 177, 32])/255
color_4 = np.array([77, 190, 238])/255
color_5 = np.array([119, 172, 48])/255
color_6 = np.array([126, 47, 142])/255
color_7 = np.array([255, 0, 0])/255
linestyles = ['-', '--', '-.', ':']
colors = [np.array([0, 114, 189])/255,np.array([217, 83, 25])/255,np.array([119, 172, 48])/255,
          np.array([77, 190, 238])/255,np.array([237, 177, 32])/255,np.array([126, 47, 142])/255,
          np.array([255, 0, 0])/255]

marsize = 5
line_width = 1

power, SCdata, Var_data = np.loadtxt('./data/Tag1.txt', unpack=True)#np.random.rand(20) * 2 * np.pi  # 角度
power2, SCdata2, Var_data2 = np.loadtxt('./data/Tag2.txt', unpack=True)
power3, SCdata3, Var_data3 = np.loadtxt('./data/Tag3.txt', unpack=True)
power4, SCdata4, Var_data4 = np.loadtxt('./data/Tag4.txt', unpack=True)
power5, SCdata5, Var_data5 = np.loadtxt('./data/Tag5.txt', unpack=True)
power6, SCdata6, Var_data6 = np.loadtxt('./data/Tag6.txt', unpack=True)
power7, SCdata7, Var_data7 = np.loadtxt('./data/Wisp.txt', unpack=True)
linewides = 2
marks = 5
fig, ax1 = plt.subplots(figsize=(5.5, 3.85))
# line = ax1.plot(power, SCdata, color=color_1, linewidth=line_width)
# scatter = ax1.scatter(power, SCdata, s=marsize, color =color_1, marker = 'o')
# fill = ax1.fill_between(power, SCdata - Var_data, SCdata + Var_data, color=color_1, alpha=0.3,edgecolor='none')
ax1.plot(power5, SCdata5, 'p', color=colors[4], linestyle=linestyles[0], linewidth=linewides, markersize=marks,
        label=' ')
ax1.fill_between(power5, SCdata5 - Var_data5, SCdata5 + Var_data5,
                color=colors[4], alpha=0.2,edgecolor='none')
ax1.plot(power6, SCdata6, '*', color=colors[5], linestyle=linestyles[1], linewidth=linewides, markersize=marks,
        label=' ')
ax1.fill_between(power6, SCdata6 - Var_data6, SCdata6 + Var_data6,
                color=colors[5], alpha=0.2,edgecolor='none')
ax1.plot(power7, SCdata7, 'o', color=colors[6], linestyle=linestyles[0], linewidth=linewides, markersize=marks,
        label=' ')
ax1.fill_between(power7, SCdata7 - Var_data7, SCdata7 + Var_data7,
                color=colors[6], alpha=0.2,edgecolor='none')

ax1.plot(power2, SCdata2, '^', color=colors[1], linestyle=linestyles[1], linewidth=linewides, markersize=marks,
        label=' ')
ax1.fill_between(power2, SCdata2 - Var_data2, SCdata2 + Var_data2,
                color=colors[1], alpha=0.2,edgecolor='none')
ax1.plot(power, SCdata, 'o', color=colors[0], linestyle=linestyles[0], linewidth=linewides, markersize=marks,
        label=' ')
ax1.fill_between(power, SCdata - Var_data, SCdata + Var_data,
                color=colors[0], alpha=0.2,edgecolor='none')
ax1.plot(power4, SCdata4, 'o', color=colors[3], linestyle=linestyles[3], linewidth=linewides, markersize=marks,
        label=' ')
ax1.fill_between(power4, SCdata4 - Var_data4, SCdata4 + Var_data4,
                color=colors[3], alpha=0.2,edgecolor='none')
ax1.plot(power3, SCdata3, 'v', color=colors[2], linestyle=linestyles[2], linewidth=linewides, markersize=marks,
        label=' ')
ax1.fill_between(power3, SCdata3 - Var_data3, SCdata3 + Var_data3,
                color=colors[2], alpha=0.2,edgecolor='none')

# ax1.set_ylim(0, 1.5)
ax1.set_ylim(0, 1.1)
ax1.set_xlim(14,31)
# ax1.set_yticks([int(0), 0.5, 1, 1.5])
# generate grid
ax1.grid(True, which='both', linestyle='-', color='gray', linewidth=1, alpha=0.5)
fig.tight_layout()

for spine in ax1.spines.values():
    spine.set_linewidth(1.5)
for label in ax1.get_xticklabels() + ax1.get_yticklabels():
    label.set_fontproperties(font_properties)
#minigrid
ax1.xaxis.set_major_locator(MultipleLocator(5))
ax1.xaxis.set_minor_locator(MultipleLocator(1))
ax1.yaxis.set_major_locator(MultipleLocator(0.5))
ax1.yaxis.set_minor_locator(MultipleLocator(0.05))

ax1.grid(which = "major", color=(0.6,0.6,0.6), linestyle='-', linewidth=1, alpha=0.6)
ax1.grid(which = "minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)

# fig.tight_layout()
# ax1.legend(loc=(1.01, -0.06),frameon=False, fontsize=10, ncol=1,handlelength=2, handletextpad=0.2, borderpad=0.1, columnspacing=7,handleheight =4)
ax1.legend(loc=(0.02, 0.67),frameon=False, fontsize=10, ncol=3,
           handlelength=2, handletextpad=0.2, borderpad=0.1, columnspacing=8.6,handleheight =2.5)

ax1.set_yticks([0, 0.5, 1], ['0 ', '', '1 '])
fig.subplots_adjust(left=0.133, right=0.994, top=0.992, bottom=0.235)
ax1.set_xlabel('Reader sending power (dBm)', fontproperties=font_properties, color='black')
ax1.set_ylabel('Phase (rad)', fontproperties=font_properties, color='black')
ax1.yaxis.set_label_coords(-0.07, 0.5)
ax1.xaxis.set_label_coords(0.45, -0.17)

###add giu
img = mpimg.imread('./image/1.png')
imagebox = OffsetImage(img, zoom=0.53)  # 设置图片的缩放比例
# 设置图片的位置 (0, 0) 为图形的左下角，(1, 1) 为右上角
ab = AnnotationBbox(imagebox, (0.217, 0.94),  # 设置图片的中心位置
        xycoords='axes fraction',  # 使用坐标轴的比例作为参考坐标
        frameon=False)  # 是否绘制边框
ax1.add_artist(ab)

img2 = mpimg.imread('./image/2.png')
imagebox2 = OffsetImage(img2, zoom=0.55)  # 设置图片的缩放比例
# 设置图片的位置 (0, 0) 为图形的左下角，(1, 1) 为右上角
ab2 = AnnotationBbox(imagebox2, (0.217, 0.84),  # 设置图片的中心位置
        xycoords='axes fraction',  # 使用坐标轴的比例作为参考坐标
        frameon=False)  # 是否绘制边框
ax1.add_artist(ab2)

img3 = mpimg.imread('./image/3.png')
imagebox3 = OffsetImage(img3, zoom=0.55)  # 设置图片的缩放比例
# 设置图片的位置 (0, 0) 为图形的左下角，(1, 1) 为右上角
ab3 = AnnotationBbox(imagebox3, (0.53, 0.94),  # 设置图片的中心位置
        xycoords='axes fraction',  # 使用坐标轴的比例作为参考坐标
        frameon=False)  # 是否绘制边框
ax1.add_artist(ab3)

img4 = mpimg.imread('./image/4.png')
imagebox4 = OffsetImage(img4, zoom=0.55)  # 设置图片的缩放比例
# 设置图片的位置 (0, 0) 为图形的左下角，(1, 1) 为右上角
ab4 = AnnotationBbox(imagebox4, (0.53, 0.84),  # 设置图片的中心位置
        xycoords='axes fraction',  # 使用坐标轴的比例作为参考坐标
        frameon=False)  # 是否绘制边框
ax1.add_artist(ab4)

img5 = mpimg.imread('./image/5.png')
imagebox5 = OffsetImage(img5, zoom=0.55)  # 设置图片的缩放比例
# 设置图片的位置 (0, 0) 为图形的左下角，(1, 1) 为右上角
ab5 = AnnotationBbox(imagebox5, (0.84, 0.94),  # 设置图片的中心位置
        xycoords='axes fraction',  # 使用坐标轴的比例作为参考坐标
        frameon=False)  # 是否绘制边框
ax1.add_artist(ab5)

img6 = mpimg.imread('./image/6.png')
imagebox6 = OffsetImage(img6, zoom=0.52)  # 设置图片的缩放比例
# 设置图片的位置 (0, 0) 为图形的左下角，(1, 1) 为右上角
ab6 = AnnotationBbox(imagebox6, (0.86, 0.84),  # 设置图片的中心位置
        xycoords='axes fraction',  # 使用坐标轴的比例作为参考坐标
        frameon=False)  # 是否绘制边框
ax1.add_artist(ab6)
ax1.text(15.8, 0.8, 'WISP', fontsize=font_size-2, color='black',
                verticalalignment='center')
ax1.spines['top'].set_linewidth(2)  # 上边框
ax1.spines['right'].set_linewidth(2)  # 右边框
ax1.spines['bottom'].set_linewidth(2)  # 下边框
ax1.spines['left'].set_linewidth(2)  # 左边框
plt.savefig('sec3_fig10.pdf',format = 'pdf')
plt.show()