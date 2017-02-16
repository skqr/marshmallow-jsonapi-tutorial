from marshmallow import pprint
from marshmallow_tutorial.models import User
from marshmallow_tutorial.schemata import UserSchema

if __name__ == "__main__":
    user = User(name="Monty", email="monty@python.org")
    schema = UserSchema()
    result = schema.dump(user)
    print("Serialize objects by passing them to your schema's dump method, which returns the formatted result (as well as a dictionary of validation errors, which we'll revisit later).\n")
    pprint(result.data)
    # {"name": "Monty",
    #  "email": "monty@python.org",
    #  "created_at": "2014-08-17T14:54:16.049594+00:00"}

    print("\n")
    print("You can also serialize to a JSON-encoded string using dumps.\n")
    json_result = schema.dumps(user)
    pprint(json_result.data)
    # '{"name": "Monty", "email": "monty@python.org", "created_at": "2014-08-17T14:54:16.049594+00:00"}'
