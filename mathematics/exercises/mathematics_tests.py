import pytest
from mathematics_exercises import *
import math

@pytest.mark.timeout(1.0)
def test_sum_and_difference_positive():
    assert sum_and_difference(5, 2) == (7, 3)
    assert sum_and_difference(99, 30) == (129, 69)
    assert sum_and_difference(514, 202) == (716, 312)
    assert sum_and_difference(0, 0) == (0, 0)


@pytest.mark.timeout(1.0)
def test_sum_and_difference_negative():
    assert sum_and_difference(-5, -2) == (-7, -3)
    assert sum_and_difference(-99, -30) == (-129, -69)
    assert sum_and_difference(-514, -202) == (-716, -312)


@pytest.mark.timeout(1.0)
def test_sum_and_difference_positive_and_negative():
    assert sum_and_difference(-5, 2) == (-3, -7)
    assert sum_and_difference(99, -30) == (69, 129)
    assert sum_and_difference(-514, 202) == (-312, -716)


# 2

@pytest.mark.timeout(1.0)
def test_float_division_integers():
    assert float_division(4, 2) == 2.0
    assert float_division(100, -25) == -4.0
    assert float_division(-9, -3) == 3.0


@pytest.mark.timeout(1.0)
def test_float_division_floats():
    assert float_division(4, 3) == 4 / 3
    assert float_division(-14, 9) == -14 / 9
    assert float_division(66, 7) == 66 / 7

# 3


@pytest.mark.timeout(1.0)
def test_integer_division_exact():
    assert integer_division(8, 2) == 4
    assert integer_division(100, 4) == 25
    assert integer_division(15, 3) == 5


@pytest.mark.timeout(1.0)
def test_integer_division_rounded_down():
    assert integer_division(4, 3) == 1
    assert integer_division(6, 9) == 0
    assert integer_division(-26, 7) == -4

# 4


@pytest.mark.timeout(1.0)
def test_powerful_operations():
    assert powerful_operations(8, 2) == (16, 64, 0)
    assert powerful_operations(11, 4) == (44, 14641, 3)
    assert powerful_operations(3, 19) == (57, 1162261467, 3)
    assert powerful_operations(9, 5) == (45, 59049, 4)
    assert powerful_operations(5, 2) == (10, 25, 1)


# 5


@pytest.mark.timeout(1.0)
def test_find_average_is_correct():
    assert find_average(5, 7) == 6
    assert find_average(24, 19) == 21.5
    assert find_average(187, 436) == 311.5
    assert find_average(0, 0) == 0
    assert find_average(592073, 24581) == 308327


# 6

def _calculate_circle_area_solution(radius):
    return round(math.pi * radius ** 2, 2)


@pytest.mark.timeout(1.0)
def test_area_of_a_circle_is_correct():
    for radius in range(0, 25):
        assert area_of_a_circle(radius) == _calculate_circle_area_solution(radius)


# 7

def _calculate_triangle_area_solution(side_length):
    return round((math.sqrt(3) * side_length ** 2) / 4)


@pytest.mark.timeout(1.0)
def test_area_of_a_equilateral_triangle_is_correct():
    for side_length in range(0, 25):
        assert area_of_an_equilateral_triangle(side_length) == _calculate_triangle_area_solution(side_length)


# 8


@pytest.mark.timeout(1.0)
def test_calculate_discriminant():
    assert calculate_discriminant(0, 0, 0) == 0
    assert calculate_discriminant(1, 0, 0) == 0
    assert calculate_discriminant(2, 1, 0) == 1
    assert calculate_discriminant(5, 7, 2) == 9
    assert calculate_discriminant(-4, 7, 2) == 81
    assert calculate_discriminant(-4, -5, 7) == 137
    assert calculate_discriminant(-1, -5, -7) == -3
    assert calculate_discriminant(-2, 0, -7) == -56


# 9

hypotenuse_test_data = ((3, 4), (1, 2), (94, 38), (9, 55), (32, 49), (36, 91), (84, 73), (51, 59),
                        (3150420, 25511639), (39451534, 20351305), (17860712, 18201977), (30726784, 9773215))


def _calculate_hypotenuse_length_solution(a, b):
    return math.sqrt(a ** 2 + b ** 2)


@pytest.mark.timeout(1.0)
def test_hypotenuse_calculation_is_correct():
    for data in hypotenuse_test_data:
        assert calculate_hypotenuse_length(data[0], data[1]) == _calculate_hypotenuse_length_solution(data[0], data[1])


# 10


cathetus_test_data = ((3, 5), (19, 50), (16, 71), (14, 15), (37, 44), (33, 43), (19698872, 45672596),
                      (6397696, 36481322), (3326314, 19023438), (15717452, 40221436), (16445750, 34693076))


def _calculate_cathetus_length_solution(a, c):
    return math.sqrt(c ** 2 - a ** 2)


@pytest.mark.timeout(1.0)
def test_cathetus_calculation_is_correct():
    for data in cathetus_test_data:
        assert calculate_cathetus_length(data[0], data[1]) == _calculate_cathetus_length_solution(data[0], data[1])


# 11

@pytest.mark.timeout(1.0)
def test_time_converter_minutes_only():
    assert time_converter(3000) == "3000 sekundit on 0 tund(i) ja 50 minut(it)."
    assert time_converter(480) == "480 sekundit on 0 tund(i) ja 8 minut(it)."
    assert time_converter(1800) == "1800 sekundit on 0 tund(i) ja 30 minut(it)."
    assert time_converter(2) == "2 sekundit on 0 tund(i) ja 0 minut(it)."


@pytest.mark.timeout(1.0)
def test_time_converter_hours_only():
    assert time_converter(3600) == "3600 sekundit on 1 tund(i) ja 0 minut(it)."
    assert time_converter(7200) == "7200 sekundit on 2 tund(i) ja 0 minut(it)."
    assert time_converter(36000) == "36000 sekundit on 10 tund(i) ja 0 minut(it)."
    assert time_converter(442800) == "442800 sekundit on 123 tund(i) ja 0 minut(it)."


@pytest.mark.timeout(1.0)
def test_time_converter_hours_and_minutes():
    assert time_converter(3661) == "3661 sekundit on 1 tund(i) ja 1 minut(it)."
    assert time_converter(7795) == "7795 sekundit on 2 tund(i) ja 9 minut(it)."
    assert time_converter(37810) == "37810 sekundit on 10 tund(i) ja 30 minut(it)."
    assert time_converter(445998) == "445998 sekundit on 123 tund(i) ja 53 minut(it)."


# 12


@pytest.mark.timeout(1.0)
def test_student_helper_is_correct():
    assert student_helper(30) == "Nurk: 30, siinus: 0.5, koosinus: 0.9."
    assert student_helper(60) == "Nurk: 60, siinus: 0.9, koosinus: 0.5."
    assert student_helper(90) == "Nurk: 90, siinus: 1.0, koosinus: 0.0."
    assert student_helper(120) == "Nurk: 120, siinus: 0.9, koosinus: -0.5."
    assert student_helper(150) == "Nurk: 150, siinus: 0.5, koosinus: -0.9."
    assert student_helper(180) == "Nurk: 180, siinus: 0.0, koosinus: -1.0."
    assert student_helper(210) == "Nurk: 210, siinus: -0.5, koosinus: -0.9."
    assert student_helper(240) == "Nurk: 240, siinus: -0.9, koosinus: -0.5."
    assert student_helper(270) == "Nurk: 270, siinus: -1.0, koosinus: -0.0."
    assert student_helper(300) == "Nurk: 300, siinus: -0.9, koosinus: 0.5."
    assert student_helper(330) == "Nurk: 330, siinus: -0.5, koosinus: 0.9."
    assert student_helper(360) == "Nurk: 360, siinus: -0.0, koosinus: 1.0."


# 13

@pytest.mark.timeout(1.0)
def test_greetings_no_hey():
    assert greetings(0) == ""


@pytest.mark.timeout(1.0)
def test_greetings_some_heys():
    assert greetings(1) == "Hey"
    assert greetings(2) == "HeyHey"
    assert greetings(3) == "HeyHeyHey"
    assert greetings(4) == "HeyHeyHeyHey"
    assert greetings(5) == "HeyHeyHeyHeyHey"


@pytest.mark.timeout(1.0)
def test_greetings_more_heys():
    hey = "HeyHeyHeyHeyHey"
    for i in range(5, 50):
        assert greetings(i) == hey
        hey += "Hey"


# 14

@pytest.mark.timeout(1.0)
def test_adding_numbers_is_correct():
    assert adding_numbers(1, 2) == "12"
    assert adding_numbers(123, 456) == "123456"
    assert adding_numbers(6803815, 23058175) == "680381523058175"
    assert adding_numbers(54, 16) == "5416"
    assert adding_numbers(91473, 2483) == "914732483"
    assert adding_numbers(0, 0) == "00"
