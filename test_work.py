import unittest
import work


class TestWork(unittest.TestCase):
    def test_square(self):
        cases = [
            (4, 16),
            (9, 81),
            (-16, 256),
            (-3, +9)
        ]

        for inp, expected in cases:
            with self.subTest(inp=inp, expected=expected):
                obtained = work.square(inp)
                self.assertEqual(obtained, expected,
                                 "square(%s) should be %s" % (inp, expected))

    def test_triple(self):
        cases = [
            (2, 6),
            (-4, -12),
            (0, 0),
            (+3, +9)
        ]

        for inp, expected in cases:
            with self.subTest(inp=inp, expected=expected):
                obtained = work.triple(inp)
                self.assertEqual(obtained, expected,
                                 "triple(%s) should be %s" % (inp, expected))

    def test_minNum(self):
        cases = [
            ([0 , 2, 4], 0),
            ([-1,-2,-3], -3),
            ([+5,+20,+15,+10,+30,+45] ,+5)
        ]

        for inp,expected in cases:
            with self.subTest(inp=inp, expected= expected):
                obtained = work.minNum(inp)
                self.assertEqual(obtained, expected,
                                "minNum(%s) should be %s" % (inp,expected))

    def test_sumArray(self):
        cases = [
            ([0],0),
            ([-1, -2, -3], -6),
            ([-5,+10,+15,20,+25], 65),
        ]

        for inp,expected in cases:
            with self.subTest(inp=inp, expected=expected):
                obtained = work.sumArray(inp)
                self.assertEqual(obtained, expected,
                                "sumArray(%s) should be %s" % (inp,expected))

    def test_bubbleSort(self):
        cases = [
            ([5, 3, 5, 1, 9, 2, 4, 7, 8, 6, 12],[1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 12]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
            ([-1, -2, -3, -4, -5],[-5 ,-4 ,-3 ,-2 ,-1])
        ]

        for inp,expected in cases:
            with self.subTest(inp=inp, expected= expected):
                obtained = work.bubbleSort(inp)
                self.assertEqual(obtained, expected,
                                "bubbleSort(%s) should be %s" %(inp,expected))

if __name__ == '__main__':
    unittest.main()
