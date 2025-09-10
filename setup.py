from setuptools import setup, find_packages

setup(
    name="pyspark_etl_framework",
    version="1.0.0",
    author="Your Name",
    description="A configuration-driven, scalable PySpark ETL framework.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        "pyspark==3.3.1",
        "pyyaml==6.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
