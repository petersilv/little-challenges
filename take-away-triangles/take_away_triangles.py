n_range = range( 1, 10 ) 
n_start_lst = [[a,b,c] for a in n_range for b in n_range for c in n_range]

n_lst = []

for n_start in n_start_lst:

    n = n_start

    if sum(n_start) == 14:
        continue

    i=0

    data = []

    while i < 100:

        data.append({'i': i, 'numbers': n, 'sum': sum(n)})

        n_1 = abs(n[0] - n[1])
        n_2 = abs(n[0] - n[2])
        n_3 = abs(n[1] - n[2])

        n = [n_1, n_2, n_3]

        i+=1

        if i >= 4:
            if data[-1]['sum'] == data[-2]['sum'] \
                and data[-2]['sum'] == data[-3]['sum'] \
                    and data[-3]['sum'] == data[-4]['sum']:
                break

    final_sum = sum(n)

    n_lst.append({'start': n_start, 'final_sum': final_sum, 'data': data})


solution_lst = [n for n in n_lst if n['final_sum'] == 14]