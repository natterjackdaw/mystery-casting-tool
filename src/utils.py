import os
import random
from typing import List, Dict
import yaml


def key_shuffle(length_of_list: int) -> List[int]:

    keys = [i for i in range(length_of_list)]
    random.shuffle(keys)
    return keys




# def make_table_of_assigment(
#         input_list: List[str],
#         chatacter_dict: Dict,

# ):
