class Node:
    def __init__(self, t, value):
        self.t = t
        self.value = value

def cmp(a, b):
    if a.value != b.value:
        return b.value - a.value
    else:
        return -1 if a.t < b.t else 1 if a.t > b.t else 0

if __name__ == "__main__":
    n, k = map(int, input().split())
    v = []
    for _ in range(n):
        t, value = input().split()
        v.append(Node(t, int(value)))

    for i in range(1, k + 1):
        num, s = input().split()
        num = int(num)
        print(f"Case {i}: {num} {s}")

        ans = []
        cnt, total = 0, 0

        if num == 1:
            ans = [node for node in v if node.t[0] == s[0]]
        elif num == 2:
            for node in v:
                if node.t[1:4] == s:
                    cnt += 1
                    total += node.value
            if cnt != 0:
                print(cnt, total)
        elif num == 3:
            m = {}
            for node in v:
                if node.t[4:10] == s:
                    sub_t = node.t[1:4]
                    m[sub_t] = m.get(sub_t, 0) + 1
            for key, value in m.items():
                ans.append(Node(key, value))

        ans.sort(key=lambda x: (-x.value, x.t))

        for node in ans:
            print(node.t, node.value)

        if (num in [1, 3] and not ans) or (num == 2 and cnt == 0):
            print("NA")
