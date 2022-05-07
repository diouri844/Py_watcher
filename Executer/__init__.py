import os
import psutil
class Executer():
    def __init__(self,file_extension,file_name):
        self.extension = file_extension
        self.file_input = file_name
        self.dispo_extention = [
            'py','java','c','cpp','go'
        ]
    def is_suported_ex(self):
        if self.extension in self.dispo_extention:
            return True
        return False
    def get_avaliabel_command(self,index):
        command = ""
        if index == 0:
            # run python file :
            command = "python "+str(self.file_input)
        if index == 1:
            # compile & run java file :
            os.system("javac "+str(self.file_input))
            command = "java "+str(self.file_input.split('.')[0])
        if index == 2:
            # compile & run c file:
            compile_command = "gcc "+str(self.file_input)+" -o "+str(self.file_input.split('.')[0])
            # run compile command : 
            os.system(compile_command)
            command = str(os.path.abspath(self.file_input.split('.')[0])+".exe")
        if index == 3:
            # compile & run cpp file: 
            compile_command = "g++ "+str(self.file_input)+" -o "+str(self.file_input.split('.')[0])
            # run compile command : 
            os.system(compile_command)
            command = str(os.path.abspath(self.file_input.split('.')[0])+".exe")
        if index == 4:
            #run go file :
            command = "go run "+str(self.file_input)
        return command
    def Run(self):
        if self.is_suported_ex():
            executed_command = self.get_avaliabel_command(self.dispo_extention.index(self.extension))
            try:
                os.system(executed_command)
            except  Exception as e:
                print("[Execute error ] : "+str(e))
        return