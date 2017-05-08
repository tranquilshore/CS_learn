def editdistIDM(str1, str2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    
    if str1[m-1] == str2[n-1]:
        return editdistIDM(str1, str2, m-1, n-1)
    
    return 1 + min(editdistIDM(str1, str2, m, n-1),editdistIDM(str1, str2, m-1, n),editdistIDM(str1, str2, m-1, n-1))

