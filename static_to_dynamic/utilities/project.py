import os


def startDjangoProject(envPath:str, projectName:str) -> bool:
    try:
        COMMAND = f'''mkdir {projectName} & cd {projectName} & django-admin startproject core . & virtualenv env & deactivate & {envPath} & pip install django whitenoise & pip freeze > requirements.txt & python manage.py startapp app & mkdir templates & cd core & mkdir static & cd static & mkdir css & mkdir js & mkdir images & mkdir webfonts & mkdir others'''
        os.system(COMMAND)
        return True
    except Exception as err:
        print('Project Error: ', err.__class__.__name__)
        return False
