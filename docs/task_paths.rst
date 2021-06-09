Task related paths
----------------------------------------------

.. http:post:: /api/v4/teams/{team_id}/tasks

  Create new task

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/post_api_v4_teams__team_id__tasks>`__
  
  :param team_id: ID of the team.
  :reqjson object: The :ref:`tdproto-Task` object.
  :resjson boolean ok: True if no error occured.
  :resjson object result: The :ref:`tdproto-Task` object.
  :status 200: No error.
