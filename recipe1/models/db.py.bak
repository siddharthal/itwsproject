db =DAL('sqlite://storage.sqlite')
from gluon.tools import *
auth=Auth(db)
auth.define_tables()
crud=Crud(db)
#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
db.define_table('page',
                Field('title'),
                Field('body','text'),
                Field('created_on','datetime',default=request.now),
                Field('created_by','reference auth_user',default=auth.user_id),
                format='%(title)s')
db.define_table('post',
                Field('page_id','reference page'),
                Field('body','text'),
                Field('created_on','datetime', default=request.now),
                Field('created_by','reference auth_user', default=auth.user_id))
db.define_table('document',
                Field('page_id','reference page'),
                Field('name'),
                Field('file','upload'),
                Field('created_on','datetime', default=request.now),
                Field('created_by','reference auth_user', default=auth.user_id),
                format='%(name)s')
db.page.title.requires=IS_NOT_IN_DB(db,'page.title')
db.page.body.requires=IS_NOT_EMPTY()
db.page.created_by.readable=db.page.created_by.writable=False
db.page.created_on.readable=db.page.created_on.writable=False
