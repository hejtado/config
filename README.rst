Hejtado Config Microservice
===========================

This microservice provides an interface to the Hejtado configuration, saved in to the Redis database.

Installation
-------------

.. code-block:: bash

    tar xvfz hejtado-config-<version>.tar.gz
    cd hejtado-config-<version>
    python setup.py install

Start Hejtado
--------------

.. code-block:: bash

    hejtado-config

By default it starts on localhost, port 5002, so you can consume the API on URL::

    http://127.0.0.1:5002/api/v1

You can modify the default setting in settings.py file. Later I will add the support for environment variables instead of settings.py.
