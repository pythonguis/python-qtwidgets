from setuptools import setup, find_packages

version = '0.17'

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='qtwidgets',
    version=version,
    author='Martin Fitzpatrick',
    author_email='martin.fitzpatrick@gmail.com',
    description='Custom widget library for PyQt5 and PySide2 (Qt for Python). Free to use in your own applications.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/learnpyqt/python-qtwidgets',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Desktop Environment',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Widget Sets',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4'
    ]
)
