import collections
import pickle
import matplotlib.pyplot as plt


def read_pickle(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)


if __name__ == '__main__':
    # read data statistics from pickle
    tw_pt = read_pickle('tw_seg_data.pickle')
    tw_ps = [' '.join(token) for line in tw_pt['tag'] for token in line]
    wb_pt = read_pickle('wb_seg_data.pickle')
    wb_ps = [' '.join(token) for line in wb_pt['tag'] for token in line]

    # set the figure layout and x
    f = plt.figure(figsize=(8, 3))
    origin_end_x = 11
    bin_size = 5
    x = range(1, origin_end_x)
    bin_range = range(1, (origin_end_x - 1) * bin_size)

    # compute the y for each bin
    tw_cnt = collections.Counter(tw_ps)
    tw_ys = [len([k for k, v in tw_cnt.most_common() if v == i]) / len(tw_cnt) for i in bin_range]
    tw_y = [sum(tw_ys[bin_size * i: bin_size * i + bin_size]) for i in x]

    wb_cnt = collections.Counter(wb_ps)
    wb_ys = [len([k for k, v in wb_cnt.most_common() if v == i]) / len(wb_cnt) for i in bin_range]
    wb_y = [sum(wb_ys[bin_size * i: bin_size * i + bin_size]) for i in x]

    # plot two lines
    plt.plot(x, tw_y, label='Twitter', marker='o')
    plt.plot(x, wb_y, label='Weibo', marker='*')

    # set the overall figure configurations and save the figure
    plt.xlabel('Occurrence count')
    plt.xticks(x, [5 * i for i in x])
    plt.ylabel('Proportion')
    plt.legend(prop={'size': 12})
    plt.grid(alpha=0.5, linestyle='--')
    plt.tight_layout()
    plt.show()
    f.savefig("dist_line.pdf", bbox_inches='tight')
