from setuptools import find_packages
from setuptools import setup
import os

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('sll', 'theme', 'docs', 'index.rst'))

setup(name='sll.theme',
      version='0.2',
      description="SLL Theme",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='INICIE, Inc.',
      author_email='taito.horiuchi@inicie.net',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['sll'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'hexagonit.testing',
          'plone.app.theming',
          'plone.browserlayer',
          'setuptools',
          'zope.i18nmessageid',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
