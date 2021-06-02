Group related paths.
----------------------------------------------

.. http:get:: /api/v4/teams/{team_id}/groups

  Get all groups in the team.

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/get_api_v4_teams__team_id__groups>`__
  
  :param team_id: ID of the team.
  :resjson boolean ok: True if no error occured.
  :resjson array result: List of :ref:`tdproto-Chat` objects.
  :status 200: No error.

.. http:delete:: /api/v4/teams/{team_id}/groups

  Delete the group.

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/delete_api_v4_teams__team_id__groups>`__
  
  :param team_id: ID of the team.
  :resjson boolean ok: True if no error occured.
  :status 200: No error.

.. http:get:: /api/v4/teams/{team_id}/groups/{group_id}/members

  Get the list of group members.

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/get_api_v4_teams__team_id__groups__group_id__members>`__
  
  :param team_id: ID of the team.
  :param group_id: ID of the group.
  :resjson boolean ok: True if no error occured.
  :resjson array result: List of :ref:`tdproto-GroupMembership` objects.
  :status 200: No error.

.. http:delete:: /api/v4/teams/{team_id}/groups/{group_id}/members/{contact_id}

  Remove member from the group.

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/delete_api_v4_teams__team_id__groups__group_id__members__contact_id_>`__
  
  :param team_id: ID of the team.
  :param contact_id: ID of the contact.
  :param group_id: ID of the group.
  :resjson boolean ok: True if no error occured.
  :resjson object result: The :ref:`tdproto-GroupMembership` object.
  :status 200: No error.
