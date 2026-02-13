"""User Management Use Cases"""
from typing import List, Optional
from app.domain.entities.user import User
from app.domain.exceptions import UserNotFoundError, UnauthorizedError
from app.infrastructure.repositories.user_repository import UserRepository
from app.infrastructure.security.password import PasswordHasher


class UserUseCase:
    """User management business logic use cases"""
    
    def __init__(
        self,
        user_repository: UserRepository,
        password_hasher: PasswordHasher
    ):
        self.user_repository = user_repository
        self.password_hasher = password_hasher
    
    def get_user_by_id(self, user_id: int) -> User:
        """Get user by ID
        
        Args:
            user_id: User ID to retrieve
            
        Returns:
            User entity
            
        Raises:
            UserNotFoundError: If user is not found
        """
        user = self.user_repository.get_by_id(user_id)
        if not user:
            raise UserNotFoundError(f"User with ID {user_id} not found")
        return user
    
    def get_all_users(self, skip: int = 0, limit: int = 100) -> List[User]:
        """Get all users with pagination
        
        Args:
            skip: Number of records to skip
            limit: Maximum number of records to return
            
        Returns:
            List of user entities
        """
        return self.user_repository.get_all(skip=skip, limit=limit)
    
    def update_user(
        self,
        user_id: int,
        current_user: User,
        email: Optional[str] = None,
        username: Optional[str] = None,
        full_name: Optional[str] = None,
        password: Optional[str] = None,
        is_active: Optional[bool] = None,
        is_superuser: Optional[bool] = None
    ) -> User:
        """Update user information
        
        Args:
            user_id: ID of user to update
            current_user: Currently authenticated user
            email: New email (optional)
            username: New username (optional)
            full_name: New full name (optional)
            password: New password (optional)
            is_active: New active status (optional)
            is_superuser: New superuser status (optional)
            
        Returns:
            Updated user entity
            
        Raises:
            UserNotFoundError: If user is not found
            UnauthorizedError: If user is not authorized to update
        """
        # Check if user exists
        user = self.user_repository.get_by_id(user_id)
        if not user:
            raise UserNotFoundError(f"User with ID {user_id} not found")
        
        # Authorization check: only allow updating own profile or if superuser
        if current_user.id != user_id and not current_user.is_superuser:
            raise UnauthorizedError("Not authorized to update this user")
        
        # Only superuser can change is_active and is_superuser
        if not current_user.is_superuser:
            is_active = None
            is_superuser = None
        
        # Prepare update data
        update_data = {}
        
        if email is not None:
            update_data["email"] = email
        
        if username is not None:
            update_data["username"] = username
        
        if full_name is not None:
            update_data["full_name"] = full_name
        
        if password is not None:
            update_data["hashed_password"] = self.password_hasher.hash(password)
        
        if is_active is not None:
            update_data["is_active"] = is_active
        
        if is_superuser is not None:
            update_data["is_superuser"] = is_superuser
        
        # Update user
        updated_user = self.user_repository.update(user_id, update_data)
        if not updated_user:
            raise UserNotFoundError(f"User with ID {user_id} not found")
        
        return updated_user
    
    def delete_user(self, user_id: int, current_user: User) -> bool:
        """Delete a user
        
        Args:
            user_id: ID of user to delete
            current_user: Currently authenticated user
            
        Returns:
            True if deleted successfully
            
        Raises:
            UserNotFoundError: If user is not found
            UnauthorizedError: If user is not authorized to delete
        """
        # Check if user exists
        user = self.user_repository.get_by_id(user_id)
        if not user:
            raise UserNotFoundError(f"User with ID {user_id} not found")
        
        # Authorization check: only superuser can delete users
        if not current_user.is_superuser:
            raise UnauthorizedError("Only superuser can delete users")
        
        # Delete user
        result = self.user_repository.delete(user_id)
        if not result:
            raise UserNotFoundError(f"User with ID {user_id} not found")
        
        return True
