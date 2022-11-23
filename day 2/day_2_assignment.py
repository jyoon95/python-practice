def max_num(a, b, c):
    return max([a, b, c])
print(max_num(1, 2, 3))
print(max_num(10, 50, 5))
print(max_num(2, 6, 69))

def multi_list(lst):
    if len(lst) == 0:
        return 0
    prod = lst[0]
    if len(lst) > 1:
        for i in lst[1:]:
            prod = prod * i
    return prod
print(multi_list([1, 2, 3]))
print(multi_list([]))
print(multi_list([15]))
#I looked at the solution for part 2, not sure how it works

def rev_str(my_str):
    return my_str[::-1]
print(rev_str(''))
print(rev_str('python'))
print(rev_str('my_string'))

def num_within(a, b, c):
    return a in range(b, c + 1)
print(num_within(3, 2, 4))
print(num_within(80, 40, 26))
print(num_within(17, 35, 78))

triangle = [[1],[1 , 1]]
def pascal(n):
    if n < 1:
        print('invalid number of rows')
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number -1]
            length = len(row_prev) + 1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length - 1:
                    row.append(triangle[row_number - 1][i - 1] + triangle[row_number - 1][i])
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1
    for row in triangle:
        print (row)

pascal(2)
pascal(10)