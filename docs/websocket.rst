Websockets documentation
=============================================

Websocket is a full-duplex communication protocol.
See `Wikipedia page <https://en.wikipedia.org/wiki/WebSocket>`__ 
for more information about Websockets.

In tada.team websockets are used to notify clients about events
and voice calls.

Connecting to websocket
----------------------------------------------

The URL to connect to websocket has the form of ``wss://web.tada.team/messaging/{team_id}``
where team_id is the team JID to create websocket for. This means each team
has to have a separated websocket connection if you want to receive events from
multiple teams.

``web.tada.team`` can be substituted for custom domain.

Event JSON objects
--------------------------------

All events sent to or from server should be wrapped in an event object.

Event object has following fields:

* ``event`` (string) - Name of event. For example, ``"client.activity"``.
* ``confirm_id`` (string) - Mostly used for debugging. Should be set to any random string.
* ``params`` (object) - The actual event object.

Example:

.. code-block:: json
   
   {
   	"confirm_id": "75a406625c58",
   	"event": "client.activity",
   	"params": {
   		"afk": true
   	}
   }

This is a :ref:`client.activity` event sent by client to indicate that user is AFK.

List of events
---------------------------------

:ref:`Client events`. These events the clients can send to server.

:ref:`Server events`. These events server sends to clients.
