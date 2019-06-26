import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['ps.useafm'] = True
matplotlib.rcParams['pdf.use14corefonts'] = True

f = plt.figure()

# plot present F1@1 measure
plt.subplot(2, 1, 1)
# set width of bar
barWidth = 0.1
# set height of bar

# Present F1@1 Measure
bars_SeqTag = [82.98, 67.91, 41.37]
error_SeqTag = [1.0, 1, 2]

bars_RNN = [75.42, 71.42, 44.34]
error_RNN = [1, 3.4, 0.6]

bars_CopyRNN = [84.68, 82.12, 53.18]
error_CopyRNN = [1.8, 0.5, 0.5]

bars_CorrRNN = [84.69, 82.28, 52.71]
error_CorrRNN = [0.5, 0.2, 0.1]

bars_TAKG = [84.90, 83.05, 54.33]
error_TAKG = [0.04, 0.3, 0.3]

bars_TG_Net = [52.55]
error_TG_Net = [0.3]

# Set position of bar on X axis
r1 = [0.1 + i * 0.7 for i in range(len(bars_CorrRNN))]
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]
r6 = [r5[-1]]
r5[-1] = r6[0] + barWidth

# Make the plot chartreuse
plt.rcParams['errorbar.capsize'] = 3
plt.bar(r1, bars_SeqTag, yerr=error_SeqTag, ecolor='black', color='pink', width=barWidth, edgecolor='white',
        label='Seq-Tag')
plt.bar(r2, bars_RNN, yerr=error_RNN, ecolor='black', color='silver', width=barWidth, edgecolor='white',
        label='Seq2Seq')
plt.bar(r3, bars_CopyRNN, yerr=error_CopyRNN, ecolor='black', color='c', width=barWidth, edgecolor='white',
        label='Seq2Seq-Copy')
plt.bar(r4, bars_CorrRNN, yerr=error_CorrRNN, ecolor='black', color='gray', width=barWidth, edgecolor='white',
        label='Seq2Seq-Corr')
plt.bar(r6, bars_TG_Net, yerr=error_TG_Net, ecolor='black', color='g', width=barWidth, edgecolor='white',
        label='TG-Net')
plt.bar(r5, bars_TAKG, yerr=error_TAKG, ecolor='black', color='y', width=barWidth, edgecolor='white', label='Our model')

# Set the visible range of y
plt.ylim(bottom=35, top=90)

# Add xticks on the middle of the group bars
plt.xticks([r + 2 * barWidth for r in r1], ['Twitter', 'Weibo', 'StackExchange'])

# Create legend & set grid, label
plt.legend(loc='upper right', fontsize='x-small')
plt.grid(axis='y', linestyle='dotted')
plt.ylabel('(a) Present F1@1 (%)')

# Plot absent Recall@5
plt.subplot(2, 1, 2)
# set width of bar
barWidth = 0.1
# set height of bar

# Absent R@5 Measure
bars_RNN = [42.38, 36.6, 28.21]
error_RNN = [0.4, 1.1, 0.1]

bars_CopyRNN = [39.57, 34.86, 27.07]
error_CopyRNN = [1.3, 0.3, 0.3]

bars_CorrRNN = [38.08, 34.15, 25.60]
error_CorrRNN = [0.6, 0.9, 0.3]

bars_TAKG = [42.17, 39.53, 30.85]
error_TAKG = [0.2, 0.3, 0.5]

bars_TG_Net = [28.01]
error_TG_Net = [0.6]

# Set position of bar on X axis
r1 = [0.1 + i * 0.7 for i in range(len(bars_CorrRNN))]
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [r4[-1]]
r4[-1] = r5[0] + barWidth

# Make the plot chartreuse
plt.rcParams['errorbar.capsize'] = 3
plt.bar(r1, bars_RNN, yerr=error_RNN, ecolor='black', color='silver', width=barWidth, edgecolor='white',
        label='Seq2Seq')
plt.bar(r2, bars_CopyRNN, yerr=error_CopyRNN, ecolor='black', color='c', width=barWidth, edgecolor='white',
        label='Seq2Seq-Copy')
plt.bar(r3, bars_CorrRNN, yerr=error_CorrRNN, ecolor='black', color='gray', width=barWidth, edgecolor='white',
        label='Seq2Seq-Corr')
plt.bar(r5, bars_TG_Net, yerr=error_TG_Net, ecolor='black', color='g', width=barWidth, edgecolor='white',
        label='TG-Net')
plt.bar(r4, bars_TAKG, yerr=error_TAKG, ecolor='black', color='y', width=barWidth, edgecolor='white', label='Our model')

# Set the visible range of y
plt.ylim(bottom=20, top=45)
# Add xticks on the middle of the group bars
plt.xticks([r + 1.5 * barWidth for r in r1], ['Twitter', 'Weibo', 'StackExchange'])
# Create legend & set grid, label
plt.legend(loc='upper right', fontsize='x-small')
plt.grid(axis='y', linestyle='dotted')
plt.ylabel('(b) Absent R@5 (%)')

# save to pdf and show the figure
plt.tight_layout()
f.savefig('hist_error_bar.pdf')
plt.show()
