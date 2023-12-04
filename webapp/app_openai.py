import os
from openai import OpenAI
"""
References for using openai_api:
    building code: https://platform.openai.com/docs/guides/code/introduction

"""
# This code is for v1 of the openai package: pypi.org/project/openai

client = OpenAI()


def submit_question(text: str):
    """This submits a question to OpenAI API"""
    api_key = os.getenv('OPENAI_API_KEY')
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{text}"},
    ],
    temperature=0.5,
    max_tokens=64,
    top_p=1
    )["choices"][0]["text"].strip("\n")

    # result = openai.Completion.create(
    #     prompt= prompt,
    #     temperature = 0,
    #     max_tokens = 300,
    #     top_p = 1,
    #     frequency_penalty = 0,
    #     presence_penalty = 0,
    #     model = "text-davinci-002",

    # )["choices"][0]["text"].strip("\n")
    return response


# # a function that converts text to python code.
# def create_code(text: str, language = "Python3"):
#     """ submits a prompt to openAI for code generation"""
#     completion = openai.ChatCompletion.create(
#         model = "gpt-3.5-turbo",
#         messages = [
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": f"{text} using {language}."},
#         ]
#     )

#     result = completion.choices[0].message["content"]
#     print(result)
    
#     return result