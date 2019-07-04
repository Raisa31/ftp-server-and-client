from ftplib import FTP
import os
from pathlib import Path

ftp = FTP()
ftp.connect('127.0.0.1', 2121)
ftp.login('user', '12345')
ftp.pwd()
ftp.retrlines('LIST')
ftp.quit()

def fetchfile():
    filename = 'syslogtest_be.txt'
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR' + filename, localfile.write)
    localfile.close()

def uploadfile():
    filename = 'C:\\Users\\Raisa Arief\\Desktop\\Software dev\\Ftp client and server\\test.txt'
    localfile = open(filename, 'rb')
    ftp.storbinary('STOR %s' %os.path.basename(filename), localfile, 1024)
    localfile.close()

uploadfile()
ftp.retrlines('LIST')
fetchfile()
ftp.quit()
