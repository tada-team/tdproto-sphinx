Miscelaneos paths
==================

.. http:get:: /api​/v4​/join​/{token}​/preview

   Invitation information.

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