from fastapi import HTTPException, status


class UserValidationError(HTTPException):

    def __init__(self, error: str):
        super(UserValidationError, self).__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            headers={'WWW-Authenticate': 'Bearer'},
            detail=error,
        )


class CouldNotValidateCredantialError(HTTPException):
    """Ошибка верификации токена"""

    def __init__(self):
        super(CouldNotValidateCredantialError, self).__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials',
            headers={'WWW-Authenticate': 'Bearer'},
        )


class IncorrectCredantialError(HTTPException):
    """Ошибка входа и регистрации."""

    def __init__(self):
        super(IncorrectCredantialError, self).__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'},
        )
