import matplotlib.pyplot as plt
import numpy as np

def plot(a, m, f, target_dict, reference_dict, fig_name): # target and reference dictionary both with format {a:f(m)}
    x_coordinates = np.arange(len(target_dict))
    width = 0.2
    plt.subplots()
    plt.xlabel(a)
    plt.ylabel('{}({})'.format(f, m))
    plt.xticks(x_coordinates + 0.5 * width, target_dict.keys())
    plt.bar(x_coordinates, target_dict.values(), width, label='target')
    plt.bar(x_coordinates + width, reference_dict.values(), width, label='reference')
    plt.legend()
    # plt.show()
    plt.savefig(fig_name)

file = open('plot_data.txt', 'r')
count = 0
while True:
    a = file.readline()
    if not a:
        break
    m = file.readline()
    f = file.readline()
    target = eval(file.readline())
    reference = eval(file.readline())
    plot(a, m, f, target, reference, 'topK_{}'.format(count))
    count += 1