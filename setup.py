from setuptools import find_packages
from setuptools import setup


setup(
    name='sll.theme',
    version='0.8',
    description="SLL Theme",
    long_description=open("README.rst").read(),
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='Taito Horiuchi',
    author_email='taito.horiuchi@abita.fi',
    url='https://github.com/taito/sll.theme',
    license='None-free',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['sll'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Products.CMFPlone',
        'Products.PloneFormGen',
        'collective.contentleadimage',
        'collective.cropimage',
        'collective.searchevent',
        'five.grok',
        'five.pt',
        'hexagonit.testing',
        'plone.app.theming',
        'plone.app.themingplugins',
        'setuptools'],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """)
