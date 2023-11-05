from pyramid.response import Response
from pyramid.request import Request
from sqlalchemy.exc import DBAPIError
from pyramid.view import view_config

from ..models import User


@view_config(route_name="register", request_method="POST", renderer="json")
def register(request: Request):
    try:
        username = request.json_body["username"]
        password = request.json_body["password"]
        role = request.json_body["role"]
        if role == "":
            role = "user"
        users = request.dbsession.query(User).filter(
            User.username == username).first()
        if users is None:
            user = User(username=username, password=password, role=role)
            request.dbsession.add(user)
            return Response(
                status=str(201),
                content_type="application/json",
                json={"message": "Register success!"},
            )
        else:
            return Response(
                status=str(400),
                content_type="application/json",
                json={"message": "Username already exist!"},
            )

    except DBAPIError:
        return Response(
            status=str(500),
            content_type="application/json",
            json={"message": "Internal server error!"},
        )


@view_config(route_name="login", request_method="POST", renderer="json")
def login(request: Request):
    try:
        username = request.json_body["username"]
        password = request.json_body["password"]
        user = request.dbsession.query(
            User).filter_by(username=username).first()
        if user is not None:
            if password == user.password:
                token = request.create_jwt_token(
                    user.id,
                    role=user.role,
                )
                return Response(
                    status=str(200),
                    content_type="application/json",
                    json={
                        "message": "Login success!",
                        "token": token,
                    },
                )
            else:
                return Response(
                    status=str(400),
                    content_type="application/json",
                    json={"message": "Wrong password!"},
                )
        else:
            return Response(
                status=str(400),
                content_type="application/json",
                json={"message": "User not found!"},
            )
    except DBAPIError:
        return Response(
            status=str(500),
            content_type="application/json",
            json={"message": "Internal server error!"},
        )


@view_config(route_name="logout", request_method="GET", renderer="json")
def logout(request: Request):
    try:
        return Response(
            status=str(200),
            content_type="application/json",
            json={"message": "Logout success!"},
        )
    except DBAPIError:
        return Response(
            status=str(500),
            content_type="application/json",
            json={"message": "Internal server error!"},
        )
