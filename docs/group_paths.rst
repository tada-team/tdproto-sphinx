Group related paths
=====================================

.. http:get:: /api/v4/teams/{team_uid}/groups

  Get all groups in the team.

  :param team_uid: UID of the team.
  :resjson boolean ok: True if no error occured.
  :resjson array result: List of :ref:`tdproto-Chat` objects.
  :status 200: No error.

.. http:post:: /api/v4/teams/{team_uid}/groups

  Create new group.

  :param team_uid: UID of the team.
  :reqjson object new_group: TODO: document group object.
  :resjson boolean ok: True if no error occured.
  :resjson array result: :ref:`tdproto-Chat` object.
  :status 200: No error.

.. http:post:: /api/v4/teams/{team_uid}/groups/{group_id}/members

  Add a new member to the team.

  :param team_uid: UID of the team.
  :param group_id: Group ID to add member to.
  :reqjson object new_group: TODO: document group object.
  :resjson boolean ok: True if no error occured.
  :resjson array result: :ref:`tdproto-GroupMembership` object.
  :status 200: No error.

.. http:get:: /api/v4/teams/{team_uid}/groups/{group_id}/members

  Get the list of group members.

  :param team_uid: UID of the team.
  :param group_id: Group ID to add member to.
  :resjson boolean ok: True if no error occured.
  :resjson array result: List of :ref:`tdproto-GroupMembership` objects.
  :status 200: No error.

.. http:delete:: /api/v4/teams/{team_uid}/groups/{group_id}/members/{contact_id}

  Remove member from the group.

  :param team_uid: UID of the team.
  :param group_id: Group ID to add member to.
  :param group_id: Contact ID of the member to remove.
  :resjson boolean ok: True if no error occured.
  :resjson array result: List of :ref:`tdproto-GroupMembership` objects.
  :status 200: No error.

.. http:delete:: /api/v4/teams/{team_uid}/groups/{group_id}

  Delete the group.

  :param team_uid: UID of the team.
  :param group_id: Group ID to add member to.
  :resjson boolean ok: True if no error occured.
  :status 200: No error.
