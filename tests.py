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

    def test_cell_properties(self):
        m1 = Maze(0, 0, 5, 5, 10, 10)
        cell = m1._cells[0][0]
        self.assertEqual(cell._x1, 0)
        self.assertEqual(cell._y1, 0)

    def test_ent_exit_walls(self):
        m1 = Maze(0, 0, 10, 10, 15, 15)
        ent = m1._cells[0][0]
        exit = m1._cells[9][9]
        self.assertEqual(ent.has_top_wall, False)
        self.assertEqual(ent.has_bottom_wall, False)

    def test_reset_visited(self):
        m1 = Maze(0, 0, 10, 10, 15, 15)
        cell1 = m1._cells[0][0]
        self.assertEqual(cell1.visited, False)
        cell2 = m1._cells[1][0]
        self.assertEqual(cell2.visited, False)

if __name__ == "__main__":
    unittest.main()