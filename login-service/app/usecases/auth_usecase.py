"""Authentication Use Cases"""
from typing import Dict, Any
from jose import JWTError
from app.domain.entities.user import User
from app.domain.exceptions import (
    InvalidCredentialsError,
    UserAlreadyExistsError,
    InactiveUserError,
    InvalidTokenError,
    TokenExpiredError
)
from app.infrastructure.repositories.user_repository import UserRepository
from app.infrastructure.security.password import PasswordHasher
from app.infrastructure.security.jwt import JWTHandler


class AuthUseCase:
    """Authentication business logic use cases"""
    
    def __init__(
        self,
        user_repository: UserRepository,
        password_hasher: PasswordHasher,
        jwt_handler: JWTHandler
    ):
        self.user_repository = user_repository
        self.password_hasher = password_hasher
        self.jwt_handler = jwt_handler
    
    def register(self, email: str, username: str, password: str, full_name: str = None) -> User:
        """Register a new user
        
        Args:
            email: User email address
            username: Unique username
            password: Plain text password
            full_name: Optional full name
            
        Returns:
            Created user entity
            
        Raises:
            UserAlreadyExistsError: If email or username already exists
        """
        # Check if user already exists
        if self.user_repository.get_by_email(email):
            raise UserAlreadyExistsError(f"User with email {email} already exists")
        
        if self.user_repository.get_by_username(username):
            raise UserAlreadyExistsError(f"User with username {username} already exists")
        
        # Hash password
        hashed_password = self.password_hasher.hash(password)
        
        # Create user entity
        user = User(
            email=email,
            username=username,
            full_name=full_name,
            hashed_password=hashed_password
        )
        
        # Save to database
        created_user = self.user_repository.create(user)
        return created_user
    
    def login(self, username: str, password: str) -> Dict[str, Any]:
        """Authenticate user and generate tokens
        
        Args:
            username: Username or email
            password: Plain text password
            
        Returns:
            Dictionary containing access_token, refresh_token, and token_type
            
        Raises:
            InvalidCredentialsError: If credentials are invalid
            InactiveUserError: If user account is inactive
        """
        # Try to find user by username or email
        user = self.user_repository.get_by_username(username)
        if not user:
            user = self.user_repository.get_by_email(username)
        
        # Verify user exists and password is correct
        if not user or not self.password_hasher.verify(password, user.hashed_password):
            raise InvalidCredentialsError("Invalid username or password")
        
        # Check if user is active
        if not user.is_active:
            raise InactiveUserError("User account is inactive")
        
        # Generate tokens
        access_token = self.jwt_handler.create_access_token(
            data={"sub": str(user.id), "username": user.username}
        )
        refresh_token = self.jwt_handler.create_refresh_token(
            data={"sub": str(user.id), "username": user.username}
        )
        
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }
    
    def refresh_access_token(self, refresh_token: str) -> Dict[str, str]:
        """Generate new access token from refresh token
        
        Args:
            refresh_token: Valid refresh token
            
        Returns:
            Dictionary containing new access_token and token_type
            
        Raises:
            InvalidTokenError: If token is invalid
            TokenExpiredError: If token has expired
        """
        try:
            payload = self.jwt_handler.decode_token(refresh_token)
            
            # Verify token type
            if payload.get("type") != "refresh":
                raise InvalidTokenError("Invalid token type")
            
            user_id = payload.get("sub")
            username = payload.get("username")
            
            if not user_id:
                raise InvalidTokenError("Invalid token payload")
            
            # Verify user still exists and is active
            user = self.user_repository.get_by_id(int(user_id))
            if not user:
                raise InvalidTokenError("User not found")
            
            if not user.is_active:
                raise InactiveUserError("User account is inactive")
            
            # Generate new access token
            access_token = self.jwt_handler.create_access_token(
                data={"sub": user_id, "username": username}
            )
            
            return {
                "access_token": access_token,
                "token_type": "bearer"
            }
            
        except JWTError as e:
            if "expired" in str(e).lower():
                raise TokenExpiredError("Refresh token has expired")
            raise InvalidTokenError(f"Invalid token: {str(e)}")
    
    def verify_token(self, token: str) -> User:
        """Verify access token and return user
        
        Args:
            token: JWT access token
            
        Returns:
            User entity
            
        Raises:
            InvalidTokenError: If token is invalid
            TokenExpiredError: If token has expired
        """
        try:
            payload = self.jwt_handler.decode_token(token)
            
            # Verify token type
            if payload.get("type") != "access":
                raise InvalidTokenError("Invalid token type")
            
            user_id = payload.get("sub")
            if not user_id:
                raise InvalidTokenError("Invalid token payload")
            
            # Get user from database
            user = self.user_repository.get_by_id(int(user_id))
            if not user:
                raise InvalidTokenError("User not found")
            
            if not user.is_active:
                raise InactiveUserError("User account is inactive")
            
            return user
            
        except JWTError as e:
            if "expired" in str(e).lower():
                raise TokenExpiredError("Access token has expired")
            raise InvalidTokenError(f"Invalid token: {str(e)}")
