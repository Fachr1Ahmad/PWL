import argparse
import sys

from pyramid.paster import bootstrap, setup_logging
from sqlalchemy.exc import OperationalError

from .. import models

def setup_models(dbsession):
    """
    Add or update models / fixtures in the database.

    """
    movies = [
        models.Movie(
            title="Ada Apa Dengan Cinta",
            studios="Miles Films",
            duration="1 hr. 52 min"
        ), 
        models.Movie(
            title="Laskar Pelangi",
            studios="Miles Films",
            duration="2 hr. 4 min"
        ),
        models.Movie(
            title="Ayat-Ayat Cinta",
            studios="MD Pictures",
            duration="2 hr"
        ),
        models.Movie(
            title="Negeri 5 Menara",
            studios="Miles Films",
            duration="1 hr. 56 min."
        ),
        models.Movie(
            title="Rudy Habibie",
            studios="MD Pictures",
            duration="2 hr. 12 min"
        ),
        models.Movie(
            title="Gie",
            studios="Miles Films",
            duration="2 hr. 2 min"
        ),
        models.Movie(
            title="Perempuan Berkalung Sorban",
            studios="Miles Films",
            duration="2 hr. 2 min"
        ),
        models.Movie(
            title="AADC 2",
            studios="Miles Films",
            duration="2 hr. 3 min"
        ),
        models.Movie(
            title="3 Hari untuk Selamanya",
            studios="Miles Films",
            duration="1 hr. 52 min"
        ),
        models.Movie(
            title="Laskar Pelangi 2: Edensor",
            studios="Miles Films",
            duration="1 hr. 57 min"
        ),
    ]

    for movie in movies:
        dbsession.add(movie)

def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "config_uri",
        help="Configuration file, e.g., development.ini",
    )
    return parser.parse_args(argv[1:])

def main(argv=sys.argv):
    args = parse_args(argv)
    setup_logging(args.config_uri)
    env = bootstrap(args.config_uri)

    try:
        with env["request"].tm:
            dbsession = env["request"].dbsession
            setup_models(dbsession)
    except OperationalError:
        print(
            """
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for description and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.
            """
        )

if __name__ == '__main__':
    main()
