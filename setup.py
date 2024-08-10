from setuptools import setup, find_packages
import json

with open('metadata.json', 'r', encoding='utf-8') as fp:
    metadata = json.load(fp)


setup(
    name='lexibank_abvdphilippines',
    description=metadata['title'],
    license=metadata['license'],
    url=metadata['url'],
    py_modules=['lexibank_abvdphilippines'],
    include_package_data=True,
    zip_safe=False,
    packages=find_packages(where="."),
    entry_points={
        'lexibank.dataset': [
            'abvdphilippines=lexibank_abvdphilippines:Dataset',
        ],
        'cldfbench.commands': [
            'abvdphilippines=abvdphilippines_commands',
        ],
    },
    extras_require={"test": ["pytest-cldf"]},
    install_requires=[
        'pylexibank>=2.1',
        'nexusmaker>=2.0.4',
    ]
)
