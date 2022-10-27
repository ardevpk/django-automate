import os


def wrtingUrlsFile(corePath:str, appPath:str, listoftemplates:list[str]) -> bool:
    try:
        finalstrforurls = []
        def returnstringforurls(list):
            for iurls in list:
                l = str(iurls.split('.')[0])
                # l = l.split('-')[0]
                lfunc = l.replace('-', '_')
                if lfunc.isdigit(): lfunc = f'N{l}'
                if 'index' in l:
                    urlsOneFile = "\n\tpath('', views.{}, name=\'{}\')".format(lfunc, l)
                else:
                    urlsOneFile = "\n\tpath('{}/', views.{}, name=\'{}\')".format(l, lfunc, l)
                finalstrforurls.append(urlsOneFile)

        returnstringforurls(listoftemplates)
        finalstrforurls2 = ('%s' % ', '.join(map(str, finalstrforurls)))
        finalstrforurlscore = (f"from django.contrib import admin\nfrom django.urls import path, include\nfrom django.conf import settings\nfrom django.conf.urls.static import static\n\nurlpatterns = [\n\tpath('admin/', admin.site.urls),\n\tpath('', include('app.urls')),\n] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\n")
        finalstrforurlapp = (f"from django.urls import path\nfrom . import views\n\nurlpatterns = [{finalstrforurls2},\n]\n")

        with open(os.path.join(corePath, 'urls.py'), 'w') as urlf:
            urlf.writelines(finalstrforurlscore)

        with open(os.path.join(appPath, 'urls.py'), 'w') as urlw:
            urlw.writelines(finalstrforurlapp)

        return True
    except Exception as err:
        print('Urls Error: ', err.__class__.__name__)
        return False
