from fastapi import  Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import os

api_keys = [
    os.environ.get('API_KEY')
]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def api_key_auth(api_key: str = Depends(oauth2_scheme)):
    if api_key not in api_keys:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Forbidden"
        )
