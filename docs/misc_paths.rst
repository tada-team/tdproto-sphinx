Miscellaneous paths
----------------------------------------------

.. http:get:: /api/v4/addr

  Returns client address for debuging purposes.

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/get_api_v4_addr>`__

  :resjson boolean ok: True if no error occured.
  :resjson string result: Address of the server.
  :status 200: No error.

.. http:get:: /api/v4/ping

  Ping the server.

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/get_api_v4_ping>`__

  :resjson boolean ok: True if no error occured.
  :resjson string result: Set to ``"pong"``.
  :status 200: No error.

.. http:get:: /features.json

  Get the server features information.

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/get_features_json>`__

  :resjson boolean ok: True if no error occured.
  :resjson object result: The :tdproto:ref:`Features` object.
  :status 200: No error.
