import copy
import pytest
from fastapi.testclient import TestClient

from src.app import app, activities as activities_store


@pytest.fixture
def client():
    """Provide a TestClient and restore in-memory activities after each test."""
    original = copy.deepcopy(activities_store)
    with TestClient(app) as c:
        yield c
    # restore original activities to avoid test interdependence
    activities_store.clear()
    activities_store.update(original)
