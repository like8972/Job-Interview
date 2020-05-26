import random

def get_random_money(total_money, total_people):
    min_money = 0.01 # Guarantee to grab at least 0.01
    remain_money = total_money - 0.01 # remain money
    money_sum = 0 # Verify that it is exactly total_money
    for i in range(total_people):
        if i == total_people - 1: # last people 
            ran_num = round(remain_money + 0.01, 2) 
        else:
            # min 0.01, max M / N * 2, As average as possible
            ran_num = random.uniform(0.01, remain_money / (total_people - i) * 2) # random uniform: random double, [)
            ran_num = round(ran_num, 2)
        print("{} th people get money {}".format(i + 1, ran_num))
        remain_money -= ran_num
        money_sum += ran_num

    print('money_sum', round(money_sum, 2))


if __name__ == '__main__':
    total_money = 1000
    total_people = 100
    get_random_money(total_money, total_people)
