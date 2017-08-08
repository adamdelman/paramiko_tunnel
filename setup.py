import setuptools

setuptools.setup(
    name='paramiko_tunnel',
    version='0.3',
    packages=[
        'paramiko_tunnel',
    ],
    install_requires=[
        'paramiko',
    ],
    download_url='https://github.com/adamdelman/paramiko_tunnel/archive/0.1.tar.gz',
    url='https://github.com/adamdelman/paramiko_tunnel',
    license='GPLv3',
    author='Adam Delman',
    author_email='flyn@flyn.cc',
    description='A lightweight library for creating SSH tunnels on top of Paramiko.',
    keywords=[
        'paramiko',
        'ssh',
        'tunnel',
    ],

)
