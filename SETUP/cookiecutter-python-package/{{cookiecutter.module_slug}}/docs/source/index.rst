.. {{cookiecutter.package_name}} documentation master file

..  You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to {{cookiecutter.package_name}}'s documentation!
{{'-' * (cookiecutter.package_name | length + 28)}}

.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. can be moved to a separate file
.. automodule:: {{cookiecutter.module_slug}}
   :members:

.. Add other modules here...

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
