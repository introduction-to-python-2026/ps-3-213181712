def approximate_pi(n_terms):
    sum_of_series = 0
    for i in range(0,n_terms,1):
        sum_of_series = (-1)**i / (1 + 2*i)
    return 4 * sum_of_series
