

import alembic
import alembic.config
import alembic.command
import os
from pyramid.paster import get_appsettings
from pyramid.scripting import prepare
from pyramid.testing import DummyRequest, testConfig
import pytest
import transaction
import webtest

from tugasindividu4_pwl_120140124 import main
from tugasindividu4_pwl_120140124 import models
from tugasindividu4_pwl_120140124.models.meta import Base

# Fixture untuk mengambil lokasi berkas konfigurasi .ini
def pytest_addoption(parser):
    parser.addoption('--ini', action='store', metavar='INI_FILE')

# Fixture untuk mendapatkan lokasi berkas .ini
@pytest.fixture(scope='session')
def ini_file(request):
    return os.path.abspath(request.config.option.ini or 'testing.ini')

# Fixture untuk mengambil pengaturan aplikasi dari berkas .ini
@pytest.fixture(scope='session')
def app_settings(ini_file):
    return get_appsettings(ini_file)

# Fixture untuk menginisialisasi database
@pytest.fixture(scope='session')
def dbengine(app_settings, ini_file):
    engine = models.get_engine(app_settings)
    alembic_cfg = alembic.config.Config(ini_file)
    Base.metadata.drop_all(bind=engine)
    alembic.command.stamp(alembic_cfg, None, purge=True)
    alembic.command.upgrade(alembic_cfg, "head")
    yield engine
    Base.metadata.drop_all(bind=engine)
    alembic.command.stamp(alembic_cfg, None, purge=True)

# Fixture untuk menginisialisasi aplikasi Pyramid
@pytest.fixture(scope='session')
def app(app_settings, dbengine):
    return main({}, dbengine=dbengine, **app_settings)

# Fixture untuk menginisialisasi transaksi
@pytest.fixture
def tm():
    tm = transaction.TransactionManager(explicit=True)
    tm.begin()
    tm.doom()
    yield tm
    tm.abort()

# Fixture untuk mengambil sesi basis data
@pytest.fixture
def dbsession(app, tm):
    session_factory = app.registry['dbsession_factory']
    return models.get_tm_session(session_factory, tm)

# Fixture untuk pengujian aplikasi web
@pytest.fixture
def testapp(app, tm, dbsession):
    testapp = webtest.TestApp(app, extra_environ={
        'HTTP_HOST': 'example.com',
        'tm.active': True,
        'tm.manager': tm,
        'app.dbsession': dbsession,
    })
    return testapp

# Fixture untuk permintaan aplikasi Pyramid
@pytest.fixture
def app_request(app, tm, dbsession):
    with prepare(registry=app.registry) as env:
        request = env['request']
        request.host = 'example.com'
        request.dbsession = dbsession
        request.tm = tm
        yield request

# Fixture untuk permintaan dummy ringan
@pytest.fixture
def dummy_request(tm, dbsession):
    request = DummyRequest()
    request.host = 'example.com'
    request.dbsession = dbsession
    request.tm = tm
    return request

# Fixture untuk konfigurasi dummy
@pytest.fixture
def dummy_config(dummy_request):
    with testConfig(request=dummy_request) as config:
        yield config
