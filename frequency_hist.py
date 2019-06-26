import numpy as np
import matplotlib.pyplot as plt

# set the figure layout
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3))

# xticks & bar patterns
freq = ['<10', '10~50', '50~100', '>100']
patterns = ["/", "\\", "-", "x", "o", "+", "|", "o", "O", ".", "*"]

# x range & set width for each bar
x = np.arange(len(freq))
width = 0.2

# plot twitter subfigure
tw_data = [[0.2, 2.28, 7.36, 25.44],
           [0, 0.27, 0.46, 26.78],
           [0.4, 3.22, 9.9, 26.98],
           [0.4, 4.03, 14.04, 30.18]]

ax1.bar(x, tw_data[0], width, alpha=0.7, label="CLASSIFIER (only post)", hatch=patterns[0])
ax1.bar(x + width, tw_data[1], width, alpha=0.7, label='CLASSIFIER (post+conv)', hatch=patterns[1])
ax1.bar(x + 2 * width, tw_data[2], width, alpha=0.7, label='SEQ2SEQ', hatch=patterns[2])
ax1.bar(x + 3 * width, tw_data[3], width, alpha=0.7, label='Our full model', hatch=patterns[3])

ax1.set_xticks(x + 1.5 * width)
ax1.set_xticklabels(freq)
ax1.set_ylabel('F1 score (%)')

# plot weibo subfigure
wb_data = [[1.31, 10.64, 22.85, 42.48],
           [0.41, 6.35, 19.95, 53.2],
           [5.9, 25.05, 34.27, 48.2],
           [5.99, 29.05, 45.05, 56.01]]

ax2.bar(x, wb_data[0], width, alpha=0.7, label="CLASSIFIER (only post)", hatch=patterns[0])
ax2.bar(x + width, wb_data[1], width, alpha=0.7, label='CLASSIFIER (post+conv)', hatch=patterns[1])
ax2.bar(x + 2 * width, wb_data[2], width, alpha=0.7, label='SEQ2SEQ', hatch=patterns[2])
ax2.bar(x + 3 * width, wb_data[3], width, alpha=0.7, label='Our full model', hatch=patterns[3])

ax2.set_xticks(x + 1.5 * width)
ax2.set_xticklabels(freq)

# set legends in the top
handles, labels = ax1.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.02),
           ncol=4, prop={'size': 8})

# show and save the figure
plt.tight_layout()
plt.show()
fig.savefig("frequency_hist.pdf", bbox_inches='tight')
