import os
import pytest
from utils.driver_factory import create_driver

def pytest_sessionstart(session):
    """Create reports directory before any tests start."""
    reports_dir = "reports"
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()
