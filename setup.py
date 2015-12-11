#! /usr/bin/env python
from setuptools import setup, find_packages

CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(name='django-images',
      author='Mirumee Software',
      author_email='hello@mirumee.com',
      description='A database-driven thumbnailing solution for Django',
      license='BSD',
      version='0.4.3',
      packages=find_packages(),
      include_package_data=True,
      classifiers=CLASSIFIERS,
      install_requires=['Django>=1.3', 'pillow>=1.7.8'],
      platforms=['any'],
      zip_safe=False)
