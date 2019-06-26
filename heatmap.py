import numpy
import matplotlib.pyplot as plt


def plot_heatmap(mma, target_labels, source_labels):
    # set figure layout and heatmap color
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.pcolor(mma, cmap=plt.cm.Blues)

    # put the major ticks at the middle of each cell
    ax.set_xticks(numpy.arange(mma.shape[1]) + 0.5, minor=False)
    ax.set_yticks(numpy.arange(mma.shape[0]) + 0.5, minor=False)

    ax.set_xlim(0, int(mma.shape[1]))
    ax.set_ylim(0, int(mma.shape[0]))

    # want a more natural, table-like display
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    # source words -> column labels
    ax.set_xticklabels(source_labels, minor=False, fontsize=10)
    # target words -> row labels
    ax.set_yticklabels(target_labels, minor=False, fontsize=10)

    # set the rotation angle of the xticks
    plt.xticks(rotation=90)

    # save and show the figure
    fig.savefig('heatmap.pdf', bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    # labels for x and y axis
    # column labels -> target words
    # row labels -> source words
    source_labels = ['on', 'the', 'topic', 'of', 'noises', 'i', 'was', 'at', 'the', 'nadal', 'tomic', 'game', 'last',
                     'night', 'and', 'i', 'loved', 'how', 'quiet', 'tomic', 'was', 'compared', 'to', 'nadal', 'he',
                     'seems', 'to', 'have', 'a', 'shitload', 'of', 'talent', 'and', 'the', 'postmatch', 'press', 'conf',
                     'he', 'showed', 'a', 'lot', 'of', 'maturity', 'and', 'he', 'seems', 'nice', 'tomic', 'has', 'a',
                     'fantastic', 'tennis', 'brain']
    target_labels = ['this', 'azarenka', 'woman', 'needs', 'a', 'talking', 'to', 'from', 'the', 'umpire', 'her',
                     'weird', 'noises', 'are', 'totes', 'inappropes', 'professionally']

    # truncate the label range for simplicity
    source_labels1 = source_labels[:source_labels.index('he')]
    source_labels2 = source_labels[source_labels.index('nice') + 1:]
    new_source_labels = source_labels1 + source_labels2

    # select the data according to the truncated range
    mma = numpy.genfromtxt('bi_attn.csv', delimiter=',')
    new_mma1 = mma[:, :source_labels.index('he')]
    new_mma2 = mma[:, source_labels.index('nice') + 1:]
    new_mma = numpy.concatenate([new_mma1, new_mma2], axis=1)

    plot_heatmap(new_mma, target_labels, new_source_labels)
