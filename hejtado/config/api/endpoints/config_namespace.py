#!/usr/bin/env python
#
#  Copyright (C) 2019 AlfaWolf s.r.o.
#  Lumir Jasiok
#  lumir.jasiok@alfawolf.eu
#  http://www.alfawolf.eu
#
#
import logging

from flask import request
from flask_restplus import Resource, fields

from hejtado.config.api import api

log = logging.getLogger(__name__)
ns = api.namespace('config/config', description='Operations with Hejtado Configuration')
config = api.model('Hejtado Config', {
    'id': fields.Integer(readonly=True, description='Unique identifier'),
})