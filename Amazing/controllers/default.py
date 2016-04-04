def index():
    return dict()
postperpage=10
@auth.requires_login()
def main():
    response.view='default/main.html'
    page=request.args(0,cast=int,default=0)
    start=page*postperpage
    stop=start+postperpage
    rows = db().select(db.image.ALL,orderby=~db.image.created_on,limitby=(start,stop))
    return locals()

def user():
    return dict(form=auth())

def create_post():
    form = SQLFORM(db.image)
    if form.process().accepted:
        redirect(URL('main',vars=dict(id=form.vars.id)))
    return dict(form=form)
def manage():
    grid = SQLFORM.grid(db.image)
    return locals()

@cache.action()
def download():
    return response.download(request, db)


#def call():
 #   return service()
def show():
        image = db.image(request.args(0,cast=int)) or redirect(URL('main'))
        return dict(image=image)
def myrecipe():
    response.view='default/myrecipe.html'
    page=request.args(0,cast=int,default=0)
    start=page*postperpage
    stop=start+postperpage
    rows = db(db.image.imageid==auth.user_id).select(db.image.ALL,orderby=~db.image.created_on,limitby=(start,stop))
    return locals()

def editrecipes():
    id=request.args(0,cast=int)
    form=SQLFORM(db.image,id)
    if form.process().accepted:
        redirect(URL('myrecipe',vars=dict(id=form.vars.id)))
    return dict(form=form)

def vote_callback():
    vars=request.post_vars
    if vars and auth.user:
        id=vars.id
        direction1=+1 if vars.direction=="up" else -1
        image=db.image(id)
        if image:
            vote=db.vote(image_id=id,posted_by=auth.user.id)
            if not vote:
                image.update_record(votes=int(image.votes)+direction1)
                db.vote.insert(image_id=id,score=direction1,posted_by=auth.user.id)
            elif vote.score!=direction1:
                image.update_record(votes=int(image.votes)+direction1*2)
                vote.update_record(score=direction1)
            else:
                pass
        print image.votes
    return str(image.votes)
def delete():
    iddelete=request.args(0)
    query = db(db.image.id==request.args(0)).select().first()  
    remove = db(db.image.id==query).delete()
    if remove:
        redirect(URL('myrecipe'))
    return dict(remove=remove)
