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
        self.users_who_favorited = []
        self.user_ids_who_favorited = []
        
    @classmethod
    def get_all(cls):
        # query = "SELECT * FROM reviews JOIN users ON reviews.user_id=users.id;"
        query = '''SELECT * FROM reviews JOIN users AS creators ON reviews.user_id = creators.id
            LEFT JOIN favorited_reviews ON reviews.id = favorited_reviews.review_id
            LEFT JOIN users AS users_who_favorited ON favorited_reviews.user_id = users_who_favorited.id;'''
        results = connectToMySQL(cls.db).query_db(query)
        reviews = []
        print(results)
        for row in results:
            new_review = True
            user_who_favorited_data = {
                'id': row['users_who_favorited.id'],
                'first_name': row['users_who_favorited.first_name'],
                'last_name': row['users_who_favorited.last_name'],
                'email': row['users_who_favorited.email'],
                'password': row['users_who_favorited.password'],
                'created_at': row['users_who_favorited.created_at'],
                'updated_at': row['users_who_favorited.updated_at']
            }

            number_of_reviews = len(reviews)
            if number_of_reviews > 0:
                last_review = reviews[number_of_reviews-1]
                if last_review.id == row['id']:
                    last_review.user_ids_who_favorited.append(row['users_who_favorited.id'])
                    last_review.users_who_favorited.append(User(user_who_favorited_data))
                    new_review = False

            if new_review:
                #create the review object
                review = cls(row)
                #create associated user object
                user_data = {
                    'id': row['creators.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'email': row['email'],
                    'password': row['password'],
                    'created_at': row['creators.created_at'],
                    'updated_at': row['creators.updated_at']
                }
                user = User(user_data)
                review.user = user
                #check to see if anyone favorited the review
                if row['users_who_favorited.id']:
                    review.user_ids_who_favorited.append(row['users_who_favorited.id'])
                    review.users_who_favorited.append(User(user_who_favorited_data))
                reviews.append(review)
        return reviews

    @classmethod
    def get_one(cls, data):
        # query = 'SELECT * FROM reviews JOIN users ON reviews.user_id=users.id WHERE reviews.id=%(id)s;'
        query='''SELECT * FROM reviews 
                JOIN users AS creators ON reviews.user_id=creators.id
                LEFT JOIN favorited_reviews ON favorited_reviews.review_id=reviews.id
                LEFT JOIN users AS users_who_favorited ON favorited_reviews.user_id = users_who_favorited.id
                WHERE reviews.id = %(id)s;'''
        
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False

        new_review = True
        for row in results:
            #if this is the first row being processed
            if new_review:
                review = cls(row)
                #Create a user object
                user_data = {
                    'id': row['creators.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'created_at': row['creators.created_at'],
                    'updated_at': row['creators.updated_at'],
                    'email': row['email'],
                    'password': row['password']  
                }
                creator = User(user_data)
                review.creator = creator
                new_review = False
            
            if row['users_who_favorited.id']:
                user_who_favorited_data = {
                    'id': row['users_who_favorited.id'],
                    'first_name': row['users_who_favorited.first_name'],
                    'last_name': row['users_who_favorited.last_name'],
                    'created_at': row['users_who_favorited.created_at'],
                    'updated_at': row['users_who_favorited.updated_at'],
                    'email': row['users_who_favorited.email'],
                    'password': row['users_who_favorited.password']  
                }
                user_who_favorited = User(user_who_favorited_data)
                review.users_who_favorited.append(user_who_favorited)
                review.user_ids_who_favorited.append(row['users_who_favorited.id'])
                
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

    @classmethod
    def favorite(cls, data):
        query='INSERT INTO favorited_reviews(user_id, review_id) VALUES(%(user_id)s, %(id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def unfavorite(cls, data):
        query='DELETE FROM favorited_reviews WHERE user_id=%(user_id)s AND review_id=%(id)s;'
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