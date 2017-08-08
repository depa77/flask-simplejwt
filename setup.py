"""
Flask-SimpleJWT
-------------------
Simple JWT extension for Flask
"""
from setuptools import setup

setup(name='Flask-SimpleJWT',
      version='0.1.0',
      url='https://github.com/depa77/flask-simplejwt',
      license='MIT',
      author='Luca Depaoli',
      author_email='depa77@gmail.com',
      description='Simple JWT extension for Flask',
      long_description='Simple JWT extension to secure Flask endpoints',
      keywords = ['flask', 'jwt', 'json web token'],
      packages=['flask_simplejwt'],
      zip_safe=False,
      platforms='any',
      install_requires=['Flask', 'PyJWT'],
      classifiers=[
          'Development Status :: 1 - Planning',
          'Environment :: Web Environment',
          'Framework :: Flask',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ])
