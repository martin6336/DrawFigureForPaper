import matplotlib.pyplot as plt

if __name__ == '__main__':
    # set figure layout
    f = plt.figure(figsize=(7, 3))

    # x and y data
    x = [1, 2, 3, 4]
    tw_y = [64.47, 78.96, 75.47, 66.61]
    wb_y = [55.36, 76.73, 86.17, 86.57]
    se_y = [42.16, 75.79, 79.24, 61.50]
    kp20k_y = [21.08, 42.97, 46.83, 55.34]
    inspec_y = [15.41, 23.70, 30.27, 35.66]
    krapivin_y = [27.45, 47, 47.54, 43.83]
    semeval_y = [35.32, 55.02, 63.72, 75.72]
    nus_y = [27.42, 47.49, 52.95, 69.08]

    # plot each line
    plt.plot(x, tw_y, label='Twitter', marker='o', color='r')
    plt.plot(x, wb_y, label='Weibo', marker='o', color='black')
    plt.plot(x, se_y, label='StackExchange', marker='o', color='y')
    plt.plot(x, kp20k_y, label='KP20k', marker='*', color='b', linestyle='dashed')
    plt.plot(x, inspec_y, label='Inspec', marker='*', color='grey', linestyle='dashed')
    plt.plot(x, krapivin_y, label='Krapivin', marker='*', color='orange', linestyle='dashed')
    plt.plot(x, semeval_y, label='SemEval', marker='*', color='purple', linestyle='dashed')
    plt.plot(x, nus_y, label='NUS', marker='*', color='g', linestyle='dashed')

    # set overall figure configurations and show the figure
    plt.xlim(left=1, right=4)
    plt.ylim(bottom=10, top=90)
    plt.xticks(x, ['1', '2', '3', '>3'], fontsize=12)
    plt.ylabel('Proprotion of Absent Keyphrase (%)', fontsize=10)
    plt.legend(loc='upper center', ncol=4, fontsize='medium', bbox_to_anchor=(0.5, -0.1))
    plt.grid(alpha=0.5, linestyle='--')
    plt.show()
    f.savefig("absent_rate_lines.pdf", bbox_inches='tight')
