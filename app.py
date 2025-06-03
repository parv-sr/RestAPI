from flask import Flask
from flask_restful import Api
from database import connect_to_db
from resources.user import User


app = Flask(__name__)
api = Api(app)

db_connection = connect_to_db()


api.add_resource(User, "/users", resource_class_kwargs={"db_connection": db_connection})


if __name__ == "__main__":
    app.run(debug=True)

