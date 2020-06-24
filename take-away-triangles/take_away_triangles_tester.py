n_1_input = int( input('Enter the first number:') or '1' )
n_2_input = int( input('Enter the second number:') or '1' )
n_3_input = int( input('Enter the third number:') or '1' )

n = [n_1_input, n_2_input, n_3_input]

if sum(n) == 14:
    print("Starting 3 numbers may not add up to 14")
        
else:

    i=0

    data = []

    while i < 100:

        print(f"i: {i}, current_numbers: {n}, sum: {sum(n)}")
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

