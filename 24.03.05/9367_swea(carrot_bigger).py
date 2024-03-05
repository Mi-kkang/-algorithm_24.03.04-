t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N = int(input())    # 당근의 개수 N
    carrot = list(map(int, input().split()))

    max_v = 0       # 연속으로 커지는 당근의 개수의 최대 수를 넣을 변수 생성
    cnt = 1         # 연속으로 커지는 당근의 개수를 넣을 변수 // 본인이 있으니 1로 시작

    for i in range(1, N) :
        if carrot[i] > carrot[i-1] :    # 전의 당근 크기와 비교해서 크다면,
            cnt += 1                    # 연속으로 커지네!

        else :                          # 아니라면...
            if max_v < cnt :            # 지금까지 연속으로 커진 개수를 최대값과 비교해서 크다면,
                max_v = cnt             # 재할당해주기
            cnt = 1                     # 카운트 초기화

    if max_v < cnt :                    # 다 끝난 후에도 최대값과 비교해줘서 크다면,
        max_v = cnt                     # 재할당

    print(f'#{tc} {max_v}')