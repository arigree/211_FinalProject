class CustomerDataError(Exception):
    """Raised when customer data cannot be retrieved."""


class CustomerQueryError(CustomerDataError):
    """Raised when customer query options are invalid."""


class CustomerValidationError(CustomerDataError):
    """Raised when submitted customer form data is invalid."""


class CustomerNotFoundError(CustomerDataError):
    """Raised when a requested customer record does not exist."""


class CustomerOperationError(CustomerDataError):
    """Raised when a create, update, or delete operation fails."""
