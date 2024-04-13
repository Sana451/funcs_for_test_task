from math import sqrt
import unittest


def do_unique_list(input_list: list[int]) -> list[int]:
    """Функция принимает на вход список целых чисел, и возвращает
    новый список, содержащий только уникальные элементы.
    """
    unique_list = []
    for i in input_list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


def filter_list_for_prime_nums(min_val: int, max_val: int) -> list[int]:
    """Функция принимает два целых числа (минимум и максимум), и возвращает
    список всех простых чисел в заданном диапазоне.
    Натуральное число (от 1 до +inf) является простым, если оно отлично от 1
    и делится без остатка только на 1 и на само себя.
    """
    prime_nums_list = []
    for val in range(min_val, max_val + 1):
        if val < 2:
            continue

        for delimiter in range(2, val):
            if val % delimiter == 0:
                break
        else:
            prime_nums_list.append(val)

    return prime_nums_list


class Point:
    """Класс представляет собой точку в двумерном пространстве,
    с координатами x и у. Метод calc_distance позволяет вычислять
    расстояние до других точек в двумерном пространстве.
    """

    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    def __getattr__(self, item: str) -> float:
        return self.__dict__[f"_{item}"]

    def __setitem__(self, item: str, value: float) -> None:
        self.__dict__[f"_{item}"] = value

    def calc_distance(self, other: 'Point' = None) -> float:
        """Вычисляет расстояние от одной точки до другой
        (если другая точка не передана, то вычисляется расстояние до начала координат).
        Формула вычисления расстояния между двумя точками A(xa, ya) и B(xb, yb) на плоскости:
        AB = √ ((x2 - x1)**2 + (y2 - y1)**2)
        """
        if not other:
            other = Point(0, 0)
        # вместо sqrt также можно использовать **0.5
        return sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)


def sort_list(input_list: list[str] = None) -> tuple[list, list[str]]:
    """Прошрама сортирует список строк по длине сначала по возрастанию, а затем по убыванию.
    """
    if not input_list:
        input_list = []
        while True:
            input_string = input("Введите очередную строку + ENTER (для выхода введите EXIT): ")
            if input_string.lower() == "exit":
                break
            input_list.append(input_string)

    ascending_list = sorted(input_list, key=len, reverse=False)
    descending_list = sorted(input_list, key=len, reverse=True)

    print(f"""\n\tРезультаты:
    \rСписок в возрастающем порядке {ascending_list}
    \rСписок в убывающем порядке {descending_list}""")

    return ascending_list, descending_list


class TestMyFuncs(unittest.TestCase):

    def test_return_unique_from_list(self):
        self.assertEqual(do_unique_list([1, 1, 2, 2, 3, 4, 5, 6, 7]), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(do_unique_list([-1, -1, 2, 2, 3, 4, 5, 6, 7]), [-1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(do_unique_list([]), [])

    def test_filter_list_for_prime_nums(self):
        self.assertEqual(filter_list_for_prime_nums(19, 54), [19, 23, 29, 31, 37, 41, 43, 47, 53])
        self.assertEqual(filter_list_for_prime_nums(-19, 10), [2, 3, 5, 7])
        self.assertEqual(filter_list_for_prime_nums(0, 1), [])

    def test_poit_class(self):
        p1 = Point(10, 12)
        self.assertEqual(p1.x, 10)
        self.assertEqual(p1.y, 12)
        p1.x, p1.y = 15, 180
        self.assertEqual(p1.x, 15)
        self.assertEqual(p1.y, 180)
        self.assertEqual(p1.calc_distance(), 180.62391868188442)
        p2 = Point(100, 15)
        p3 = Point(-100, 15)
        self.assertEqual(p1.calc_distance(other=p2), 185.60711193270586)
        self.assertEqual(p1.calc_distance(other=p3), 201.12185361118767)

    def test_sort_list(self):
        self.assertEqual(
            sort_list(['книга', 'очки', 'растение']),
            (['очки', 'книга', 'растение'], ['растение', 'книга', 'очки']))
        self.assertEqual(
            sort_list(['sana451', 'sa', '12345678', 'qwerty', '', '']),
            (['', '', 'sa', 'qwerty', 'sana451', '12345678'], ['12345678', 'sana451', 'qwerty', 'sa', '', '']))


if __name__ == '__main__':
    sort_list()