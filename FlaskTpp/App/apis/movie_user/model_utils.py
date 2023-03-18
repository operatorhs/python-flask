from App.models.movie_user import MovieUser


def get_user(user_ident):
    user = MovieUser.query.get(user_ident)
    if user:
        return user

    user = MovieUser.query.filter(MovieUser.phone == user_ident).first()
    if user:
        return user

    user = MovieUser.query.filter(MovieUser.username == user_ident).first()
    if user:
        return user

    return None

