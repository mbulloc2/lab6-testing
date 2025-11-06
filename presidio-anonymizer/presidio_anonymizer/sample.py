# presidio_anonymizer/sample.py

from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig


def sample_run_anonymizer(text: str, start: int, end: int):
    """
    Runs anonymization for a fixed PERSON entity and returns the result.
    Signature kept minimal for testability per lab spec.
    """
    engine = AnonymizerEngine()
    result = engine.anonymize(
        text=text,
        analyzer_results=[
            RecognizerResult(entity_type="PERSON", start=start, end=end, score=0.8)
        ],
        operators={"PERSON": OperatorConfig("replace", {"new_value": "BIP"})},
    )
    return result


if __name__ == "__main__":
    # Required: call with the Bond example and save to a variable
    res = sample_run_anonymizer("My name is Bond.", 11, 15)
    print(res)
