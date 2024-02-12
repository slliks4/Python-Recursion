def sum_odd_integers(N):
    number = 0
    # BASE CASE
    if N ==1:
        return 1

    number = 2*N - 1
    
    return number + sum_odd_integers(N-1)

print(sum_odd_integers(5))