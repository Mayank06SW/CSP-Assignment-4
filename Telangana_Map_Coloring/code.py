places = ["Adilabad", "Nizamabad", "Karimnagar", "Warangal", "Khammam"]

links = {
    "Adilabad": ["Nizamabad"],
    "Nizamabad": ["Adilabad", "Karimnagar"],
    "Karimnagar": ["Nizamabad", "Warangal"],
    "Warangal": ["Karimnagar", "Khammam"],
    "Khammam": ["Warangal"]
}

colors = ["Red", "Green", "Blue", "Yellow"]
res = {}

def ok(place, color):
    for nb in links[place]:
        if nb in res and res[nb] == color:
            return False
    return True

def solve_map(idx):
    if idx == len(places):
        return True
    
    p = places[idx]
    
    for col in colors:
        if ok(p, col):
            res[p] = col
            
            if solve_map(idx + 1):
                return True
            
            del res[p]
    
    return False

solve_map(0)

print("Telangana Coloring:")
for d, c in res.items():
    print(d, "->", c)
