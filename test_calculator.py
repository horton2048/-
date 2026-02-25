"""简单测试任务：验证 add 函数的行为。"""

import unittest

from calculator import add


class TestCalculator(unittest.TestCase):
    def test_add_positive_numbers(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_add_with_zero(self) -> None:
        self.assertEqual(add(7, 0), 7)


if __name__ == "__main__":
    unittest.main()
