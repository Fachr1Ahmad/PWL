from pyramid.response import Response
from sqlalchemy.exc import DBAPIError
from pyramid.view import view_defaults, view_config

from ..models import User


@view_defaults(route_name="user")
class UserView:
    def __init__(self, request):
        self.request = request

    def server_error(self):
        return Response(
            status=str(500),
            content_type="application/json",
            json={"message": "Internal server error!"},
        )

    @view_config(request_method="POST", permission="admin")
    def create_new_user(self):
        try:
            username = self.request.json_body["username"]
            password = self.request.json_body["password"]
            role = self.request.json_body["role"]
            user = User(username=username, password=password, role=role)
            self.request.dbsession.add(user)

            return Response(
                status=str(201),
                content_type="application/json",
                json={"message": "Success add new user"},
            )
        except DBAPIError:
            self.server_error()

    @view_config(request_method="GET", permission="admin")
    def get_all_users(self):
        try:
            users = self.request.dbsession.query(User).all()
            return Response(
                status=str(200),
                content_type="application/json",
                json={
                    "data": [
                        {
                            "id": user.id,
                            "username": user.username,
                            "password": user.password,
                            "role": user.role,
                        }
                        for user in users
                    ]
                },
            )
        except DBAPIError:
            self.server_error()
