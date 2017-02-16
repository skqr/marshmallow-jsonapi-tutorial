from marshmallow_jsonapi import Schema, fields

class ArticleSchema(Schema):
    id = fields.Str(dump_only=True)
    title = fields.Str()

    class Meta:
        type_ = 'articles'
        self_url = '/articles/{id}'
        self_url_kwargs = {'id': '<id>'}
        self_url_many = '/articles/'
        strict = True
