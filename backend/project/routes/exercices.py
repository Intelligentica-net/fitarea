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

api = Namespace("Exercices", description="Exercices Operations", path="/api/v1/exercices")
