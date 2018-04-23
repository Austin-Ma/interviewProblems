from math import sqrt

def confidence(ups, downs):
    n = ups + downs

    if n == 0:
        return 0

    z = 1.281551565545
    p = float(ups) / n

    left = p + 1/(2*n)*z*z
    right = z*sqrt(p*(1-p)/n + z*z/(4*n*n))
    under = 1+1/n*z*z

    return ((left - right) / under)* 1000000

'''
print (confidence(5500, 4500))
print (confidence(600, 400))        #0.5799979262962219
print (confidence(160, 80))
print (confidence(100, 20))         #0.7852955988103241

print (confidence(80, 0))
'''

print (confidence(600, 400))        #0.5799979262962219
print (confidence(100, 30))         #0.7186917298177017
print (confidence(100, 20))         #0.7852955988103241
print (confidence(240, 0))          #0.9932032847337895
