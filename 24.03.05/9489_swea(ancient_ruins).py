t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, M = map(int, input().split())    # NxM 사진의 해상도
    shot = [list(map(int,input().split())) for _ in range(N)]   # 사진
    max_v = 0       # 유적의 최대 길이를 저장할 변수 / 초기값 0

    di = [1, 0]
    dj = [0, 1]

    for i in range(N) :         # 전체를 둘러볼 예정입니당
        for j in range(M) :

            if shot[i][j] == 1 :    # 그 부분이 유적이 있다면,

                for k in range(2) : # 오른쪽과 아래를 볼 예정입니당
                    ni = i
                    nj = j
                    cnt = 0
                    while 0<=ni<N and 0<=nj<M and shot[ni][nj] == 1 :   # 유적이 이어져 있으면,
                        cnt += 1                                        # 유적 길이를 추가하고 다시 탐색
                        ni = ni + di[k]
                        nj = nj + dj[k]

                    if max_v < cnt :
                        max_v = cnt


    print(f'#{tc} {max_v}')