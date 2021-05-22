
import subprocess


class nuxt:
    def __init__(self, *args, **kwargs):
        self.data = args[0]

    def run(self):
        subprocess.run(["powershell.exe",
                        'Start   wt -PassThru -WorkingDirectory "'+self.data['path']+'" -ArgumentList "PowerShell.exe", "-NoExit", "-Command", "npm","run","dev",";","PowerShell.exe","-Command","code"," .",";","explorer","http://localhost:3000" '])
        pass
