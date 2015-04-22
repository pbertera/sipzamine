#!/usr/bin/env python
from distutils.core import setup

with open('README.rst') as file:
    long_description = file.read()


setup(
    name='sipzamine',
    version='0.1.1',
    scripts=['src/sipzamine', 'src/sipcaparseye'],
    package_dir={'sipzamine': 'src'},
    packages=['sipzamine'],
    data_files=[('', ['LICENSE.txt', 'README.rst'])],
    description='SIP dialog examine utility (formerly sipcaparseye)',
    long_description=long_description,
    author='Walter Doekes, OSSO B.V.',
    author_email='wjdoekes+sipzamine@osso.nl',
    url='https://github.com/ossobv/sipzamine',
    license='GPLv3+',
    platforms=['linux'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        ('License :: OSI Approved :: GNU General Public License v3 '
         'or later (GPLv3+)'),
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: Communications :: Telephony',
        'Topic :: System :: Networking :: Monitoring',
    ],
    install_requires=[
        # 'pylibpcap' || 'pypcapfile'
        # The former refuses to install easily using pip, use your
        # OS package manager if possible.
    ],
)

# vim: set ts=8 sw=4 sts=4 et ai tw=79: