import requests
import json
import numpy as np

ENDPOINT_URL = "https://gzomty3pre.execute-api.us-east-1.amazonaws.com/dev/llm-inference"


EXAMPLE_PAYLOAD = {
    "data": {
        "text_inputs": "Tell me the steps to make beer",
        "max_length": 50,
        "num_return_sequences": 3,
        "top_k": 50,
        "top_p": 0.95,
        "do_sample": True
    }
}


def process_request(payload):
    response = requests.post(
        ENDPOINT_URL,
        data=json.dumps(payload),
        headers={"Content-Type": "application/json"})
    if response.status_code == 200:
        return response.json()
    else:
        print(
            f"Error querying endpoint. Status code: {response.status_code}")
        print(response.text)
        return None


def get_stakeholders_sdg(policy: str) -> str:

    sdgs = ['Eradicate poverty', 'Eradicate hunger', 'Improve health', 'Improve education', 'Improve genders equality', 'Water sanitation',
            'Make energy clean and affordable', 'Improve work conditions and support economic growth',
            'Be more innovative', 'Fight inequalities', 'Make cities and communities more sustainable',
            'Make consumption and production more responsible', 'Climate action', 'Protect underwater fauna',
            'Protect terrestrial fauna', 'Improve peace, justice and institutions strength', 'Improve partnership for goals']

    payload_sh = {
        "text_inputs": f"The three main stakeholders involved in the following policy: '{policy}' are",
        "max_length": 50,
        "max_time": 50,
        "num_return_sequences": 1,
        "top_k": 50,
        "top_p": 0.95,
        "do_sample": True,
    }
    answer_sh = process_request({"data": payload_sh})
    if 'and' in answer_sh[0]:
        answer_sh = answer_sh[0].split('and')
    stakeholders = []
    print(answer_sh)
    for elm in answer_sh:
        if ',' in elm:
            stakeholders += elm.strip().strip(',').split(',')
        else:
            stakeholders += [elm.strip()]
    print(stakeholders)
    res = []
    for stakeholder in stakeholders:
        payload_imp = {
            "text_inputs": f"Thinking step-by-step, in the following policy '{policy}', the main impact on {stakeholder} is",
            "max_length": 200,
            "min_length": 50,
            "max_time": 50,
            "num_return_sequences": 1,
            "top_k": 50,
            "top_p": 0.95,
            "do_sample": True,
        }
        answer_imp = process_request({"data": payload_imp})

        positive, neutral, negative = [], [], []
        for sdg in sdgs:
            payload_relevance = {
                "text_inputs": f"Answering by 'yes' or 'no', is the impact of the following policy '{policy}' on {stakeholder} related to {sdg}?",
                "max_length": 5,
                "max_time": 50,
                "num_return_sequences": 1,
                "top_k": 50,
                "top_p": 0.95,
                "do_sample": True,
            }
            answer_relevance = process_request({"data": payload_relevance})[0]

            if answer_relevance == 'yes':
                payload_pos = {
                    "text_inputs": f"Answering by 'yes' or 'no', is the impact of the following policy '{policy}' on {stakeholder} with regards to '{sdg}' positive?",
                    "max_length": 5,
                    "max_time": 50,
                    "num_return_sequences": 1,
                    "top_k": 50,
                    "top_p": 0.95,
                    "do_sample": True,
                }
                answer_pos = process_request({"data": payload_pos})[0]
                payload_neg = {
                    "text_inputs": f"Answering by 'yes' or 'no', is the impact of the following policy '{policy}' on {stakeholder} with regards to '{sdg}' negative?",
                    "max_length": 5,
                    "max_time": 50,
                    "num_return_sequences": 1,
                    "top_k": 50,
                    "top_p": 0.95,
                    "do_sample": True,
                }
                answer_neg = process_request({"data": payload_neg})[0]
                if answer_pos == 'yes' and answer_neg == 'no':
                    positive.append(sdg)
                elif answer_pos == 'no' and answer_neg == 'yes':
                    negative.append(sdg)
                else:
                    neutral.append(sdg)
            else:
                neutral.append(sdg)

        res.append({
            "Name": stakeholder,
            "Impact": answer_imp[0],
            "Positive impact": positive,
            "Negative impacat": negative,
            "Overall": [len(positive), len(neutral), len(negative)]
        })

    return str(res)


def get_stakeholders(policy: str) -> str:
    payload_sh = {
        "text_inputs": f"The three main stakeholders involved in the following policy: '{policy}' are",
        "max_length": 50,
        "max_time": 50,
        "num_return_sequences": 1,
        "top_k": 50,
        "top_p": 0.95,
        "do_sample": True,
    }
    answer_sh = process_request({"data": payload_sh})

    print(answer_sh)
    if "and" in answer_sh[0]:
        answer_sh = answer_sh[0].split('and')
    stakeholders = []
    for elm in answer_sh:
        if ", " in elm:
            stakeholders += elm.strip().strip(',').split(',')
        else:
            stakeholders += [elm.strip()]

    res = []
    for stakeholder in stakeholders:
        payload_imp = {
            "text_inputs": f"In the following policy '{policy}', the main impact on {stakeholder} is",
            "max_length": 200,
            "min_length": 100,
            "max_time": 50,
            "num_return_sequences": 1,
            "top_k": 50,
            "top_p": 0.95,
            "do_sample": True,
        }
        answer_imp = process_request({"data": payload_imp})

        payload_factor = {
            "text_inputs": f"Between 'low', 'medium' and 'high', the word that desribes the impact on {stakeholder} of the following policy: '{policy}' best would be",
            "max_length": 50,
            "max_time": 50,
            "num_return_sequences": 1,
            "top_k": 50,
            "top_p": 0.95,
            "do_sample": True,
        }
        answer_factor = process_request({"data": payload_factor})

        res.append(
            {
                "Name": stakeholder,
                "Impact": answer_imp[0],
                "Factor": answer_factor[0]
            }
        )
    return res
