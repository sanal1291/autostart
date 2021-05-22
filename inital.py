import inquirer
import json
from frameworks.vue import vue
from frameworks.fns import fns
from frameworks.nuxt import nuxt


class inputs:
    project = None

    def __init__(self, *args, **kwargs):
        f = open('projects.json')
        self.projects = json.loads(f.read())['projects']
        super(inputs, self).__init__(*args, **kwargs)

    def getProject(self):
        questions = [
            inquirer.List('project', message="select project to run.",
                          choices=[item['name'] for item in self.projects])
        ]
        answer = inquirer.prompt(questions)['project']
        # answer = 'fazart_nuxt'
        self.project = False
        for item in self.projects:
            if item['name'] == answer:
                self.project = item
        if not self.project:
            exit()
        self.framework = self.project['framework']
        if self.framework == 'vue':
            self.setVue()
            self.runVue()
            # self.stop()
        elif self.framework == "firebase-functions":
            self.setfns()
            self.runfns()
        elif self.framework == "nuxt":
            self.setnuxt()
            self.runnuxt()
        else:
            pass

    def setVue(self):
        self.vue = vue(self.project)

    def runVue(self):
        self.vue.run()

    def setfns(self):
        self.fns = fns(self.project)

    def runfns(self):
        self.fns.run()

    def setnuxt(self):
        self.nuxt = nuxt(self.project)

    def runnuxt(self):
        self.nuxt.run()

    def stop(self):
        answer = None
        while answer not in ("y", "Y"):
            answer = input("Stop?: y/n ")
            if answer == "y" or answer == 'Y':

                if self.framework == 'vue':
                    self.vue.terminate()
                else:
                    pass
