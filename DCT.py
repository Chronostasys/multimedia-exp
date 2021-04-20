# -*- coding: utf-8 -*-
import cv2
import numpy as np
from numpy.lib.function_base import copy


new_dct = []
img = []


def loadRaw(imgp):
    return dct(cv2.imread(imgp, 0).astype('float'))


def indctraw(obj, dst):
    cv2.idct(obj)
    cv2.imwrite(dst, cv2.idct(obj).astype('int'))


def load(imgp):
    global img
    img = np.float64(cv2.imread(imgp, 0))
    global new_dct
    new_dct = dct(img)
    # print(img1)
    after_dct = []
    for i in range(len(new_dct)):
        for j in range(len(new_dct[0])):
            after_dct.append(new_dct[i][j])
    after_dct = np.round(after_dct).astype('int')
    return after_dct


def dct(m):
    return cv2.dct(np.float64(m))


# def indct(m, dst):
#     d = copy(new_dct)
#     for i in range(len(new_dct)):
#         for j in range(len(new_dct[0])):
#             d[i][j] = round(m[i*len(new_dct[0])+j])
#     m = d
#     m = cv2.idct(np.float32(m))
#     m = cv2.resize(m, (len(new_dct[0]), len(new_dct)))
#     cv2.imwrite(dst, m)
#     return m


def indct(m, dst):
    d = copy(new_dct)
    for i in range(len(new_dct)):
        for j in range(len(new_dct[0])):
            d[i][j] = m[i*len(new_dct[0])+j]
    m = d
    m = cv2.idct(np.float32(m))
    m = cv2.resize(m, (len(new_dct[0]), len(new_dct)))
    m = np.round(m).astype('int')
    cv2.imwrite(dst, m)
    return m


# print(dct(img1).shape)
first = True
# print(dct(img1).shape)
# new_dct = dct(img1)
# print(img1)
if first:
    after_dct = load('a.png')

first = False
# print(new_dct)
# new_dct=new_dct.reshape(-1,1)
# print(len(after_dct))
# print(after_dct[:600])
