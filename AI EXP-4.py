from itertools import permutations

def solve_cryptarithm():
    letters = ('S','E','N','D','M','O','R','Y')
    
    for perm in permutations(range(10), len(letters)):
        d = dict(zip(letters, perm))
        
        # Leading digits should not be zero
        if d['S'] == 0 or d['M'] == 0:
            continue
        
        send = d['S']*1000 + d['E']*100 + d['N']*10 + d['D']
        more = d['M']*1000 + d['O']*100 + d['R']*10 + d['E']
        money = d['M']*10000 + d['O']*1000 + d['N']*100 + d['E']*10 + d['Y']
        
        if send + more == money:
            print("Solution found:")
            print(f"SEND = {send}")
            print(f"MORE = {more}")
            print(f"MONEY = {money}")
            print("Mapping:", d)
            return

solve_cryptarithm()
