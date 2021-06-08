Task related paths
----------------------------------------------

.. http:post:: /api/v4/teams/{task_id}/tasks

  Create new task

  `🔍 Try it! <https://tada-team.github.io/td-swagger-ui/#/default/post_api_v4_teams__task_id__tasks>`__
  
  :reqjson object: The :ref:`tdproto-Task` object.
  :resjson boolean ok: True if no error occured.
  :resjson object result: The :ref:`tdproto-Task` object.
  :status 200: No error.
