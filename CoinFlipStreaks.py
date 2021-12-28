try:
    import logging as lg
    lg.basicConfig(filename="logging.txt",
                   filemode='a',
                   format='%(asctime)s %(levelname)s -%(message)s',
                   datefmt='%Y-%m-%d %H:%M:%S')
    import random
    total_list, total_streaks, streak, count_h, count_t = [], 0, 0, 0, 0
    for i in range(100000):
        num = random.randint(0, 1)
        if num == 0:
            chance = "H"
            count_h += 1
        else:
            chance = "T"
            count_t += 1
        total_list.append(chance)
    for i in range(len(total_list)):
        if total_list[i] == total_list[-1]: streak += 1
        else: streak = 0
        if streak == 6:
            total_streaks += 1
    print("Total Tails in the coin flip -", count_t, "\nHeads  in the coin flip -", count_h)
    print('Chance of a successful streak in a row of 6 - %s%%' % (total_streaks / 100))
except (AttributeError, TypeError, ValueError, AssertionError, Exception, ArithmeticError) as e:
    print("Error is: \n", e)
    lg.error("Error found in the code. Pl rectify and try again.")