"""
Unit tests for the find_neighbor_values() function

Using the following grid:
1  2  3  4
5  6  7  8
9  10 11 12
13 14 15 16
"""

from simcity2 import find_neighbor_values

GRID = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]


def test_find_neighbor_values_top_left_corner():
    """
    Corner cell (top left)
    Neighbors of 1 should be 2, 5, 6 (in any order)
    """
    assert len(find_neighbor_values(GRID, 0, 0)) == len([2, 5, 6])
    assert set(find_neighbor_values(GRID, 0, 0)) == set([2, 5, 6])


def test_find_neighbor_values_top_right_corner():
    """
    Corner cell (top right)
    Neighbors of 4 should be 3, 7, 8 (in any order)
    """
    assert len(find_neighbor_values(GRID, 0, 3)) == len([3, 7, 8])
    assert set(find_neighbor_values(GRID, 0, 3)) == set([3, 7, 8])


def test_find_neighbor_values_bottom_left_corner():
    """
    Corner cells (bottom left)
    Neighbors of 13 should be 9, 10, 14 (in any order)
    """
    assert len(find_neighbor_values(GRID, 3, 0)) == len([9, 10, 14])
    assert set(find_neighbor_values(GRID, 3, 0)) == set([9, 10, 14])


def test_find_neighbor_values_bottom_right_corner():
    """
    Corner cells (bottom right)
    Neighbors of 16 should be 11, 12, 15 (in any order)
    """
    assert len(find_neighbor_values(GRID, 3, 3)) == len([11, 12, 15])
    assert set(find_neighbor_values(GRID, 3, 3)) == set([11, 12, 15])


def test_find_neighbours_left_edge():
    """
    Edge cell (left edge)
    Neighbors of 5 should be 1, 2, 6, 9, 10 (in any order)
    """
    assert len(find_neighbor_values(GRID, 1, 0)) == len([1, 2, 6, 9, 10])
    assert set(find_neighbor_values(GRID, 1, 0)) == set([1, 2, 6, 9, 10])


def test_find_neighbor_values_top_edge():
    """
    Edge cell (top edge)
    Neighbors of 2 should be 1, 3, 5, 6, 7 (in any order)
    """
    assert len(find_neighbor_values(GRID, 0, 1)) == len([1, 3, 5, 6, 7])
    assert set(find_neighbor_values(GRID, 0, 1)) == set([1, 3, 5, 6, 7])


def test_find_neighbor_values_right_edge():
    """
    Edge cell (right edge)
    Neighbors of 8 should be 3, 4, 7, 11, 12 (in any order)
    """
    assert len(find_neighbor_values(GRID, 1, 3)) == len([3, 4, 7, 11, 12])
    assert set(find_neighbor_values(GRID, 1, 3)) == set([3, 4, 7, 11, 12])


def test_find_neighbor_bottom_edge():
    """
    Edge cell (bottom edge)
    Neighbors of 15 should be 10, 11, 12, 14, 16 (in any order)
    """
    assert len(find_neighbor_values(GRID, 3, 2)) == len([10, 11, 12, 14, 16])
    assert set(find_neighbor_values(GRID, 3, 2)) == set([10, 11, 12, 14, 16])


def test_find_neighbor_middle():
    """
    Middle cell
    Neighbors of 6 should be 1, 2, 3, 5, 7, 9, 10, 11 (in any order)
    """
    assert len(find_neighbor_values(GRID, 1, 1)) == len([1, 2, 3, 5, 7, 9, 10, 11])
    assert set(find_neighbor_values(GRID, 1, 1)) == set([1, 2, 3, 5, 7, 9, 10, 11])
