import data
import lab4
import unittest
import math
# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)


    def test_first_element_2(self):
        # write a second test here
        input = [[3,5], [7,6],[],[2,1]]
        result = lab4.first_element(input)
        expected = [3,7,2]
        self.assertEqual(expected, result)

    # Part 2
    def test_second_element_1(self):
        p1 = data.Point(1,2)
        p2 = data.Point(2,3)
        input = [p1, p2]
        result = lab4.x_coord(input)
        expected = [2,3]
        self.assertEqual(expected, result)

    def test_second_element_2(self):
        p1 = data.Point(9,2)
        p2 = data.Point(5,3)
        input = [p1, p2]
        result = lab4.x_coord(input)
        expected = [9,5]
        self.assertEqual(expected, result)

    # Part 3
    def test_third_element_1(self):
        p1 = data.Point(1,2)
        p2 = data.Point(3,4)
        input = [p1, p2]
        result = lab4.are_in_positive_quad(input)
        expected = [p1,p2]
        self.assertEqual(expected, result)

    def test_third_element_2(self):
        p1 = data.Point(1,2)
        p2 = data.Point(3,-4)
        input = [p1, p2]
        result = lab4.are_in_positive_quad(input)
        expected = [p1]
        self.assertEqual(expected, result)
    # Part 4
    def test_fourth_element_1(self):
        p1 = data.Point(1,2)
        p2 = data.Point(3,4)
        result = lab4.distance(p1,p2)
        expected = 2 * math.sqrt(2)
        self.assertEqual(expected, result, place=0)

    # Part 5
    def test_five_element_1(self):
        p1 = data.Point(1,2)
        p2 = data.Point(3,4)
        result = lab4.manhattan_distance([p1,p2])
        expected = 1
        self.assertEqual(expected, result)
    def test_five_element_2(self):
        p1 = data.Point(4,5)
        p2 = data.Point(6,7)
        result = lab4.manhattan_distance(p1,p2)
        expected = 4
        self.assertEqual(expected, result)

    # Part 6
    def test_six_element_1(self):
        p1 = data.Point(3,4)
        p2 = data.Point(6,8)
        p3 = data.Point(9,12)
        p4 = data.Point(12,16)
        input = [p1, p2, p3, p4]
        result = lab4.distance_all(input)
        expected = [5,10,15,20]
        self.assertEqual(expected, result)

    def test_six_element_2(self):
        p1 = data.Point(24,18)
        p2 = data.Point(32,24)
        input = [p1, p2]
        result = lab4.distance_all(input)
        expected = [30,40]
        self.assertEqual(expected, result)




if __name__ == '__main__':
    unittest.main()
