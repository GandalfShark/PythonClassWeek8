
def fun(a):
    if a > 30:
        print('~~ R3 ~~')
        print('a is: ',a)
        return 3
    else:
        print('...')
        print(a)
        print('...')
        return a + fun(a + 3)
        # 25 + (25+3) --> feed back in fun(28)
        # 28 + (28+3) --> feed back in fun(31) -- stops here
        # adds 25 and 28 to get 53 and the adds 3 and thats 56.

print(fun(20))
print('^^^')
# 25 returns 56
# 24 returns 84
# 0 returns 168
# 15 returns 138
# 100 returns 3


