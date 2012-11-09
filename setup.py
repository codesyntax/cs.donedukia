from setuptools import setup, find_packages
import os

version = '2.1.2'

setup(name='cs.donedukia',
      version=version,
      description="Folderish pages to simplify plone page-folder story",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone page folderish',
      author='Mikel Larreategi',
      author_email='mlarreategi@codesyntax.com',
      url='http://github.com/codesyntax/cs.donedukia',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cs'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone >= 4.0',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
