def funk_infinity(*numbers):
    num_list = []
    for num in numbers:
        k = 0
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                k = k + 1
        if k <= 0 and num != 1:
            num_list.append(num)
    print(num_list)


funk_infinity(1, 2, 3, 4, 5, 6, 7, 8, 9)


def funk_str(stringi):
    res = []
    for str1 in stringi:
        if str1 in res:
            continue
        else:
            res.append(str1)
    print(res)


funk_str("Hello world!!!")


sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
print(sales.items())

sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
print(sales)

