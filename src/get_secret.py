import json
import os
from typing import List

secret_path = os.path.abspath(__file__ + "/../../" + "secret.json")


def get_token() -> str:
    with open(secret_path, mode='r') as fp:
        return json.load(fp).get('token')


def get_guild_id() -> List[int]:
    with open(secret_path, mode='r') as fp:
        return json.load(fp).get('guild_id')
