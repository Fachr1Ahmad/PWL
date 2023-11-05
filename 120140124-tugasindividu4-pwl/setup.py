import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyjwt',
    'plaster_pastedeploy',
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'waitress',
    'PyMySQL',
    'bcrypt',
    'alembic',
    'pyramid_retry',
    'pyramid_tm',
    'pyramid_jwt',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
]

tests_require = [
    'WebTest',
    'pytest',
    'pytest-cov',
]

setup(
    name='tugasindividu4_pwl_120140124',
    version='0.0',
    description='tugasindividu4-pwl-120140124',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = tugasindividu4_pwl_120140124:main',
        ],
        'console_scripts': [
            'initialize_tugasindividu4_pwl_120140124_db=tugasindividu4_pwl_120140124.scripts.initialize_db:main',
        ],
    },
)
