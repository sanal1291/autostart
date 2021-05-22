import subprocess
from subprocess import PIPE, STDOUT
import sys
import signal
import os


class vue:

    def __init__(self, *args, **kwargs):
        self.data = args[0]

    def run(self):
        # self.ui = subprocess.Popen(
        #     ["powershell.exe", "vue ui"], creationflags=subprocess.CREATE_NEW_CONSOLE)
        # self.serve = subprocess.Popen(
        #     ["powershell.exe", "cd "+self.data['path'], " ; npx vue-cli-service serve --open --mode development --dashboard"
        #      ], creationflags=subprocess.CREATE_NEW_CONSOLE)
        # subprocess.run(
        #     ["powershell.exe", "cd "+self.data['path'], "; code ."])
        # self.ui = subprocess.run(["powershell.exe", "vue ui"])
        # os.system(
        #     'start cmd /c wt new-tab -p "Windows PowerShell" -d "%cd%" cmd /k vue ui;cmd /k ls')
        # self.terminal = subprocess.run(["powershell.exe",
        #                                 '$proc = Start   wt -PassThru -WorkingDirectory "D:/movies" -ArgumentList "PowerShell.exe", "-NoExit", "-Command", "ls",";","PowerShell.exe","-NoExit","-Command","pwd"', ";$proc.ID"], capture_output=True, text=True)
        # self.terminal = subprocess.Popen(
        #     ["powershell.exe", ''' Start  wt -PassThru -WorkingDirectory "D:" -ArgumentList "PowerShell.exe", "-NoExit", "-Command", "ls",";","PowerShell.exe","-NoExit","-Command","pwd"'''], stdout=subprocess.PIPE)
        subprocess.run(["powershell.exe",
                        'Start   wt -PassThru -WorkingDirectory "'+self.data['path']+'" -ArgumentList "PowerShell.exe", "-NoExit", "-Command", "vue","ui",";","PowerShell.exe","-NoExit","-Command","npx vue-cli-service serve --open",";","PowerShell.exe","-Command","code"," .",";","PowerShell.exe","-Command","explorer","https://console.firebase.google.com/u/0/" '])
        pass

    def terminate(self):
        # subprocess.run(
        #     ["powershell.exe", "Stop-Process -id "+self.terminal.stdout])
        # self.terminal.terminate()
        # self.ui.terminate()
        # self.serve.terminate()
        # command = "taskkill /PID " + \
        #     str(self.ui.pid)+" /PID "+str(self.serve.pid) + " /F"
        # subprocess.run(["powershell.exe", command])

        pass
