from functools import wraps
from flask import request, abort
import jwt


class SimpleJWT:
    """
    Class to manage JWT Token in Flask
    """

    def __init__(self, secret, realm=None, algorithms=None):
        """
        Class constructor

        Initializes the secret key for the token
        :param secret: string - JWT Secret key
        :param realm: string - Authorization realm. Default Bearer
        :param algorithms: strings array - Supported algorithms. Default empty
        """
        self.secret = secret
        self.realm = realm if realm is not None else 'Bearer'
        self.algorithms = algorithms if algorithms is not None else []

    def jwt_required(self):
        """
        Decorator used to enforce JWT Authentication
        on views

        :return: function - endpoint secured with JWT
        """

        def decorator(f):
            @wraps(f)
            def decorated_function(*args, **kwargs):

                if not request.headers.has_key('Authorization'):
                    abort(401, "Authorization required")

                auth = request.headers['Authorization'].split()

                if len(auth) != 2:
                    abort(400, "Malformed authorization header")

                if auth[0].lower() != self.realm.lower():
                    abort(401, "Unsupported realm")

                try:
                    jwt.decode(auth[1], self.secret, algorithms=self.algorithms)
                except jwt.ExpiredSignatureError:
                    abort(401, "Signature has expired")
                except jwt.DecodeError:
                    abort(401, "Signature verification failed")
                except Exception:
                    abort(400, "JWT Error")

                return f(*args, **kwargs)

            return decorated_function

        return decorator
