#!/usr/bin/python
# encoding=utf8
# Developer: hfjimenez@utp.edu.co, Homework #1
# High Performance Computing, UTP, 2018-2
# Notes : Conformable matrix, Acols == Brows.
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import numpy as np
import time
import matplotlib.pyplot as plt
from pprint import pprint
from src.util import *


class MatrizError(Exception):
    """ An exception class for Matrix """
    pass


class Matriz(object):
    """ A matriz representation """

    def __init__(self, rows, cols, prng=True, maxr=100):
        print('{}Generando Matriz'.format(ok))
        if prng:
            self.rows = rows
            self.cols = cols
            self.m = np.random.randint(0, maxr, size=(
                self.rows, self.cols), dtype=np.int64)
            print('{}Matriz Aleatoria creada'.format(ok))
        else:
            self.m = np.zeros((rows, cols), dtype=np.int64)
            # self.m = [[0]*n for x in range(m)]    # Another way if I don't want to use np

    def info(self):
        print('Matriz Information:\nDimensions:{}\nSize:{}\nShape:{}\nDatatype in usage:{}\nItemSize:{}bytes'.format(
            self.m.ndim, self.m.size, self.m.shape, self.m.dtype, self.m.itemsize))

    def printm(self):
        pprint(self.m)

    def naiveProdSeq(self, B):
        if not (self.cols == B.rows):
            raise MatrizError(
                "Error, numero de columnas de A debe ser igual al numero de Filas de B!")

        """ n**3 multiplication, sequential """
        result = np.zeros((self.rows, B.cols), dtype=np.int64)
        for row in range(len(self.m)):
            for col in range(len(B.m)):
                for k in range(len(self.m)):
                    result[row][col] += self.m[row][k] * B.m[k][col]
        return result

    def parallelNaiveProduct(self):
        # ToDo
        return None

    def processNaiveProduct(self):
        # ToDo
        return None


def main():
    s = int(input('{}Insert rows for the matrix:: '.format(atn)))
    mh = Matriz(s, s, prng=True)
    m2 = Matriz(s, s, prng=True)
    mh.printm()
    m2.printm()
    print(mh.naiveProdSeq(m2))


if __name__ == '__main__':
    main()
