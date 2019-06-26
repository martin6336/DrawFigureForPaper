import numpy
import matplotlib.pyplot as plt


def plot_heatmap(mma1, mma2, target_labels, source_labels):
    # set the figure layout and heatmap colors
    fig = plt.figure(figsize=(3.5, 2.4))
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)
    ax1.pcolor(mma1, cmap=plt.cm.Reds)
    ax2.pcolor(mma2, cmap=plt.cm.Reds)

    # put the major ticks at the middle of each cell
    ax1.set_xticks(numpy.arange(mma1.shape[1]) + 0.5, minor=False)
    ax1.set_yticks(numpy.arange(mma1.shape[0]) + 0.5, minor=False)

    ax1.set_xlim(0, int(mma1.shape[1]))
    ax1.set_ylim(0, int(mma1.shape[0]))

    # source words -> column labels
    ax1.set_xticklabels(source_labels, rotation=45, minor=False, fontsize=7)
    # target words -> row labels
    ax1.set_yticklabels(target_labels, minor=False, fontsize=7)

    ax1.invert_yaxis()
    ax1.xaxis.tick_top()
    ax1.yaxis.tick_right()
    ax1.set_ylabel('(a) Seq2Seq-Copy', fontsize=6)

    # put the major ticks at the middle of each cell
    ax2.set_xticks(numpy.arange(mma2.shape[1]) + 0.5, minor=False)
    ax2.set_yticks(numpy.arange(mma2.shape[0]) + 0.5, minor=False)

    ax2.set_xlim(0, int(mma2.shape[1]))
    ax2.set_ylim(0, int(mma2.shape[0]))

    # set y ticklabels and make x-axis invisible
    ax2.set_yticklabels(target_labels, minor=False, fontsize=7)
    ax2.get_xaxis().set_visible(False)

    ax2.invert_yaxis()
    ax2.yaxis.tick_right()
    ax2.set_ylabel('(b) Our Model', fontsize=6)

    # save and show the figure
    fig.savefig('double_heatmap.pdf', bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    # labels for x and y axis
    # column labels -> target words
    # row labels -> source words
    source_labels = ['wife', 'paying', 'attention', 'game', 'want', 'team', 'yellow', 'pants', 'win']
    target_labels = ['super', 'bowl']

    # the weights (in numpy type) for each grid
    weights_1 = [[0.03, 0.15, 0.19, 0.11, 0.03, 0.62, 0.03, 0.05, 0.16],
                 [0.01, 0.05, 0.15, 0.12, 0.09, 0.41, 0.07, 0.09, 0.03]]
    new_mma_1 = numpy.array(weights_1)

    weights_2 = [[0.03, 0.05, 0.08, 0.17, 0.003, 0.42, 0.25, 0.05, 0.10],
                 [0.02, 0.07, 0.09, 0.11, 0.09, 0.31, 0.18, 0.27, 0.13]]
    new_mma_2 = numpy.array(weights_2)

    # plot the heat map with the weight and labels
    plot_heatmap(new_mma_1, new_mma_2, target_labels, source_labels)
