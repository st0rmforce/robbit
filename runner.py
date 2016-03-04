import subprocess, time,shutil, os, filecmp

running = True
error = False
last_running = False
while running:
    time.sleep(1)
    stamp = time.strftime("%Y_%m_%d_%H_%M_%S")
    subprocess.call(["tar",'czf','versions/'+stamp+'.tgz']+file_list)
    
    for root,dirs,files in os.walk('./versions'):
        for fn in files:
            if fn != stamp+'.tgz' and filecmp.cmp('./versions/'+fn,'./versions/'+stamp+'.tgz'):
                os.remove('./versions/'+stamp+'.tgz')
                os.symlink("fn",'./versions/'+stamp+'.tgz')

    output = open("logs/current.log",'w')


    result = subprocess.call(['python2', 'main.py'],stdout=output,stderr=subprocess.STDOUT)
    if result == 201:
        subprocess.call(['echo', 'shutdown'])
        running = False
    elif result == 202:
        running = False
    elif result != 0:
        error = True
    output.close()
    shutil.move("logs/current.log","logs/{0}.log".format(stamp))
