# Australia Map Coloring (same logic, different style)

regions = ["WA", "NT", "Q", "SA", "NSW", "V", "T"]

adj = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "Q": ["NT", "SA", "NSW"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "NSW": ["Q", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": []
}

cols = ["Red", "Green", "Blue"]
ans = {}

def check_ok(r, c):
    for x in adj[r]:
        if x in ans and ans[x] == c:
            return False
    return True

def fill(i):
    if i == len(regions):
        return True
    
    curr = regions[i]
    
    for c in cols:
        if check_ok(curr, c):
            ans[curr] = c
            
            if fill(i + 1):
                return True
            
            ans.pop(curr)
    
    return False

fill(0)

print("Australia Coloring:")
for k, v in ans.items():
    print(k, "->", v)