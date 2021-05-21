Task related paths
============================

.. http:post:: /api/v4/teams/%s/tasks

  Create new task.

  :param team_uid: UID of the team.
  :reqjson object task: TODO: document ``Task`` object.
  :resjson boolean ok: True if no error occured.
  :resjson array result: TODO: document ``Task`` object.
  :status 200: No error.
