def check(s):
    return s[:-1].isdigit() and s[-1] == dic[sum(int(s[i]) * weight[i] for i in range(17)) % 11]


weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
dic = {
    0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'
}

n = int(input())
res = list(filter(lambda x: not check(x), (input() for _ in range(n))))
print('\n'.join(res) if res else 'All passed')
