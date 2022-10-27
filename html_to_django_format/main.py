import os
from html_to_django_format.utilities import (
    copy, html, css,
)


def htmltodjango():
    mainPath:str = os.getcwd()
    os.chdir(mainPath)

    while True:
        # htmlsDir = 'sneat'
        htmlsDir = input('Enter your template folder name (Case-Sensitive): ')
        if os.path.exists(os.path.join(mainPath, htmlsDir)):
            convertedProjectName = f'{htmlsDir}_django'
            os.mkdir(convertedProjectName)
            os.mkdir(f'{convertedProjectName}/templates')
            os.mkdir(f'{convertedProjectName}/static')
            os.mkdir(f'{convertedProjectName}/static/css')
            os.mkdir(f'{convertedProjectName}/static/images')
            os.mkdir(f'{convertedProjectName}/static/js')
            os.mkdir(f'{convertedProjectName}/static/webfonts')
            os.mkdir(f'{convertedProjectName}/static/other')
            break


    currentProjectPath = os.path.join(mainPath, htmlsDir)
    convertedProjectPath = os.path.join(mainPath, convertedProjectName)
    convertProjectHtmlPath = os.path.join(convertedProjectPath, 'templates')
    assetsPath = os.path.join(convertedProjectPath, 'static')
    cssPath = os.path.join(assetsPath, 'css')


    ####### Start Copying static files... #######
    copy.copyAllfiles(assetsPath, currentProjectPath, convertProjectHtmlPath, cssPath)
    ####### End Copying static files! #############

    listoftemplates = os.listdir(convertProjectHtmlPath)
    ####### Modifying html files... #############
    html.html(listoftemplates, convertProjectHtmlPath)
    ####### Ending html files modifications! ######

    # ####### Modifying html files... #############
    css.css(cssPath)
    # ####### Ending html files modifications! ######


if __name__ == 'main':
    htmltodjango()
