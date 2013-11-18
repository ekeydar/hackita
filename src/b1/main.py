import bottle
import os
from bottle import route, run, template, post,request, redirect

tpl_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)),"templates")

print tpl_dir

bottle.TEMPLATE_PATH = [tpl_dir] 

def multi(n):
    return [[i*j for i in xrange(1,n+1)] for j in xrange(1,n+1)]


@post('/multi')
def create_multi():
    num = int(request.POST['num'])
    return redirect('/multi/%d' % num)
    

@route('/multi/<num:int>')
def get_multi(num):
    return get_multi_html(num)

def get_multi_html(num):
    return template('multi.html',num=num,table=multi(num))

@route('/')
def index():
    return template('form.html')

bottle.TEMPLATES.clear()
run(host='localhost', port=8080,reloader=True)

