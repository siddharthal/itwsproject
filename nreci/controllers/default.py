# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################
@auth.requires_login()
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
        """
    recipes=db().select(db.recipe.id,db.recipe.title,db.recipe.summary,db.recipe.image,orderby=~db.recipe.created_on)
    return dict(recipes=recipes)
@auth.requires_login()
def create():
    form=SQLFORM(db.recipe).process(next=URL('index'))
    return dict(form=form)
@auth.requires_login()
def show():
    this_page = db.recipe(request.args(0,cast=int)) or redirect(URL('index'))
    return dict(recipe=this_page)
@auth.requires_login()
def mrecis():
    recipes=db(db.recipe.created_by==auth.user_id).select(db.recipe.id,db.recipe.title,db.recipe.summary,db.recipe.image)
    return dict(recipes=recipes)
@auth.requires_login()
@auth.requires_login()
def edit():
    this_page = db.recipe(request.args(0,cast=int)) or redirect(URL('index'))
    form = SQLFORM(db.recipe, this_page).process(next = URL('show',args=request.args))
    return dict(form=form)
def register():
    return dict(form=auth.register())
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
