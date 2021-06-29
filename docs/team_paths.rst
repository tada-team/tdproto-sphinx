Team related paths
----------------------------------------------

.. http:get:: /api/v4/teams

  Get the list of teams on the server.

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/get_api_v4_teams>`__

  :resjson boolean ok: True if no error occured.
  :resjson array result: List of :ref:`tdproto-Team` objects.
  :status 200: No error.

.. http:get:: /api/v4/teams/{team_id}

  Get team info.

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/get_api_v4_teams__team_id_>`__

  :param team_id: ID of the team.
  :resjson boolean ok: True if no error occured.
  :resjson object result: The :ref:`tdproto-Team` object.
  :status 200: No error.

.. http:put:: /api/v4/teams/{team_id}

  Update team settings.

  Must have admin rights.

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/put_api_v4_teams__team_id_>`__

  :param team_id: ID of the team.
  :reqjson object: :ref:`tdproto-Team` object with updated fields.
  :resjson boolean ok: True if no error occured.
  :resjson object result: Updated :ref:`tdproto-Team` object of the team.
  :status 200: No error.

.. http:delete:: /api/v4/teams/{team_id}

  Delete the team.

  Must have admin rights.

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/delete_api_v4_teams__team_id_>`__

  :param team_id: ID of the team.
  :resjson boolean ok: True if no error occured.
  :resjson object result: :ref:`tdproto-Team` object of deleted team.
  :status 200: No error.

.. http:get:: /api/v4/teams/{team_id}/chats

  Get the list of chats in the team.

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/get_api_v4_teams__team_id__chats>`__

  :param team_id: ID of the team.
  :resjson boolean ok: True if no error occured.
  :resjson array result: List of :ref:`tdproto-Chat` objects.
  :status 200: No error.

.. http:get:: /api/v4/teams/{team_id}/contacts

  Get the list of contacts of the team.

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/get_api_v4_teams__team_id__contacts>`__

  :param team_id: ID of the team.
  :resjson boolean ok: True if no error occured.
  :resjson array result: List of :ref:`tdproto-Contact` objects.
  :status 200: No error.

.. http:get:: /api/v4/teams/{team_id}/contacts/{contact_id}

  Get contact details.

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/get_api_v4_teams__team_id__contacts__contact_id_>`__

  :param team_id: ID of the team.
  :param contact_id: ID of the contact.
  :resjson boolean ok: True if no error occured.
  :resjson object result: The :ref:`tdproto-Contact` object.
  :status 200: No error.

.. http:post:: /api/v4/teams/{team_id}/contacts/{contact_id}

  Update contact details.

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/post_api_v4_teams__team_id__contacts__contact_id_>`__

  :param team_id: ID of the team.
  :param contact_id: ID of the contact.
  :reqjson object: The :ref:`tdproto-Contact` object.
  :resjson boolean ok: True if no error occured.
  :resjson object result: Updated :ref:`tdproto-Contact` object.
  :status 200: No error.

.. http:delete:: /api/v4/teams/{team_id}/contacts/{contact_id}

  Remove contact from the team.

  Must have admin rights.

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/delete_api_v4_teams__team_id__contacts__contact_id_>`__

  :param team_id: ID of the team.
  :param contact_id: ID of the contact.
  :resjson boolean ok: True if no error occured.
  :resjson object result: Removed :ref:`tdproto-Contact` object.
  :status 200: No error.
