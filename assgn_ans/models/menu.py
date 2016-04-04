# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('Cuisine'),XML('&trade;&nbsp;'),
                  _class="navbar-brand",_href="http://127.0.0.1:8000/assgn_ans/",
                  _id="web2py-logo")
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'yshivaganesh25@gmail.com'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('myrecipes'),False,URL('default','myrecipe'),[]),
    (T('upload'),False,URL('default','create_post')),
    
]

if auth.has_membership('admin'):
    response.menu.append((T('admin'),False,URL('default','manage')))
#########################################################################
## provide shortcuts for development. remove in production
################################
if "auth" in locals(): auth.wikimenu()
