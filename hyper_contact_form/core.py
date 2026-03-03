"""
Hyper static site contact form (formspree/getform)

Usage:
    from hyper_contact_form import form

    result = form("Hello World")
    print(result)
"""

__version__ = "1.0.0"


def form(text: str) -> str:
    """Process the input text.

    Args:
        text: Input string to process.

    Returns:
        Processed string result.
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected str, got {type(text).__name__}")
    if not text:
        return text

    return _process(text)


def _process(text: str) -> str:
    """Internal processing logic."""
    # Implementation varies by specific utility
    result = text.strip()
    return result


def batch(texts: list[str]) -> list[str]:
    """Process multiple strings at once.

    Args:
        texts: List of strings to process.

    Returns:
        List of processed strings.
    """
    return [form(t) for t in texts]


def is_valid(text: str) -> bool:
    """Check if the input is valid for processing.

    Args:
        text: String to validate.

    Returns:
        True if valid, False otherwise.
    """
    return isinstance(text, str) and len(text) > 0
