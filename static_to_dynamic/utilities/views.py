import os


def wrtingViewsFile(appPath:str, listoftemplates:list[str]) -> bool:
    try:
        finalstrforviews = []
        def returnStringforviews(list):
            for iViews in list:
                l = str(iViews.split('.')[0])
                # l = l.split('-')[0]
                l = l.replace('-', '_')
                if l.isdigit(): l = f'N{l}'
                viewsOneFile = "\n\ndef {}(request):\n\treturn render(request, '{}')\n".format(l, iViews)
                finalstrforviews.append(viewsOneFile)
        returnStringforviews(listoftemplates)
        finalstrforviewsmain = ('%s' % ''.join(map(str, finalstrforviews)))
        viewContent = (f"from django.shortcuts import render\n{finalstrforviewsmain}")
        with open(os.path.join(appPath, 'views.py'), 'w') as vieww:
            vieww.write(viewContent)
        return True
    except Exception as err:
        print('Views Error: ', err.__class__.__name__)
        return False
