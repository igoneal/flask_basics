from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HomePage(Resource):
    @staticmethod
    def get():
        return {'about': 'hello world!'}

    @staticmethod
    def post():
        # print(request.data)
        sent_data = request.get_json()
        return {'you sent': sent_data}, 201


class Times5(Resource):
    @staticmethod
    def get(num):
        return {'result': num*5}


class Multiply(Resource):
    @staticmethod
    def get(text):   # 5,5 or 10,2
        nums = text.strip().split(',')
        return {'result': int(nums[0]) * int(nums[1])}


api.add_resource(HomePage, '/')
api.add_resource(Times5, '/times5/<int:num>')
api.add_resource(Multiply, '/multiply/<text>')


if __name__ == '__main__':
    app.run(debug=True)
