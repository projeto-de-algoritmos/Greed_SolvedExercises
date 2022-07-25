def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif wt[i - 1] <= j:
                K[i][j] = max(
                    val[i - 1] + K[i - 1][j - wt[i - 1]],
                    K[i - 1][j]
                )
            else:
                K[i][j] = K[i - 1][j]
    return K[n][W]

while True:
  # number of orders
  n = int(input())

  # end condition
  if n==0:
    break

  # max number of pizzas
  P = int(input())

  # init arrays
  time = []
  quan = []

  # read orders
  for i in range(n):
    # read time and quantity of order
    t, q = map(int, input().split())
    time.append(t)
    quan.append(q)
  
  # present knapsack result
  print("{} min.".format(knapSack(P, quan, time, len(time))))