from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="LimeSoDa",
    version="0.1.0", 
    author="Jonas Schmidinger",
    author_email="jonas.schmidinger@uni-osnabrueck.de",
    description="Precision Liming Soil Datasets (Lime.SoDa) for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/a11to1n3/LimeSoDa",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License", 
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.5.0",
        "numpy>=1.23.0",
        "scikit-learn>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0", 
            "isort>=5.0.0",
            "flake8>=4.0.0"
        ]
    },
    package_data={
        "LimeSoDa": ["data/*.pkl"],
    },
    include_package_data=True,
)