
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