#!/bin/python3

from PyInquirer import prompt
from json import dumps
import jwt

ALGORITHM = "HS256"


def get_token():
    answer = prompt([
        {
            "type": "input",
            "name": "token",
            "message": "Please enter the token"
        }
            ])
    return "".join(answer.get("token").split())


def get_secret():
    answers = prompt([
        {
            "type": "input",
            "name": "secret",
            "message": "Please enter the secret",
        }
    ])
    return answers.get("secret")


def get_header(token):
    return jwt.get_unverified_header(token)


def get_payload(token, secret=None, verify=False):
    if not verify or secret is None:
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
            return payload
        except jwt.exceptions.DecodeError:
            return False
    try:
        jwt.decode(token, secret, ALGORITHM)
        return True
    except jwt.exceptions.InvalidSignatureError:
        return False


token = get_token()
secret = get_secret()

header = get_header(token)
payload = get_payload(token)
verify = get_payload(token, secret, verify=True)

print(f"Header\n{dumps(header, indent=4)}")
print("==============================")
print(f"Payload\n{dumps(payload, indent=4)}")
print("==============================")
print(f"Verified: {verify}")
