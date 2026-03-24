class Fibonacci:
    def __init__(self):
        ...
    def Nth_term(self, N):
        F = [0, 1]
        for i in range(N-2):
            F.append(F[-1] + F[-2])
        return F[-1]

    def N_over_M(self, N, M):
        F = [0, 1]
        N_over_M = []
        for i in range(N-2):
            f_new = F[-1] + F[-2]
            F.append(f_new)
            if f_new % M == 0:
                N_over_M.append(f_new)
        return N_over_M

print(Fibonacci().Nth_term(100))
print(Fibonacci().N_over_M(100, 7))