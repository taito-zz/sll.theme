from setuptools import find_packages
from setuptools import setup
import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


version = read('sll', 'theme', 'version.txt').strip()

long_description = (
    read('sll', 'theme', 'docs', 'index.rst'))

setup(name='sll.theme',
      version=version,
      description="SLL Theme",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Hexagon IT',
      author_email='oss@hexagonit.fi',
      url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['sll'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'hexagonit.portletstyle',
          'hexagonit.testing',
          'manuel',
          'plone.app.testing',
          'plone.app.theming',
          'plone.browserlayer',
          'setuptools',
          'unittest2',
          'zope.i18nmessageid',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
