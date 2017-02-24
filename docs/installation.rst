Installation
============

The installation process i very easy and quick. This process will install everything you need to use both types of integrations, the HPP and the API. Before you have an account on Addon Payments if you do not have it, you can do so via the `Addon Payments registration form <https://www.addonpayments.com/en/register?payment%20solution=Online>`_.

Please follow these steps to installation:

1. Install AddonPayments SDK and its dependencies via :code:`pip install addonpayments-sdk-python`.

2. Configure the SDK with your Addon Payments account. Create the settings.ini file in your root project with the content that we provide in the addonpayments/settings.ini.template file::

    [settings]
    DEBUG=True
    MERCHANT_ID = yourmerchantid
    SHARED_SECRET = yoursharedsecret
    ADDONPAYMENTS_HPP_URL = https://hpp.sandbox.addonpayments.com/pay
    ADDONPAYMENTS_API_URL = https://remote.sandbox.addonpayments.com/remote

