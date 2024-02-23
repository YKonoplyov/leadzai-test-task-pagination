import unittest
from pagination_generator import pagination_generator


class TestPaginationGeneration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_pages_pagiantion_case_list = [
            [(3, 5, 0, 2), "1 2 3 4 5"],
            [(1, 10, 5, 0), "1 2 3 4 5 6 7 8 9 10"],
            [(7, 9, 3, 3), "1 2 3 4 5 6 7 8 9"],
        ]

        cls.around_in_left_boundary_case_list = [
            [(3, 15, 6, 2), "1 2 3 4 5 6 ... 10 11 12 13 14 15"],
            [(2, 5, 2, 0), "1 2 ... 4 5"],
            [(5, 30, 9, 1), "1 2 3 4 5 6 7 8 9 ... 22 23 24 25 26 27 28 29 30"],
        ]
        cls.around_overlaps_left_boundary_case_list = [
            [(4, 20, 3, 2), "1 2 3 4 5 6 ... 18 19 20"],
            [(5, 15, 2, 4), "1 2 3 4 5 6 7 8 9 ... 14 15"],
            [(5, 30, 5, 5), "1 2 3 4 5 6 7 8 9 10 ... 26 27 28 29 30"],
        ]

        cls.around_in_right_boundary_case_list = [
            [(14, 15, 6, 2), "1 2 3 4 5 6 ... 10 11 12 13 14 15"],
            [(4, 5, 2, 0), "1 2 ... 4 5"],
            [(25, 30, 9, 1), "1 2 3 4 5 6 7 8 9 ... 22 23 24 25 26 27 28 29 30"],
        ]
        cls.around_overlaps_right_boundary_case_list = [
            [(17, 20, 3, 2), "1 2 3 ... 15 16 17 18 19 20"],
            [(10, 15, 2, 4), "1 2 ... 6 7 8 9 10 11 12 13 14 15"],
            [(26, 30, 5, 5), "1 2 3 4 5 ... 21 22 23 24 25 26 27 28 29 30"],
        ]

        cls.around_dont_crosses_boundaries_case_list = [
            [(10, 20, 3, 2), "1 2 3 ... 8 9 10 11 12 ... 18 19 20"],
            [(17, 30, 1, 5), "1 ... 12 13 14 15 16 17 18 19 20 21 22 ... 30"],
            [(3, 5, 1, 0), "1 ... 3 ... 5"],
        ]

        cls.no_boundaries_case_list = [
            [(5, 8, 0, 2), "... 3 4 5 6 7 ..."],
            [(30, 100, 0, 10), "... 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 ..."],
            [(10, 15, 0, 1), "... 9 10 11 ..."],
        ]

        cls.no_around_case_list = [
            [(5, 8, 1, 0), "1 ... 5 ... 8"],
            [(12, 26, 3, 0), "1 2 3 ... 12 ... 24 25 26"],
            [(8, 10, 2, 0), "1 2 ... 8 9 10"],
        ]
        cls.around_overlaping_pagination_ends = [
            [(5, 8, 0, 3), "... 2 3 4 5 6 7 8"],
            [(12, 26, 0, 12), "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ..."],
            [(8, 10, 0, 16), "1 2 3 4 5 6 7 8 9 10"],
        ]
    
    def test_all_pages_pagination(self):
        [
            self.assertEqual(pagination_generator(*test_case_args), expectation)
            for test_case_args, expectation in self.all_pages_pagiantion_case_list
        ]

    def test_around_in_left_boundary(self):
        [
            self.assertEqual(pagination_generator(*test_case_args), expectation)
            for test_case_args, expectation in self.around_in_left_boundary_case_list
        ]

    def test_around_overlaps_left_boundary(self):
        [
            self.assertEqual(pagination_generator(*test_case_args), expectation)
            for test_case_args, expectation in self.around_overlaps_left_boundary_case_list
        ]

    def test_around_in_right_boundary(self):
        [
            self.assertEqual(pagination_generator(*test_case_args), expectation)
            for test_case_args, expectation in self.around_in_right_boundary_case_list
        ]

    def test_around_overlaps_right_boundary(self):
        [
            self.assertEqual(pagination_generator(*test_case_args), expectation)
            for test_case_args, expectation in self.around_overlaps_right_boundary_case_list
        ]

    def test_around_dont_crosses_boundaries(self):
        [
            self.assertEqual(pagination_generator(*test_case_args), expectation)
            for test_case_args, expectation in self.around_dont_crosses_boundaries_case_list
        ]

    def test_generate_pagination_no_boundaries(self):
        [
            self.assertEqual(pagination_generator(*test_case_args), expectation)
            for test_case_args, expectation in self.no_boundaries_case_list
        ]

    def test_no_around(self):
        [
            self.assertEqual(pagination_generator(*test_case_args), expectation)
            for test_case_args, expectation in self.no_around_case_list
        ]        
    def test_around_overlaps_pagination_ends_no_boundaries(self):
        [
            self.assertEqual(pagination_generator(*test_case_args), expectation)
            for test_case_args, expectation in self.around_overlaping_pagination_ends
        ]       
if __name__ == "__main__":
    unittest.main()
