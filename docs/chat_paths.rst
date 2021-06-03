Chat related paths.
----------------------------------------------

.. http:get:: /api/v4/teams/{team_id}/chats/{chat_id}

  Get the chat information.

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/get_api_v4_teams__team_id__chats__chat_id_>`__
  
  :param team_id: ID of the team.
  :param chat_id: ID of the chat.
  :resjson boolean ok: True if no error occured.
  :resjson object result: The :ref:`tdproto-Chat` object.
  :status 200: No error.

.. http:put:: /api/v4/teams/{team_id}/chats/{chat_id}

  Change chat settings.

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/put_api_v4_teams__team_id__chats__chat_id_>`__
  
  :param team_id: ID of the team.
  :param chat_id: ID of the chat.
  :reqjson object: The :ref:`tdproto-Chat` object.
  :resjson boolean ok: True if no error occured.
  :resjson object result: The :ref:`tdproto-Chat` object.
  :status 200: No error.

.. http:post:: /api/v4/teams/{team_id}/chats/{chat_id}/messages

  Send text message to chat.

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/post_api_v4_teams__team_id__chats__chat_id__messages>`__
  
  :param team_id: ID of the team.
  :param chat_id: ID of the chat.
  :reqjson object: The :ref:`tdproto-Message` object.
  :resjson boolean ok: True if no error occured.
  :status 200: No error.

.. http:post:: /api/v4/teams/{team_id}/chats/{chat_id}/messages/{message_id}

  Edit message.

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/post_api_v4_teams__team_id__chats__chat_id__messages__message_id_>`__
  
  :param team_id: ID of the team.
  :param chat_id: ID of the chat.
  :param message_id: ID of the message.
  :reqjson object: The :ref:`tdproto-Message` object.
  :resjson boolean ok: True if no error occured.
  :resjson object result: The :ref:`tdproto-Message` object.
  :status 200: No error.

.. http:delete:: /api/v4/teams/{team_id}/chats/{chat_id}/messages/{message_id}

  Delete message.

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/delete_api_v4_teams__team_id__chats__chat_id__messages__message_id_>`__
  
  :param team_id: ID of the team.
  :param chat_id: ID of the chat.
  :param message_id: ID of the message.
  :resjson boolean ok: True if no error occured.
  :resjson object result: The :ref:`tdproto-Message` object.
  :status 200: No error.

.. http:post:: /api/v4/teams/{team_id}/chats/{contact_id}/messages

  Send text message to direct chat.

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/post_api_v4_teams__team_id__chats__contact_id__messages>`__
  
  :param team_id: ID of the team.
  :param contact_id: ID of the contact.
  :reqjson object: The :ref:`tdproto-Message` object.
  :resjson boolean ok: True if no error occured.
  :status 200: No error.

.. http:post:: /api/v4/teams/{team_id}/chats/{contact_id}/messages/{message_id}

  Edit message in direct chat.

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/post_api_v4_teams__team_id__chats__contact_id__messages__message_id_>`__
  
  :param team_id: ID of the team.
  :param contact_id: ID of the contact.
  :param message_id: ID of the message.
  :reqjson object: The :ref:`tdproto-Message` object.
  :resjson boolean ok: True if no error occured.
  :resjson object result: The :ref:`tdproto-Message` object.
  :status 200: No error.

.. http:delete:: /api/v4/teams/{team_id}/chats/{contact_id}/messages/{message_id}

  Delete message in direct chat.

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/delete_api_v4_teams__team_id__chats__contact_id__messages__message_id_>`__
  
  :param team_id: ID of the team.
  :param contact_id: ID of the contact.
  :param message_id: ID of the message.
  :resjson boolean ok: True if no error occured.
  :resjson object result: The :ref:`tdproto-Message` object.
  :status 200: No error.
