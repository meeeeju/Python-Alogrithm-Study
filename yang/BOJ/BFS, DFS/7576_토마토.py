# 98720KB / 2244ms (Python3)
# 231692 / 508ms (PyPy3)
import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
tomatoBox = []
tomatoCount = 0
dq = deque()
for i in range(N):
    tomatoBox.append(list(map(int, input().split())))
    for j in range(M):
        if tomatoBox[i][j]==1:
            dq.append((0, i, j))
        elif tomatoBox[i][j]==0:
            tomatoCount += 1

if tomatoCount == 0:
    print(0)
    exit()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 0
while dq:
    day, x, y = dq.popleft()
    for v in range(4):
        nextX = x+dx[v]
        nextY = y+dy[v]
        if 0<=nextX<N and 0<=nextY<M:
            if tomatoBox[nextX][nextY]==0: # 토마토 익히기
                tomatoCount -= 1
                tomatoBox[nextX][nextY]=1
                ans = day+1
                dq.append((day+1, nextX, nextY)) # 익은 토마토 추가
if tomatoCount == 0:
    print(ans)
else:
    print(-1)
