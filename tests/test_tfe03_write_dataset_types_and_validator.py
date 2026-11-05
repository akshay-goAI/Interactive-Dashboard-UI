# Unit tests for e75d0ee0-21c9-40a4-a89d-59686a2fbd4b
from src.services.tfe03_write_dataset_types_and_validator_service import execute_tfe03_write_dataset_types_and_validator

def test_execute_tfe03_write_dataset_types_and_validator():
    res = execute_tfe03_write_dataset_types_and_validator()
    assert res['status'] == 'success'
