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
    session.lt1=0
    session.lt2=5
    lt1=session.lt1;
    lt2=session.lt2;
    query=db(db.recipe.id>0).count()
    session.query=query;
    recipes=db().select(db.recipe.id,db.recipe.title,db.recipe.votes,db.recipe.summary,db.recipe.serves,db.recipe.preparation_time,db.recipe.image,db.recipe.created_on,db.recipe.created_by,orderby=~db.recipe.created_on,limitby=(lt1,lt2))
    return dict(recipes=recipes)
@auth.requires_login()
def next():
    session.lt1+=5
    session.lt2+=5
    if session.lt1>=session.query:
        session.lt1-=5
        session.lt2-=5
    recipes=db().select(db.recipe.id,db.recipe.title,db.recipe.summary,db.recipe.votes,db.recipe.serves,db.recipe.preparation_time,db.recipe.image,db.recipe.created_on,db.recipe.created_by,orderby=~db.recipe.created_on,limitby=(session.lt1,session.lt2))
    return dict(recipes=recipes)
@auth.requires_login()
def previous():
    session.lt1-=5
    session.lt2-=5
    if session.lt1<=0:
        return index()
    recipes=db().select(db.recipe.id,db.recipe.title,db.recipe.summary,db.recipe.serves,db.recipe.votes,db.recipe.preparation_time,db.recipe.image,db.recipe.created_on,db.recipe.created_by,orderby=~db.recipe.created_on,limitby=(session.lt1,session.lt2))
    return dict(recipes=recipes)
@auth.requires_login()
def create():
    form=SQLFORM(db.recipe).process(next=URL('index'))
    return dict(form=form)
@auth.requires_login()
def show():
    this_page = db.recipe(request.args(0,cast=int)) or redirect(URL('index'))
    session.page_id=this_page.id
    session.count=db((db.like.created_by==auth.user_id) & (db.like.liked_page==this_page.id) ).count()
    if session.count == 0:
        var='Like'
    else:
        var='Unlike'
    return dict(recipe=this_page,var=var)
def Like():
    this_page=db.recipe(session.page_id)
    session.count=db((db.like.created_by==auth.user_id) & (db.like.liked_page==this_page.id) ).count()
    if session.count==0:
            likes=this_page.votes+1
            response.flash=T('You have liked this recipe')
            db.like.insert(liked_page=this_page.id,created_by=auth.user_id)
            db(db.recipe.id==session.page_id).update(votes=likes)
    var='Unlike'
    this_page=db.recipe(session.page_id)
    return dict(recipe=this_page,var=var)
def Unlike():
    this_page=db.recipe(session.page_id)
    session.count=db((db.like.created_by==auth.user_id) & (db.like.liked_page==this_page.id )).count()
    if session.count==1:
            likes=this_page.votes-1
            response.flash=T('You have unliked this recipe')
            db(db.like.created_by==auth.user.id and db.like.liked_page==session.page_id).delete()
            db(db.recipe.id==session.page_id).update(votes=likes)
    var='Like'
    this_page=db.recipe(session.page_id)
    return dict(recipe=this_page,var=var)
@auth.requires_login()
def mrecis():
    recipes=db(db.recipe.created_by==auth.user.id).select(db.recipe.id,db.recipe.title,db.recipe.summary,db.recipe.votes,db.recipe.serves,db.recipe.preparation_time,db.recipe.image,db.recipe.created_on,db.recipe.created_by,orderby=~db.recipe.created_on)
    return dict(recipes=recipes)
@auth.requires_login()
@auth.requires_login()
def edit():
    this_page = db.recipe(request.args(0,cast=int)) or redirect(URL('index'))
    form = SQLFORM(db.recipe, this_page).process(next = URL('show',args=request.args))
    return dict(form=form)
def vote():
    recipe = db.recipe[request.vars.id]
    new_votes = recipe.votes + 1
    recipe.update_record(votes=new_votes)
    return str(new_votes)
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
