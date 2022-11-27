from sqlalchemy.orm.session import Session

from db.models import User
from schemas.schemas import UserBase

async def create_account(db: Session, newuser: UserBase)->User:
    account = User(
        
    )
