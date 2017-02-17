from marshmallow import pprint
from jsonapi_tutorial.models import Article, Person
from jsonapi_tutorial.schemata import ArticleSchema

if __name__ == "__main__":
    author = Person(1, "Javi", "Lorenzana", "skaiuoquer")
    article = Article(1, "Monty", author)
    schema = ArticleSchema(include_data=('author',))
    result = schema.dump(article)
    print("Serialize objects by passing them to your schema's dump method, which returns the formatted result (as well as a dictionary of validation errors, which we'll revisit later).\n")
    pprint(result.data)

    print("\n\n")
    print("You can also serialize to a JSON-encoded string using dumps.\n")
    json_result = schema.dump(article)
    pprint(json_result.data)
    # {
    #     'data': {
    #         'id': '1',
    #         'type': 'articles',
    #         'attributes': {'title': 'Django is Omakase'}
    #     }
    # }
