def f(V) :
    q = []      # 큐 생성
    for i in range(1, V+1) :    # 진입차수가 0인 정점 인큐
        if cnt[i] == 0 :
            q.append(i)

    while q :
        t = q.pop(0)    # 디큐
        print(t, end=' ')
        for i in adjl[t] :      # t에 인접인 정점 i의
            cnt[i] -= 1         # 진입차수 1 감소,
            if cnt[i] == 0 :    # 0이면 앞선 정점이 모두 처리된 것이므로 인큐
                q.append(i)
    print()

t = 10

for tc in range(1, t+1) :
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))

    adjl = [[] for _ in range(V+1)]
    cnt = [0] * (V + 1)  # 집입차수

    for i in range(E) :
        n1, n2 = arr[i*2], arr[i*2+1]
        adjl[n1].append(n2)
        cnt[n2] += 1         # 진입차수

    print(f'#{tc}', end=' ')
    f(V)        # 위장정렬