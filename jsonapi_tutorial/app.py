from marshmallow import pprint
from jsonapi_tutorial.schemata import ArticleSchema

if __name__ == "__main__":
    print("You can also serialize to a JSON-encoded string using dumps.\n")
    json_result = ArticleSchema().dump(article)
    pprint(json_result.data)
    # {
    #     'data': {
    #         'id': '1',
    #         'type': 'articles',
    #         'attributes': {'title': 'Django is Omakase'}
    #     }
    # }
