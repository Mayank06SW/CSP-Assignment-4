import itertools

chars = "TWOFUR"

for comb in itertools.permutations(range(10), len(chars)):
    
    mp = {}
    for i in range(len(chars)):
        mp[chars[i]] = comb[i]
    
    if mp['T'] == 0 or mp['F'] == 0:
        continue
    
    num1 = mp['T']*100 + mp['W']*10 + mp['O']
    num2 = num1
    
    result = mp['F']*1000 + mp['O']*100 + mp['U']*10 + mp['R']
    
    if num1 + num2 == result:
        print("Solution Found:")
        print(mp)
        print(num1, "+", num2, "=", result)
        break
