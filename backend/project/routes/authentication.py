# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - Intelligentica (Morocco)
Email: a.benmhamed@intelligentica.net
Website: https://intelligentica.net
Client: Insitut National de Recherche Halieutique (Morocco)
"""
from http import HTTPStatus
from flask import request
from flask_restx import Resource, Namespace
from project.models import User
from flask_bcrypt import generate_password_hash

api = Namespace("Authentication", description="Authentication Operations", path="/api/v1/auth")


@api.route("/register")
class RegisterResources(Resource):
    def post(self):
        data = request.json
        print(data)
        uname = data["username"]
        mail = data["email"]
        pwd = data["password"]

        user = User.query.filter_by(username=uname).first()

        if user:
            return {"message": "Username existe déjà"}, HTTPStatus.BAD_REQUEST

        user = User(username=uname, email=mail, password_hash=pwd)
        user.save()

        return {"status": "success", "message": "User registered successfully!"}, HTTPStatus.CREATED


@api.route("/login")
class RegisterResources(Resource):
    def post(self):
        pass


@api.route("/logout")
class RegisterResources(Resource):
    def post(self):
        pass
