from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    @staticmethod
    def get():
        return {'about': 'hello world!'}

    @staticmethod
    def post():
        # print(request.data)
        some_json = request.get_json()
        return {'you sent': some_json}, 201


class Multi(Resource):
    @staticmethod
    def get(num):
        return {'result': num*10}


api.add_resource(HelloWorld, '/')
api.add_resource(Multi, '/multi/<int:num>')


if __name__ == '__main__':
    app.run(debug=True)
