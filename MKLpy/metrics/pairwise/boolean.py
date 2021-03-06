"""
.. codeauthor:: Ivano Lauriola <ivanolauriola@gmail.com>
.. codeauthor:: Mirko Polato

================
Kernel functions
================

.. currentmodule:: MKLpy.metrics.pairwise

This module contains all boolean kernel functions of MKLpy

"""

import numpy as np
from scipy.special import binom
from scipy.sparse import issparse
from sklearn.metrics.pairwise import check_pairwise_arrays
from sklearn.metrics.pairwise import linear_kernel



#----------BOOLEAN KERNELS----------

def monotone_conjunctive_kernel(X,Z=None,c=2):
    L = linear_kernel(X,Z)
    return binom(L,c)


def monotone_disjunctive_kernel(X,Z=None,d=2):
    L = linear_kernel(X,Z)
    n = X.shape[1]

    XX = np.dot(X.sum(axis=1).reshape(X.shape[0],1), np.ones((1,Z.shape[0])))
    TT = np.dot(Z.sum(axis=1).reshape(Z.shape[0],1), np.ones((1,X.shape[0])))
    N_x = n - XX
    N_t = n - TT
    N_xz = N_x - TT.T + L

    N_d = binom(n, d)
    N_x = binom(N_x,d)
    N_t = binom(N_t,d)
    N_xz = binom(N_xz,d)
    return (N_d - N_x - N_t.T + N_xz)


def monotone_dnf_kernel(X,Z=None,d=2,c=2):
    X, Z = check_pairwise_arrays(X, Z)
    n = X.shape[1]
    n_c = binom(n,c)
    XX = np.dot(X.sum(axis=1).reshape(X.shape[0],1), np.ones((1,Z.shape[0])))
    ZZ = np.dot(T.sum(axis=1).reshape(Z.shape[0],1), np.ones((1,X.shape[0])))
    XXc = binom(XX,c)
    ZZc = binom(ZZ,c)
    return binom(n_c,d) - binom(n_c - XXc, d) - binom(n_c - ZZc.T, d) + binom(my_mdk(X,Z,c),d)


def monotone_cnf_kernel(X,Z=None,c=2,d=2):
    pass

def conjunctive_kernel(X,Z=None,c=2):
    pass

def disjunctive_kernel(X,Z=None,d=2):
    pass

def dnf_kernel(X,Z=None,d=2,c=2):
    pass

def cnf_kernel(X,Z=None,c=2,d=2):
    pass

def tanimoto_kernel(X,Z=None):#?
    L = linear_kernel(X,Z)
    xx = np.linalg.norm(X,axis=1)
    tt = np.linalg.norm(T,axis=1)
    pass

