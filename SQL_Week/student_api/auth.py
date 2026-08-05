from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException,Depends
from database import get_db
from sqlalchemy.orm import Session
import models

SECRET_KEY="ANGEL_BEN"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data):
    to_encode=data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})

    encode_jwt =jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return encode_jwt

def verify_access_token(token):
    try:
        decode_jwt=jwt.decode(
          token,
          SECRET_KEY,
          algorithms=[ALGORITHM]
        )
        email = decode_jwt["sub"]
    
        if email is None:
            raise HTTPException(
            status_code=401,
            detail="Invalid token"
        ) 
        return email

    except JWTError:
        raise HTTPException(
         status_code=401,
         detail ="Invalid token"
        )
def get_current_user(
    token:str = Depends(oauth2_scheme),
    db:Session = Depends(get_db)
    ):
    email = verify_access_token(token)
    user = db.query(models.User).filter(models.User.email == email).first()
    
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )
    return user