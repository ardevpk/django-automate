import os
import glob
import shutil
from bs4 import BeautifulSoup as BS
import time
from tqdm import tqdm
import webbrowser

try:
    projectnameinput =  input('Enter Your Project Name: ')
    if projectnameinput == 'test':
        raise NameError
except NameError:
    print('Test name is used by django itself so please choose another name')
    exit()


projectname = projectnameinput.lower()



mainPath = os.getcwd()

print("Creating A Temporary.Batch File To Create Your Django, {} Project.".format(projectname))
startprojectCMD = 'django-admin startproject {}\ncd {}\nvirtualenv env\nmd templates\nmd static\ncd static\nmd css\nmd js\nmd img\nmd webfonts\nmd other\ncd ..\nmd media\n'.format(projectname, projectname)
with open(os.path.join(mainPath, 'temp.bat'), 'w') as f:
    f.write(startprojectCMD)

print("Running The Temporary.Batch File.")        
os.startfile(os.path.join(mainPath, 'temp.bat'))
# input("If Batch File Completed Please continue By Pressing Any Key:")
for itqdm in tqdm(range(8), desc='Modifying Your Project'):
    time.sleep(1)


htmlPath = os.path.join(os.path.join(mainPath, projectname), 'templates')
cssPath = os.path.join(os.path.join(os.path.join(mainPath, projectname), 'static'), 'css')
imgPath = os.path.join(os.path.join(os.path.join(mainPath, projectname), 'static'), 'img')
jsPath = os.path.join(os.path.join(os.path.join(mainPath, projectname), 'static'), 'js')
webfontPath = os.path.join(os.path.join(os.path.join(mainPath, projectname), 'static'), 'webfonts')
otherPath = os.path.join(os.path.join(os.path.join(mainPath, projectname), 'static'), 'other')

class fileSearcher():
    def __init__(self, ext, dotext):
        self.ext = glob.glob(HtmlDir + '/**/*.{}'.format(ext), recursive=True)
        self.dotext = dotext

    def path(self):
        if self.ext:
            for file in self.ext:
                if os.path.exists(os.path.join(mainPath, file)):
                    return True
                else:
                    return False
        else:
            print("There Is No File In {}".format(self.ext))
        
    def fileMover(self):
        if self.path() is True:
            for ifileMover in self.ext:
                try:
                    iPath = os.path.join(mainPath, ifileMover)
                    if os.path.isfile(iPath):
                        if self.dotext == '.html':
                            shutil.copy2(iPath, htmlPath)
                            print("From {}, File {}, Is Copied To {}.".format(iPath, ifileMover, htmlPath))

                        elif self.dotext == '.css':
                            shutil.copy2(iPath, cssPath)
                            print("From {}, File {}, Is Copied To {}.".format(iPath, ifileMover, cssPath))

                        elif self.dotext == '.js':
                            shutil.copy2(iPath, jsPath)
                            print("From {}, File {}, Is Copied To {}.".format(iPath, ifileMover, jsPath))

                        elif self.dotext == '.jpg' or self.dotext == '.jpeg' or self.dotext == '.svg' or self.dotext == '.png' or self.dotext == '.pdf' or self.dotext == '.ico' or self.dotext == '.gif':
                            shutil.copy2(iPath, imgPath)
                            print("From {}, File {}, Is Copied To {}.".format(iPath, ifileMover, imgPath))

                        elif self.dotext == '.eoff' or self.dotext == '.eoff2' or self.dotext == '.eot' or self.dotext == '.woff' or self.dotext == '.woff2' or self.dotext == '.ttf':
                            shutil.copy2(iPath, webfontPath)
                            print("From {}, File {}, Is Copied To {}.".format(iPath, ifileMover, webfontPath))
                        
                        else:
                            shutil.copy2(iPath, otherPath)
                            print("From {}, File {}, Is Copied To {}.".format(iPath, ifileMover, otherPath))

                    else:
                        continue
                except shutil.Error:
                    print('Shutil Error: {}'.format(shutil.Error))
                    continue
                except FileNotFoundError:
                    print('File: {}, Not Found: {}'.format(ifileMover, FileNotFoundError))
                    continue
                except PermissionError:
                    print('Permision Error On: {}\nError is: {}'.format(iPath, PermissionError))
                    continue
                except shutil.SameFileError:
                    print('File: {} Already Exist, Error: {}'.format(ifileMover, shutil.SameFileError))





while True:
    HtmlDir = input('Enter Your Template Folder Name (Case-Sensitive): ')
    if os.path.exists(os.path.join(mainPath, HtmlDir)):
        break
    else:
        continue


html = fileSearcher('html', '.html')
css = fileSearcher('css', '.css')
js = fileSearcher('js', '.js')
imgjpg = fileSearcher('jpg', '.jpg')
imgjpeg = fileSearcher('jpeg', '.jpeg')
imgpng = fileSearcher('png', '.png')
imgico = fileSearcher('ico', '.ico')
imgpdf = fileSearcher('pdf', '.pdf')
imgsvg = fileSearcher('svg', '.svg')
imggif = fileSearcher('gif', '.gif')
fonteot = fileSearcher('eot', '.eot')
fonteoff = fileSearcher('eoff', '.eoff')
fonteoff2 = fileSearcher('eoff2', '.eoff2')
fontwoff = fileSearcher('woff', '.woff')
fontwoff2 = fileSearcher('woff2', '.woff2')
fontttf = fileSearcher('ttf', '.ttf')
scss = fileSearcher('scss', '.scss')
sass = fileSearcher('sass', '.sass')


def Test(file):
    print("Searching For {} Files.".format(file.dotext))
    return file.fileMover()


Test(html)
Test(css)
Test(js)
Test(imgjpg)
Test(imgjpeg)
Test(imgpng)
Test(imgico)
Test(imgpdf)
Test(imgsvg)
Test(fonteot)
Test(fonteoff)
Test(fonteoff2)
Test(fontwoff)
Test(fontwoff2)
Test(fontttf)
Test(imggif)
Test(scss)
Test(sass)



secondpath = os.path.join(os.path.join(mainPath, projectnameinput), projectnameinput)


print("Reading settings.py From: {}".format(projectname))
with open(os.path.join(secondpath, 'settings.py'), 'r') as settingsf:
    settingsread = settingsf.readlines()


print("Modifying...")
settingsread[56] = "        'DIRS': ['templates'],\n"
settingsread[125:200] = "\nSTATICFILES_DIRS = [\n   BASE_DIR, 'static'\n]\n\nMEDIA_ROOT = BASE_DIR / 'media'\nMEDIA_URL = '/media/'\n\n"

print("Finalyzing And Writting The settings.py File.")
with open(os.path.join(secondpath, 'settings.py'), 'w') as settingsw:
    settingsw.writelines(settingsread)



listoftemplates = os.listdir(htmlPath)
finalstrforviews = []
def returnStringforviews(list):
    for iViews in list:
        l = iViews.split('.')[0]
        l = l.split('-')[0]
        viewsOneFile = "\ndef {}(request):\n    return render(request, '{}')\n".format(l, iViews)
        finalstrforviews.append(viewsOneFile)

print("Collecting views.py File Data")
returnStringforviews(listoftemplates)
finalstrforviewsmain = ('%s' % ' '.join(map(str, finalstrforviews)))

print("Modifying...")
viewContent = (f"# This Is Views.py Created By Python Function\nfrom django.shortcuts import render\n\n{finalstrforviewsmain}\n")
print("Finalyzing And Writting The views.py File.")
with open(os.path.join(secondpath, 'views.py'), 'w') as vieww:
    vieww.write(viewContent)



finalstrforurls = []
def returnstringforurls(list):
    for iurls in list:
        l = iurls.split('.')[0]
        l = l.split('-')[0]
        if 'index' in l:
            urlsOneFile = "\npath('', views.{}, name=\'{}\')".format(l, l)
        else:
            urlsOneFile = "\npath('{}/', views.{}, name=\'{}\')".format(l, l, l)
        finalstrforurls.append(urlsOneFile)

print("Collecting urls.py File Data")
returnstringforurls(listoftemplates)
finalstrforurls2 = ('%s' % ', '.join(map(str, finalstrforurls)))
finalstrforurlsmain = (f"from . import views\nfrom django.conf import settings\nfrom django.conf.urls.static import static\n\nurlpatterns = [path('admin/', admin.site.urls),{finalstrforurls2},\n] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)")

print("Reading urls.py File From: {}".format(projectname))
with open(os.path.join(secondpath, 'urls.py'), 'r') as urlf:
    urlread = urlf.readlines()

print("Modifying...")
urlread[17:100] = finalstrforurlsmain
print("Finalyzing And Writting The urls.py File.")
with open(os.path.join(secondpath, 'urls.py'), 'w') as urlw:
    urlw.writelines(urlread)
    


print("Writting Forms.py In {}".format(projectname))
FormsContent = '# This Is Forms.py Created By Python Function\n'
with open(os.path.join(os.path.join(os.path.join(mainPath, projectnameinput), projectnameinput), 'forms.py'), 'w') as formsCreting:
    formsCreting.write(FormsContent)


print("Creating A Batch File For Installing Django In Your, {} Project Virtual Environment.".format(projectname))
batchpath = os.path.join(os.path.join(os.path.join(os.path.join(mainPath, projectname), 'env'), 'Scripts'), 'activate.bat')
with open(batchpath, 'r') as envbatch:
    batchcontent = envbatch.readlines()

batchtowrite = batchcontent[2:100]
finalbatch = "%s" % ' '.join(map(str, batchtowrite))

print("Finalyzing And Writting The Runproject.bat File In: {}.".format(mainPath))
with open(os.path.join(mainPath, 'RunProject.bat'), 'w') as envOut:
    envOut.write("\n\ncd {}\n\n{}\n\ncd {}\n\npip install django\n\npython manage.py migrate\n".format(mainPath, finalbatch, projectname))

print("Creating A Batch File That Helps You To Run Your {} Project On Your Local Server Every Time When You Click On Main.bat file.".format(projectname))
with open(os.path.join(mainPath, 'Main.bat'), 'w') as MainOut:
    MainOut.write("\n\ncd {}\n\n{}\n\ncd {}\n\npython browser.py\n\npython manage.py runserver\n\ncmd /k\n".format(mainPath, finalbatch, projectname))
    print("Main.bat File Created On Path: {}".format(mainPath))


    
WebsitTitle = input('Enter Your Website Title: ')

print("In Html Editing Section...")
for iT in listoftemplates:
    with open(os.path.join(htmlPath, iT), 'r', encoding='utf-8') as htmlread:
        htmlcontent = htmlread.read()

    soup = BS(htmlcontent, 'html.parser')

    linktoadd = '{% load static %}'
    if linktoadd in htmlcontent:
            pass
    else:
        if soup.meta:
            soup.meta.append(linktoadd)
        else:
            continue
    
    try:
        if WebsitTitle in soup.title.string:
            continue
        else:
            soup.title.string = WebsitTitle
    except AttributeError:
        soup.title = WebsitTitle
    else:
        print(f'\n\n\n This Is The Error In Title \n\n\n')

    print("Editing All Links In: {}".format(iT))
    for link in soup.find_all('link',{"href":True}):
        Linkvalue = link['href']
        if 'http' in Linkvalue:
            continue
        else:
            if "{% static '" in Linkvalue:
                continue
            else:
                Linkvalue = str(link['href']).split('/')
                Linkvalue = Linkvalue[-1]
                if os.path.splitext(Linkvalue)[1] == '.css':
                    url = 'static'
                    link['href'] = "% {} 'css/{}' %".format(url, Linkvalue)
                    link['href'] = "{%s}" % link['href']
                else:
                    url = 'static'
                    link['href'] = "% {} 'img/{}' %".format(url, Linkvalue)
                    link['href'] = "{%s}" % link['href']

        
        

    print("Editing All Images In: {}".format(iT))
    for img in soup.find_all('img',{"src":True}):
        Imgvalue = img['src']
        if 'http' in Imgvalue:
            continue
        else:
            if "{% static '" in Imgvalue:
                continue
            else:
                Imgvalue = str(img['src']).split('/')
                Imgvalue = Imgvalue[-1]
                url = 'static'
                img['src'] = "% {} 'img/{}' %".format(url, Imgvalue)
                img['src'] = "{%s}" %img['src']


    print("Editing All Scripts In: {}".format(iT))
    for script in soup.find_all('script',{"src":True}):
        Scriptvalue = script['src']
        if 'http' in Scriptvalue:
            continue
        else:
            if "{% static '" in Scriptvalue:
                continue
            else:
                Scriptvalue = str(script['src']).split('/')
                Scriptvalue = Scriptvalue[-1]
                url = 'static'
                script['src'] = "% {} 'js/{}' %".format(url, Scriptvalue)
                script['src'] = "{%s}" %script['src']


    print("Editing All Anchors In: {}".format(iT))
    for a in soup.find_all('a',{"href":True}):
        avalue = a['href']
        if 'http' in avalue or 'mailto' in avalue or 'tel' in avalue or '#' in avalue or avalue == '' or avalue == '/':
            continue
        else:
            if "{% url '" in avalue:
                continue
            else:
                avalue = str(a['href']).split('/')
                avalue = avalue[-1]
                if os.path.splitext(avalue)[1] == '.html':
                    ill = avalue.split('.')[0]
                    if 'index' in ill:
                        a['href'] = "/"
                    else:
                        if os.path.exists(os.path.join(htmlPath, "{}.html".format(ill))):
                            l2d = ill.split('-')[0]
                            url = 'url'
                            a['href'] = "% {} '{}' %".format(url, l2d)
                            a['href'] = "{%s}" %a['href']
                else:
                    url = 'static'
                    a['href'] = "% {} 'img/{}' %".format(url, avalue)
                    a['href'] = "{%s}" %a['href']


    last_value = soup.prettify()
    
    with open(os.path.join(htmlPath, iT), 'w', encoding='utf-8') as htmlwrite:
        htmlwrite.write(last_value)


    with open(os.path.join(htmlPath, iT), 'r', encoding='utf-8') as htmlread2:
        htmlcontent2 = htmlread2.readlines()


    for count, line in enumerate(htmlcontent2):
        if '</meta>' in line:
                htmlcontent2[count] = '\n'
        elif '<meta charset="utf-8"' in line:
                htmlcontent2[count] = '<meta charset="utf-8"/>\n'
        elif '<meta charset=\'utf-8\'' in line:
                htmlcontent2[count] = '<meta charset="utf-8"/>\n'
        else:
            continue
    htmlwrite2final = "%s" %''.join(map(str, htmlcontent2))
    
    print("Finally Writing {} File In utf-8, encoding".format(iT))
    with open(os.path.join(htmlPath, iT), 'w', encoding='utf-8') as htmlwrite2:
        htmlwrite2.write(htmlwrite2final)
        print("Template, {} Succesfully Modified.".format(iT))





def returnstringValue(x):
    if "\');\"" in x:
        return "\');\""
    elif "\");\'" in x:
        return "\");\'"
    elif ");\'" in x:
        return ");\'"
    elif ");\"" in x:
        return ");\""
    elif "\')\"" in x:
        return "\')\""
    elif "\")\'" in x:
        return "\")\'"
    elif ")\'" in x:
        return ")\'"
    elif ")\"" in x:
        return ")\""
    elif "\')" in x:
        return "\')"
    elif "\")" in x:
        return "\")"
    elif ")" in x:
        return ")"



def backgroundurl(xr):
    if "background-image:url(\"" in xr:
        return "background-image:url(\""
    elif "background-image: url(\"" in xr:
        return "background-image: url(\""
    elif "background-image : url(\"" in xr:
        return "background-image : url(\""
    elif "background-image :url(\"" in xr:
        return "background-image :url(\""
    elif "background-image:url(\'" in xr:
        return "background-image:url(\'"
    elif "background-image: url(\'" in xr:
        return "background-image: url(\'"
    elif "background-image : url(\'" in xr:
        return "background-image : url(\'"
    elif "background-image :url(\'" in xr:
        return "background-image :url(\'"
    elif "background-image:url(" in xr:
        return "background-image:url("
    elif "background-image: url(" in xr:
        return "background-image: url("
    elif "background-image : url(" in xr:
        return "background-image : url("
    elif "background-image :url(" in xr:
        return "background-image :url("


for lasthtmliT in listoftemplates:
    with open(os.path.join(htmlPath, lasthtmliT), 'r', encoding='utf-8') as htmlread3:
        htmlcontent3 = htmlread3.readlines()

    for htmlcount, htmllines in enumerate(htmlcontent3):
        if 'background-image' in htmllines:

            if 'style=\"background-image' in htmllines:
                if backgroundurl(htmllines):
                    htmlurlsplitvar0 = htmlcontent3[htmlcount].split('style="{}'.format(backgroundurl(htmllines)))[0]
                    htmlurlsplitvar1 = htmlcontent3[htmlcount].split('style="{}'.format(backgroundurl(htmllines)))[-1]
                    if returnstringValue(htmlurlsplitvar1):
                        htmlurlsplitvar2 = htmlurlsplitvar1.split(returnstringValue(htmlurlsplitvar1))[0]
                        htmlurlsplitvar3 = htmlurlsplitvar1.split(returnstringValue(htmlurlsplitvar1))[-1]
                        last_split = htmlurlsplitvar2.split('/')[-1]
                        htmlcontent3[htmlcount] = "{}style='background-image:url(static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
              
            elif 'style=\'background-image' in htmllines:
                if backgroundurl(htmllines):
                    htmlurlsplitvar0 = htmlcontent3[htmlcount].split('style=\'{}'.format(backgroundurl(htmllines)))[0]
                    htmlurlsplitvar1 = htmlcontent3[htmlcount].split('style=\'{}'.format(backgroundurl(htmllines)))[-1]
                    if returnstringValue(htmlurlsplitvar1):
                        htmlurlsplitvar2 = htmlurlsplitvar1.split(returnstringValue(htmlurlsplitvar1))[0]
                        htmlurlsplitvar3 = htmlurlsplitvar1.split(returnstringValue(htmlurlsplitvar1))[-1]
                        last_split = htmlurlsplitvar2.split('/')[-1]
                        htmlcontent3[htmlcount] = "{}style='background-image:url(static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)


    finalhtml = "%s" %''.join(map(str, htmlcontent3))
    with open(os.path.join(htmlPath, lasthtmliT), 'w', encoding='utf-8') as htmlwrite:
        htmlwrite.write(finalhtml)





print("In Css Editing Section...")
cssPath = os.path.join(os.path.join(os.path.join(mainPath, projectname), 'static'), 'css')
listofcss = os.listdir(cssPath)
for cssCount2, iCssMover2 in enumerate(listofcss):
    with open(os.path.join(cssPath, iCssMover2)) as cssread2:
        cssContent2 = cssread2.readlines()

    for lineCount2, cssline2 in enumerate(cssContent2):
        if ";src" in cssline2:
            cssContent2[lineCount2] = cssContent2[lineCount2].replace(";src", ';\nsrc')
        if "; src" in cssline2:
            cssContent2[lineCount2] = cssContent2[lineCount2].replace("; src", ';\nsrc')
        if ",url" in cssline2:
            cssContent2[lineCount2] = cssContent2[lineCount2].replace(",url", ',\nurl')
        if ", url" in cssline2:
            cssContent2[lineCount2] = cssContent2[lineCount2].replace(", url", ',\nurl')

                    
    finalcss2 = "%s" %''.join(map(str, cssContent2))
    with open(os.path.join(cssPath, iCssMover2), 'w') as csswrite2:
        csswrite2.write(finalcss2)



for cssCount, iCssMover in enumerate(listofcss):
    with open(os.path.join(cssPath, iCssMover)) as cssread:
        cssContent = cssread.readlines()

    for lineCount, cssline in enumerate(cssContent):
        if "url(\"" in cssline:
                urlSplit = cssContent[lineCount].split("url(\"", 1)
                bracketSplit = urlSplit[-1].split("\")", 1)
                slashSplit = bracketSplit[0].split("/")
                mainImage = slashSplit[-1]
                if '.jpg' in mainImage or '.png' in mainImage or '.svg' in mainImage or '.jpeg' in mainImage:
                    cssContent[lineCount] = "{}url(\"../img/{}\"){}".format(urlSplit[0], mainImage, bracketSplit[-1])
                    print(cssContent[lineCount])
                elif '.eot' in mainImage or '.ttf' in mainImage or '.woff' in mainImage or '.woff2' in mainImage or '.eoff' in mainImage or '.eoff2' in mainImage:
                    cssContent[lineCount] = "{}url(\"../webfonts/{}\"){}".format(urlSplit[0], mainImage, bracketSplit[-1])
                    print(cssContent[lineCount])
                elif '.css' in mainImage:
                    cssContent[lineCount] = "{}url(\"../css/{}\"){}".format(urlSplit[0], mainImage, bracketSplit[-1])
                    print(cssContent[lineCount])
                else:
                    continue

        elif "url(\'" in cssline:
                urlSplit = cssContent[lineCount].split("url(\'", 1)
                bracketSplit = urlSplit[-1].split("\')", 1)
                slashSplit = bracketSplit[0].split("/")
                mainImage = slashSplit[-1]
                if '.jpg' in mainImage or '.png' in mainImage or '.svg' in mainImage or '.jpeg' in mainImage:
                    cssContent[lineCount] = "{}url(\'../img/{}\'){}".format(urlSplit[0], mainImage, bracketSplit[-1])
                    print(cssContent[lineCount])
                elif '.eot' in mainImage or '.ttf' in mainImage or '.woff' in mainImage or '.woff2' in mainImage or '.eoff' in mainImage or '.eoff2' in mainImage:
                    cssContent[lineCount] = "{}url(\'../webfonts/{}\'){}".format(urlSplit[0], mainImage, bracketSplit[-1])
                    print(cssContent[lineCount])
                elif '.css' in mainImage:
                    cssContent[lineCount] = "{}url(\'../css/{}\'){}".format(urlSplit[0], mainImage, bracketSplit[-1])
                    print(cssContent[lineCount])
                else:
                    continue

        elif "url(" in cssline:
                urlSplit = cssContent[lineCount].split("url(", 1)
                bracketSplit = urlSplit[-1].split(")", 1)
                slashSplit = bracketSplit[0].split("/")
                mainImage = slashSplit[-1]
                if '.jpg' in mainImage or '.png' in mainImage or '.svg' in mainImage or '.jpeg' in mainImage:
                    cssContent[lineCount] = "{}url(../img/{}){}".format(urlSplit[0], mainImage, bracketSplit[-1])
                    print(cssContent[lineCount])
                elif '.eot' in mainImage or '.ttf' in mainImage or '.woff' in mainImage or '.woff2' in mainImage or '.eoff' in mainImage or '.eoff2' in mainImage:
                    cssContent[lineCount] = "{}url(../webfonts/{}){}".format(urlSplit[0], mainImage, bracketSplit[-1])
                    print(cssContent[lineCount])
                elif '.css' in mainImage:
                    cssContent[lineCount] = "{}url(../css/{}){}".format(urlSplit[0], mainImage, bracketSplit[-1])
                    print(cssContent[lineCount])
                else:
                    continue

                    
    finalcss = "%s" %''.join(map(str, cssContent))
    with open(os.path.join(cssPath, iCssMover), 'w') as csswrite:
        csswrite.write(finalcss)





print("Your Django Project Is Ready And  Your Server Starts Automatically In A While...\nThank You")
print("Starting Runproject.bat File...")
os.startfile(os.path.join(mainPath, 'Runproject.bat'))
# for i in tqdm(range(40), desc='Finalizing Your Project..'):
#     time.sleep(1)
input("Press Any Key When Django Is Installed In Your Virtual Environmenet... > ")
print("Runproject.bat Proccess Completed.")

print("Starting Your Localhost Server.")

with open(os.path.join(os.path.join(mainPath, projectname), 'browser.py'), 'w') as browserbatch:
    browserbatch.write("import webbrowser\n\n\n\nWeburl = 'http://127.0.0.1:8000'\n\nchrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'\n\nwebbrowser.get(chrome_path).open_new(Weburl)\n")
    
print("Starting Main.bat File...")
os.startfile(os.path.join(mainPath, 'Main.bat'))
for i in tqdm(range(8), desc='Finalyzing and Running Your Project...'):
    time.sleep(1)

print("Congratualations Your Project: {}, Completed And Hosted On Your LocalHost Server.".format(projectname))

