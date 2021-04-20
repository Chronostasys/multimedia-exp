# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib


matplotlib.rcParams['font.family'] = 'SimHei'  # 黑体
style.use('_classic_test')


def plotIt(a, title):
    color = ['black']
    if title == 'f4':
        color = ['grey', 'black', 'white', 'black', 'white', 'black', 'white', 'black',
                 'white', 'white', 'black', 'white', 'black', 'white', 'black', 'white', 'black']

    plt.bar(a.keys(), a.values(), color=color, align='center')
    plt.xticks((0, 1, 2, 3, 4, 5, 6, 7, 8, -1, -2, -3, -4, -5, -6, -7, -8), ('0', '1',
               '2', '3', '4', '5', '6', '7', '8', '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8'))
    plt.title(title)
    plt.show()


if __name__ == "__main__":
    a = {0: 32939, 1: 15730, 2: 13427, 3: 11523, 4: 9540, 5: 7957, 6: 6607, 7: 5697,
         8: 4834, -1: 15294, -2: 13637, -3: 11479, -4: 9683, -5: 7979, -6: 6878, -7: 5631, -8: 4871}

    plt.bar(a.keys(), a.values(), color=['black'], align='center')
    plt.xticks((0, 1, 2, 3, 4, 5, 6, 7, 8, -1, -2, -3, -4, -5, -6, -7, -8), ('0', '1',
               '2', '3', '4', '5', '6', '7', '8', '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8'))
    plt.title('original coefficient')
    plt.savefig('original.png')
    plt.show()

    b = {0: 32939, 1: 15730, 2: 12552, 3: 12398, 4: 8739, 5: 8758, 6: 6165, 7: 6139,
         8: 4487, -1: 15294, -2: 12721, -3: 12395, -4: 8891, -5: 8771, -6: 6319, -7: 6190, -8: 4463}
    c = {0: 47068, 1: 13416, 2: 13519, 3: 10075, 4: 9545, 5: 7077, 6: 6650, 7: 5016,
         8: 4754, -1: 13308, -2: 13668, -3: 10124, -4: 9571, -5: 7249, -6: 6591, -7: 5098, -8: 4733}
    d = {0: 59320, 1: 13618, 2: 11987, 3: 9875, 4: 8328, 5: 6860, 6: 5883, 7: 4910,
         8: 4239, -1: 13692, -2: 11976, -3: 9976, -4: 8428, -5: 7007, -6: 5834, -7: 4964, -8: 4190}
    plt.bar(b.keys(), b.values(), color=['black'], align='center')
    plt.xticks((0, 1, 2, 3, 4, 5, 6, 7, 8, -1, -2, -3, -4, -5, -6, -7, -8), ('0', '1',
               '2', '3', '4', '5', '6', '7', '8', '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8'))
    plt.title('after Jsteg coefficient')
    plt.savefig('Jsteg.png')
    plt.show()

    # 黑色嵌入1，白色嵌入0
    plt.bar(c.keys(), c.values(), color=['black'], align='center')
    plt.xticks((0, 1, 2, 3, 4, 5, 6, 7, 8, -1, -2, -3, -4, -5, -6, -7, -8), ('0', '1',
               '2', '3', '4', '5', '6', '7', '8', '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8'))
    plt.title('after F3 coefficient')
    plt.savefig('F3.png')
    plt.show()

    plt.bar(d.keys(), d.values(), color=['grey', 'black', 'white', 'black', 'white', 'black', 'white', 'black',
            'white', 'white', 'black', 'white', 'black', 'white', 'black', 'white', 'black'], align='center')
    plt.xticks((0, 1, 2, 3, 4, 5, 6, 7, 8, -1, -2, -3, -4, -5, -6, -7, -8), ('0', '1',
               '2', '3', '4', '5', '6', '7', '8', '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8'))
    plt.title('after F4 coefficient')
    plt.savefig('F4.png')
    plt.show()
