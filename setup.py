import setuptools
import re

with open('./treestructure/version.py', 'rt') as f:
    rule = r"^__version__ = ['\"]([^'\"]*)['\"]"
    version = re.search(rule, f.read(), re.M).group(1)

with open('./README.md', 'r', encoding='utf-8') as f:
    longDescription = f.read()

setuptools.setup(
    name='treestructure',
    version=version,
    author='Tony Chiu',
    author_email='pi3141592676@yahoo.com.tw',
    description='Tree Structure is a module that implements some common trees in data structure.',
    long_description=longDescription,
    long_description_content_type='text/markdown',
    url='https://github.com/Musicmathstudio/treeStructure',
    keywords=['tree structure', 'data structure', 'binary search tree', 'binary heap'],
    packages=setuptools.find_packages(),
    python_requires='>=3',
    license_files=('./LICENSE',),
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ]
)
