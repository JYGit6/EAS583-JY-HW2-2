#!/usr/bin/env python3
import random
import json
import sys
from pathlib import Path

def validate(code_path):
    try:
        import get_ape_info
    except ImportError as e:
        print(f"Could not import homework file 'get_ape_info.py'\n{e}")
        sys.exit(1)

    required_methods = ["get_ape_info"]
    for m in required_methods:
        if m not in dir(get_ape_info):
            print( "%s not defined"%m )
            sys.exit(1)

    apes_json = Path(__file__).parent.absolute()
    apes_json = apes_json / 'apes.json'
    if not apes_json.is_file():  # if runtests_local
        apes_json = Path(__file__).parent.absolute()
        apes_json = apes_json / '.guides' / 'tests' / 'apes.json'
    try:
        with open(apes_json, 'r') as json_file:
            apes = json.load(json_file)
    except Exception as e:
        print( "Failed to load ape_data -- please contact your instructor" )
   
    num_tests = 5
    num_passed = 0
    apeIDs = random.sample(apes.keys(),num_tests)

    for apeID in apeIDs:
        print( f"Test {apeID}" )
        try:
            ape_data = get_ape_info.get_ape_info(int(apeID))
        except Exception as e:
            print( "Error: get_ape_info failed" )
            print( e )
            continue

        if ape_data['eyes'] == apes[apeID]['eyes'] and ape_data['image'] == apes[apeID]['image'] and ape_data['owner'][0:2] == "0x":
            num_passed += 1
        else:
            print(f"Expected: eyes: {apes[apeID]['eyes']}\timage: {apes[apeID]['image']}\towner: {apes[apeID]['owner']}")
            print(f"Returned: eyes: {ape_data['eyes']}\timage: {ape_data['image']}\towner: {ape_data['owner']}")

    return int( 100*float(num_passed)/num_tests )

if __name__ == '__main__':
    print( validate("") )
