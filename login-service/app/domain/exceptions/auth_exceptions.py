"""Authentication and Authorization Exceptions"""


class AuthenticationError(Exception):
    """Base authentication exception"""
    pass


class InvalidCredentialsError(AuthenticationError):
    """Raised when credentials are invalid"""
    pass


class TokenExpiredError(AuthenticationError):
    """Raised when token has expired"""
    pass


class InvalidTokenError(AuthenticationError):
    """Raised when token is invalid"""
    pass


class UserAlreadyExistsError(Exception):
    """Raised when attempting to create a user that already exists"""
    pass


class UserNotFoundError(Exception):
    """Raised when user is not found"""
    pass


class InactiveUserError(AuthenticationError):
    """Raised when user account is inactive"""
    pass


class UnauthorizedError(AuthenticationError):
    """Raised when user is not authorized to perform action"""
    pass
