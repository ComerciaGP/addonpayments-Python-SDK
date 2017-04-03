AddonPayments SDK Python
========================

AddonPayments SDK Python is a library that allows integration with the SDK's of AddonPayments in a easy and fast way.
There are two types of integration: HPP (Hosted Payment Page) and API.

Features
~~~~~~~~

HPP
---

* Integrates in minutes
* Minimises the merchant’s PCI overheads
* Customisable, for a seamless checkout process

API
---

* Gives you full control of the payment process
* Provides access to a full suite of transaction management requests
* Suitable for call centre integrations

Quick start
~~~~~~~~~~~

First of all, you need to install AddonPayments SDK Python package::

    pip install addonpayments-sdk-python

In order to use the SDK it is necessary to have an account in Addon Payments, then it will be necessary to configure
the SDK with the values ​​of your account. Create the settings.ini file in your project with the content that we provide
in the addonpayments/settings.ini.template file:

.. code-block::

    ; cp settings.ini.template your_project_folder/settings.ini
    [settings]
    DEBUG=True
    MERCHANT_ID = yourmerchantid
    SHARED_SECRET = yoursharedsecret
    ADDONPAYMENTS_HPP_URL = https://hpp.sandbox.addonpayments.com/pay
    ADDONPAYMENTS_API_URL = https://remote.sandbox.addonpayments.com/remote

Usage
~~~~~

Take a look at the Django demo project


Documentation
~~~~~~~~~~~~~
Visit the `documentation <http://addonpayments.readthedocs.io/en/github/>`_ for an in-depth look at AddonPayments SDK Python.
