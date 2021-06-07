How to create bot
=========================

Create new bot account
--------------------------

In order to create new bot account use the
``/newbot {NAME}`` command in ``@TadaBot`` direct chat.

Only admins have ability to create new bots.

Using the token header
------------------------------------

After creating the new bot account the new authorization
token should be returned in the same chat.

You need to use this token in all HTTP request headers
under the key name ``token``. Please consult your HTTP client
library on how to add new HTTP header. 

Available HTTP paths
---------------------------------------

See the paths documentations:

* :doc:`/team_paths`
* :doc:`/chat_paths`
* :doc:`/task_paths`
* :doc:`/group_paths`
* :doc:`/misc_paths`
