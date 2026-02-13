"""Password Hashing Utility using bcrypt"""
from passlib.context import CryptContext


class PasswordHasher:
    """Handles password hashing and verification using bcrypt"""
    
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    def hash(self, password: str) -> str:
        """Hash a plain text password
        
        Args:
            password: Plain text password to hash
            
        Returns:
            Hashed password string
        """
        return self.pwd_context.hash(password)
    
    def verify(self, plain_password: str, hashed_password: str) -> bool:
        """Verify a password against a hash
        
        Args:
            plain_password: Plain text password to verify
            hashed_password: Hashed password to verify against
            
        Returns:
            True if password matches, False otherwise
        """
        return self.pwd_context.verify(plain_password, hashed_password)
