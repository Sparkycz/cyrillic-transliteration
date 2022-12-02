from distutils.core import setup
setup(
  name='cyrtranslit',
  packages=['cyrtranslit'],
  version='0.4',
  description='Bi-directional Cyrillic transliteration. Transliterate Cyrillic script text to Roman alphabet text and vice versa.',
  author='Open Data Kosovo',
  author_email='dev@opendatakosovo.org',
  url='https://github.com/opendatakosovo/cyrillic-transliteration',
  download_url='https://github.com/opendatakosovo/cyrillic-transliteration/archive/v0.4.tar.gz',
  license='MIT',
  long_description='Transliteration is the conversion of a text from one script to another. Current version supports transliteration for Serbian, Macedonian, Montenegrin, and Russian.',
  keywords=['cyrillic', 'latin', 'transliteration', 'transliterate', 'cyrtranslit', 'serbian', 'macedonian', 'montenegrin', 'russian'],
  classifiers=['Development Status :: 5 - Production/Stable',
               'Intended Audience :: Developers',
               'License :: OSI Approved :: MIT License',
               'Programming Language :: Python',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Programming Language :: Python :: 3.2',
               'Programming Language :: Python :: 3.3',
               'Programming Language :: Python :: 3.4',
               'Programming Language :: Python :: 3.5',
               'Programming Language :: Python :: 3.6'],
  entry_points={
      "console_scripts": [
          "cyrtranslit=cyrtranslit.cyrtranslit:main",
      ]
  },
)
