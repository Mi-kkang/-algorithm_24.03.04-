t = int(input())    # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, M = map(int, input().split())    # NxM 구역 길이
    arr = [list(map(int, input().split())) for _ in range(N)]   # 화성탐사 구역

    di = [0,1,1,1,-1,-1,-1,0]   # 8방향 델타
    dj = [1,1,0,-1,-1,0,1,-1]

    cnt = 0     # 예비 후보지로 선택할 곳 개수 넣을 변수

    for i in range(N) :
        for j in range(M) :
            stan = arr[i][j]    # 기준 높이 설정
            num = 0             # 기준 높이보다 낮은 지역 넣을 변수

            for k in range(8) : # 8방향을 모두 살펴본다.
                ni = i + di[k]
                nj = j + dj[k]

                if 0<=ni<N and 0<=nj<M and stan > arr[ni][nj] : # 범위에 있고, 기준 높이보다 낮으면,
                    num += 1                                    # 추가해주기

            if num >= 4 :   # 기준 높이보다 낮은 지역이 4곳 이상이면,
                cnt += 1    # 예비 후보지로 선택


    print(f'#{tc} {cnt}')