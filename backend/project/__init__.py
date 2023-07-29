# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - Intelligentica (Morocco)
Email: a.benmhamed@intelligentica.net
Website: https://intelligentica.net
Client: Insitut National de Recherche Halieutique (Morocco)
"""
import os
from flask import Flask
from .config import CONFIG_DICT
from dotenv import load_dotenv
from .extensions import db, migrate
from flask_restx import Api
from project.models import User
from project.routes import authApi, exercicesApi

load_dotenv()


def create_app():
    app = Flask(__name__)
    env = os.getenv("FLASK_ENV")

    app.config.from_object(CONFIG_DICT[env])

    db.init_app(app)
    migrate.init_app(app=app, db=db)

    api = Api(app=app, description="Fit Area API", doc="/docs")

    api.add_namespace(authApi)

    return app
