from flask import request, jsonify, Blueprint, g
from functools import wraps
from .success import ResultSuccess

def format_response(f):
    @wraps(f)
    def decorate(*args, **kwargs):
        return jsonify(dict(ResultSuccess(f(*args, **kwargs))))
    return decorate