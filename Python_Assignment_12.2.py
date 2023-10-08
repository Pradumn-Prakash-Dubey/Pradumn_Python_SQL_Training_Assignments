def suppress_exception(exception_type=None, result=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if exception_type is None:
                    return result
                else:
                    raise e
        return wrapper
    return decorator

@suppress_exception(exception_type=KeyError, result=False)
def authenticate(user, password):
    users={}
    print(f'authenticating {user}')
    try:
        return users[user]== password
    except KeyError:
        return False

result = authenticate("example_user", "password")
print(result)