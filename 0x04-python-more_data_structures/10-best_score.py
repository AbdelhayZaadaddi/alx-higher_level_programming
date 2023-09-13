#!/usr/bin/python
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    score_h = max(a_dictionary.values())
    if a_dictionary:
        for key, value in a_dictionary.items():
            if value is score_h:
                return key
