from flask_restful import Resource
from flask import request
import mysql.connector as sql
from database import connect_to_db
import secrets
import requests 

class User(Resource):

    def __init__(self, db_connection):
        self.db = db_connection                  #self.db IS the connection

    def get(self):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT id, name, size, api_key FROM user")
        users = cursor.fetchall()

        

        return users, 

    def generate_apikey(self):
        return secrets.token_hex(16)


    def post(self):
        try:
            data = request.get_json()
            name = data.get("name")
            size = data.get("size")
        except Exception as e:
            print("Error: ", e)

        try:
            cursor = self.db.cursor(dictionary = True)
            query = "INSERT INTO user (name, size, api_key) VALUES (%s, %s, %s)"
            values = (name, size, self.generate_apikey())
            cursor.execute(query, values)
            self.db.commit()
        except sql.Error as err:
            print(f"Error: {err}")
            self.db.rollback()
        finally:
            cursor.close()

        return {"message" : "User created", "api_key" : values[2]}, 201



    