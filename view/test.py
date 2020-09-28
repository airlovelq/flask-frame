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
    with controller:
        result = controller.test(params['msg'])
        return result