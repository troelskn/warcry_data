"""
Utility functions and script for data manipulation and management
"""
from data_parsing import FighterJSONPayload, sort_data
from pathlib import Path
from typing import List, Dict
import uuid


def cheapest_fighters(fighter_data: List[Dict]) -> Dict:
    cheapos = dict()

    grand_alliances = ['chaos', 'death', 'destruction', 'order']
    for ga in grand_alliances:
        cheapos[ga] = min([x for x in fighter_data if x['grand_alliance'] == ga], key=lambda x: x['points'])

    return cheapos


def get_fighter_type(dude: dict) -> dict:
    types = list()
    for t in ['hero', 'monster', 'thrall', 'ally']:
        if t in dude['runemarks']:
            types.append(t)
    if dude['bladeborn']:
        types.append('bladeborn')
    if len(types) == 0:
        types.append('fighter')
    dude['fighter_type'] = types
    return dude


def generate_id(guy: dict) -> dict:
    # This should be how ids are generated. Once a fighter has an id, they should not be given a new one.
    if '_id' in guy.keys():
        return guy

    guy['_id'] = str(uuid.uuid4()).split('-')[0]
    return guy


if __name__ == '__main__':
    src_data = Path(Path(__file__).parent.parent, 'data', 'fighters.json')

    data_payload = FighterJSONPayload(src_file=src_data)
    data = data_payload.data

    new_data = list()  # type: List[Dict]

    # Do stuff with data, add it to new_data

    data_payload.data = sort_data(new_data)

    # data_payload.write_aggregate_file_to_disk()
    # data_payload.write_warbands_to_disk()

    z = 1 + 2