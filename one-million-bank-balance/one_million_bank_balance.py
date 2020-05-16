# ----------------------------------------------------------------------------
import json

# ----------------------------------------------------------------------------
# Set up variables

deposit_range = range( 1, int( input('Max deposit value:') or '250' ) ) 
deposits = [(a,b) for a in deposit_range for b in deposit_range]

daily_results_list = []
results_list = []

# ----------------------------------------------------------------------------
# Loop through all deposit combinations

for d in deposits:    

    day = 0
    balance_lst = [0]

    while balance_lst[-1] < 1000000:

        day += 1

        if day == 1:
            balance_lst += [d[0]]
        elif day == 2:
            balance_lst += [d[0] + d[1]]
        else:
            balance_lst += [balance_lst[-1] + balance_lst[-2]]

        daily_result = {
                            'first': d[0], 
                            'second': d[1], 
                            'day': day, 
                            'balance': balance_lst[-1]
                       }
        
        daily_results_list.append(daily_result)

    overall_result = daily_result.copy()
    overall_result.update({'diff': balance_lst[-1]-1000000})
    results_list.append(overall_result)

# ----------------------------------------------------------------------------
# Print final output

print(
    json.dumps(
        sorted([r for r in results_list if r['diff']==0], 
            key = lambda r : (r['diff'], -r['day']), 
            reverse=False
        ),
        indent=2
    )     
)