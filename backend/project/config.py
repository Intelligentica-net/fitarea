# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - Intelligentica (Morocco)
Email: a.benmhamed@intelligentica.net
Website: https://intelligentica.net
Client: Insitut National de Recherche Halieutique (Morocco)
"""
import os
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY")
    POSTGRES_USER = os.getenv("PG_USER")
    POSTGRES_PASSWORD = os.getenv("PG_PASSWORD")
    POSTGRES_HOST = os.getenv("PG_HOST")
    POSTGRES_ENGINE = os.getenv("PG_ENGINE")
    POSTGRES_PORT = os.getenv("PG_PORT")
    POSTGRES_DB = os.getenv("PG_DB")
    SQLALCHEMY_DATABASE_URI = f"{POSTGRES_ENGINE}://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


class DevConfig(BaseConfig):
    DEBUG = True


class TestConfig(BaseConfig):
    DEBUG = False
    TESTING = True


class ProdConfig(BaseConfig):
    DEBUG = False
    TESTING = False


CONFIG_DICT = {
    "development": DevConfig,
    "testing": TestConfig,
    "production": ProdConfig
}
