from setuptools import setup, find_packages


extras_require = {
    'sync': ['requests>=2.25.1'],
    'async': ['aiohttp>=3.7.3']
}

setup(
    name='fipper-python-sdk',
    version='0.0.4',
    packages=find_packages(),
    author='RafRaf',
    author_email='smartrafraf@gmail.com',
    description='Fipper SDK',
    license='MIT',
    keywords=('fipper', 'sdk', 'feature', 'toggle'),
    test_suite='tests',
    extras_require=extras_require,
    url='https://github.com/RafRaf/fipper-python-sdk',
)
