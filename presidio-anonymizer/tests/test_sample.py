import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    res = sample_run_anonymizer("My name is Bond.", 11, 15)

    # Result text should be anonymized
    assert isinstance(res.text, str)
    assert res.text == "My name is BIP."

    # Result structure should be a list with one OperatorResult describing the replacement
    assert isinstance(res.items, list)
    assert len(res.items) == 1

    item = res.items[0]
    # OperatorResult exposes attributes, not dict keys
    assert item.entity_type == "PERSON"
    assert item.text == "BIP"
    assert item.operator == "replace"
    assert item.start == 11
    # Presidio reports the replaced slice end as inclusive (15 -> 14)
    assert item.end == 14
    
    pass