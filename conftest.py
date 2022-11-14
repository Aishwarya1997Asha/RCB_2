import json
import logging

import pytest
from Library.details_extract import json_file_players


# conftest 1 file is opened and yielded that file with test file and closed the file

@pytest.fixture
def setup_file():
    with open(json_file_players) as file:
        logging.info("File Stream Opened")
        obj = json.load(file)
        yield obj
    logging.info("File Stream closed")