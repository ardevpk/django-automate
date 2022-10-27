from pick import pick
from static_to_dynamic.main import static_to_dynamic
from html_formatter.main import htmlformat
from html_to_django_format.main import htmltodjango


title = 'Please choose which tool you wants to use: '
options = ['Static to dynamic!', 'Html formatter!', 'Html to django format!', 'New project!', 'Deployment!']
option, index = pick(options, title, indicator='=>', default_index=0)
functions = [static_to_dynamic, htmlformat, htmltodjango]
functions[index]()
# functions[2]()
