from pyramid.response import Response
from pyramid.request import Request
from sqlalchemy.exc import DBAPIError
from pyramid.view import view_defaults, view_config
from datetime import datetime

from ..models import movie


@view_defaults(route_name="movie")
class movieView:
    def __init__(self, request):
        self.request: Request = request

    def server_error(self):
        return Response(
            status=str(500),
            content_type="application/json",
            json={"message": "Internal server error!"},
        )

    @view_config(request_method="GET", permission="view")
    def get_all_movies(self):
        try:
            movies = self.request.dbsession.query(movie).all()
            return Response(
                status=str(200),
                content_type="application/json",
                json={
                    "data": [
                        {
                            "id": movie.id,
                            "title": movie.title,
                            "studios": movie.studios,
                            "duration": movie.duration,
                            "created_at": str(movie.created_at),
                        }
                        for movie in movies
                    ]
                },
            )
        except DBAPIError:
            self.server_error()

    @view_config(request_method="POST", permission="admin")
    def create_new_movie(self):
        try:
            title = self.request.json_body["title"]
            studios = self.request.json_body["studios"]
            duration = self.request.json_body["duration"]
            movie = movie(title=title, studios=studios, duration=duration)
            self.request.dbsession.add(movie)

            return Response(
                status=str(201),
                content_type="application/json",
                json={"message": "Success add new movie"},
            )

        except DBAPIError:
            self.server_error()

    @view_config(route_name="movie_id", request_method="GET", permission="view")
    def get_movie_by_id(self):
        try:
            id = self.request.matchdict["id"]  # type:ignore
            movie = (
                self.request.dbsession.query(
                    movie).filter_by(id=id).first()
            )
            if movie:
                return Response(
                    status=str(200),
                    content_type="application/json",
                    json={
                        "data": {
                            "id": movie.id,
                            "title": movie.title,
                            "studios": movie.studios,
                            "duration": movie.duration,
                            "created_at": str(movie.created_at),
                        }
                    },
                )
            else:
                return Response(
                    status=str(404),
                    content_type="application/json",
                    json={"message": "movie not found!"},
                )
        except DBAPIError:
            self.server_error()

    @view_config(route_name="movie_id", request_method="PUT", permission="admin")
    def update_movie_by_id(self):
        try:
            id = self.request.matchdict["id"]  # type:ignore
            movie = (
                self.request.dbsession.query(
                    movie).filter_by(id=id).first()
            )
            if movie:
                movie.title = self.request.json_body["title"]
                movie.studios = self.request.json_body["studios"]
                movie.duration = self.request.json_body["duration"]
                movie.created_at = datetime.now()

                return Response(
                    status=str(200),
                    content_type="application/json",
                    json={"message": "Success update movie!"},
                )
            else:
                return Response(
                    status=str(404),
                    content_type="application/json",
                    json={"message": "movie not found!"},
                )
        except DBAPIError:
            self.server_error()

    @view_config(
        route_name="movie_id", request_method="DELETE", permission="admin"
    )
    def delete_movie_by_id(self):
        try:
            id = self.request.matchdict["id"]  # type:ignore
            movie = (
                self.request.dbsession.query(
                    movie).filter_by(id=id).first()
            )
            if movie:
                self.request.dbsession.delete(movie)
                return Response(
                    status=str(200),
                    content_type="application/json",
                    json={"message": "Success delete movie!"},
                )
            else:
                return Response(
                    status=str(404),
                    content_type="application/json",
                    json={"message": "movie not found!"},
                )
        except DBAPIError:
            self.server_error()
