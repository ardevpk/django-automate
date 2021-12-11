
# import os

# mainPath = os.getcwd()
# projectname = 'djangospify'
# htmlPath = os.path.join(os.path.join(mainPath, projectname), 'templates')


# def lastIndex(object):
#     return (len(object) - 1)

# cssPath = os.path.join(os.path.join(os.path.join(mainPath, projectname), 'static'), 'css')

# listofcss = os.listdir(cssPath)

# for cssCount, iCssMover in enumerate(listofcss):
#     # print(i)
#     with open(os.path.join(cssPath, iCssMover)) as cssread:
#         cssContent = cssread.readlines()
    
#     for lineCount, cssline in enumerate(cssContent):
#         if "url(\"" in cssline:
#             if '.eot' in cssline or '.ttf' in cssline or '.woff' in cssline or '.woff2' in cssline or '.eoff' in cssline or '.eoff2' in cssline:
#                 # cssContent[lineCount].strip('\n')
#                 urlSplit = cssContent[lineCount].split("url(\"", 1)
#                 bracketSplit3 = urlSplit[lastIndex(urlSplit)].split("\")", 1)
#                 slashSplit0 = bracketSplit3[0].split("/")
#                 mainImage = slashSplit0[lastIndex(slashSplit0)]
#                 cssContent[lineCount] = "{}url(\"static/webfonts/{}\"){}".format(urlSplit[0], mainImage, bracketSplit3[lastIndex(bracketSplit3)])
#                     # cssContent[lineCount] = "{}url(\"static/webfonts/{}\"){}".format(urlSplit0, mainImage, "".join(map(str, bracketSplit3)))
#                 print(cssContent[lineCount])



            
#         # elif "url(\'" in cssline:

#         #     if '.jpg' in cssline or '.png' in cssline or '.svg' in cssline or '.jpeg' in cssline:
#         #         urlSplit0 = cssContent[lineCount].split("url(\'")[0]
#         #         urlSplit1 = cssContent[lineCount].split("url(\'")
#         #         bracketSplit2 = urlSplit1[lastIndex(urlSplit1)].split("\')")[0]
#         #         bracketSplit3 = urlSplit1[lastIndex(urlSplit1)].split("\')")
#         #         slashSplit0 = bracketSplit2.split("/")
#         #         mainImage = slashSplit0[lastIndex(slashSplit0)]
#         #         if '.jpg' in mainImage or '.png' in mainImage or '.svg' in mainImage or '.jpeg' in mainImage:
#         #             cssContent[lineCount] = "{}url(\"static/img/{}\"){}".format(urlSplit0, mainImage, "".join(map(str, bracketSplit3[1:])))
#         #             print(cssContent[lineCount])
#         #         else:
#         #             continue
            


#         #     elif '.eot' in cssline or '.ttf' in cssline or '.woff' in cssline or '.woff2' in cssline or '.eoff' in cssline or '.eoff2' in cssline:
#         #         # cssContent[lineCount].strip('\n')
#         #         urlSplit0 = cssContent[lineCount].split("url(\'", 1)[0]
#         #         urlSplit1 = cssContent[lineCount].split("url(\'", 1)
#         #         bracketSplit2 = urlSplit1[lastIndex(urlSplit1)].split("\')", 1)[0]
#         #         bracketSplit3 = urlSplit1[lastIndex(urlSplit1)].split("\')", 1)
#         #         slashSplit0 = bracketSplit2.split("/")
#         #         mainImage = slashSplit0[lastIndex(slashSplit0)]
#         #         if '.eot' in mainImage or '.ttf' in mainImage or '.woff' in mainImage or '.woff2' in mainImage or 'eoff' in mainImage or 'eoff2' in mainImage:
#         #             cssContent[lineCount] = "{}url(\"static/webfonts/{}\"){}".format(urlSplit0, mainImage, "".join(map(str, bracketSplit3)))
#         #             # cssContent[lineCount] = "{}url(\"static/webfonts/{}\"){}".format(urlSplit0, mainImage, "".join(map(str, bracketSplit3)))
#         #             print(cssContent[lineCount])
#         #         else:
#         #             continue

                    
            
            
            
            
        


#     finalcss = "%s" %''.join(map(str, cssContent))
#     with open(os.path.join(cssPath, iCssMover), 'w') as csswrite:
#         csswrite.write(finalcss)

# import re
    

# listMain = 'src:url(\'../fonts/fontawesome-webfont.eot?v=4.7.0\');src:url(\'../fonts/fontawesome-webfont.eot?#iefix&v=4.7.0\') format(\'embedded-opentype\'),url(\'../fonts/fontawesome-webfont.woff2?v=4.7.0\') format(\'woff2\'),url(\'../fonts/fontawesome-webfont.woff?v=4.7.0\') format(\'woff\')'


# for count, f in enumerate(listMain):
#     if listMain[count] == 'u' and listMain[count+1] == 'r' and listMain[count+2] == 'l':
#         matched = re.findall('url', listMain)
#         print(matched)
#         # print(listMain[count:count+3])
        






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
    if "background-url:url(\"" in xr:
        return "background-url:url(\""

    elif "background-url: url(\"" in xr:
        return "background-url: url(\""

    elif "background-url : url(\"" in xr:
        return "background-url : url(\""

    elif "background-url :url(\"" in xr:
        return "background-url :url(\""

    elif "background-url:url(\'" in xr:
        return "background-url:url(\'"

    elif "background-url: url(\'" in xr:
        return "background-url: url(\'"

    elif "background-url : url(\'" in xr:
        return "background-url : url(\'"

    elif "background-url :url(\'" in xr:
        return "background-url :url(\'"

    elif "background-url:url(" in xr:
        return "background-url:url("

    elif "background-url: url(" in xr:
        return "background-url: url("

    elif "background-url : url(" in xr:
        return "background-url : url("

    elif "background-url :url(" in xr:
        return "background-url :url("



listMain = ("adsaaaaaaaaaaaaaaaaaaa( asafsfas()\' ()adhasdhasdha sdajsdjaw297056163584087%(%&)&%^$$(")



print(returnstringValue(listMain))