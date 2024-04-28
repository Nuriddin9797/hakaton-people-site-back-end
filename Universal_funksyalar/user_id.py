from fastapi import Depends

from models.users import Users
from routes.login import get_current_user


def get_current_user_id(current_user: Users = Depends(get_current_user)):
    return current_user.id