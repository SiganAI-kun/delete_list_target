list1 = [1, 2, 3, 4, 5]
target1 = 3
list1.remove(target1)

print(list1)
# [1, 2, 4, 5]

'''
----------------------------------
'''

list2 = [1, 2, 3, 1, 2, 3]
target2 = 2
list2.remove(target2)

print(list2)
# [1, 3, 1, 2, 3]

'''
----------------------------------
'''

list2_a = [1, 2, 3, 1, 2, 3]
target2_a = 2

i = len(list2_a)-1
while i >= 0:
    if list2_a[i] == target2_a:
        list2_a.pop(i)
    i -= 1
print(list2_a)
# [1, 3, 1, 3]

for i in range(len(list2_a)-1, -1, -1):
    if list2_a[i] == target2_a:
        list2_a.pop(i)
print(list2_a)
# [1, 3, 1, 3]

'''
----------------------------------
'''
import time

list2_b1, list2_b2 = [], []
target2_b = 2
for i in range(100000):
    lst = [1, 2, 3]
    list2_b1.extend(lst)
    list2_b2.extend(lst)

print(len(list2_b1))
# 300000
print(len(list2_b2))
# 300000

start_time = time.time()

for i in range(len(list2_b1)-1, -1, -1):
    if list2_b1[i] == target2_b:
        list2_b1.pop(i)

# print(list2_b1)

end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)
# 2.1199512481689453

start_time = time.time()

list2_b2_ = [x for x in list2_b2 if x != target2_b]

# print(list2_b2_)

end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)
# 0.020160675048828125


'''
----------------------------------
'''



'''
----------------------------------
'''



'''
----------------------------------
'''
