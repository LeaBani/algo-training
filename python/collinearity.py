def collinearity(x1, y1, x2, y2):
    return (x1 * y2) == (y1 * x2)
    
result = collinearity(2, 4, 5 ,20)
print(result)