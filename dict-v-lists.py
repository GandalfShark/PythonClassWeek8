d1 = {'BONKY': '13', 'WONKY': '42', 'FONKY': '23'}
# pro-tip: fonky is not a word
d2 = {'xxx': '123', 'zzz': '321', 'yyy': 'antidisestablishmentarianism'}
d3 = {}

for item in (d1, d2):
    # d1 is considered an 'item' as is d2
    d3.update(item)
    # this adds d1 as a whole to d3 then adds d2 as a whole to d3
print(d3)
# now d3 is a dict containing the values from d1 and d2

listA = ['blinky', 'pinky', 'inky', 'clyde']
listB = ['creepy', 'kooky', 'mysterious', 'spooky']
list3 = []

for i in (listA, listB):
    list3.append(i) # update is not a thing for lists
    # makes list 3 into a list of 2 lists
print(list3)
# the 0th item in list3 is listA and the 1th item is listB

