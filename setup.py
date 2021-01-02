from distutils.core import setup
setup(
  name = 'yacache',
  packages = ['yacache'],
  version = '0.1',
  license = 'MIT',
  description = 'yacache is yet another python cache. This library allows for caching function results in whatever type they were initially returned. This is meant to be fast, optional, and, most importantly, retain all docstrings unlike some other caching libs.',
  author = 'conceptual.io',
  author_email = 'admin@conceptual.io',
  url = 'https://github.com/conceptualio',
  download_url = 'https://github.com/conceptualio/yacache/archive/0.1.tar.gz',
  keywords = ['CACHE'],
  install_requires = [
          'copy',
          'datetime',
          'json',
          'wrapt'
      ],
  classifiers = [
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Build Tools',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 3'
  ],
)