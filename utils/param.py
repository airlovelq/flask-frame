from flask import request
from functools import reduce, wraps
import re
from error_code import ParameterError
from setting import ParamTypes

def parser_requests():
    params = dict()
    if request.get_json():
        params['json'] = request.get_json() or {}
    if request.files.to_dict():
        params['files'] = request.files.to_dict()
    if request.form.to_dict():
        params['data'] = request.form.to_dict()
    if request.args:
        params['params'] = {k: v for k, v in request.args.items()}

    return params

def param_check(required_parameters=None):

    def decorator(f):

        @wraps(f)
        def wrapped(*args, **kwargs):
            params = parser_requests()
            if required_parameters:
                # check file fields
                for location in required_parameters:
                    for field_name in required_parameters[location]:
                        required_type = required_parameters[location][field_name][1] 
                        if required_parameters[location][field_name][0]:
                            if location not in params:
                                raise ParameterError(
                                    '{} must be provided in {}'.format(
                                        field_name, location))
                            if field_name not in params[location]:
                                raise ParameterError(
                                    '{} must be provided'.format(field_name))
                            check_param_type(params[location][field_name], required_type)
                        else:
                            if location in params:
                                if field_name in params[location]:
                                    check_param_type(params[location][field_name], required_type)

            combined_params = reduce(lambda d1, d2: dict(d1, **d2),
                                     list(params.values()), {})

            return f(params=combined_params, *args, **kwargs)

        return wrapped

    return decorator

def check_param_type(param, required_type):
    if required_type == ParamTypes.INT:
        check_int(param)
    elif required_type == ParamTypes.EMAIL:
        check_email(param) 
    elif required_type == ParamTypes.STRING:
        check_string(param)
    elif required_type == ParamTypes.UUID4:
        check_uuid4(param)
    elif required_type == ParamTypes.BYTES:
        check_bytes(param)
    elif required_type == ParamTypes.LIST:
        check_list(param)
    elif required_type == ParamTypes.NOSPECIALSTRING:
        check_no_specail_char(param)

def check_email(email):
    check_string(email)
    if re.match("^[\.A-Za-z0-9\u4e00-\u9fa5]+@[\.a-zA-Z0-9_-]+$", email) is None:
        raise ParameterError()

def check_uuid4(sid):
    check_string(sid)
    if re.match("^[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}$", sid) is None:
        raise ParameterError()

def check_int(i):
    if isinstance(id, str):
        if re.match("[1-9]{1}[0-9]*$", i) is None and re.match("0$", i) is None:
            raise ParameterError()
    else:
        if not isinstance(id, int):
            raise ParameterError()

def check_list(li):
    if not isinstance(li, list):
        raise ParameterError()
    if len(li) == 0:
        raise ParamError()

def check_no_specail_char(str):
    check_string(str)
    if re.match("^[\.A-Za-z0-9@_-]+$", str) is None:
        raise ParameterError()

def check_bytes(bts):
    if not isinstance(bts, bytes):
        raise ParameterError()

def check_string(sstr):
    if not isinstance(sstr, str):
        raise ParameterError()