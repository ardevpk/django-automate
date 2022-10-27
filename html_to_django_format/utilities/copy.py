import shutil
import os
import glob


def copyAllfiles(assetsPath: str, currentPath: str, convertedProjectHtmlPath: str, cssPath: str) -> bool:
    try:
        imagesPath = os.path.join(assetsPath, 'images')
        jsPath = os.path.join(assetsPath, 'js')
        webfontPath = os.path.join(assetsPath, 'webfonts')
        otherPath = os.path.join(assetsPath, 'other')

        class fileSearcher():

            def __init__(self, ext, dotext):
                self.ext = glob.glob(
                    currentPath + '/**/*.{}'.format(ext), recursive=True)
                self.dotext = dotext

            def path(self):
                if self.ext:
                    for file in self.ext:
                        if os.path.exists(os.path.join(currentPath, file)): return True
                        else: return False
                else:
                    print(f"There is no {self.dotext} file!")

            def fileMover(self):
                if self.path() is True:
                    extension = str(self.dotext).replace('.', '').capitalize()
                    print(f'{extension} files moving...')
                    for ifileMover in self.ext:
                        try:
                            iPath = os.path.join(currentPath, ifileMover)
                            if os.path.isfile(iPath):
                                if self.dotext == '.html':
                                    shutil.copy2(iPath, convertedProjectHtmlPath)
                                elif self.dotext == '.css':
                                    shutil.copy2(iPath, cssPath)
                                elif self.dotext == '.js':
                                    shutil.copy2(iPath, jsPath)
                                elif self.dotext == '.jpg' or self.dotext == '.jpeg' or self.dotext == '.svg' or self.dotext == '.png' or self.dotext == '.pdf' or self.dotext == '.ico' or self.dotext == '.gif':
                                    shutil.copy2(iPath, imagesPath)
                                elif self.dotext == '.eoff' or self.dotext == '.eoff2' or self.dotext == '.eot' or self.dotext == '.woff' or self.dotext == '.woff2' or self.dotext == '.ttf':
                                    shutil.copy2(iPath, webfontPath)
                                else:
                                    shutil.copy2(iPath, otherPath)
                            else:
                                continue
                        except shutil.Error:
                            print('Shutil Error: {}'.format(shutil.Error))
                            continue
                        except FileNotFoundError:
                            print('File: {}, Not Found: {}'.format(
                                ifileMover, FileNotFoundError))
                            continue
                        except PermissionError:
                            print('Permision Error On: {}\nError is: {}'.format(
                                iPath, PermissionError))
                            continue
                        except shutil.SameFileError:
                            print('File: {} Already Exist, Error: {}'.format(
                                ifileMover, shutil.SameFileError))
                            continue

        fileSearcher('html', '.html').fileMover()
        fileSearcher('css', '.css').fileMover()
        fileSearcher('js', '.js').fileMover()
        fileSearcher('jpg', '.jpg').fileMover()
        fileSearcher('jpeg', '.jpeg').fileMover()
        fileSearcher('png', '.png').fileMover()
        fileSearcher('ico', '.ico').fileMover()
        fileSearcher('pdf', '.pdf').fileMover()
        fileSearcher('svg', '.svg').fileMover()
        fileSearcher('gif', '.gif').fileMover()
        fileSearcher('eot', '.eot').fileMover()
        fileSearcher('eoff', '.eoff').fileMover()
        fileSearcher('eoff2', '.eoff2').fileMover()
        fileSearcher('woff', '.woff').fileMover()
        fileSearcher('woff2', '.woff2').fileMover()
        fileSearcher('ttf', '.ttf').fileMover()
        fileSearcher('scss', '.scss').fileMover()
        fileSearcher('sass', '.sass').fileMover()
        return True
    except Exception as err:
        print('Copy Error: ', err.__class__.__name__)
        return False
