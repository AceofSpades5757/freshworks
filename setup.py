import setuptools


with open('README.md', 'r') as fin:
    long_description = fin.read()


setuptools.setup(
    name='freshworks',
    version='0.0.1',
    author='Kyle L. Davis',
    author_email='AceofSpades5757.github@gmail.com',
    url='https://github.com/AceofSpades5757/freshworks',
    license='MIT',
    description='Python client library for interacting with Freshworks products.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src', 'freshdesk': 'src/freshdesk'},
    python_requires='>=3.6',
    install_requires=['requests', 'python-dateutil'],
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
)