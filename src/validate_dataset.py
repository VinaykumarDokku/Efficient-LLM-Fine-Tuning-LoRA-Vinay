"""Validate instruction-tuning JSON datasets."""

import json
import sys
from pathlib import Path


def validate_dataset(file_path):
    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"Dataset not found: {path}")

    with path.open(encoding="utf-8") as file:
        records = json.load(file)

    if not isinstance(records, list) or not records:
        raise ValueError("Dataset must be a non-empty JSON list.")

    required_fields = ("instruction", "input", "output")

    for index, record in enumerate(records, start=1):
        if not isinstance(record, dict):
            raise ValueError(f"Record {index} must be an object.")

        for field in required_fields:
            if field not in record:
                raise ValueError(
                    f"Record {index} missing field: {field}"
                )
            if not isinstance(record[field], str):
                raise ValueError(
                    f"Record {index}: {field} must be a string."
                )

        if not record["instruction"].strip():
            raise ValueError(
                f"Record {index}: instruction cannot be empty."
            )

        if not record["output"].strip():
            raise ValueError(
                f"Record {index}: output cannot be empty."
            )

    print(f"Dataset valid: {len(records)} records checked.")
    return True


if __name__ == "__main__":
    dataset_path = (
        sys.argv[1]
        if len(sys.argv) > 1
        else "instruction_dataset.json"
    )
    validate_dataset(dataset_path)
