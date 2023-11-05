from tugasindividu4_pwl_120140124 import models
from tugasindividu4_pwl_120140124.views.default import my_view
from tugasindividu4_pwl_120140124.views.notfound import notfound_view


def test_my_view_failure(app_request):
    info = my_view(app_request)
    assert info.status_int in [500, 200]


def test_my_view_success(app_request, dbsession):
    model = models.MyModel(name='one', value=55)
    dbsession.add(model)
    dbsession.flush()

    info = my_view(app_request)
    assert app_request.response.status_int == 200
    assert info.body.decode('utf-8') == 'Server running at port 6543'

    print(info.body)


def test_notfound_view(app_request):
    info = notfound_view(app_request)
    assert app_request.response.status_int == 404
    assert info == {'message': 'Not Found!'}
