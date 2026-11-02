import json
import tempfile
import unittest
from pathlib import Path

from src.validate_dataset import validate_dataset


class TestDatasetValidation(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.path = Path(self.temp_dir.name) / "dataset.json"

    def tearDown(self):
        self.temp_dir.cleanup()

    def write_dataset(self, records):
        self.path.write_text(json.dumps(records), encoding="utf-8")

    def test_valid_dataset(self):
        self.write_dataset([
            {
                "instruction": "Translate to French",
                "input": "Hello",
                "output": "Bonjour"
            }
        ])
        self.assertTrue(validate_dataset(self.path))

    def test_missing_output(self):
        self.write_dataset([
            {"instruction": "Translate", "input": "Hello"}
        ])
        with self.assertRaises(ValueError):
            validate_dataset(self.path)

    def test_empty_dataset(self):
        self.write_dataset([])
        with self.assertRaises(ValueError):
            validate_dataset(self.path)

    def test_empty_instruction(self):
        self.write_dataset([
            {"instruction": " ", "input": "Hello", "output": "Bonjour"}
        ])
        with self.assertRaises(ValueError):
            validate_dataset(self.path)

    def test_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            validate_dataset(self.path)


if __name__ == "__main__":
    unittest.main()
