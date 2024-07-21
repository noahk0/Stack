def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    days, wait = [], [0] * len(temperatures)

    for i in range(len(temperatures)):
        while days and temperatures[days[-1]] < temperatures[i]:
            day = days.pop()
            wait[day] = i - day

        days.append(i)

    return wait
