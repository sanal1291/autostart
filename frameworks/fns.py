
import subprocess


class fns:
    def __init__(self, *args, **kwargs):
        self.data = args[0]

    def run(self):
        subprocess.run(["powershell.exe",
                        'Start   wt -PassThru -WorkingDirectory "'+self.data['path']+'" -ArgumentList "PowerShell.exe", "-NoExit", "-Command", "firebase","emulators:start","--only functions",";","PowerShell.exe","-Command","code"," ."'])
        pass
