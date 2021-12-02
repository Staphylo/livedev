from setuptools import setup

setup(
    name='livedev',
    author='Samuel Angebault',
    maintainer='Samuel Angebault',
    description='',
    license='MIT',
    scripts=[
        'livedev/livedev'
    ],
    install_requires=[
        'inotify>=0.2.10',
    ],
    tests_require=[
        'pytest',
    ],
    packages=[
        'tests',
    ],
    # test_suite='setup.get_test_suite',
    # test_suite='tests',
)
