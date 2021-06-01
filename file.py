import pprint

File_Name = '/home/hackme/passwd'

shellDict = {}
singleList = []
with  open(File_Name,'r') as fh:
    data = fh.readlines()
    for line in data:
        user_info =  line.replace('\n','').split(':')
        user_name = user_info[0]
        user_shell   =  user_info[-1]
        
        if user_shell not in shellDict:
            shellDict[user_shell] = []
            shellDict[user_shell].append(user_name)
        else:
            shellDict[user_shell].append(user_name)

#pprint.pprint(shellDict)

'''
for shell,uList in shellDict.items():
    print(shell,len(uList))
'''

for inner_list in shellDict.values():
    for item in inner_list:
        singleList.append(item)

singleList.sort(key=len)
print(singleList[-1])






