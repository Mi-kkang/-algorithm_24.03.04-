def find_tank(H, W) :
    for i in range(H) :
        for j in range(W) :
            if bf[i][j] in '^v<>' :
                return (i, j)


def game(x, H, W) :
    global tank
    i, j = tank # 현재 위치
    dir = bf[i][j]      # 탱크의 현재 방향
    # di, dj = dij[dir][0], dij[dir][1]      # 탱크의 진행 방향
    if x in 'UDLR' :               # 방향을 바꾸고, 이동한 칸이 평지라면 그 칸으로 이동
        bf[i][j] = to[x]
        ni, nj = i+dij[x][0], j+dij[x][1]
        if 0<=ni<H and 0<=nj<W and bf[ni][nj] =='.' :
            bf[ni][nj] = to[x]
            bf[i][j] = '.'
            tank = (ni, nj)
    elif x == 'S' :             # 전차가 현재 바라보고 있는 방향으로 포탄을 발사한다.
        di, dj = dij[dir][0], dij[dir][1]
        ni, nj = i+di, j+dj
        while 0<=ni<H and 0<=nj<W :
            if bf[ni][nj] == '*' :    # 벽돌 벽
                bf[ni][nj] = '.'      # 파괴
                break
            elif bf[ni][nj] == '#' :    # 강철 벽
                break                   # 포탄 소멸
            ni += di
            nj += dj



dij = {'^' :[-1,0], 'v':[1,0], '<':[0,-1], '>':[0,1], 'U' :[-1,0], 'D':[1,0], 'L':[0,-1], 'R':[0,1]}
to = {'U':'^', 'D':'v', 'L':'<', 'R':'>'}

t = int(input())

for tc in range(1, t+1) :
    H, W = map(int, input().split())
    bf = [list(input()) for _ in range(H)]
    N = int(input())
    cmd = input()

    tank = find_tank(H, W)

    for x in cmd :
        game(x, H, W)

    print(f'#{tc}', end=' ')
    for row in bf:
        print(''.join(row))