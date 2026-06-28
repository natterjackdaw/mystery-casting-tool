import os
import random
from typing import List
import yaml

import streamlit as st

def key_shuffle(length_of_list: int) -> List[int]:

    keys = [i for i in range(length_of_list)]
    random.shuffle(keys)
    return keys


def return_characters_from_yml(
    yml_file_name: str,
    yml_folder: str = "characters"
):

    with open(f"{yml_folder}/{yml_file_name}", 'r') as file:
        return yaml.safe_load(file)

