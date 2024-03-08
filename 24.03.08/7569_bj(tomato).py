def find_toma() :
    toma_0 = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato[i][j][k] == 0:
                    toma_0 += 1
                    near = 0
                    ran = 0
                    for p,q in [(1,0),(0,1),(-1,0),(0,-1)] :
                        if 0<=j+p<N and 0<=k+q<M :
                            ran += 1
                            if tomato[i][j+p][k+q] == -1 :
                                near += 1

                    for m in [1, -1] :
                        if 0<=i+m<H :
                            ran += 1
                            if tomato[i+m][j][k] == -1 :
                                near += 1
                    if near == ran:
                        return -1
                    # if near == 0 :
                    #     return -1
                    # else:
                    #     toma_0 += 1

    if toma_0 == 0 :
        return 0

    return toma_0






M, N, H = map(int,input().split())      # 가로 M 세로 N 높이 H
tomato = []
ans = 'toma'

for _ in range(H) :
    arr = [list(map(int, input().split())) for _ in range(N)]
    tomato.append(arr)

ans = find_toma()

if ans == -1 or ans == 0 :
    print(ans)

else :
    toma_no = ans
    ans = 0

    while toma_no > 0 :
        ans += 1
        for i in range(H) :
            for j in range(N) :
                for k in range(M) :
                    if tomato[i][j][k] == 1 :
                        for p, q in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                            if 0 <= j + p < N and 0 <= k + q < M and tomato[i][j + p][k + q] == 0:
                                toma_no -= 1
                                tomato[i][j+p][k+q] = 1
                        for m in [1, -1]:
                            if 0 <= i + m < H and tomato[i + m][j][k] == 0:
                                toma_no -= 1
                                tomato[i+m][j][k] = 1


    print(ans)