from flask import request, jsonify, Blueprint, g
from utils import auth_check
from utils import param_check
from response import format_response
from controller import test_controller_generator
from setting import ParamTypes

test_view = Blueprint('test', __name__)

@test_view.route('/user', methods=['GET'])
@format_response
@auth_check()
@param_check({'params':{'msg':[False, ParamTypes.EMAIL]}})
@test_controller_generator
def get_user(auth, params, controller):
    """
    This is the language awesomeness API
    Call this api passing a language name and get back its features
    ---
    tags:
      - Test API
    consumes:
      - application/json
    parameters:
      - name: msg
        in: path
        type: string
        required: true
        description: message
    responses:
      500:
        description: Error
      200:
        description: Success
        schema:
          id: res
          properties:
            data:
              type: string
              description: data
              default: o
            code:
              type: integer
              description: error code
              default: 0
            message:
              type: string
              description: msg
              default: o

    """
    with controller:
        result = controller.test(params['msg'])
        return result