from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='django-highlander',
    version='0.0.1',
    description=u"Django management Command that prevents simultaneous instances",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author=u"Paulo Scardine",
    author_email='paulos@xtend.com.br',
    url='https://github.com/scardine/django-highlander',
    license='MIT',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'django',
        'tendo',
    ],
)