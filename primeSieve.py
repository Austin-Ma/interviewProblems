'''
Lambda functions:
- Functions that only need to be called once
- Must return something (Assignment statements cannot be used. Remember your issue while studying)
  before the final and playing around with lambdas
  TRICK: If you can imagine it on the rhs of an assignment, you can lambda-ize it
- Saves you from having to define the function below after calling it
- Lambda can only take one expression
https://pythonconquerstheuniverse.wordpress.com/2011/08/29/lambda_tutorial/#footnote2

'''


'''
Write a conditional expression in Lambda
Write a list comprehension in Lambda
Write a function call with arguments passed in into lambda
'''


sample_list = range(1, 20)
for i in range(2, 8):
    sample_list = filter(lambda x: x == i, sample_list)
print(sample_list)

sample_list2 = range(2, 50)
for j in range(2, 8):
    sample_list2 = filter(lambda x: x % j or x == j, sample_list2)
    print(sample_list2)
    '''
[2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    '''

sample_list2 = range(2, 50)
for j in range(2, 8):
    sample_list2 = filter(lambda x: x % j, sample_list2)
    print(sample_list2)
    '''
[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
[5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49]
[5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49]
[7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49]
[7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49]
[11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    '''



def sieve(x):
    store = []
    for i in range(len(x)):
        for j in range (2,8):
            if (x[i]==j or x[i]%j):
                store.append(x)
    return store
nums = range(2,50)
print (sieve(nums))


def rob(nums):
    last, now = 0,0
    for i in nums:
        print (last, now)
        print (last + i)
        print ('\n')
        last, now = now, max(last + i, now)
    return now

a = [1, 5, 20, 6]
print(rob(a))
