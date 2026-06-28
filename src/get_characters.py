import os
from typing import List, Dict
import yaml

import streamlit as st


def pasta_passion_pistols(
    number_of_attendees: int,
    yml_file_name: str = "pasta_passion_pistols.yml",
    yml_folder: str = "characters"
) -> Dict:
    """Should just read a yml file and return the characters that you need.
    """
    main_directory = os.getcwd()

    # ./characters/pasta_passion_pistols.yml
    with open(f"{main_directory}/{yml_folder}/{yml_file_name}", 'r') as file:
        all_characters = yaml.safe_load(file)

    # if you have exactly 6, all is easy
    if number_of_attendees == 6:
        characters = all_characters['suspects']
    elif number_of_attendees == 7:
        characters = all_characters['suspects']
        guests = all_characters['guests']

        characters.append({
            "name": f"Choice: {guests[0]['name']} or {guests[1]['name']}",
            "summary": f"Attendee can choose between: {guests[0]['summary']} or {guests[1]['summary']}",
            "gender": "choice"
        })
    
    elif number_of_attendees == 8:
        characters = all_characters['suspects']
        guests = all_characters['guests']

        for guest in guests:
            characters.append(guest)
    
    else:
        # not great error catching but I can live with this
        st.write(f"Error - what the heck? You cannot have {number_of_attendees} people.")
    
    return characters


def for_table(
    dict_from_yaml: Dict,
    headers: List[str] = ["name", "summary", "gender"]
) -> Dict:

    # I am going to tidy up in an (inefficient?) way
    headers = headers

    output = {}
    for header in headers:
        _col_data = []
        for i in range(len(dict_from_yaml)):
            _col_data.append(dict_from_yaml[i][header])
        output[header] = _col_data