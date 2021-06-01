import os
import zipfile
import subprocess
import time


backup_source = '/home/hackme/Desktop/dickson/projects/backupScript/docRoot'
backup_destination = '/home/hackme/Desktop/dickson/projects/backupScript/backupSource'
timestamp=time.strftime("%d-%b-%Y-%H-%M-%S")

subprocess.call('clear',shell=True)

msg = 'web-site backup tool'
print('')
print('',msg.upper())
print('','-' * len(msg))
print('')
contents = os.listdir(backup_source)

for content in contents:
    if os.path.isdir(os.path.join(backup_source,content)):
        print(' -',content)
print('')
domain = input(' Enter Your Domain Name : ')
if  os.path.exists( os.path.join(backup_source,domain )):
    zipName = backup_destination+'/'+domain+'-'+timestamp+'-backup.zip'
    archive = zipfile.ZipFile(zipName,'w')
    
    os.chdir(backup_source)
    for rootDir,subDirs,subFiles in os.walk( domain ):
        for filename in subFiles:
            abs_name = os.path.join(rootDir,filename)
            #print(abs_name)
            archive.write(abs_name)

    archive.close()     
else:
    print(' No such Domain')




