import math

P1 = 0.24
P2 = 0.49
P3 = 0.83
P4 = 0.85
P5 = 0.75

R23 = 1 - (1 - P2) * (1 - P3)
R24 = 1 - (1 - P2) * (1 - P4)
R34 = 1 - (1 - P3) * (1 - P4)

R123 = P1 * R23
R345 = R34 * P5

T1 = 1 - (1 - R24) * (1 - R345)

S1 = R123 * T1

def func (P1, P2, P3, P4, P5):

    R23 = 1 - (1 - P2) * (1 - P3)
    R24 = 1 - (1 - P2) * (1 - P4)
    R34 = 1 - (1 - P3) * (1 - P4)

    R123 = P1 * R23
    R345 = R34 * P5

    T1 = 1 - (1 - R24) * (1 - R345)

    S1 = R123 * T1
    return S1

print("R23=", R23, "\nR24=", R24, "\nR34=", R34, "\nR56=", "\nR123=", R123,
      "\nR345=", R345, "\nT1=", T1, "\nS1=", func (P1, P2, P3, P4, P5))
print("Вероятность безотказной работы системы на протяжении 10 часов равняется ", func (P1, P2, P3, P4, P5))

time = 711
k1 = 3
k2 = 2

P_s = S1
Q_s = 1 - P_s
T_s = -time / math.log(P_s, math.e)

Q_r_s = (1 - P_s)**(k1 + 1)
P_r_s = 1 - Q_r_s
T_r_s = -time / math.log(P_r_s, math.e)
G_q = Q_r_s / Q_s
G_p = P_r_s / P_s
G_t = T_r_s / T_s

Q_reserved_1 = (1 - P1)**(k2 + 1)
Q_reserved_2 = (1 - P2)**(k2 + 1)
Q_reserved_3 = (1 - P3)**(k2 + 1)
Q_reserved_4 = (1 - P4)**(k2 + 1)
Q_reserved_5 = (1 - P5)**(k2 + 1)

P_reserved_1 = 1 - Q_reserved_1
P_reserved_2 = 1 - Q_reserved_2
P_reserved_3 = 1 - Q_reserved_3
P_reserved_4 = 1 - Q_reserved_4
P_reserved_5 = 1 - Q_reserved_5

P_all_reserved_system = func(P_reserved_1, P_reserved_2, P_reserved_3, P_reserved_4, P_reserved_5)
Q_all_reserved_system = 1 - P_all_reserved_system
T_all_reserved_system = -time / math.log(P_all_reserved_system, math.e)
G_all_q = Q_all_reserved_system / Q_s
G_all_p = P_all_reserved_system / P_s
G_all_t = T_all_reserved_system / T_s

print("Базовая вероятность безотказной работы = {}\n"
      "Базовая вероятность отказа = {}\n"
      "Базовая средняя наработка на отказ = {}\n".format(P_s, Q_s, T_s))

print("Вероятность безотказной работы системы с нагруженным общим резервированием = {}\n"
      "Вероятность отказа системы с нагруженным общим резервированием = {}\n"
      "Среднее время работы системы с нагруженным общим резервированием = {}".format(P_r_s, Q_r_s, T_r_s))
print("Выигрыш системы с нагруженным общим резервированием по вероятности безотказной работы = {}\n"
      "Выигрыш системы с нагруженным общим резервированием по вероятности отказа = {}\n"
      "Выигрыш системы с нагруженным общим резервированием по среднему времени работы = {}\n".format(G_p, G_q, G_t))

print("Вероятность безотказной работы системы с нагруженным распределенным резервированием = {}\n"
      "Вероятность отказа системы с нагруженным распределенным резервированием = {}\n"
      "Среднее время работы системы с нагруженным распределенным резервированием = {}".format(P_all_reserved_system, Q_all_reserved_system, T_all_reserved_system))
print("Выигрыш системы с нагруженным распределенным резервированием по вероятности безотказной работы = {}\n"
      "Выигрыш системы с нагруженным распределенным резервированием по вероятности отказа = {}\n"
      "Выигрыш системы с нагруженным распределенным резервированием по среднему времени работы = {}\n".format(G_all_p, G_all_q, G_all_t))
