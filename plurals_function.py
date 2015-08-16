import re

def plural(noun):
    if re.search('[sxz]$', noun):
        return re.sub('$', 'es', noun)
    elif re.search('[^aeioudgkprt]h$', noun):
        return re.sub('$', 'es', noun)
    elif re.search('y$', noun):
        return re.sub('$', 'ies', noun)
    else:
        return noun + 's'
        
print plural('inch')
