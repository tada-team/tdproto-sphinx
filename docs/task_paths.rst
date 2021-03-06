Task related paths
----------------------------------------------

.. http:get:: /api/v4/teams/{team_id}/tasks

  Get the list of tasks

  Query parameters: :ref:`tdproto-TaskFilterQuery`

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/get_api_v4_teams__team_id__tasks>`__

  :param team_id: ID of the team.
  :resjson boolean ok: True if no error occured.
  :resjson array result: List of :tdproto:ref:`Task` objects.
  :status 200: No error.

.. http:post:: /api/v4/teams/{team_id}/tasks

  Create new task

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/post_api_v4_teams__team_id__tasks>`__

  :param team_id: ID of the team.
  :reqjson object: The :tdproto:tdmodels:`Task` object.
  :resjson boolean ok: True if no error occured.
  :resjson object result: The :tdproto:ref:`Task` object.
  :status 200: No error.

.. http:get:: /api/v4/teams/{team_id}/tasks/{task_id}

  Get task

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/get_api_v4_teams__team_id__tasks__task_id_>`__

  :param team_id: ID of the team.
  :param task_id: ID of the task.
  :resjson boolean ok: True if no error occured.
  :resjson object result: The :tdproto:ref:`Task` object.
  :status 200: No error.

.. http:post:: /api/v4/teams/{team_id}/tasks/{task_id}

  Update task

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/post_api_v4_teams__team_id__tasks__task_id_>`__

  :param team_id: ID of the team.
  :param task_id: ID of the task.
  :reqjson object: The :tdproto:tdmodels:`Task` object.
  :resjson boolean ok: True if no error occured.
  :resjson object result: The :tdproto:ref:`Task` object.
  :status 200: No error.

.. http:delete:: /api/v4/teams/{team_id}/tasks/{task_id}

  Delete task

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/delete_api_v4_teams__team_id__tasks__task_id_>`__

  :param team_id: ID of the team.
  :param task_id: ID of the task.
  :resjson boolean ok: True if no error occured.
  :resjson object result: The :tdproto:ref:`Task` object.
  :status 200: No error.
