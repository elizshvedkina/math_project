import pandas as pd
import numpy as np

def count_var_sum(path, alpha):

    df = pd.read_csv(path)

    sum_bid_ask = df['Close'].values * 2

    changes = []

    for i in range(len(sum_bid_ask) - 1):
        if i == 0:
            pass
        else:
            changes.append(np.log(sum_bid_ask[i] / sum_bid_ask[i - 1]))

    VarSt = sorted(changes)[int(len(changes) * alpha)]

    day_mean_price = (df['High'] + df['Low']) / 2

    first = df['Close'] - day_mean_price
    first = first[2:]
    second = df['Close'][0:-1:] - day_mean_price[1::]
    second = second.dropna()
    result = []
    for f, s in zip(first, second):
        result.append(f * s)

    spread = 2 * math.sqrt(abs(np.mean(result)))
    dispersia = np.var(np.log(S))
    qua = np.quantile(S, 1 - alpha)
    COL = df['Close'].values[-1] * (S.values[-1] + dispersia * qua)

    VAR_sum = VarSt + COL
    
    return VAR_sum

alphas = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]
result = []
result_2 = []

for i in alphas:
    result.append(count_var_sum('UNM.csv', i))

for i in alphas:
    result_2.append(count_var_sum('FEES.ME.csv', i))
    
plt.plot(alphas, result, label= 'UNM')
plt.plot(alphas, result_2, label = 'FEES.ME')
plt.legend()
plt.ylabel('VarSum')
plt.xlabel('alpha')
plt.savefig('result.png', dpi=200)
