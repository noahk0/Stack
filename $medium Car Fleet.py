def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    fleet, check, position = 0, 0, sorted([(position[i], (target - position[i]) / speed[i]) for i in range(len(position))])

    for time in position[::-1]:
        if check < time[1]:
            fleet += 1
            check = time[1]

    return fleet
