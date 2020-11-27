from json_dumps import json_dumps

def test_turn_int_into_string():
    assert json_dumps(1) == '1'

def test_turn_float_into_string():
    assert json_dumps(1.2) == '1.2'

def test_turn_a_list_into_string():
    assert json_dumps([1, 2]) == "['1', '2']"

def test_turn_a_dict_into_string():
    assert json_dumps({1: 2}) == "{'1': '2'}"

def test_turn_special_object_into_string():
    assert json_dumps(None) == "null"

def test_turn_multiple_spec_objects_intro_string():
    assert json_dumps([None, True, False]) == "['null', 'true', 'false']"

def test_turn_mutliple_spec_object_into_string2():
    assert json_dumps({None: True}) == "{'null': 'true'}"

def test_turn_nested_list_into_string():
    assert json_dumps([1, [1, 2]]) == "['1', ['1', '2']]"

def test_turn_nested_dict_into_string():
    assert json_dumps({1: {1: 2}}) == "{'1': {'1': '2'}}"