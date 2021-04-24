import related


@related.mutable
class User(object):
    id = related.IntegerField()
    name = related.StringField()
    password = related.StringField()
    created_at = related.DateField()
    updated_at = related.DateField()
