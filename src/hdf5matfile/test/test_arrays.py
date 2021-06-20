import numpy as np

from . import assert_array_equal, get_matfile

matfile = get_matfile('test_arrays.mat')


def test_scalar():
    a0 = matfile.load_variable('a0')
    assert_array_equal(a0, np.array([[1.]]))


def test_1d():
    a1 = matfile.load_variable('a1')
    assert_array_equal(a1, np.array([[1., 2., 3.]]))


def test_2d():
    a2 = matfile.load_variable('a2')
    assert_array_equal(a2, np.array([[1., 2., 3.], [4., 5., 6.]]))


def test_3d():
    a3 = matfile.load_variable('a3')
    assert_array_equal(a3, np.arange(1., 24 + 1).reshape(2, 3, 4, order='F'))
