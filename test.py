import unittest
from sokoban import SokobanProblem, read_file

class TestSokoban(unittest.TestCase):
    def setUp(self):
        self.initial_state = read_file('test01.xsb')
        self.problem = SokobanProblem(self.initial_state)

    def test_actions(self):
        actions = self.problem.actions(self.problem.state_to_string(self.initial_state))
        self.assertIn((0, 1), actions)
        self.assertIn((-1, 0), actions)

    def test_result(self):
        new_state = self.problem.result(self.problem.state_to_string(self.initial_state), (0, 1))
        self.assertNotEqual(new_state, self.problem.state_to_string(self.initial_state))

    def test_goal_test(self):
        self.assertFalse(self.problem.goal_test(self.problem.state_to_string(self.initial_state)))
        self.assertTrue(self.problem.goal_test(self.problem.state_to_string(self.problem.goal)))

    def test_h(self):
        node = self.problem.problem.Node(self.problem.state_to_string(self.initial_state))
        self.assertEqual(self.problem.h(node), 2)

if __name__ == '__main__':
    unittest.main()
