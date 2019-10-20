"""
После футбольного матча фанаты пытаются уехать домой
на такси. Чтобы сэкономить, они объединяются в группы:
фанат присоединяется к группе, если знает хотя бы
одного человека из неё, группа хочет ехать исключительно
в одной машине, а две разные группы отказываются ехать
вместе. Таксопарк владеет ограниченным числом машин
заданной вместимости. Определите, получится ли у
таксопарка развезти экономных фанатов.
"""

from pathlib import Path
from collections import namedtuple


scriptDir = Path.cwd()


def load_input(fn='input.txt') -> tuple:
    with open(str(scriptDir.joinpath(fn))) as f:
        fans = set(fan for fan
                   in range(int(f.readline())))
        assert 1 <= len(fans) <= 1000

        related_fans = tuple(
            set(map(int, f.readline().split()))
            for _ in range(int(f.readline()))
        )

        CarType = namedtuple('CarType', 'cap count')
        car_type_details = tuple(
            CarType(*tuple(map(int, f.readline().split())))
            for _ in range(int(f.readline()))
        )
        assert len(car_type_details) <= 1000

    return fans, related_fans, car_type_details


def main():
    possible = 1

    fans, relates, car_types = load_input()

    cars = tuple(sorted(reduce(
            lambda caps, car_t: caps + [
                car_t.cap for _ in range(car_t.count)],
            car_types, []
        ), reverse=True))

    # Is there enough seats?
    if len(fans) > sum(cars):
        possible = 0
    print(possible)


if __name__ == '__main__':
    main()

