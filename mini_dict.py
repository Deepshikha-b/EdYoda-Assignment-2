# my_dict = {}
 
# for i in range(97, 97 + 26):
#     my_dict[chr(i)] = i
#     print(my_dict)
 
# print(my_dict)
keys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
values = []
for j in range(97,97+26):
    values.append(j)
ans = dict(zip(keys,values))
print(ans)