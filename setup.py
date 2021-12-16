import io
from setuptools import find_packages, setup

packages = find_packages(where='src', exclude=['docs', 'tests*'])

# package_data : files(not *.py) that should be contained with the package

setup(
    name='discord-bot-aws',
    version='0.0.1',
    description='distributable discord bot',
    author='ccppoo',
    author_email='shmishmi79@gmail.com',
    url='https://github.com/ccppoo/discord-bot-AWS-CaI',
    download_url='https://github.com/ccppoo/discord-bot-AWS-CaI.git',

    install_requires=[],

    packages=find_packages(),

    keywords=['AWS', 'discord-bot'],
    python_requires='>=3.7',

    package_data={},

    zip_safe=False,

    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ]
)
