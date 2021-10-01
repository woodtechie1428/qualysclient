.. toctree::
   :hidden:

   Home page <self>
   API reference <_autosummary/qualysclient>


qualysclient documentation
========================================

About
------

**qualysclient** is a Python library for interacting with the Qualys API

.. note ::
   This project is under active development


Installation
------------

To use qualysclient, first install it using pip:

.. code-block:: console

   (.venv) $ pip install qualysclient

Usage Examples
--------------

.. code-block:: python

   from qualysclient import QualysClient

   qc = QualysClient(username = "your_username", password = "your_password")
   api_resp = qc.reports.list_reports()
   print (api_resp.text)
   qc.logout()

.. code-block:: python

   from qualysclient import QualysClient

   with QualysClient(username = "your_username", password = "your_password") as qc:
      api_resp = qc.reports.list_reports()
      print (api_resp.text)


API Reference
---------------
.. toctree::
   :maxdepth: 3

   _autosummary/qualysclient



Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


