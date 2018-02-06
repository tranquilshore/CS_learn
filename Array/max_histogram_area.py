#naive solution O(n^2)

def maxHistogramArea(height):
    n = len(height)
    if n == 0:
        return 0

    maxArea = 0
    for i in range(n):
        minHeight = height[i]
        maxArea = max(maxArea,minHeight)
        for j in range(i+1,n):
            minHeight = min(minHeight,height[j])
            maxArea = max(maxArea,minHeight*(j-i+1))
    return maxArea

a = [2,1,2,3,1]
print maxHistogramArea(a)
