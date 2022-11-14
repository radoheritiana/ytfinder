from setuptools import setup

setup(
    name='Youtube tag finder',
    version='1.0',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "beautifulsoup4==4.11.1",
        "bs4==0.0.1",
        "certifi==2022.9.24",
        "charset-normalizer==2.1.1",
        "click==8.1.3",
        "Flask==2.2.2",
        "Flask-Cors==3.0.10",
        "gunicorn==20.1.0",
        "idna==3.4",
        "itsdangerous==2.1.2",
        "Jinja2==3.1.2",
        "MarkupSafe==2.1.1",
        "requests==2.28.1",
        "six==1.16.0",
        "soupsieve==2.3.2.post1",
        "urllib3==1.26.12",
        "Werkzeug==2.2.2",
        "YTagFinder==0.0.2"
    ]
)