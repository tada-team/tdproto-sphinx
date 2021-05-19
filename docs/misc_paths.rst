Miscelaneos paths
==================

.. http:get:: /api​/v4​/addr

  Returns client address for debuging purposes.

  `Try it! <https://tada-team.github.io/td-swagger-ui/#/default/get_api_v4_addr>`__

  **Example**:

  .. code-block:: json

    {
      "ok": true,
      "result": "127.0.0.1"
    }

  :resjson boolean ok: True if no error occured.
  :resjson string result: Set to ``"pong"``. 

  :status 200: No error

.. http:get:: ​/api​/v4​/alltimezones

  Get list of timezones.

  `Try it! <https://tada-team.github.io/td-swagger-ui/#/default/get_api_v4_alltimezones>`__

  :status 200: No error

.. http:get:: ​/api​/v4​/countries

  Get list of country phone codes.

  `Try it! <https://tada-team.github.io/td-swagger-ui/#/default/get_api_v4_countries>`__

  :status 200: No error

.. http:get:: /api​/v4​/emoji

  Get the emoji list.

  `Try it! <https://tada-team.github.io/td-swagger-ui/#/default/get_api_v4_emoji>`__

  :status 200: No error

.. http:post:: /api​/v4​/join​/{token}

  Join the team.

  `Try it! <https://tada-team.github.io/td-swagger-ui/#/default/post_api_v4_join__token_>`__

  :param token: Invite token to join team.
  :resjson boolean ok: True if no error occured.
  :resjson object result: :ref:`tdproto-team` object.

.. http:get:: /api​/v4​/join​/{token}​/preview

   Invitation information.

   `Try it! <https://tada-team.github.io/td-swagger-ui/#/default/get_api_v4_join__token__preview>`__

   .. code-block:: json

      {
        "ok": true,
        "result": {
          "icons": {
            "blurhash": "string",
            "color": "string",
            "letters": "string",
            "lg": {
              "height": 0,
              "url": "string",
              "width": 0
            },
            "sm": {
              "height": 0,
              "url": "string",
              "width": 0
            },
            "stub": "string"
          },
          "name": "string",
          "uid": "string"
        }
      }

   :param token: Invite token to preview.
   :resjson boolean ok: True if no error occured.
   :resjson object result: Invite information.

.. http:get:: ​/api​/v4​/ping

   Ping the server.

   `Try it! <https://tada-team.github.io/td-swagger-ui/#/default/get_api_v4_ping>`__

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: text/javascript

      {
        "ok": true,
        "result": "pong"
      }

   :resjson boolean ok: True if no error occured.
   :resjson string result: Set to ``"pong"``. 

   :status 200: No error

.. http:get:: /api​/v4​/reactions

  Get the list of available reactions.

  `Try it! <https://tada-team.github.io/td-swagger-ui/#/default/get_api_v4_reactions>`__

  :status 200: No error

.. http:get:: /api​/v4​/time

  Get server time.

  `Try it! <https://tada-team.github.io/td-swagger-ui/#/default/get_api_v4_time>`__

  :status 200: No error

.. http:get:: features.json

  Get the server information.

  `Try it! <https://tada-team.github.io/td-swagger-ui/#/default/getfeatures_json>`__

  :resjson boolean ok: True if no error occured.
  :resjson object result: :ref:`tdproto-Features` object. 
  :status 200: No error
