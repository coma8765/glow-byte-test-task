from typing import Annotated

from fastapi import Header, Depends, HTTPException

from src.datasources import UserSource


def get_user(
    x_user_name: Annotated[str | None, Header()] = None,
    user_source: UserSource = Depends(),
):
    try:
        user = user_source.get_by_username(x_user_name)
    except user_source.errors.userNotFound:
        raise HTTPException(status_code=404, detail="user not found")

    return user
