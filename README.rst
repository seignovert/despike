===============================
Despike
===============================
|Build| |Coverage| |PyPI| |Status| |Version| |Python| |License|

.. |Build| image:: https://travis-ci.org/seignovert/despike.svg?branch=master
        :target: https://travis-ci.org/seignovert/despike
.. |Coverage| image:: https://coveralls.io/repos/github/seignovert/despike/badge.svg?branch=master
        :target: https://coveralls.io/github/seignovert/despike?branch=master
.. |PyPI| image:: https://img.shields.io/badge/PyPI-despike-blue.svg
        :target: https://pypi.python.org/project/despike
.. |Status| image:: https://img.shields.io/pypi/status/despike.svg?label=Status
.. |Version| image:: https://img.shields.io/pypi/v/despike.svg?label=Version
.. |Python| image:: https://img.shields.io/pypi/pyversions/despike.svg?label=Python
.. |License| image:: https://img.shields.io/pypi/l/despike.svg?label=License

*Python package to remove spikes in 2D images*

Desciption
----------
The spikes in 2D-images correspond to high-energy pixels generated
by cosmic rays, sensor noise or dead pixels. They use to have values
very different from the rest of their neighboor.

To find them, we use a moving box (5×5 pixels by default) on the
image and we compare the mean/median of this sub-image to the central
pixel. If the value is n (3 by default) times larger than the observed
standard deviation we use the median value a the surrounding pixels
(8 pixels by default) to replace the spike.

Install
-------
With ``pip``:

.. code:: bash

    $ pip install despike

With the ``source files``:

.. code:: bash

    $ git clone https://github.com/seignovert/despike.git
    $ cd despike ; python setup.py install

Usage
------

.. code:: python

    >>> import despike

    >>> despike.spikes(img) # Search the location of spikes in the image

    >>> despike.clean(img) # Clean the image from spikes


An example can be find in this `Jupyter NoteBook <https://nbviewer.jupyter.org/github/seignovert/despike/blob/master/example.ipynb>`_.
