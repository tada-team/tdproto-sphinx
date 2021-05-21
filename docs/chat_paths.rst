Chat related paths
========================

.. http:get:: /api/v4/teams/{team_uid}/chats/{chat_jid}

  Get the chat information.

  :param team_uid: UID of the team.
  :param chat_jid: JID of the chat.
  :resjson boolean ok: True if no error occured.
  :reqjson object message: The :ref:`tdproto-Chat` object.
  :status 200: No error

.. http:put:: /api/v4/teams/{team_uid}/chats/{chat_jid}

  Change chat settings.

  :param team_uid: UID of the team.
  :param chat_jid: JID of the chat.
  :reqjson object: :ref:`tdproto-Chat` objects
  :resjson boolean ok: True if no error occured.
  :reqjson object message: Updated :ref:`tdproto-Chat` object.
  :status 200: No error

.. http:post:: /api/v4/teams/{team_uid}/chats/{chat_jid}/messages

  Send text message to chat.

  :param team_uid: UID of the team.
  :param chat_jid: JID of the chat.
  :reqjson object message: New :ref:`tdproto-Message` object.
  :resjson boolean ok: True if no error occured.
  :status 200: No error

.. http:get:: /api/v4/teams/{team_uid}/chats/{chat_jid}/messages

  Get the chat messages.

  :param team_uid: UID of the team.
  :param chat_jid: JID of the chat.
  :reqjson object filter: TODO: document filter object.
  :resjson boolean ok: True if no error occured.
  :resjson array messages: List of :ref:`tdproto-Message` objects.
  :status 200: No error

.. http:post:: /api/v4/teams/{team_uid}/chats/{chat_jid}/messages/{message_id}

  Edit a message.

  :param team_uid: UID of the team.
  :param chat_jid: JID of the chat.
  :param message_id: Message id to edit.
  :reqjson object: :ref:`tdproto-Message` object with updated fields.
  :resjson boolean ok: True if no error occured.
  :resjson object result: Updated :ref:`tdproto-Message` object.
  :status 200: No error

.. http:delete:: /api/v4/teams/{team_uid}/chats/{chat_jid}/messages/{message_id}

  Delete message.

  :param team_uid: UID of the team.
  :param chat_jid: JID of the chat.
  :param message_id: Message id to delete.
  :resjson boolean ok: True if no error occured.
  :resjson object result: :ref:`tdproto-Message` object of deleted message.
  :status 200: No error
