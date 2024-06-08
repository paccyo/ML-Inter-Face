# from components.project.projectdata import ProjectData
# from components.project.dataselect import DataSelect
# from components.project.preprocessing import Preprocessing
# from components.project.modelbuild import ModelBuild
# from components.project.modelcompile import ModelCompile
# from components.project.option import Option

# import flet as ft


# def main(page: ft.Page):
#     # Define the UI components
#     page.title = "Neural Network Designer"
#     page.vertical_alignment = ft.MainAxisAlignment.START


#     t = ft.Tabs(
#         selected_index=1,
#         animation_duration=300,
#         tabs=[
#             ProjectData(page),
#             DataSelect(page),
#             Preprocessing(page),
#             ModelBuild(page),
#             ModelCompile(page),
#             Option(page),
#         ],
#         expand=1,
#     )


#     page.add(t)


# # Start the app
# ft.app(target=main)

print('\'valid\'' == "\'" + "valid" + "\'")