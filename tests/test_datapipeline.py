import os
from unittest.mock import MagicMock, patch
import pytest
from src.enums.resource_types import resource_types
from src.data_pipeline import DataPipeline

pipeline = DataPipeline()

@pytest.fixture
def mock_insert_bulk_data():
    # Create a mock for the insert_bulk_data function
    with patch('src.data_pipeline.insert_bulk_data') as mock_insert:
        yield mock_insert

@pytest.fixture
def mock_create_db_engine():
    # Mock the create_db_engine function to return the mock_db_engine
    with patch('src.data_pipeline.create_db_engine') as mock_engine:
        yield mock_engine
        

@pytest.mark.parametrize('file_name, expected_output', 
[
    ('test_data.json', 'Processing'),
    ('test_data.csv', 'skipped'),
])
def test_extract(file_name, expected_output, capsys):
    pipeline.extract(os.path.join(os.path.abspath('tests'),file_name))
    assert expected_output in capsys.readouterr().out

@pytest.mark.parametrize('file_name', 
[
    ('test_data.json')
])
def test_transform(file_name):
    data = pipeline.extract(os.path.join(os.path.abspath('tests'), file_name))
    data_model = pipeline.transform(data)
    assert len(data_model) > 0
    assert len(data_model[resource_types.Patient.value]) == 1    
    assert len(data_model[resource_types.Observation.value]) == 2

@pytest.mark.parametrize('file_name', 
[
    ('test_data.json')
])
def test_load_data(file_name, mock_create_db_engine, mock_insert_bulk_data):
    data = pipeline.extract(os.path.join(os.path.abspath('tests'), file_name))
    data_model = pipeline.transform(data)
    pipeline.load(data_model)

    mock_create_db_engine.assert_called_once()
    mock_insert_bulk_data.call_count == 2

def test_load_empty_data( mock_create_db_engine, mock_insert_bulk_data):
    pipeline.load([])

    mock_create_db_engine.assert_not_called()
    mock_insert_bulk_data.assert_not_called()
    