
from setuptools import setup, find_packages

setup(
    name='HistoricalEarningsData',  # Updated name
    version='0.3',                   # Incremented version
    description='A package to query historical earnings report dates for stock tickers with implied volatility',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/historical_earnings_package',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'HistoricalEarningsData': ['data/aggregated_earnings_data_with_iv.csv'],  # Updated file name
    },
    install_requires=[
        'pandas',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
