# Day 4 in Advent of Code
import datetime

def part1(data):
    sleepScheduleGuards = {}

    for line in data:
        splitLine = line.split()

        if splitLine[2] == 'Guard':
            if splitLine[3] not in sleepScheduleGuards:
                sleepScheduleGuards[splitLine[3]] = [0 for _ in range(60)]
            currentGuard = splitLine[3]

        elif splitLine[2] == 'falls':
            startSleep = int(splitLine[1][3:5])

        elif splitLine[2] == 'wakes':
            stopSleep = int(splitLine[1][3:5])
            minutesAsleep = [1 if (i >= startSleep and i < stopSleep) else 0 for i in range(60)]
            sleepScheduleGuards[currentGuard] = [x+y for x, y in zip(sleepScheduleGuards[currentGuard], minutesAsleep)]

    sleepiestGuard = max([(sum(sleepScheduleGuards[guard]), guard) for guard in sleepScheduleGuards])[1]
    minuteMostAsleep = sleepScheduleGuards[sleepiestGuard].index(max(sleepScheduleGuards[sleepiestGuard]))

    return int(sleepiestGuard.replace('#','')) * minuteMostAsleep

def part2():
    pass


def main():
    with open('input.txt') as f:
        data = f.readlines()

    tupledData = [(str(line[1:17]), str(line[19:])) for line in data]
    sortedTuplesByDates = sorted(tupledData, key=lambda x: datetime.datetime.strptime(x[0], '%Y-%m-%d %H:%M'))
    sortedData = [tup[0] + ' ' + tup[1] for tup in sortedTuplesByDates]
    print(part1(sortedData))


if __name__ == '__main__':
    main()