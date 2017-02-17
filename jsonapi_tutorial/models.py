# {
#   "type": "articles",
#   "id": "1",
#   "attributes": {
#     "title": "JSON API paints my bikeshed!"
#   },
#   "relationships": {
#     "author": {
#       "links": {
#         "self": "http://example.com/articles/1/relationships/author",
#         "related": "http://example.com/articles/1/author"
#       },
#       "data": { "type": "people", "id": "9" }
#     },
#     "comments": {
#       "links": {
#         "self": "http://example.com/articles/1/relationships/comments",
#         "related": "http://example.com/articles/1/comments"
#       },
#       "data": [
#         { "type": "comments", "id": "5" },
#         { "type": "comments", "id": "12" }
#       ]
#     }
#   },
#   "links": {
#     "self": "http://example.com/articles/1"
#   }
# }


class Model():

    def __init__(self, id: str):
        self.id = id


class Person(Model):

    def __init__(self,
                 id: str,
                 first_name: str,
                 last_name: str,
                 twitter: str):
        super(Person, self).__init__(id)
        self.first_name = first_name
        self.last_name = last_name
        self.twitter = twitter

    def __repr__(self) -> str:
        return '<Person(twitter={self.twitter!r})>'.format(self=self)


class Article(Model):

    def __init__(self, id: str, title: str, author: Person):
        super(Article, self).__init__(id)
        self.title = title
        self.author = author

    def __repr__(self) -> str:
        return '<Article(title={self.title!r})>'.format(self=self)
