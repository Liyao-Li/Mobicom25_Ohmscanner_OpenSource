import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator
#plt.style.use('seaborn-whitegrid')
# load data
font = 30
lasize = 30
linewides = 2
plt.rcParams['font.family'] = 'Times New Roman'

font_properties = FontProperties(family='Times New Roman', weight='normal', size=font)
colors = [np.array([255, 46, 41]) / 255, np.array([0, 114, 189]) / 255,
          np.array([237, 177, 32]) / 255, np.array([119, 172, 48]) / 255,
          np.array([136, 137, 139]) / 255, np.array([100, 100, 100]) / 255]

file_path = './data/0904/OCRSS.txt'
# file_path = './Fig7-OCRSS_power/OCRSS.txt'
power = []
SCdata = []
Var_data = []
with open(file_path, 'r') as file:
    for line in file:
        values = line.strip().split()
        power.append(values[0])
        SCdata.append(values[1])
        Var_data.append(values[2])
power2,SCdata2,SCerror2 = np.loadtxt('./data/0904/1.txt', unpack=True)
power3,SCdata3,SCerror3 = np.loadtxt('./data/0904/2.txt', unpack=True)
power4,SCdata4,SCerror4 = np.loadtxt('./data/0904/3.txt', unpack=True)

power = [float(i) for i in power]
SCdata = [int(float(i)) for i in SCdata]
Var_data = [int(float(i)) for i in Var_data]
red_rgb = (1, 0.2118, 0.1569)
blue_rgb = (0.09, 0.47, 0.72)
linewide = 2
fig = plt.figure(figsize=(5.3, 3.7))
ax1 = fig.add_subplot(111)
SCdata = np.array(SCdata)
Var_data = np.array(Var_data)

ax1.plot(power[0:len(power)-1], SCdata[0:len(power)-1],'s-', linewidth = linewides,color = red_rgb,markersize=4,label = 'Ant.1')
ax1.fill_between(power[0:len(power)-1],SCdata[0:len(power)-1] - Var_data[0:len(power)-1], SCdata[0:len(power)-1] + Var_data[0:len(power)-1], color = red_rgb,alpha = 0.2)

SCdata2 = SCdata2+20
SCdata4 = SCdata4-30
SCdata3 = np.array(SCdata3)-40

ax1.plot(power2, SCdata2,'o-', linewidth = linewides,color = colors[1],markersize=4,label = 'Ant.2')
ax1.fill_between(power2,SCdata2 - SCerror2, SCdata2 +SCerror2, color = colors[1],alpha = 0.2)
ax1.plot(power3, SCdata3,'o-', linewidth = linewides,color = colors[2],markersize=4,label = 'Ant.3')
ax1.fill_between(power3,SCdata3 - SCerror3, SCdata3 +SCerror3, color = colors[2],alpha = 0.2)
ax1.plot(power4, SCdata4,'o-', linewidth = linewides,color = colors[3],markersize=4,label = 'Ant.4')
ax1.fill_between(power4,SCdata4 - SCerror4, SCdata4 +SCerror4, color = colors[3],alpha = 0.2)

ax1.set_xlabel('OC-RSS', fontsize=font, fontweight='normal', fontname='Times New Roman', color='black')
ax1.set_ylabel('Register Value', fontsize=font, fontweight='normal', fontname='Times New Roman', color='black')
ax1.tick_params(axis='y', labelcolor='black', labelsize=lasize)


ax1.set_ylim(40,180)
# ax1.set_xlim(10,31.5)
for label in ax1.get_xticklabels() + ax1.get_yticklabels():
    label.set_fontproperties(font_properties)
ax1.xaxis.set_major_locator(MultipleLocator(5))
ax1.xaxis.set_minor_locator(MultipleLocator(0.5))
ax1.yaxis.set_major_locator(MultipleLocator(50))
ax1.yaxis.set_minor_locator(MultipleLocator(10))

ax1.grid(which = "major", color=(0.6,0.6,0.6), linestyle='-', linewidth=1.5, alpha=0.6)
ax1.grid(which = "minor", color=(0.6, 0.6, 0.6), linestyle='--', linewidth=0.75, alpha=0.3)

fig.tight_layout()
fig.subplots_adjust(left=0.22, right=0.99, top=0.99, bottom=0.236)
ax1.spines['top'].set_linewidth(2)    # 上边框
ax1.spines['right'].set_linewidth(2)  # 右边框
ax1.spines['bottom'].set_linewidth(2) # 下边框
ax1.spines['left'].set_linewidth(2)   # 左边框
# plt.subplots_adjust(right=0.93)
ax1.legend(loc=(0, 0), ncol=2, handlelength=0.8, frameon=False,handletextpad=0.1,
           fontsize=font-3, columnspacing=0.3)

ax1.xaxis.set_label_coords(0.5, -0.175)
plt.savefig('sec3_fig12.pdf',format = 'pdf')
plt.show()