from packages import copy_to_userproject
from packages import GenerateBatfile

from packages import read_activate_path

import flet as ft

class ModelTrain_ML(ft.Container):
    def __init__(self,page:ft.Page):
        super().__init__()
        self.page = page

        self.project_path = self.page.client_storage.get("project_file_path")
        print(self.project_path)
        self.alg = self.page.client_storage.get("alg")
        self.run = read_activate_path.read_activ_path()


        self.content = ft.ElevatedButton(text="train",on_click=self.on_click_train)


    def on_click_train(self, e):
        part_dict = self.page.client_storage.get("part_dict")
        copy_to_userproject.CopyMLTrain(self.project_path+"/Scripts")
        GenerateBatfile.generateML(
            target_path=self.project_path+"/Scripts", 
            run_path=self.run, 
            part_dict=part_dict, 
            dataset_path=self.project_path+"/Data/dataset" , 
            export_path=self.project_path+"/Result", 
            alg=self.alg, 
            train_mode="categorical"
        )
        GenerateBatfile.Runbat(self.project_path+"/Scripts/run.bat")