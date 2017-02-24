HPP Reference
=============
L'HPP (Hosted Payment Page) genera i rep sol·licituds JSON amb la informació de la transacció escollida. Posteriorment, la biblioteca JavaScript proporcionada per Addon Payments s'encarregarà de gestionar les peticions i respostes corresponents. Podeu trobar més informació a `Addon Payments developer hub <https://desarrolladores.addonpayments.com/#!/>`_.

A continuació veurem els passos que s'han de seguir per generar les peticions JSON per cada tipus de transacció:

.. note:: Hi ha una sèrie de valors obligatoris que són auto-generats per l'HPP:

    - sha1hash: L'HPP genera automàticament una signatura digital amb l'algorisme SHA-1 per a cada una de les peticions JSON generades.
    - order_id: L'identificador de la transacció pot ser definida per l'usuari o auto-generada per l'HPP.
    - timestamp: La data i hora de la transacció és auto-generada per l'HPP.

Process a Payment (Auth)
------------------------

Documentació més detallada a `Addon Payments developer hub <https://desarrolladores.addonpayments.com/#!/hpp/transaction-processing>`_.

1. Crea la petició de pagament

2. Autogeneració de valors i transformació a JSON.

.. code-block:: python

    from addonpayments.hpp.payment.requests import PaymentRequest
    # create request to send
    request = PaymentRequest(
        merchant_id='my_merchant_id',
        amount=10,
        currency='EUR',
        auto_settle_flag=True
    )
    # create request/response handler
    hpp = Hpp('my_secrect')
    # parse request object to json object
    json_request = hpp.request_to_json(req)

Card storage
------------

Create a payer and store card
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Documentació més detallada a `Addon Payments developer hub <https://desarrolladores.addonpayments.com/#!/hpp/card-storage-and-management/create-payer-and-store-card>`_.

1. Crea la petició d'emmagatzemament de targeta:
    - payer_ref i pmt_ref si són buits Addon Payments genera automàticament la referència

2. Autogeneració de valors i transformació a JSON.

.. code-block:: python

    from addonpayments.hpp.payment.requests import PaymentRequest
    # create request to send
    request = CardStorageRequest(
        merchant_id='my_merchant_id',
        amount=10,
        currency='EUR',
        auto_settle_flag=True,
        card_storage_enable=True,
        offer_save_card=True,
        payer_exists=False,
        payer_ref='payer_ref',
        pmt_ref='pmt_ref'
    )
    # create request/response handler
    hpp = Hpp('my_secrect')
    # parse request object to json object
    json_request = hpp.request_to_json(req)

Display stored cards to the customer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Documentació més detallada a `Addon Payments developer hub <https://desarrolladores.addonpayments.com/#!/hpp/card-storage-and-management/display-stored-cards>`_.

1. Crea la petició per mostrar les targetes desades del dlient

2. Autogeneració de valors i transformació a JSON.

.. code-block:: python

    from addonpayments.hpp.payment.requests import PaymentRequest
    # create request to send
    request = DisplayCardsRequest(
        merchant_id='my_merchant_id',
        amount=10,
        currency='EUR',
        auto_settle_flag=True,
        hpp_select_stored_card='payer_ref',
        payer_exists=True,
        offer_save_card=True,
    )
    # create request/response handler
    hpp = Hpp('my_secrect')
    # parse request object to json object
    json_request = hpp.request_to_json(req)