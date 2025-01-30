Installation
============

Requirements
------------

LimeSoDa requires Python 3.8 or later. It also depends on the following Python packages:

- numpy >= 1.23.0
- pandas >= 1.5.0
- scikit-learn >= 1.0.0

Optional development dependencies:

- pytest >= 7.0.0
- black >= 22.0.0
- isort >= 5.0.0
- flake8 >= 4.0.0

Installing with pip
-------------------

You can install LimeSoDa using pip:

.. code-block:: bash

   pip install LimeSoDa

For development dependencies:

.. code-block:: bash

   pip install LimeSoDa[dev]

Installing from source
----------------------

To install LimeSoDa from source:

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/a11to1n3/LimeSoDa.git
      cd LimeSoDa

2. Install the package:

   .. code-block:: bash

      pip install -e .

   For development dependencies:

   .. code-block:: bash

      pip install -e .[dev]

Verifying Installation
----------------------

To verify that LimeSoDa is installed correctly, you can run:

.. code-block:: python

   import LimeSoDa
   print(LimeSoDa.__version__)

This should print the version number of the installed package.