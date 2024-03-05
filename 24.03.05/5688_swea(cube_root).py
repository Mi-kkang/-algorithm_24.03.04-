t = int(input())    # 테스트 케이스 개수 받기
sample = [0] + [i**3 for i in range(1,10**6 + 1)]

for tc in range(1, t+1) :
    N = int(input())        # 숫자 N 받기
    ans = -1

    if N in sample :
        ans = sample.index(N)

    print(f'#{tc} {ans}')