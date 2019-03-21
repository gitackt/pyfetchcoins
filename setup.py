setup(
    name='pyfetchcoins',
    version='0.1.0',
    description='Fetch curypto currency volume from exchanges',
    long_description=readme,
    author='Takuto Mitsuhashi',
    author_email='git.tackt@gmail.com',
    url='https://github.com/gitackt/pyfetchcoins',
    license=license,
    # packages=find_packages(exclude=('tests', 'docs'))
    install_requires=[
        'requests', 
        'pybitflyer', 
        'python-binance', 
        'python-kucoin', 
        'zaifapi', 
        'coincheck', 
        'python-quoine', 
    ],
    dependency_links=[
        'git+https://github.com/bitbankinc/python-bitbankcc.git'
        'https://github.com/s4w3d0ff/python-poloniex/archive/v0.4.7.zip'
    ],
)
