sl = ["The", "he","ThereAfter", "There", "After"]

sl.sort(lambda x,y: ~cmp(len(x), len(y)))

def fnc(sl):
    for S in sl:
        b = None
        for s in sl:
            if cmp(s,b) < 0 and s in S:
                S = S.replace(s,"")
        if len(S) == 0:
            return b
        return None
print fnc(sl)
