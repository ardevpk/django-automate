# # # # # import os
# # # # # cpath = os.getcwd()


# # # # # secondpath = os.path.join(os.path.join(os.getcwd(), 'etc'), 'etc')

# # # # # templatespath = os.path.join(cpath, os.path.join('etc','templates'))
# # # # # # print(templatespath)
# # # # # listoftemplates = os.listdir(templatespath)

# # # # # finalstrforviews = []
# # # # # def returnStringforviews(list):
# # # # #     for i in list:
# # # # #         l = i.split('.')[0]
# # # # #         viewsOneFile = "\ndef {}(request):\n    return render(request, '{}')\n".format(l, i)
# # # # #         finalstrforviews.append(viewsOneFile)

# # # # # returnStringforviews(listoftemplates)
# # # # # finalstrforviewsmain = ('%s' % ' '.join(map(str, finalstrforviews)))

# # # # # viewContent = (f"# This Is Views.py Created By Python Function\nfrom django.shortcuts import render\n\n{finalstrforviewsmain}\n")

# # # # # with open(os.path.join(secondpath, 'views.py'), 'w') as vieww:
# # # # #     vieww.write(viewContent)






# # # # # finalstrforurls = []
# # # # # def returnstringforurls(list):
# # # # #     for i in list:
# # # # #         l = i.split('.')[0]
# # # # #         if 'index' in l:
# # # # #             urlsOneFile = "\npath('', views.{}, name=\'{}\')".format(l, l)
# # # # #         else:
# # # # #             urlsOneFile = "\npath('{}/', views.{}, name=\'{}\')".format(l, l, l)
# # # # #         finalstrforurls.append(urlsOneFile)

# # # # # returnstringforurls(listoftemplates)
# # # # # finalstrforurls2 = ('%s' % ', '.join(map(str, finalstrforurls)))
# # # # # finalstrforurlsmain = (f"from . import views\nfrom django.conf import settings\nfrom django.conf.urls.static import static\n\nurlpatterns = [{finalstrforurls2},\n] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)")






# # # # # with open(os.path.join(secondpath, 'urls.py'), 'r') as urlf:
# # # # #     urlread = urlf.readlines()

# # # # # urlread[17:100] = finalstrforurlsmain
# # # # # with open(os.path.join(secondpath, 'urls.py'), 'w') as urlw:
# # # # #     urlw.writelines(urlread)









# # # # # from ntpath import join
# # # # # import os
# # # # # mainPath = os.getcwd()
# # # # # projectname = 'etc'
# # # # # batchpath = os.path.join(os.path.join(os.path.join(os.path.join(mainPath, projectname), 'env'), 'Scripts'), 'activate.bat')
# # # # # with open(batchpath, 'r') as envbatch:
# # # # #         batchcontent = envbatch.readlines()

# # # # # batchtowrite = batchcontent[2:100]
# # # # # finalbatch = "%s" % ' '.join(map(str, batchtowrite))

# # # # # with open(os.path.join(mainPath, 'runevironment.bat'), 'w') as envOut:
# # # # #     envOut.write("\n\ncd {}\n\n{}\n\ncd {}\n\npip install django\n\npython manage.py runserver\n".format(mainPath, finalbatch, projectname))




# # import os
# # from bs4 import BeautifulSoup as BS

# # mainPath = os.getcwd()
# # projectname = 'djangokreative'
# # htmlPath = os.path.join(os.path.join(mainPath, projectname), 'templates')
# # listoftemplates = os.listdir(htmlPath)

# # # if __name__ == '__main__':
# # #     WebsitTitle = 'djangotest'
# # #     def lastIndex(object):
# # #         return (len(object) - 1)

# # #     for iT in listoftemplates:
# # #         with open(os.path.join(htmlPath, iT), 'r') as htmlread:
# # #             htmlcontent = htmlread.read()

# # #         soup = BS(htmlcontent, 'html.parser')

# # #         linktoadd = '{% load static %}'
# # #         if linktoadd in htmlcontent:
# # #             pass
# # #         else:
# # #             soup.meta.append(linktoadd)

# # #         if WebsitTitle in soup.title.string:
# # #             continue
# # #         else:
# # #             soup.title.string = WebsitTitle

# # #         for link in soup.find_all('link'):
# # #             Linkvalue = link['href']
# # #             if 'http' in Linkvalue:
# # #                 continue
# # #             else:
# # #                 if "{% static '" in Linkvalue:
# # #                     continue
# # #                 else:
# # #                     Linkvalue = str(link['href']).split('/')
# # #                     Linkvalue = Linkvalue[lastIndex(Linkvalue)]
# # #                     if os.path.splitext(Linkvalue)[1] == '.css':
# # #                         url = 'static'
# # #                         link['href'] = "% {} 'css/{}' %".format(url, Linkvalue)
# # #                         link['href'] = "{%s}" % link['href']
# # #                     else:
# # #                         url = 'static'
# # #                         link['href'] = "% {} 'img/{}' %".format(url, Linkvalue)
# # #                         link['href'] = "{%s}" % link['href']



# # #         for img in soup.find_all('img'):
# # #             Imgvalue = img['src']
# # #             if 'http' in Imgvalue:
# # #                 continue
# # #             else:
# # #                 if "{% static '" in Imgvalue:
# # #                     continue
# # #                 else:
# # #                     Imgvalue = str(img['src']).split('/')
# # #                     Imgvalue = Imgvalue[lastIndex(Imgvalue)]
# # #                     url = 'static'
# # #                     img['src'] = "% {} 'img/{}' %".format(url, Imgvalue)
# # #                     img['src'] = "{%s}" %img['src']



# # #         for script in soup.find_all('script'):
# # #             Scriptvalue = script['src']
# # #             if 'http' in Scriptvalue:
# # #                 continue
# # #             else:
# # #                 if "{% static '" in Scriptvalue:
# # #                     continue
# # #                 else:
# # #                     Scriptvalue = str(script['src']).split('/')
# # #                     Scriptvalue = Scriptvalue[lastIndex(Scriptvalue)]
# # #                     url = 'static'
# # #                     script['src'] = "% {} 'js/{}' %".format(url, Scriptvalue)
# # #                     script['src'] = "{%s}" %script['src']





# # #         for a in soup.find_all('a'):
# # #             avalue = a['href']
# # #             if 'http' in avalue or 'mailto' in avalue or 'tel' in avalue or '#' in avalue or avalue == '':
# # #                 continue
# # #             else:
# # #                 if "{% url '" in avalue:
# # #                     continue
# # #                 else:
# # #                     avalue = str(a['href']).split('/')
# # #                     avalue = avalue[lastIndex(avalue)]
# # #                     if os.path.splitext(avalue)[1] == '.html':
# # #                         ill = avalue.split('.')[0]
# # #                         if 'index' in ill:
# # #                             a['href'] = "/"
# # #                         else:
# # #                             l2d = ill.split('-')[0]
# # #                             url = 'url'
# # #                             a['href'] = "% {} '{}' %".format(url, l2d)
# # #                             a['href'] = "{%s}" %a['href']
# # #                     else:
# # #                         url = 'url'
# # #                         a['href'] = "% {} 'img/{}' %".format(url, avalue)
# # #                         a['href'] = "{%s}" %a['href']




# # #         last_value = soup.prettify()

# # #         with open(os.path.join(htmlPath, iT), 'w') as htmlwrite:
# # #             htmlwrite.write(last_value)

# # #         with open(os.path.join(htmlPath, iT), 'r') as htmlread2:
# # #             htmlcontent2 = htmlread2.readlines()

# # #         for count, line in enumerate(htmlcontent2):
# # #             if '</meta>' in line:
# # #                 htmlcontent2[count] = '\n'
# # #             elif '<meta charset="utf-8"' in line:
# # #                 htmlcontent2[count] = '<meta charset="utf-8"/>\n'
# # #             else:
# # #                 continue
            
# # #         htmlwrite2final = "%s" %''.join(map(str, htmlcontent2))
# # #         with open(os.path.join(htmlPath, iT), 'w', encoding='utf-8') as htmlwrite2:
# # #             htmlwrite2.write(htmlwrite2final)




# # def lastIndex(object):
# #     return (len(object) - 1)


# # cssPath = os.path.join(os.path.join(os.path.join(mainPath, projectname), 'static'), 'css')
# # listofcss = os.listdir(cssPath)

# # for cssCount2, iCssMover2 in enumerate(listofcss):
# #     with open(os.path.join(cssPath, iCssMover2)) as cssread2:
# #         cssContent2 = cssread2.readlines()

# #     for lineCount2, cssline2 in enumerate(cssContent2):
# #         if "url(\"" in cssline2 or "url(\'" in cssline2 or "url(" in cssline2:
# #             if ";" in cssline2:
# #                 cssContent2[lineCount2] = cssContent2[lineCount2].replace(";", ';\n')
# #             if ",url(" in cssline2:
# #                 cssContent2[lineCount2] = cssContent2[lineCount2].replace(",url(", ',\nurl')
# #             elif ", url(" in cssline2:
# #                 cssContent2[lineCount2] = cssContent2[lineCount2].replace(", url(", ',\nurl')

                    
# #     finalcss2 = "%s" %''.join(map(str, cssContent2))
# #     with open(os.path.join(cssPath, iCssMover2), 'w') as csswrite2:
# #         csswrite2.write(finalcss2)







# # for cssCount, iCssMover in enumerate(listofcss):
# #     with open(os.path.join(cssPath, iCssMover)) as cssread:
# #         cssContent = cssread.readlines()

# #     for lineCount, cssline in enumerate(cssContent):
# #         if "url(\"" in cssline:
# #                 urlSplit = cssContent[lineCount].split("url(\"", 1)
# #                 bracketSplit = urlSplit[-1].split("\")", 1)
# #                 slashSplit = bracketSplit[0].split("/")
# #                 mainImage = slashSplit[-1]
# #                 if '.jpg' in mainImage or '.png' in mainImage or '.svg' in mainImage or '.jpeg' in mainImage:
# #                     cssContent[lineCount] = "{}url(\"../img/{}\"){}".format(urlSplit[0], mainImage, bracketSplit[-1])
# #                     print(cssContent[lineCount])
# #                 elif '.eot' in mainImage or '.ttf' in mainImage or '.woff' in mainImage or '.woff2' in mainImage or '.eoff' in mainImage or '.eoff2' in mainImage:
# #                     cssContent[lineCount] = "{}url(\"../webfonts/{}\"){}".format(urlSplit[0], mainImage, bracketSplit[-1])
# #                     print(cssContent[lineCount])
# #                 elif '.css' in mainImage:
# #                     cssContent[lineCount] = "{}url(\"../css/{}\"){}".format(urlSplit[0], mainImage, bracketSplit[-1])
# #                     print(cssContent[lineCount])
# #                 else:
# #                     continue

# #         elif "url(\'" in cssline:
# #                 urlSplit = cssContent[lineCount].split("url(\'", 1)
# #                 bracketSplit = urlSplit[-1].split("\')", 1)
# #                 slashSplit = bracketSplit[0].split("/")
# #                 mainImage = slashSplit[-1]
# #                 if '.jpg' in mainImage or '.png' in mainImage or '.svg' in mainImage or '.jpeg' in mainImage:
# #                     cssContent[lineCount] = "{}url(\'../img/{}\'){}".format(urlSplit[0], mainImage, bracketSplit[-1])
# #                     print(cssContent[lineCount])
# #                 elif '.eot' in mainImage or '.ttf' in mainImage or '.woff' in mainImage or '.woff2' in mainImage or '.eoff' in mainImage or '.eoff2' in mainImage:
# #                     cssContent[lineCount] = "{}url(\'../webfonts/{}\'){}".format(urlSplit[0], mainImage, bracketSplit[-1])
# #                     print(cssContent[lineCount])
# #                 elif '.css' in mainImage:
# #                     cssContent[lineCount] = "{}url(\'../css/{}\'){}".format(urlSplit[0], mainImage, bracketSplit[-1])
# #                     print(cssContent[lineCount])
# #                 else:
# #                     continue

# #         elif "url(" in cssline:
# #                 urlSplit = cssContent[lineCount].split("url(", 1)
# #                 bracketSplit = urlSplit[-1].split(")", 1)
# #                 slashSplit = bracketSplit[0].split("/")
# #                 mainImage = slashSplit[-1]
# #                 if '.jpg' in mainImage or '.png' in mainImage or '.svg' in mainImage or '.jpeg' in mainImage:
# #                     cssContent[lineCount] = "{}url(../img/{}){}".format(urlSplit[0], mainImage, bracketSplit[-1])
# #                     print(cssContent[lineCount])
# #                 elif '.eot' in mainImage or '.ttf' in mainImage or '.woff' in mainImage or '.woff2' in mainImage or '.eoff' in mainImage or '.eoff2' in mainImage:
# #                     cssContent[lineCount] = "{}url(../webfonts/{}){}".format(urlSplit[0], mainImage, bracketSplit[-1])
# #                     print(cssContent[lineCount])
# #                 elif '.css' in mainImage:
# #                     cssContent[lineCount] = "{}url(../css/{}){}".format(urlSplit[0], mainImage, bracketSplit[-1])
# #                     print(cssContent[lineCount])
# #                 else:
# #                     continue

                    
# #     finalcss = "%s" %''.join(map(str, cssContent))
# #     with open(os.path.join(cssPath, iCssMover), 'w') as csswrite:
# #         csswrite.write(finalcss)























# for lasthtmliT in listoftemplates:
#     with open(os.path.join(htmlPath, lasthtmliT), 'r', encoding='utf-8') as htmlread3:
#         htmlcontent3 = htmlread3.readlines()

#     for htmlcount, htmllines in enumerate(htmlcontent3):
#         if 'background-image' in htmllines:

#             if 'style=\"background-image' in htmllines:
#                 if "background-image:url" in htmllines:
#                     htmlurlsplitvar0 = htmlcontent3[htmlcount].split('style="background-image:url(')[0]
#                     htmlurlsplitvar1 = htmlcontent3[htmlcount].split('style="background-image:url(')[-1]
#                     if ");\"" in htmlurlsplitvar1:
#                         htmlurlsplitvar2 = htmlurlsplitvar1.split(');\"')[0]
#                         htmlurlsplitvar3 = htmlurlsplitvar1.split(');\"')[-1]
#                         last_split = htmlurlsplitvar2.split('/')[-1]
#                         if "index.html" in  lasthtmliT:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                         else:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(../static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                     elif ")\"" in htmlurlsplitvar1:
#                         htmlurlsplitvar2 = htmlurlsplitvar1.split(')\"')[0]
#                         htmlurlsplitvar3 = htmlurlsplitvar1.split(')\"')[-1]
#                         last_split = htmlurlsplitvar2.split('/')[-1]
#                         if "index.html" in  lasthtmliT:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                         else:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(../static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                     elif ")" in htmlurlsplitvar1:
#                         htmlurlsplitvar2 = htmlurlsplitvar1.split(')')[0]
#                         htmlurlsplitvar3 = htmlurlsplitvar1.split(')')[-1]
#                         last_split = htmlurlsplitvar2.split('/')[-1]
#                         if "index.html" in  lasthtmliT:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                         else:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(../static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)


#                 elif "background-image : url" in htmllines:
#                     htmlurlsplitvar0 = htmlcontent3[htmlcount].split('style="background-image : url(')[0]
#                     htmlurlsplitvar1 = htmlcontent3[htmlcount].split('style="background-image : url(')[-1]
#                     if ");\"" in htmlurlsplitvar1:
#                         htmlurlsplitvar2 = htmlurlsplitvar1.split(');\"')[0]
#                         htmlurlsplitvar3 = htmlurlsplitvar1.split(');\"')[-1]
#                         last_split = htmlurlsplitvar2.split('/')[-1]
#                         if "index.html" in  lasthtmliT:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                         else:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(../static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                     elif ")\"" in htmlurlsplitvar1:
#                         htmlurlsplitvar2 = htmlurlsplitvar1.split(')\"')[0]
#                         htmlurlsplitvar3 = htmlurlsplitvar1.split(')\"')[-1]
#                         last_split = htmlurlsplitvar2.split('/')[-1]
#                         if "index.html" in  lasthtmliT:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                         else:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(../static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                     elif ")" in htmlurlsplitvar1:
#                         htmlurlsplitvar2 = htmlurlsplitvar1.split(')')[0]
#                         htmlurlsplitvar3 = htmlurlsplitvar1.split(')')[-1]
#                         last_split = htmlurlsplitvar2.split('/')[-1]
#                         if "index.html" in  lasthtmliT:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                         else:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(../static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)

#                 elif "background-image: url" in htmllines:
#                     htmlurlsplitvar0 = htmlcontent3[htmlcount].split('style="background-image: url(')[0]
#                     htmlurlsplitvar1 = htmlcontent3[htmlcount].split('style="background-image: url(')[-1]
#                     if ");\"" in htmlurlsplitvar1:
#                         htmlurlsplitvar2 = htmlurlsplitvar1.split(');\"')[0]
#                         htmlurlsplitvar3 = htmlurlsplitvar1.split(');\"')[-1]
#                         last_split = htmlurlsplitvar2.split('/')[-1]
#                         if "index.html" in  lasthtmliT:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                         else:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(../static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                     elif ")\"" in htmlurlsplitvar1:
#                         htmlurlsplitvar2 = htmlurlsplitvar1.split(')\"')[0]
#                         htmlurlsplitvar3 = htmlurlsplitvar1.split(')\"')[-1]
#                         last_split = htmlurlsplitvar2.split('/')[-1]
#                         if "index.html" in  lasthtmliT:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                         else:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(../static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                     elif ")" in htmlurlsplitvar1:
#                         htmlurlsplitvar2 = htmlurlsplitvar1.split(')')[0]
#                         htmlurlsplitvar3 = htmlurlsplitvar1.split(')')[-1]
#                         last_split = htmlurlsplitvar2.split('/')[-1]
#                         if "index.html" in  lasthtmliT:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                         else:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(../static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)

#                 elif "background-image :url" in htmllines:
#                     htmlurlsplitvar0 = htmlcontent3[htmlcount].split('style="background-image :url(')[0]
#                     htmlurlsplitvar1 = htmlcontent3[htmlcount].split('style="background-image :url(')[-1]
#                     if ");\"" in htmlurlsplitvar1:
#                         htmlurlsplitvar2 = htmlurlsplitvar1.split(');\"')[0]
#                         htmlurlsplitvar3 = htmlurlsplitvar1.split(');\"')[-1]
#                         last_split = htmlurlsplitvar2.split('/')[-1]
#                         if "index.html" in  lasthtmliT:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                         else:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(../static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                     elif ")\"" in htmlurlsplitvar1:
#                         htmlurlsplitvar2 = htmlurlsplitvar1.split(')\"')[0]
#                         htmlurlsplitvar3 = htmlurlsplitvar1.split(')\"')[-1]
#                         last_split = htmlurlsplitvar2.split('/')[-1]
#                         if "index.html" in  lasthtmliT:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                         else:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(../static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                     elif ")" in htmlurlsplitvar1:
#                         htmlurlsplitvar2 = htmlurlsplitvar1.split(')')[0]
#                         htmlurlsplitvar3 = htmlurlsplitvar1.split(')')[-1]
#                         last_split = htmlurlsplitvar2.split('/')[-1]
#                         if "index.html" in  lasthtmliT:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                         else:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(../static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
              

#             elif 'style=\'background-image' in htmllines:
#                 if "background-image:url" in htmllines:
#                     htmlurlsplitvar0 = htmlcontent3[htmlcount].split('style=\'background-image:url(')[0]
#                     htmlurlsplitvar1 = htmlcontent3[htmlcount].split('style=\'background-image:url(')[-1]
#                     if ");\'" in htmlurlsplitvar1:
#                         htmlurlsplitvar2 = htmlurlsplitvar1.split(');\'')[0]
#                         htmlurlsplitvar3 = htmlurlsplitvar1.split(');\'')[-1]
#                         last_split = htmlurlsplitvar2.split('/')[-1]
#                         if "index.html" in  lasthtmliT:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                         else:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(../static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                     elif ")\'" in htmlurlsplitvar1:
#                         htmlurlsplitvar2 = htmlurlsplitvar1.split(')\'')[0]
#                         htmlurlsplitvar3 = htmlurlsplitvar1.split(')\'')[-1]
#                         last_split = htmlurlsplitvar2.split('/')[-1]
#                         if "index.html" in  lasthtmliT:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                         else:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(../static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                     elif ")" in htmlurlsplitvar1:
#                         htmlurlsplitvar2 = htmlurlsplitvar1.split(')')[0]
#                         htmlurlsplitvar3 = htmlurlsplitvar1.split(')')[-1]
#                         last_split = htmlurlsplitvar2.split('/')[-1]
#                         if "index.html" in  lasthtmliT:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                         else:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(../static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)

#                 elif "background-image : url" in htmllines:
#                     htmlurlsplitvar0 = htmlcontent3[htmlcount].split('style=\'background-image : url(')[0]
#                     htmlurlsplitvar1 = htmlcontent3[htmlcount].split('style=\'background-image : url(')[-1]
#                     if ");\'" in htmlurlsplitvar1:
#                         htmlurlsplitvar2 = htmlurlsplitvar1.split(');\'')[0]
#                         htmlurlsplitvar3 = htmlurlsplitvar1.split(');\'')[-1]
#                         last_split = htmlurlsplitvar2.split('/')[-1]
#                         if "index.html" in  lasthtmliT:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                         else:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(../static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                     elif ")\'" in htmlurlsplitvar1:
#                         htmlurlsplitvar2 = htmlurlsplitvar1.split(')\'')[0]
#                         htmlurlsplitvar3 = htmlurlsplitvar1.split(')\'')[-1]
#                         last_split = htmlurlsplitvar2.split('/')[-1]
#                         if "index.html" in  lasthtmliT:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                         else:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(../static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                     elif ")" in htmlurlsplitvar1:
#                         htmlurlsplitvar2 = htmlurlsplitvar1.split(')')[0]
#                         htmlurlsplitvar3 = htmlurlsplitvar1.split(')')[-1]
#                         last_split = htmlurlsplitvar2.split('/')[-1]
#                         if "index.html" in  lasthtmliT:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                         else:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(../static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)

#                 elif "background-image: url" in htmllines:
#                     htmlurlsplitvar0 = htmlcontent3[htmlcount].split('style=\'background-image: url(')[0]
#                     htmlurlsplitvar1 = htmlcontent3[htmlcount].split('style=\'background-image: url(')[-1]
#                     if ");\'" in htmlurlsplitvar1:
#                         htmlurlsplitvar2 = htmlurlsplitvar1.split(');\'')[0]
#                         htmlurlsplitvar3 = htmlurlsplitvar1.split(');\'')[-1]
#                         last_split = htmlurlsplitvar2.split('/')[-1]
#                         if "index.html" in  lasthtmliT:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                         else:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(../static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                     elif ")\'" in htmlurlsplitvar1:
#                         htmlurlsplitvar2 = htmlurlsplitvar1.split(')\'')[0]
#                         htmlurlsplitvar3 = htmlurlsplitvar1.split(')\'')[-1]
#                         last_split = htmlurlsplitvar2.split('/')[-1]
#                         if "index.html" in  lasthtmliT:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                         else:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(../static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                     elif ")" in htmlurlsplitvar1:
#                         htmlurlsplitvar2 = htmlurlsplitvar1.split(')')[0]
#                         htmlurlsplitvar3 = htmlurlsplitvar1.split(')')[-1]
#                         last_split = htmlurlsplitvar2.split('/')[-1]
#                         if "index.html" in  lasthtmliT:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                         else:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(../static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)

#                 elif "background-image :url" in htmllines:
#                     htmlurlsplitvar0 = htmlcontent3[htmlcount].split('style=\'background-image :url(')[0]
#                     htmlurlsplitvar1 = htmlcontent3[htmlcount].split('style=\'background-image :url(')[-1]
#                     if ");\'" in htmlurlsplitvar1:
#                         htmlurlsplitvar2 = htmlurlsplitvar1.split(');\'')[0]
#                         htmlurlsplitvar3 = htmlurlsplitvar1.split(');\'')[-1]
#                         last_split = htmlurlsplitvar2.split('/')[-1]
#                         if "index.html" in  lasthtmliT:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                         else:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(../static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                     elif ")\'" in htmlurlsplitvar1:
#                         htmlurlsplitvar2 = htmlurlsplitvar1.split(')\'')[0]
#                         htmlurlsplitvar3 = htmlurlsplitvar1.split(')\'')[-1]
#                         last_split = htmlurlsplitvar2.split('/')[-1]
#                         if "index.html" in  lasthtmliT:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                         else:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(../static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                     elif ")" in htmlurlsplitvar1:
#                         htmlurlsplitvar2 = htmlurlsplitvar1.split(')')[0]
#                         htmlurlsplitvar3 = htmlurlsplitvar1.split(')')[-1]
#                         last_split = htmlurlsplitvar2.split('/')[-1]
#                         if "index.html" in  lasthtmliT:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)
#                         else:
#                             htmlcontent3[htmlcount] = "{}style='background-image:url(../static/img/{})'{}".format(htmlurlsplitvar0, last_split, htmlurlsplitvar3)


#     finalhtml = "%s" %''.join(map(str, htmlcontent3))
#     with open(os.path.join(htmlPath, lasthtmliT), 'w', encoding='utf-8') as htmlwrite:
#         htmlwrite.write(finalhtml)




































import os
mainPath = os.getcwd()
projectname = 'djangoalotan'



# with open(os.path.join(os.path.join(mainPath, projectname), 'browser.py'), 'w') as browserbatch:
#     browserbatch.write("import webbrowser\n\n\n\nWeburl = 'http://127.0.0.1:8000'\n\nchrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'\n\nwebbrowser.get(chrome_path).open_new(Weburl)\n")
    



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






htmlPath = os.path.join(os.path.join(mainPath, projectname), 'templates')
listoftemplates = os.listdir(htmlPath)

WebsitTitle = 'djangotest'
def lastIndex(object):
    return (len(object) - 1)

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