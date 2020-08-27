def salary_maker(n):
    digits = list(map(int, input().split()))
    answer = []
    while digits != []:
        large_digit = 0
        for i in digits:
            if int(str(i) + str(large_digit)) >= int(str(large_digit) + str(i)):
                large_digit = i
        answer.append(large_digit)
        digits.remove(large_digit)
    result = ""
    for l in answer:
        result += str(l)
    return int(result)

print(salary_maker(int(input())))