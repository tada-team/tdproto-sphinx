Team related paths
========================

.. http:get:: /api/v4/teams

  Get the list of teams on the server.

  :resjson boolean ok: True if no error occured.
  :resjson array result: List of :ref:`tdproto-Team` objects.
  :status 200: No error.

.. TODO post /api/v4/teams

  Create a new team.

  :reqjson object: :ref:`tdproto-Team` info to create.
  :resjson boolean ok: True if no error occured.
  :resjson array result: List of :ref:`tdproto-Team` objects.
  :status 200: No error.

.. http:get:: /api/v4/teams/{team_uid}

  Get team info.

  :param team_uid: UID of the team.
  :resjson boolean ok: True if no error occured.
  :resjson object result: :ref:`tdproto-Team` object.
  :status 200: No error.

.. http:put:: /api/v4/teams/{team_uid}

  Update team settings.

  Must have admin rights.

  :param team_uid: UID of the team.
  :reqjson object: :ref:`tdproto-Team` info to create.
  :resjson boolean ok: True if no error occured.
  :resjson object result: Updated :ref:`tdproto-Team` object of the team.
  :status 200: No error.

.. http:delete:: /api/v4/teams/{team_uid}

  Delete the team.

  Must have admin rights.

  :param team_uid: UID of the team.
  :resjson boolean ok: True if no error occured.
  :resjson object result: :ref:`tdproto-Team` object of deleted team.
  :status 200: No error.

.. http:get:: /api/v4/teams/{team_uid}/chats

  Get the list of chats in the team.

  :param team_uid: UID of the team.
  :resjson boolean ok: True if no error occured.
  :resjson array result: List of :ref:`tdproto-Chat` objects.
  :status 200: No error.

.. http:get:: /api/v4/teams/{team_uid}/contacts

  Get the list of contacts of the team.

  :param team_uid: UID of the team.
  :resjson boolean ok: True if no error occured.
  :resjson array result: List of :ref:`tdproto-Contact` objects.
  :status 200: No error.

.. http:post:: /api/v4/teams/{team_uid}/contacts

  Add new contant to the team. Requires :ref:`tdproto-Contact` object
  as input with phone number set.

  :param team_uid: UID of the team.
  :reqjson string phone: Phone number of new contact. 
  :resjson boolean ok: True if no error occured.
  :resjson object result: New :ref:`tdproto-Contact` object.
  :status 200: No error.

.. http:get:: /api/v4/teams/{team_uid}/contacts/{contact_id}

  Get contact details.

  :param team_uid: UID of the team.
  :param contact_id: ID of the contact.
  :resjson boolean ok: True if no error occured.
  :resjson object result: The :ref:`tdproto-Contact` object.
  :status 200: No error.

.. http:post:: /api/v4/teams/{team_uid}/contacts/{contact_id}

  Update contact details.

  :param team_uid: UID of the team.
  :param contact_id: ID of the contact.
  :reqjson object: :ref:`tdproto-Contact` object with updated fields. 
  :resjson boolean ok: True if no error occured.
  :resjson object result: Updated :ref:`tdproto-Contact` object.
  :status 200: No error.

.. http:delete:: /api/v4/teams/{team_uid}/contacts/{contact_id}

  Remove contact from the team.

  Must have admin rights.

  :param team_uid: UID of the team.
  :param contact_id: ID of the contact.
  :resjson boolean ok: True if no error occured.
  :resjson object result: Removed :ref:`tdproto-Contact` object.
  :status 200: No error.