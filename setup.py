import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='key_value_ds',
    version='1.0.3',
    author='SomasekharGoudAddakula',
    author_email='somashekhar34@gmail.com',
    description='A key value datastore which stores data locally in a memory-mapped file.',
    license='MIT',
    url='https://github.com/somashekhar34/key-value-ds',
    download_url='https://github.com/somashekhar34/key-value-ds/releases/tag/v1.0.3',
    packages=['key_value_ds', 'tests'],
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    extras_require={
        'dev': ['pytest', 'wheel']
    },
)
