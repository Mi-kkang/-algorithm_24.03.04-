N = int(input())                    # 보드의 크기 N
arr = [[0]*N for _ in range(N)]
apple = int(input())                # 사과의 개수

for _ in range(apple) :
    i, j = map(int,input().split())
    arr[i][j] = 1

print(arr)