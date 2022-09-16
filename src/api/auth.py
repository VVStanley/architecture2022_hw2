from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from models import Token, User, UserCreate
from services.auth import AuthService, get_current_user

router = APIRouter(prefix='/auth', tags=['auth'])


@router.post(
    '/sign-up/', response_model=Token, status_code=status.HTTP_201_CREATED,
)
def sign_up(
    user_data: UserCreate,
    auth_service: AuthService = Depends(),
):
    return auth_service.register_new_user(user_data)


@router.post('/sign-in/', response_model=Token)
def sign_in(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(),
):
    return auth_service.authenticate_user(
        form_data.username, form_data.password,
    )


@router.get('/token/', response_model=Token)
def get_token(
    user: User = Depends(get_current_user),
    auth_service: AuthService = Depends(),
):
    return auth_service.create_token(user)


@router.get('/user/', response_model=User)
def get_user(
    user: User = Depends(get_current_user),
    auth_service: AuthService = Depends(),
):
    db_user = auth_service.get_user_by_username(user.username)
    return User.from_orm(db_user)
