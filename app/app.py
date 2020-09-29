#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
import traceback

from flask import Flask, g, jsonify
from flask_cors import CORS
from flasgger import Swagger

from error_code import BaseException, SystemInternalError

from view import test_view
from response import ResultSuccess

def create_app():
    app = Flask(__name__)

    swagger_config = Swagger.DEFAULT_CONFIG
    swagger_config['title'] = 'test'    # 配置大标题
    swagger_config['description'] = 'test'    # 配置公共描述内容
    swagger_config['host'] = 'localhost:1000'    # 请求域名
    swag = Swagger(app, config=swagger_config)
    
    app.register_blueprint(test_view, url_prefix='/test')

    CORS(app)

    @app.before_request
    def requests_context():
        pass

    @app.route('/')
    def index():
        return 'Service is up.'

    @app.errorhandler(BaseException)
    def handle_error(error):
        return jsonify(dict(error))

    @app.errorhandler(500)
    def handle_internal_error(error):
        return jsonify(dict(SystemInternalError())), 500

    # @app.after_request
    # def after_request_handler(resp):
    #     if resp.is_json:
    #         data = resp.get_json()
    #         if isinstance(data, dict):
    #             if 'error_code' and 'message' and 'success' in data:
    #                 return resp
    #             if 'swagger' in data:
    #                 return resp
    #         result = ResultSuccess(data)
    #         return jsonify(dict(result))
    #     else:
    #         return resp

    return app