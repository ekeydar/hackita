import cgi
def html_table(l):
    return '<table>\n' + '\n'.join([line_to_tr(item) for item in l]) + '\n<table>\n'

def line_to_tr(item): 
    (key,value) = item
    escaped_key = cgi.escape(key)
    escaped_value = cgi.escape(value)
    return ('<tr>' + '<td>' + escaped_key + 
            '</td></td>' + escaped_value + '</tr>')

