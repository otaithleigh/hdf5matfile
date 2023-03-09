import numpy as np

from . import assert_array_equal, get_matfile

matfile = get_matfile("test_arrays.mat")


def test_scalar():
    a0 = matfile.load_variable("a0")
    assert_array_equal(a0, np.array([[1.0]]))


def test_1d():
    a1 = matfile.load_variable("a1")
    assert_array_equal(a1, np.array([[1.0, 2.0, 3.0]]))


def test_2d():
    a2 = matfile.load_variable("a2")
    assert_array_equal(a2, np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]))


def test_3d():
    a3 = matfile.load_variable("a3")
    assert_array_equal(a3, np.arange(1.0, 24 + 1).reshape(2, 3, 4, order="F"))


def test_index_scalar():
    a0 = matfile["a0"]
    value = a0[0, 0]
    assert value == 1.0


def test_index_column():
    a2 = matfile["a2"]
    assert_array_equal(a2[:, 0], np.array([1.0, 4.0]))


def test_index_3d():
    a3 = matfile["a3"]
    assert_array_equal(
        a3[:, :, 0],
        np.array(
            [
                [1.0, 3.0, 5.0],
                [2.0, 4.0, 6.0],
            ]
        ),
    )
    assert_array_equal(
        a3[:, :, 1],
        np.array(
            [
                [7.0, 9.0, 11.0],
                [8.0, 10.0, 12.0],
            ]
        ),
    )
    assert_array_equal(
        a3[:, :, 2],
        np.array(
            [
                [13.0, 15.0, 17.0],
                [14.0, 16.0, 18.0],
            ]
        ),
    )
    assert_array_equal(
        a3[:, :, 3],
        np.array(
            [
                [19.0, 21.0, 23.0],
                [20.0, 22.0, 24.0],
            ]
        ),
    )
