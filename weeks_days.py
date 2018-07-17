# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 21:07:33 2018

@author: VidyaSagar

Problem
RJ is a very curious observer. On the first day of every month, he tries to figure out, for each of the seven days of the week, how many times that day occurs in the current month.

RJ got confused so badly doing this that he asks for your help! He asks several queries; in each query, he gives you the number of days in the current month and which day of the week is on the 1st of the current month.

For each query, you should tell him how many times each day of the week occurs.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains an integer W and a string S, separated by a space.
W denotes the number of days in the current month.
S is one of the strings "mon", "tues", "wed", "thurs", "fri", "sat" or "sun", denoting the day of the week on the 1st of the current month.
Output
For each query, print seven space-separated integers denoting the number of occurrences of Monday, Tuesday, Wednesday, Thursday, Friday, Saturday and Sunday.

Constraints
1 ≤ T ≤ 103
28 ≤ W ≤ 31

Subtasks
Subtask #1 (20 points): W = 28
Subtask #2 (80 points): original constraints
"""


user_input = []
buffer1 = 0
month = [0, 0, 0, 0, 0, 0, 0]
number_of_cases = raw_input()
if (int(number_of_cases) < 1 or int(number_of_cases) > 1000):
        print "Enter valid number of Cases"
else:
    for i in range(0, int(number_of_cases)):
        partial_input = raw_input()
        user_input.append(partial_input)
    for j in range(0, int(number_of_cases)):
        days, day = user_input[j].split(" ")
        if (int(days) < 28 or int(days) > 31):
            print "Enter valid Number of Days"
            break
        else:
            if (day.lower() == 'mon'):
                val = 0
            elif (day.lower() == 'tue'):
                val = 1
            elif (day.lower() == 'wed'):
                val = 2
            elif (day.lower() == 'thu'):
                val = 3
            elif (day.lower() == 'fri'):
                val = 4
            elif (day.lower() == 'sat'):
                val = 5
            else:
                val = 6
            rem = int(days) % 7
            for i in range(0, int(rem)):
                k = int(val) + i
                if k > 6:
                    k = 0
                    if(buffer1 == 1):
                        month[buffer1] += 1
                    else:
                        month[k] += 1
                        buffer1 = 1
                else:
                    month[k] += 1
            for i in range(0, 7):
                month[i] += 4
            month1 = ' '.join(str(e) for e in month)
            print month1
            month = [0, 0, 0, 0, 0, 0, 0]
