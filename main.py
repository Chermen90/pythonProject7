
first_num = int(input("введите первое число: "))
second_num = int(input("введите второе число: "))

#26
def rec_square(n, m):
    if m == 0:
        return 1
    return n * rec_square(n, m-1)

print(rec_square(first_num, second_num))

#28
def rec_sum(n, m):
    if n == 0:
        return m
    return rec_sum(n-1, m + 1)
print(rec_sum(first_num, second_num))



