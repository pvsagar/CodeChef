weekdays = {"mon": 0, "tue": 1, "wed": 2, "thu": 3,"fri": 4, "sat": 5, "sun": 6}
number_of_cases = input()
for i in xrange(number_of_cases):
    if (int(number_of_cases) > 0 and int(number_of_cases) < 1001):
        output = [4] * 7
        number_of_days, day_of_week = raw_input().split()
        if (int(number_of_days) > 27 and int(number_of_days) < 32):
            j = weekdays[day_of_week]
            for i in xrange(29, int(number_of_days)+1):
                output[j] += 1
                j = (j+1) % 7
            print " ".join(map(str, output))
        else:
            break
    else:
        break
