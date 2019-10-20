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
from functools import reduce
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


def get_groups(fans: set, relates: tuple) -> tuple:
    all_freinds = reduce(lambda x, y: x.union(set(y)), relates, set())
    loners = fans.difference(all_freinds)

    def add2team(teams: list, friends: set):
        added = False
        for i, team in enumerate(teams):
            if any(fan in team for fan in friends):
                teams[i] = team.union(friends)
                added = True
        if not added:
            teams.append(friends)
        return teams

    teams = reduce(add2team, relates, [])

    return tuple([{fan} for fan in loners] + teams)


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
    else:
        groups = get_groups(fans, relates)
        # # check all fans in groups
        # assert fans == reduce(
        #         lambda x, y: x.union(y), groups, set())

        # Is there enough cars?
        if len(groups) > len(cars):
            possible = 0
        else:
            group_sizes = sorted(map(len, groups),
                                 reverse=True)

            some_group_is_too_big = any(
                group_fans > car_cap
                for group_fans, car_cap
                in zip(group_sizes, cars)
            )

            if some_group_is_too_big:
                possible = 0

    print(possible)


if __name__ == '__main__':
    main()

