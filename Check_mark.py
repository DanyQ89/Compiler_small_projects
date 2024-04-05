from functools import total_ordering


@total_ordering
class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        return f'{self.name} {self.x} {self.y}'

    def __invert__(self):
        return Point(self.name, self.y, self.x)

    def __repr__(self):
        # return f'Point{self.name, self.x, self.y}'
        return f"Point('{self.name}', {self.x}, {self.y})"

    def __eq__(self, other):
        return [self.name, self.x, self.y] == [other.name, other.x, other.y]

    def __lt__(self, other):
        return [self.name, self.x, self.y] < [other.name, other.x, other.y]


class ColoredPoint(Point):
    def __init__(self, name, x, y, colors=(0, 0, 0)):
        Point.__init__(self, name, x, y)
        self.colors = colors

    def get_color(self):
        return self.colors

    def __invert__(self):
        return ColoredPoint(self.name, self.y, self.x, tuple(map(lambda x: 255 - x, self.colors)))


def get_elements(i):
    if type(i) is list:
        return [list(map(lambda x: str(x) if not x.isnumeric() and not x.startswith('-') else int(x), str(g).split()))
                for g in i]
    return list(map(lambda x: str(x) if not x.isnumeric() and not x.startswith('-') else int(x), str(i).split()))


class CheckMark:
    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third

    def __str__(self):
        return ''.join(map(lambda x: str(x).split()[0], [self.first, self.second, self.third]))

    def __bool__(self):
        need = set()
        need_x = set()
        need_y = set()
        for i in [self.first, self.second, self.third]:
            i = str(i).split()
            need.add(''.join(i))
            need_x.add(i[1])
            need_y.add(i[-1])

        x1, y1 = get_elements(self.first)[1], get_elements(self.first)[-1]
        # print(self.first, self.second)
        x2, y2 = get_elements(self.second)[1], get_elements(self.second)[-1]
        x3, y3 = get_elements(self.third)[1], get_elements(self.third)[-1]
        # print(x, y, x1, y1)
        # a = y1 - y
        # b = x - x1
        # c = a * x + b * y
        # print(a, b, c)
        # print(self.first, self.second, self.third)
        if len(need) == 3 and len(need_x) >= 2 and len(need_y) >= 2 and (x2 - x1) * (y3 - y1) != (x3 - x1) * (y2 - y1):
            # if len(need) == 3 and (max(len(need_y), len(need_x)) == 3 and min(len(need_x), len(need_y)) >= 2):
            return True
        return False

    def __eq__(self, other):
        a = list(map(lambda x: x[1:], get_elements([other.first, other.second, other.third])))
        b = list(map(lambda x: x[1:], get_elements([self.first, self.second, self.third])))
        # print(a, b)
        if a[1] == b[1] and sorted([a[0], a[-1]]) == sorted([b[0], b[-1]]):
            return True
        return False
