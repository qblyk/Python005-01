import logging
import time
import os,sys,stat



now_date = time.strftime('%Y%m%d',time.localtime())
logpath = "/var/log/newdir/python-"+ now_date
filepath = logpath+"/test.log"
print(logpath)

# os.chmod("/var/log/",stat.S_IRWXU+ stat.S_IRWXG + stat.S_IRWXO)

def mkdir(path):
    #path_crt
    path=path.strip()
    path=path.rstrip("/")
    isExists=os.path.exists(path)
    if not isExists:
        logfile=path+"/test.log"
        os.makedirs(path)
        # os.chmod(path,stat.S_IRWXU+ stat.S_IRWXG + stat.S_IRWXO)
        print(path+' 创建成功')
        # time.sleep(2)
        print("logfile 路径： "+logfile)
        # open(logfile)
        os.mknod(logfile,S_IRWXU)
        # os.chmod(logfile)
        return True 
    else:
            print(path+' 目录已存在')
            return False

mkpath=logpath
mkdir(mkpath)

logging.basicConfig(filename=filepath,
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s %(name)-8s %(levelname)-8s [line: %(lineno)d] %(message)s')

def cl(aa, bb):
    # c = 1;
    c = aa+bb;
    logging.error("test error log")
    logging.info("test info log")
    logging.warning("test warning log")
    logging.critical("test critical log")  
    print(c);
    return c;
cl(2,4);



