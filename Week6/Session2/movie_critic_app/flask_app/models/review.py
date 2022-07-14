from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class Review:
    db = "movie_critic_june_2022"

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.rating = data['rating']
        self.date_watched = data['date_watched']
        self.content = data['content']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM reviews JOIN users ON reviews.user_id=users.id;"
        results = connectToMySQL(cls.db).query_db(query)
        reviews = []
        for row in results:
            #create the review object
            review = cls(row)
            #create associated user object
            user_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            user = User(user_data)
            review.user = user
            reviews.append(review)
        return reviews

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM reviews JOIN users ON reviews.user_id=users.id WHERE reviews.id=%(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        row = results[0]
        review = cls(row)
        user_data = {
            'id': row['users.id'],
            'first_name': row['first_name'],
            'last_name': row['last_name'],
            'email': row['email'],
            'password': row['password'],
            'created_at': row['users.created_at'],
            'updated_at': row['users.updated_at']
        }
        user = User(user_data)
        review.user = user
        return review
    @classmethod
    def create(cls, data):
        query = "INSERT INTO reviews(title, rating, date_watched, content, user_id) VALUES(%(title)s, %(rating)s, %(date_watched)s, %(content)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query ="UPDATE reviews SET title=%(title)s, rating=%(rating)s, date_watched=%(date_watched)s, content=%(content)s WHERE id=%(id)s"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM reviews WHERE id = %(id)s"
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate_create(review):
        is_valid = True
        if len(review['title']) < 1:
            flash("Title must be at least 1 characters", "error")
            is_valid = False
        if len(review['rating']) < 1:
            flash("Rating must be entered", "error")
            is_valid = False
        else:
            if int(review['rating']) < 0 or int(review['rating']) > 5:
                flash("Rating needs to be in between 0-5", "error")
                is_valid = False

        return is_valid