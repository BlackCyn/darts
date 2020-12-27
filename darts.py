game=int(input("Введите количество игр которое хотите сыграть: "))
for i in range(game):
    N,K=map(int,input("Введите количество секторов и номер черной мишени: ").split())
    max=-999
    arr = list(map(int, input("Введите баллы за каждый сектор: ").split()))
    if len(arr)!=N:
        print('Введеено неверное количество секторов ')
        break
    else:
            arr[K] = min(arr)
            if arr[K] > 0:
                arr[K] = 0
            for i in range(N):
                sum = 0
                for j in range(N):
                    d = i + j
                    if d > N - 1:
                        d = d - N
                    sum = sum + arr[d]
                    if sum > max:
                        max = sum
            print("Максимальный рузельтат, который может получить игрок = ",max)
else:
            if (K == -1):
                for i in range(N):
                    sum = 0
                    for j in range(N):
                        d = i + j
                        if d > N - 1:
                            d = d - N
                        sum = sum + arr[d]
                        if sum > max:
                            max = sum
                print("Максимальный рузельтат, который может получить игрок = ",max)
