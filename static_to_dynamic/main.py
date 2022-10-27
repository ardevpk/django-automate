import os
from static_to_dynamic.utilities import (
    project, copy,
    settings, views,
    urls, autoopen,
    html, css,
)

def static_to_dynamic():
    mainPath:str = os.getcwd()
    os.chdir(mainPath)

    try:
        # projectName:str =  'Scraper'.lower()
        projectName:str =  input('Enter your project folder name (Case-In-Sensitive): ').lower()
        if projectName == 'test': raise NameError
        if os.path.exists(projectName): raise NameError
    except NameError as err:
        print('Error: ', err.__class__.__name__)
        exit()


    while True:
        # HtmlDir = 'sneat'
        HtmlDir = input('Enter your template folder name (Case-Sensitive): ')
        if os.path.exists(os.path.join(mainPath, HtmlDir)): break
        else: continue


    projectPath = os.path.join(mainPath, projectName)
    envPath = os.path.join(projectPath, 'env/Scripts/activate')
    ####### Starting Project... ###################
    project.startDjangoProject(envPath, projectName)
    ####### Ending Project! #######################

    htmlPath = os.path.join(projectPath, 'templates')
    corePath = os.path.join(projectName, 'core')
    appPath = os.path.join(projectName, 'app')
    staticPath = os.path.join(corePath, 'static')
    cssPath = os.path.join(staticPath, 'css')

    ####### Start Copying static files... #######
    copy.copyAllfiles(staticPath, HtmlDir, mainPath, htmlPath, cssPath)
    ####### End Copying static files! #############

    ####### Modifying settings... ###############
    settings.wrtingSettingsFile(corePath)
    ####### Ending settings modifications! ########

    listoftemplates = os.listdir(htmlPath)
    ####### Modifying views... ##################
    views.wrtingViewsFile(appPath, listoftemplates)
    ####### Ending views modifications! ###########

    ####### Modifying urls... ###################
    urls.wrtingUrlsFile(corePath, appPath, listoftemplates)
    ####### Ending urls modifications! ############

    ####### Writing auto open python file... #####
    autoopen.autoOpen(projectPath)
    ####### Auto open file writing completed! #####

    ####### Modifying html files... #############
    html.html(listoftemplates, htmlPath)
    ####### Ending html files modifications! ######

    ####### Modifying html files... #############
    css.css(cssPath)
    ####### Ending html files modifications! ######

    print('Starting...')
    ####### Calling browser file... #############
    os.system(f'cd {projectPath} & python browser.py')
    ####### End! ######
    print('Done!')


if __name__ == 'main':
    static_to_dynamic()
