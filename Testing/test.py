import unittest
import main

class TestGame(unittest.TestCase):

    def test_correct_guess(self):
        self.assertEqual(
            main.check_guess(5, 5),
            "correct"
        )

    def test_high_guess(self):
        self.assertEqual(
            main.check_guess(10, 5),
            "high"
        )

    def test_low_guess(self):
        self.assertEqual(
            main.check_guess(2, 5),
            "low"
        )

    def test_invalid_guess(self):
        self.assertEqual(
            main.check_guess(501, 5),
            "invalid"
        )

if __name__ == "__main__":
    unittest.main()