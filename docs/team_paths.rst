Team related paths
========================

.. http:get:: /api/v4/teams/{team_uid}/chats

    Get the list of chats in the team.

    :param team_uid: UID of the team.
    :resjson boolean ok: True if no error occured.
    :resjsonarr object result: List of :ref:`tdproto-Chat` objects.
    :status 200: No error.

.. http:get:: /api/v4/teams/{team_uid}/contacts/

    Get the list of contacts of the team.

    :param team_uid: UID of the team.
    :resjson boolean ok: True if no error occured.
    :resjsonarr object result: List of :ref:`tdproto-Contact` objects.
    :status 200: No error.

.. http:get:: /api/v4/teams/{team_uid}

    Get my contact info.

    :param team_uid: UID of the team.
    :resjson boolean ok: True if no error occured.
    :resjsonarr object result: My :ref:`tdproto-Contact` object.
    :status 200: No error.

.. http:post:: /api/v4/teams/{team_uid}/contacts

    Add new contant to the team. Requires :ref:`tdproto-Contact` object
    as input with phone number set.

    :param team_uid: UID of the team.
    :reqjson string phone: Phone number of new contact. 
    :resjson boolean ok: True if no error occured.
    :resjsonarr object result: New :ref:`tdproto-Contact` object.
    :status 200: No error.
