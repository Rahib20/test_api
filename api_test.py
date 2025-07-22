from playwright.sync_api import Playwright, APIRequestContext
import pytest
import json
from typing import Generator


@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> APIRequestContext:
    url = "http://localhost:5000/"
    request_context = playwright.request.new_context(base_url=url)

    yield request_context
    request_context.dispose()


def test_get_schemas(api_request_context: APIRequestContext):
    response = api_request_context.get("/schemas")
    assert response.ok, 200


def test_post_schema(api_request_context: APIRequestContext):
    schema = {
        "name": "rahibschema",
        "schema": {
            "name": "string",
            "job": "job",
            "country code": "country code"
        }
    }
    response = api_request_context.post("/schema", data=schema)
    assert response.ok, 200
