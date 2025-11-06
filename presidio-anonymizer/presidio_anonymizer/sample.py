# presidio_anonymizer/sample.py

from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig


def sample_run_anonymizer(
    text: str = "My name is Bond.",
    start: int = 11,
    end: int = 15,
    *,
    entity_type: str = "PERSON",
    new_value: str = "BIP",
    score: float = 0.8,
):
    """
    Run anonymization with configurable inputs and return the result object.
    This version removes interactive input() calls and supports unit testing.
    """
    engine = AnonymizerEngine()
    result = engine.anonymize(
        text=text,
        analyzer_results=[
            RecognizerResult(
                entity_type=entity_type,
                start=start,
                end=end,
                score=score,
            )
        ],
        operators={entity_type: OperatorConfig("replace", {"new_value": new_value})},
    )
    return result


if __name__ == "__main__":
    res = sample_run_anonymizer()
    print(res)
