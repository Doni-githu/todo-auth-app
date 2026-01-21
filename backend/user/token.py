from rest_framework_simplejwt.tokens import RefreshToken # type: ignore
from rest_framework_simplejwt.exceptions import AuthenticationFailed # type: ignore

class UserId:
    def __init__(self, id) -> None:
        self.id = id
    def __str__(self) -> str:
        return self.id

def get_token_for_user(user):
    if not user['is_active']:
        raise AuthenticationFailed("User is not active")
    user_id = UserId(user['id'])
    refresh = RefreshToken.for_user(user_id) # type: ignore

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }