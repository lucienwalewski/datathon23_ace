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

    # @app.post('/generate_response')
    @app.route("/generate_response", methods=['POST'])
    @cross_origin()
    def generate_response():
        input_string = request.get_json()['data']
        # Uncomment below to call model
        # response = get_stakeholders_sdg(input_string)
        response = [{'Name': 'the public', 'Impact': 'People are discouraged from throwing plastic into the sea. Therefore, the final answer is encourage people to throw plastic in the sea. However, the government cannot completely ban plastic from people from throwing it into the sea. Therefore, the final answer is it is not yet possible to predict the impact of the policy.', 'Positive impact': [], 'Negative impacat': ['Improve peace, justice and institutions strength'], 'Overall': [0, 16, 1]}, {'Name': ' the government', 'Impact': 'The government collects fines from people who throw plastic in the sea. The final answer: imposing fines on people.. The policy started imposing fines on people who throw plastic in the sea. The main impact on the government is to collect fines from people who throw plastic in the sea.', 'Positive impact': ['Improve health', 'Make cities and communities more sustainable', 'Climate action'], 'Negative impacat': ['Be more innovative'], 'Overall': [3, 13, 1]}, {'Name': 'marine life', 'Impact': 'People will no longer throw plastic in the sea as they will be fined for it. Therefore, the final answer is stop people throwing plastic in the sea. However, the policy is specific in who is being fined as it is targeted at people who throw plastic in the sea.', 'Positive impact': ['Water sanitation', 'Improve partnership for goals'], 'Negative impacat': [], 'Overall': [2, 15, 0]}]
        return jsonify(response)


    return app


# def generate_sample_response(payload):
# EXAMPLE_PAYLOAD = {
#     "data": {
#         "text_inputs": "Tell me the steps to make beer",
#         "max_length": 50,
#         "num_return_sequences": 3,
#         "top_k": 50,
#         "top_p": 0.95,
#         "do_sample": True
#     }
# }


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
