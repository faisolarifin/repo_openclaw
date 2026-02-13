"""User Repository Implementation"""
from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.entities.user import User
from app.infrastructure.database.models import UserModel


class UserRepository:
    """Repository for User data access"""
    
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, user: User) -> User:
        """Create a new user in database
        
        Args:
            user: User entity to create
            
        Returns:
            Created user entity with ID
        """
        db_user = UserModel(
            email=user.email,
            username=user.username,
            full_name=user.full_name,
            hashed_password=user.hashed_password,
            is_active=user.is_active,
            is_superuser=user.is_superuser
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return User.model_validate(db_user)
    
    def get_by_id(self, user_id: int) -> Optional[User]:
        """Get user by ID
        
        Args:
            user_id: User ID to search for
            
        Returns:
            User entity if found, None otherwise
        """
        db_user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if db_user:
            return User.model_validate(db_user)
        return None
    
    def get_by_email(self, email: str) -> Optional[User]:
        """Get user by email
        
        Args:
            email: Email address to search for
            
        Returns:
            User entity if found, None otherwise
        """
        db_user = self.db.query(UserModel).filter(UserModel.email == email).first()
        if db_user:
            return User.model_validate(db_user)
        return None
    
    def get_by_username(self, username: str) -> Optional[User]:
        """Get user by username
        
        Args:
            username: Username to search for
            
        Returns:
            User entity if found, None otherwise
        """
        db_user = self.db.query(UserModel).filter(UserModel.username == username).first()
        if db_user:
            return User.model_validate(db_user)
        return None
    
    def get_all(self, skip: int = 0, limit: int = 100) -> List[User]:
        """Get all users with pagination
        
        Args:
            skip: Number of records to skip
            limit: Maximum number of records to return
            
        Returns:
            List of user entities
        """
        db_users = self.db.query(UserModel).offset(skip).limit(limit).all()
        return [User.model_validate(db_user) for db_user in db_users]
    
    def update(self, user_id: int, user_data: dict) -> Optional[User]:
        """Update user data
        
        Args:
            user_id: ID of user to update
            user_data: Dictionary of fields to update
            
        Returns:
            Updated user entity if found, None otherwise
        """
        db_user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if not db_user:
            return None
        
        for key, value in user_data.items():
            if hasattr(db_user, key) and value is not None:
                setattr(db_user, key, value)
        
        self.db.commit()
        self.db.refresh(db_user)
        return User.model_validate(db_user)
    
    def delete(self, user_id: int) -> bool:
        """Delete a user
        
        Args:
            user_id: ID of user to delete
            
        Returns:
            True if deleted, False if not found
        """
        db_user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if not db_user:
            return False
        
        self.db.delete(db_user)
        self.db.commit()
        return True
