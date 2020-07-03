from scipy import integrate

help(integrate.quad)
a = lambda x, y: x * y ** 2
b = lambda x: 1
c = lambda x: -1
print(integrate.quad(a, 0, 1,1))

print(integrate.dblquad(a,0,2,b,c))
