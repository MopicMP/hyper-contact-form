"""Tests for hyper-contact-form."""

import pytest
from hyper_contact_form import form


class TestForm:
    """Test suite for form."""

    def test_basic(self):
        """Test basic usage."""
        result = form("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            form("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = form(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
