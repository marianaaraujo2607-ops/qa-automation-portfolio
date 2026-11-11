from pathlib import Path

import pytest
import schemathesis
from hypothesis import settings
from schemathesis.specs.openapi.checks import unsupported_method

pytestmark = pytest.mark.contract

SPEC = Path(__file__).resolve().parent.parent / "openapi.yaml"
schema = schemathesis.openapi.from_path(SPEC)


@schema.include(method="GET").parametrize()
@settings(max_examples=20, deadline=None)
def test_api_contract(case, base_url):
    case.call_and_validate(
        base_url=base_url,
        excluded_checks=[unsupported_method],
    )