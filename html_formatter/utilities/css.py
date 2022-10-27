import os


def css(cssPath: str) -> bool:
    try:
        listofcss = os.listdir(cssPath)
        for cssCount2, iCssMover2 in enumerate(listofcss):
            with open(os.path.join(cssPath, iCssMover2), 'r', encoding='utf-8') as cssread2:
                cssContent2 = cssread2.readlines()

            for lineCount2, cssline2 in enumerate(cssContent2):
                if ";src" in cssline2:
                    cssContent2[lineCount2] = cssContent2[lineCount2].replace(
                        ";src", ';\nsrc')
                if "; src" in cssline2:
                    cssContent2[lineCount2] = cssContent2[lineCount2].replace(
                        "; src", ';\nsrc')
                if ",url" in cssline2:
                    cssContent2[lineCount2] = cssContent2[lineCount2].replace(
                        ",url", ',\nurl')
                if ", url" in cssline2:
                    cssContent2[lineCount2] = cssContent2[lineCount2].replace(
                        ", url", ',\nurl')

            finalcss2 = "%s" % ''.join(map(str, cssContent2))
            with open(os.path.join(cssPath, iCssMover2), 'w', encoding='utf-8') as csswrite2:
                csswrite2.write(finalcss2)

        for cssCount, iCssMover in enumerate(listofcss):
            with open(os.path.join(cssPath, iCssMover), 'r', encoding='utf-8') as cssread:
                cssContent = cssread.readlines()

            for lineCount, cssline in enumerate(cssContent):
                if "url(\"" in cssline:
                    urlSplit = cssContent[lineCount].split("url(\"", 1)
                    bracketSplit = urlSplit[-1].split("\")", 1)
                    slashSplit = bracketSplit[0].split("/")
                    mainImage = slashSplit[-1]
                    if '.jpg' in mainImage or '.png' in mainImage or '.svg' in mainImage or '.jpeg' in mainImage:
                        cssContent[lineCount] = "{}url(\"../images/{}\"){}".format(
                            urlSplit[0], mainImage, bracketSplit[-1])
                    elif '.eot' in mainImage or '.ttf' in mainImage or '.woff' in mainImage or '.woff2' in mainImage or '.eoff' in mainImage or '.eoff2' in mainImage:
                        cssContent[lineCount] = "{}url(\"../webfonts/{}\"){}".format(
                            urlSplit[0], mainImage, bracketSplit[-1])
                    elif '.css' in mainImage:
                        cssContent[lineCount] = "{}url(\"../css/{}\"){}".format(
                            urlSplit[0], mainImage, bracketSplit[-1])
                    else:
                        continue

                elif "url(\'" in cssline:
                    urlSplit = cssContent[lineCount].split("url(\'", 1)
                    bracketSplit = urlSplit[-1].split("\')", 1)
                    slashSplit = bracketSplit[0].split("/")
                    mainImage = slashSplit[-1]
                    if '.jpg' in mainImage or '.png' in mainImage or '.svg' in mainImage or '.jpeg' in mainImage:
                        cssContent[lineCount] = "{}url(\'../images/{}\'){}".format(
                            urlSplit[0], mainImage, bracketSplit[-1])
                    elif '.eot' in mainImage or '.ttf' in mainImage or '.woff' in mainImage or '.woff2' in mainImage or '.eoff' in mainImage or '.eoff2' in mainImage:
                        cssContent[lineCount] = "{}url(\'../webfonts/{}\'){}".format(
                            urlSplit[0], mainImage, bracketSplit[-1])
                    elif '.css' in mainImage:
                        cssContent[lineCount] = "{}url(\'../css/{}\'){}".format(
                            urlSplit[0], mainImage, bracketSplit[-1])
                    else:
                        continue

                elif "url(" in cssline:
                    urlSplit = cssContent[lineCount].split("url(", 1)
                    bracketSplit = urlSplit[-1].split(")", 1)
                    slashSplit = bracketSplit[0].split("/")
                    mainImage = slashSplit[-1]
                    if '.jpg' in mainImage or '.png' in mainImage or '.svg' in mainImage or '.jpeg' in mainImage:
                        cssContent[lineCount] = "{}url(../images/{}){}".format(
                            urlSplit[0], mainImage, bracketSplit[-1])
                    elif '.eot' in mainImage or '.ttf' in mainImage or '.woff' in mainImage or '.woff2' in mainImage or '.eoff' in mainImage or '.eoff2' in mainImage:
                        cssContent[lineCount] = "{}url(../webfonts/{}){}".format(
                            urlSplit[0], mainImage, bracketSplit[-1])
                    elif '.css' in mainImage:
                        cssContent[lineCount] = "{}url(../css/{}){}".format(
                            urlSplit[0], mainImage, bracketSplit[-1])
                    else:
                        continue

            finalcss = "%s" % ''.join(map(str, cssContent))
            with open(os.path.join(cssPath, iCssMover), 'w', encoding='utf-8') as csswrite:
                csswrite.write(finalcss)
        return True
    except Exception as err:
        print('Css Error: ', err.__class__.__name__)
        return False
