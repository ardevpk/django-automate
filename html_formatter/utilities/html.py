import os
from bs4 import BeautifulSoup as BS


def html(listoftemplates: list[str], htmlPath: str) -> bool:
    try:
        for iT in listoftemplates:
            # if not iT == 'index.html': continue
            with open(os.path.join(htmlPath, iT), 'r', encoding='utf-8') as htmlread:
                htmlcontent = htmlread.read()
            soup = BS(htmlcontent, 'html.parser')

            for link in soup.find_all('link', {"href": True}):
                Linkvalue = link['href']
                if 'http' in Linkvalue: continue
                else:
                    Linkvalue = str(link['href']).split('/')
                    Linkvalue = Linkvalue[-1]
                    if os.path.splitext(Linkvalue)[1] == '.css':
                        link['href'] = f'./assets/css/{Linkvalue}'
                    else:
                        link['href'] = f'./assets/images/{Linkvalue}'

            for img in soup.find_all('img', {"src": True}):
                Imgvalue = img['src']
                if 'http' in Imgvalue: continue
                else:
                    Imgvalue = str(img['src']).split('/')
                    Imgvalue = Imgvalue[-1]
                    img['src'] = f'./assets/images/{Imgvalue}'

            for script in soup.find_all('script', {"src": True}):
                Scriptvalue = script['src']
                if 'http' in Scriptvalue: continue
                else:
                    Scriptvalue = str(script['src']).split('/')
                    Scriptvalue = Scriptvalue[-1]
                    script['src'] = f'./assets/js/{Scriptvalue}'

            for a in soup.find_all('a', {"href": True}):
                avalue = a['href']
                check = lambda x: str(avalue).startswith(x)
                if check('http') or check('mailto') or check('tel') or check('#') or check('javascript') or avalue in ['', None, False, 0, ' ', '/'] : continue
                else:
                    avalue = str(a['href']).split('/')
                    avalue = avalue[-1]
                    if os.path.splitext(avalue)[1] == '.html':
                        ill = avalue.split('.')[0]
                        if 'index' in ill: a['href'] = "./index.html"
                        else:
                            if os.path.exists(os.path.join(htmlPath, "{}.html".format(ill))):
                                a['href'] = f'./{ill}.html'
                    else:
                        a['href'] = f'./assets/images/{avalue}'

            last_value = soup.prettify()
            with open(os.path.join(htmlPath, iT), 'w', encoding='utf-8') as htmlwrite:
                htmlwrite.write(last_value)

            # with open(os.path.join(htmlPath, iT), 'r', encoding='utf-8') as htmlread2:
            #     htmlcontent2 = htmlread2.readlines()

            # for count, line in enumerate(htmlcontent2):
            #     if '</meta>' in line:
            #         htmlcontent2[count] = '\n'
            #     elif '<meta charset="utf-8"' in line:
            #         htmlcontent2[count] = '<meta charset="utf-8"/>\n'
            #     elif '<meta charset=\'utf-8\'' in line:
            #         htmlcontent2[count] = '<meta charset="utf-8"/>\n'
            #     else: continue
            # htmlwrite2final = "%s" % ''.join(map(str, htmlcontent2))

            # with open(os.path.join(htmlPath, iT), 'w', encoding='utf-8') as htmlwrite2:
            #     htmlwrite2.write(htmlwrite2final)


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
                            htmlurlsplitvar0 = htmlcontent3[htmlcount].split(
                                'style="{}'.format(backgroundurl(htmllines)))[0]
                            htmlurlsplitvar1 = htmlcontent3[htmlcount].split(
                                'style="{}'.format(backgroundurl(htmllines)))[-1]
                            if returnstringValue(htmlurlsplitvar1):
                                htmlurlsplitvar2 = htmlurlsplitvar1.split(
                                    returnstringValue(htmlurlsplitvar1))[0]
                                htmlurlsplitvar3 = htmlurlsplitvar1.split(
                                    returnstringValue(htmlurlsplitvar1))[-1]
                                last_split = htmlurlsplitvar2.split('/')[-1]
                                htmlcontent3[htmlcount] = "{}style='background-image:url(./assets/images/{})'{}".format(
                                    htmlurlsplitvar0, last_split, htmlurlsplitvar3)

                    elif 'style=\'background-image' in htmllines:
                        if backgroundurl(htmllines):
                            htmlurlsplitvar0 = htmlcontent3[htmlcount].split(
                                'style=\'{}'.format(backgroundurl(htmllines)))[0]
                            htmlurlsplitvar1 = htmlcontent3[htmlcount].split(
                                'style=\'{}'.format(backgroundurl(htmllines)))[-1]
                            if returnstringValue(htmlurlsplitvar1):
                                htmlurlsplitvar2 = htmlurlsplitvar1.split(
                                    returnstringValue(htmlurlsplitvar1))[0]
                                htmlurlsplitvar3 = htmlurlsplitvar1.split(
                                    returnstringValue(htmlurlsplitvar1))[-1]
                                last_split = htmlurlsplitvar2.split('/')[-1]
                                htmlcontent3[htmlcount] = "{}style='background-image:url(./assets/images/{})'{}".format(
                                    htmlurlsplitvar0, last_split, htmlurlsplitvar3)

            finalhtml = "%s" % ''.join(map(str, htmlcontent3))
            with open(os.path.join(htmlPath, lasthtmliT), 'w', encoding='utf-8') as htmlwrite:
                htmlwrite.write(finalhtml)
        return True
    except Exception as err:
        print('Html Error:', err)
        return False
