from setuptools import setup, find_packages

import versioneer
# Versioneer configuration
versioneer.VCS = 'git'
versioneer.versionfile_source = 'testversioneer/_version.py'
versioneer.versionfile_build = 'testversioneer/_version.py'
versioneer.tag_prefix = 'v'  # tags are like v1.2.0
versioneer.parentdir_prefix = 'testversioneer-'


setup(
    name='testversioneer',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license='BSD',
    description='Library of web-related functions',
    author='Yo',
    author_email='yo@foo.org',
    url='https://github.com/dangra/testversioneer',
    packages=find_packages(exclude=('tests', 'tests.*')),
    include_package_data=True,
    platforms=['Any'],
)
