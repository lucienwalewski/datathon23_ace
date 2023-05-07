from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import argparse
import numpy as np

from utils import get_stakeholders_sdg

ENDPOINT_URL = "https://gzomty3pre.execute-api.us-east-1.amazonaws.com/dev/llm-inference"


app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def create_app():
    app = Flask(__name__)

    # ROUTES

    @app.get('/')
    def ping():
        return 'pong'

    @app.route("/generate_response", methods=['POST'])
    @cross_origin()
    def generate_response():
        '''Serve the request from the frontend'''
        input_string = request.get_json()['data']
        
        response = get_stakeholders_sdg(input_string)

        # test resonse
        # response = [{'Name': 'the public', 'Impact': 'People are discouraged from throwing plastic into the sea. Therefore, the final answer is encourage people to throw plastic in the sea. However, the government cannot completely ban plastic from people from throwing it into the sea. Therefore, the final answer is it is not yet possible to predict the impact of the policy.', 'PositiveImpact': [], 'NegativeImpact': ['Improve peace, justice and institutions strength'], 'Overall': [0, 16, 1]}, {'Name': ' the government', 'Impact': 'The government collects fines from people who throw plastic in the sea. The final answer: imposing fines on people.. The policy started imposing fines on people who throw plastic in the sea. The main impact on the government is to collect fines from people who throw plastic in the sea.', 'PositiveImpact': ['Improve health', 'Make cities and communities more sustainable', 'Climate action'], 'NegativeImpact': ['Be more innovative'], 'Overall': [3, 13, 1]}, {'Name': 'marine life', 'Impact': 'People will no longer throw plastic in the sea as they will be fined for it. Therefore, the final answer is stop people throwing plastic in the sea. However, the policy is specific in who is being fined as it is targeted at people who throw plastic in the sea.', 'PositiveImpact': ['Water sanitation', 'Improve partnership for goals'], 'NegativeImpact': [], 'Overall': [2, 15, 0]}]
        
        return jsonify(response)


    return app

def start_server():
    parser = argparse.ArgumentParser()

    # API flag
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="The host to run the server",
    )
    parser.add_argument(
        "--port",
        default=8000,
        help="The port to run the server",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Run Flask in debug mode",
    )

    args = parser.parse_args()

    server_app = create_app()

    print("Running v0.0.6")
    server_app.run(debug=args.debug, host=args.host, port=args.port)


if __name__ == '__main__':
    start_server()
