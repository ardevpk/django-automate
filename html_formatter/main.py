import os
from html_formatter.utilities import (
    copy, html, css,
)


def htmlformat():
    mainPath:str = os.getcwd()
    os.chdir(mainPath)

    while True:
        # htmlsDir = 'sneat'
        htmlsDir = input('Enter your template folder name (Case-Sensitive): ')
        if os.path.exists(os.path.join(mainPath, htmlsDir)):
            htmlToDir = f'{htmlsDir}_html'
            os.mkdir(htmlToDir)
            os.mkdir(f'{htmlToDir}/assets')
            os.mkdir(f'{htmlToDir}/assets/css')
            os.mkdir(f'{htmlToDir}/assets/images')
            os.mkdir(f'{htmlToDir}/assets/js')
            os.mkdir(f'{htmlToDir}/assets/webfonts')
            os.mkdir(f'{htmlToDir}/assets/other')
            break


    currentProjectPath = os.path.join(mainPath, htmlsDir)
    convertedProjectPath = os.path.join(mainPath, htmlToDir)
    assetsPath = os.path.join(convertedProjectPath, 'assets')
    cssPath = os.path.join(assetsPath, 'css')


    ####### Start Copying static files... #######
    copy.copyAllfiles(assetsPath, currentProjectPath, convertedProjectPath, cssPath)
    ####### End Copying static files! #############

    listoftemplates = os.listdir(convertedProjectPath)
    listoftemplates.pop(0)

    ####### Modifying html files... #############
    html.html(listoftemplates, convertedProjectPath)
    ####### Ending html files modifications! ######

    # ####### Modifying html files... #############
    css.css(cssPath)
    # ####### Ending html files modifications! ######


if __name__ == 'main':
    htmlformat()
