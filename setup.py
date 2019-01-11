import os
from setuptools import setup


def get_files_by_path(path):
    files = []
    for root, dirs_, files_ in os.walk(path, followlinks=True):
        for file_ in files_:
            files.append(os.path.join(root, file_))
    return files


DIR = os.path.dirname(__file__)
EXTRA_FILES = get_files_by_path(os.path.join(DIR, "example"))
EXTRA_FILES.extend(get_files_by_path(os.path.join(DIR, "schema")))

setup(
    name='esse',
    version='0.1.0',
    description='Exabyte Source of Schemas and Examples',
    url='https://github.com/Exabyte-io/exabyte-esse',
    author='Exabyte Inc.',
    author_email='info@exabyte.io',
    packages=['esse'],
    package_dir={'': 'src/py'},
    package_data={'esse': [f.replace(DIR, "data") for f in EXTRA_FILES]},
    install_requires=[
        "pyyaml==3.12",
        "jsonschema==2.6.0",
        "python-slugify==2.0.1",
        "exabyte_json_include==0.1.1"
    ],
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development'
    ]
)
