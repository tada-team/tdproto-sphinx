Basics
=================

JID
---------------

Basic unit is Team. Inside the team there are contacts, tasks,
group chats. Contact from one team cannot interact with contact from
another team.

Each user in the team has an identifier in the form of ``d-<UID>``.
For historical reasons it is called ``JID``.

The number of ``JID`` that user has depends on how many teams they
are a part of. If the user is a part of 3 teams they have 3 ``JID`` s.
If the user is new they have no ``JID`` s.

``is_archive`` field
--------------------------

Nothing get deleted from the database. Instead the ``is_archive`` flag
will be set. The exception are devices.

``can_*`` fields
--------------------------

When a reply is received from a request there maybe an additional
fields in the form of ``can_DO_SOMETHING``. They mean "can I do
something with the returned object?"

Examples:

* ``{"can_send_message": false}`` in the self profile means that you
  can't send message to yourself.
* ``{"can_add_to_team": true}`` in the team means that you can add
  new participants to the team. (maybe you are the admin or owner)

In reality those fields to not exists in database - they are calculated
on the fly.

They are needed to ensure that the logic is stored in a single place.

For example, we decided that its possible to send yourself a message.
We only need to change the server now without any additional changes.
Both web and mobile clients will change their logic.

Second example, eventually we might add new administrator role with
tunnable rights. Using the can_* flags it will be backward compatible.

``/features.json``
-------------------------

In the server root there is a ``/features.json`` file with fields that
depend on installation. On different nodes different features might
be enabled.

This file is not a part of API. API might have version changes, old
APIs might get disabled but this file will always be present.

There is also ``features.js`` wrapper. If you run it as script it will
automatically create window.FEATURES.
