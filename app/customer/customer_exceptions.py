class CustomerDataError(Exception):
    """Raised when customer data cannot be retrieved."""


class CustomerQueryError(CustomerDataError):
    """Raised when customer query options are invalid."""
