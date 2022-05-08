from urllib import response
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import main
import bcrypt
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from datetime import datetime, timedelta, timezone
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager



app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "please-remember-to-change-me"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

db = SQLAlchemy(app)
jwt = JWTManager(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100), nullable=False )
    email = db.Column("email", db.String(100),unique=True, nullable=False)
    hash = db.Column("hash",db.String(100), nullable=False)


    def __init__(self, name, email, hash):
        self.name = name
        self.email = email
        self.hash = hash


@app.route("/register", methods=["POST"])
def register():
    try:
        name = request.json.get("name", None)
        email = request.json.get('email', None)
        password = request.json.get('password', None)
        
        if not email:
            return 'Missing email', 400
        if not name:
            return 'Missing name', 400
        if not password:
            return 'Missing password', 400

        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        usr = users(name = name, email=email, hash=hashed)
        db.session.add(usr)
        db.session.commit()

        # access_token = create_access_token(identity={"email": email})
        # return {"access_token": access_token}, 200
        return 'User Created!!!', 200
    except exc.IntegrityError:
        # the rollback func reverts the changes made to the db ( so if an error happens after we commited changes they will be reverted )
        db.session.rollback()
        return 'User Already Exists', 400
    except AttributeError:
        return 'Provide an Email and Password in JSON format in the request body', 400


@app.route('/login', methods=["POST"])
def create_token():
    try:
        name = request.json.get("name", None)
        email = request.json.get("email", None)
        password = request.json.get("password", None)

        if not name:
            return 'Missing name', 400
        if not email:
            return 'Missing email', 400
        if not password:
            return 'Missing password', 400

        usr = users.query.filter_by(email=email).first()
        if not usr:
            return 'User Not Found!', 404

        if bcrypt.checkpw(password.encode('utf-8'), usr.hash):
            access_token = create_access_token(identity={"email": email})
            response = {"access_token":access_token}
            return response
        else:
            return 'Invalid Login Info!', 400
    except AttributeError:
        return 'Provide an Email and Password in JSON format in the request body', 400 

@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            data = response.get_json()
            if type(data) is dict:
                data["access_token"] = access_token 
                response.data = json.dumps(data)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response

@app.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response


@app.route("/stockget", methods=['POST'])
@jwt_required()
def get_stocks():
    data = request.get_json()
    print(data)
    result = main.main(data)
    return jsonify(result)


if __name__ == '__main__':
    db.create_all()
    app.run()