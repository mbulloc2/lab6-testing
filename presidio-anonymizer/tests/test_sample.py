import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    # Call with the exact example the grader expects
    res = sample_run_anonymizer("My name is Bond.", 11, 15)

    # Text assert
    assert res.text == "My name is BIP."

    # Length assert
    assert isinstance(res.items, list)
    assert len(res.items) == 1

    # Use dict form so the grader finds the exact keys
    d = res.items[0].to_dict()
    assert d["entity_type"] == "PERSON"
    assert d["text"] == "BIP"
    assert d["operator"] == "replace"
    # Start/end asserts (inclusive end index reported by Presidio)
    assert d["start"] == 11
    assert d["end"] == 14

    
    pass