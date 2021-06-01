import subprocess
import json
'''
cmdDict = {
    '1':{
            'description':'Memory Usage Information.',
            'command':'free -m'
    },
    '2':{
            'description':'Disk Usage Information.',
            'command':'df -h'
    },
    '3':{
            'description':'Connected Users.',
            'command':'w'
    },
    '4':{
            'description':'Uptime Information.',
            'command':'uptime'
    },
    '5':{
            'description':'Quit.'
    }
}
'''
def runCommand(cmdID):
    executable = cmdDict[cmdID]['command']  
    subprocess.call('clear',shell=True)
    print('')
    print('')
    subprocess.call(executable,shell=True)
    print('')
    print('')
    input('  ENTER TO CONTINUE :: ')

##START--###################
with open('serverinfo.json','r') as fh:
    cmdDict = json.load(fh)



while True:
    subprocess.call('clear',shell=True)
    header = 'menu driven execution'
    print('')
    print('',header.upper())
    print('','-' * len(header))
    print('')
    for key,cmdInfo  in sorted(cmdDict.items()):
        print(' ',key,cmdInfo['description'])
    print('')
    choice = input(' SELECT AN OPTION :: ')
    if choice == '1':
        runCommand('1')
    elif choice == '2':
        runCommand('2')
    elif choice == '3':
        runCommand('3')
    elif choice == '4':
        runCommand('4')
    elif choice == '5':
        break
    else:
        input(' Invalid Number , PRESS ENTER TO CONTINUE')







