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


def should_verify():
    answer = prompt([
        {
            "type": "confirm",
            "name": "validate",
            "message": "Should the token's signature be verified?",
            "default": True
        }
    ])
    return answer.get("validate")


def get_secret():
    answer = prompt([
        {
            "type": "input",
            "name": "secret",
            "message": "Please enter the secret?",
        }
    ])
    return answer.get("secret")


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


def print_output(header, payload, verify=None):
    print(f"Header\n{dumps(header, indent=4)}")
    print("==============================")
    print(f"Payload\n{dumps(payload, indent=4)}")
    print("==============================")
    print(f"Verified: {verify if verify else 'Not Requested'}")


def main():
    token = get_token()
    header = get_header(token)
    payload = get_payload(token)
    verify = should_verify()
    if verify:
        secret = get_secret()
        verify = get_payload(token, secret, verify=True)
        print_output(header, payload, verify)
        return
    print_output(header, payload, verify)


if __name__ == "__main__":
    main()
