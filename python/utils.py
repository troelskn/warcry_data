"""
Utility functions and script for data manipulation and management
"""
from data_parsing import FighterJSONPayload, sort_data
from pathlib import Path
from typing import List, Dict


def cheapest_fighters(fighter_data: List[Dict]) -> Dict:
    cheapos = dict()

    grand_alliances = ['chaos', 'death', 'destruction', 'order']
    for ga in grand_alliances:
        cheapos[ga] = min([x for x in fighter_data if x['grand_alliance'] == ga], key=lambda x: x['points'])

    return cheapos


if __name__ == '__main__':
    src_data = Path(Path(__file__).parent.parent, 'data', 'fighters.json')

    data_payload = FighterJSONPayload(src_file=src_data)
    data = sort_data(data_payload.data)
    cheapest_fighters(data)

    # data.write_aggregate_file_to_disk()
    # data.write_warbands_to_disk()
    z = 1
