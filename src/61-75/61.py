n, m = map(int, input().split())
scores = list(map(int, input().split()))
answers = list(map(int, input().split()))
for i in range(n):
    stuans = list(map(int, input().split()))
    print(sum([scores[i] for i in range(m) if answers[i] == stuans[i]]))
