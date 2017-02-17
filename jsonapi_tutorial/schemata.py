from marshmallow_jsonapi import Schema, fields

class ArticleSchema(Schema):
    id = fields.Str(dump_only=True)
    title = fields.Str()

    author = fields.Relationship(
        related_url='/articles/{article_id}/author',
        related_url_kwargs={'article_id': '<id>'},
        include_resource_linkage=True,
        type_='people',
        # define a schema for rendering included data
        schema='PersonSchema'
    )

    # comments = fields.Relationship(
    #     related_url='/posts/{post_id}/comments',
    #     related_url_kwargs={'post_id': '<id>'},
    #     many=True, include_resource_linkage=True,
    #     type_='comments',
    #     # define a schema for rendering included data
    #     schema='CommentSchema'
    # )

    class Meta:
        type_ = 'articles'
        self_url = '/articles/{id}'
        self_url_kwargs = {'id': '<id>'}
        self_url_many = '/articles/'
        strict = True


class PersonSchema(Schema):
    id = fields.Str(dump_only=True)
    first_name = fields.Str()
    last_name = fields.Str()
    twitter = fields.Str()

    class Meta:
        type_ = 'people'
        self_url = '/people/{id}'
        self_url_kwargs = {'id': '<id>'}
        self_url_many = '/people/'
        strict = True
