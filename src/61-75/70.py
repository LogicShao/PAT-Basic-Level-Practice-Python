import heapq

n = int(input())
heap = list(map(int, input().split()))
heapq.heapify(heap)
while len(heap) > 1:
    heapq.heappush(heap, (heapq.heappop(heap) + heapq.heappop(heap)) / 2)
print(int(heap[0]))
