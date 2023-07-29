# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - Intelligentica (Morocco)
Email: a.benmhamed@intelligentica.net
Website: https://intelligentica.net
Client: Insitut National de Recherche Halieutique (Morocco)
"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
