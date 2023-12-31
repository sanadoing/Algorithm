dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

N, M = map(int, input().split())
max_value = 0
board = []

for _ in range(N):
    a = list(map(int, input().split()))
    board.append(a)
    max_value = max(max_value, max(a))

visited = [[0] * M for _ in range(N)]
result = 0


def DFS(y, x, cnt, total):
    global result

    # board의 가장 큰 값을 남은 횟수만큼 더해도 지금껏 나온 최댓값보다 작을 경우
    if total + max_value * (4-cnt) < result:
        return
    if cnt == 4:
        result = max(result, total)
        return
    else:
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0 <= yy < N and 0 <= xx < M and visited[yy][xx] == 0:

                if cnt == 2:    # ㅏ, ㅓ, ㅜ, ㅓ 는 두번째 지점에서 다시 나머지 1개 이동
                    visited[yy][xx] = 1
                    DFS(y, x, cnt + 1, total + board[yy][xx])
                    visited[yy][xx] = 0

                visited[yy][xx] = 1
                DFS(yy, xx, cnt + 1, total + board[yy][xx])
                visited[yy][xx] = 0


for y in range(N):
    for x in range(M):
        visited[y][x] = 1
        DFS(y, x, 1, board[y][x])
        visited[y][x] = 0

print(result)
