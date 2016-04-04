db = DAL('sqlite://storage.sqlite')
from gluon.tools import *
auth = Auth(db)
auth.define_tables()
password_is_match = IS_MATCH('^(?=.*?[A-Z])(?=(.*[a-z]){1,})(?=(.*[\d]){1,})(?=(.*[\W]){1,})(?!.*\s).{8,}$', error_message='Invalid Password!! Should have atleast a number and a special character and more than 8 characters',
                             search=True)
db.auth_user.password.requires.insert(0, password_is_match)
crud = Crud(db)
db.define_table('image',
Field('imageid', default=auth.user_id,readable=False,writable=False),
Field('title', unique=True),
Field('file', 'upload'),
Field('created_on', 'datetime', default=request.now,readable=False,writable=False),
Field('author'),
Field('body', 'text'),
Field('votes',default=0,readable=False,writable=False)    )

db.define_table('vote',
                Field('image_id','reference image'),
                Field('score','integer'),
                Field('posted_on','datetime',readable=False,writable=False),
                Field('posted_by','reference auth_user',readable=False,writable=False))

db.image.title.requires = IS_NOT_IN_DB(db, db.image.title)
db.image.author.requires = IS_NOT_EMPTY()
db.image.body.requires = IS_NOT_EMPTY()
db.image.created_on.requires = IS_NOT_EMPTY()