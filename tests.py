import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 20
        num_rows = 20
        m1 = Maze(0, 0, num_rows, num_cols, 40, 40)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    # def test_cell_properties(self):
    #     m1 = Maze(0, 0, 5, 5, 10, 10)
    #     cell = m1._cells[0][0]
    #     self.assertEqual(cell._x1, 0)
    #     self.assertEqual(cell._y1, 0)
    #     self.assertFalse(cell.visited)

if __name__ == "__main__":
    unittest.main()