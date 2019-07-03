from ftplib import FTP

ftp = FTP('ftp.dlptest.com')
ftp.login(user = 'dlpuser@dlptest.com', passwd = 'fLDScD4Ynth0p4OJ6bW6qCxjh')
ftp.pwd()
ftp.retrlines('LIST')
ftp.quit()

def fetchfile():
    filename = 'syslogtest_be.txt'
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR' + filename, localfile.write)
    ftp.quit()
    localfile.close()

def uploadfile():
    filename = 'test.txt'
    localfile = open(filename, 'rb')
    ftp.storbinary('STOR', filename, localfile, 1024)
    ftp.quit()

uploadfile()
ftp.retrlines('LIST')
ftp.quit()

fetchfile()
