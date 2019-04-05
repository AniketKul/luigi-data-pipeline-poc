from setuptools import setup, find_packages

desc = 'Data Pipeline with Luigi'

setup(
    name='luigi-data-pipeline-poc',
    version='0.0.1',
    description='Data Pipeline with Luigi',
    long_description=desc,
    url='https://github.com',
    author='Aniket Kulkarni',
    license='',
    keywords='',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'luigi',
                                    'luigistate', 'docker', 'data', 'examples', 'report']),
    install_requires=[
        'luigi',
        'requests',
    ],
    package_data={},
    data_files=[],
    entry_points={
        'console_scripts': [
            'example = example.main:main'
        ],
    },
)