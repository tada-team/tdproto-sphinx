Enums index
============================

.. _tdproto-ChatType:

ChatType enum
-------------------------------------------------------------
**Possible values**:

#. direct
#. group
#. task


.. _tdproto-GroupStatus:

GroupStatus enum
-------------------------------------------------------------
**Possible values**:

#. admin
#. member


.. _tdproto-MarkupType:

MarkupType enum
-------------------------------------------------------------
**Possible values**:

#. bold
#. italic
#. underscore
#. strike
#. code
#. codeblock
#. quote
#. link
#. time
#. unsafe


.. _tdproto-Mediasubtype:

Mediasubtype enum
-------------------------------------------------------------
**Possible values**:

#. sticker
#. newtask


.. _tdproto-Mediatype:

Mediatype enum
-------------------------------------------------------------
**Possible values**:

#. plain
#. change
#. deleted
#. file
#. image
#. video
#. audiomsg
#. contact
#. pdf


.. _tdproto-TeamStatus:

TeamStatus enum
-------------------------------------------------------------
**Possible values**:

#. owner
#. admin
#. member
#. guest


.. _tdproto-UploadMediaType:

UploadMediaType enum
-------------------------------------------------------------
**Possible values**:

#. file
#. image
#. video
#. audio
#. imagefile

Type aliases
============================

.. _tdproto-ActiveUserDailyStatList:

ActiveUserDailyStatList type alias of ``ActiveUserDailyStat``
-------------------------------------------------------------

**Base Type**: ActiveUserDailyStat

**Is array**


.. _tdproto-ISODateTimeString:

ISODateTimeString type alias of ``string``
-------------------------------------------------------------

**Base Type**: string




.. _tdproto-JID:

JID type alias of ``string``
-------------------------------------------------------------

**Base Type**: string




.. _tdproto-MessageLinks:

MessageLinks type alias of ``MessageLink``
-------------------------------------------------------------

**Base Type**: MessageLink

**Is array**


.. _tdproto-PushDeviceType:

PushDeviceType type alias of ``int``
-------------------------------------------------------------

**Base Type**: int




.. _tdproto-TaskFilterKey:

TaskFilterKey type alias of ``string``
-------------------------------------------------------------

**Base Type**: string




.. _tdproto-TaskSortKey:

TaskSortKey type alias of ``string``
-------------------------------------------------------------

**Base Type**: string




.. _tdproto-TaskTabKey:

TaskTabKey type alias of ``string``
-------------------------------------------------------------

**Base Type**: string



JSON objects index
============================

.. _tdproto-ActiveUserDailyStat:

ActiveUserDailyStat
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``calls_count`` (number) - DOCUMENTATION MISSING

    **Maybe omitted**

    **Might be null**
#. ``call_seconds_total`` (number) - DOCUMENTATION MISSING

    **Maybe omitted**

    **Might be null**
#. ``day`` (string) - DOCUMENTATION MISSING
#. ``family_name`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**

    **Might be null**
#. ``given_name`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**

    **Might be null**
#. ``messages_count`` (number) - DOCUMENTATION MISSING

    **Maybe omitted**

    **Might be null**
#. ``patronymic`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**

    **Might be null**
#. ``phone`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**

    **Might be null**
#. ``user_id`` (number) - DOCUMENTATION MISSING

.. _tdproto-AnyEvent:

AnyEvent
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING

.. _tdproto-BaseEvent:

BaseEvent
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING

.. _tdproto-ButtonColors:

ButtonColors
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``brand_static`` (string) - DOCUMENTATION MISSING
#. ``brand_disable`` (string) - DOCUMENTATION MISSING
#. ``brand_active`` (string) - DOCUMENTATION MISSING
#. ``simple_static`` (string) - DOCUMENTATION MISSING
#. ``simple_disable`` (string) - DOCUMENTATION MISSING
#. ``simple_active`` (string) - DOCUMENTATION MISSING

.. _tdproto-CallDevice:

CallDevice
-------------------------------------------------------------

Call participant device

**Fields**:

#. ``muted`` (boolean) - Device muted
#. ``useragent`` (string) - Device description

.. _tdproto-CallEvent:

CallEvent
-------------------------------------------------------------

Audio call information

**Fields**:

#. ``audiorecord`` (boolean) - Call record enabled
#. ``finish`` (string) - Call finish

    **Might be null**
#. ``onliners`` ( :ref:`tdproto-CallOnliner` ) - Call participants

    **Maybe omitted**
#. ``start`` (string) - Call start

    **Might be null**

.. _tdproto-CallOnliner:

CallOnliner
-------------------------------------------------------------

Call participant

**Fields**:

#. ``devices`` ( :ref:`tdproto-CallDevice` ) - Member devices, strictly one for now
#. ``display_name`` (string) - Contact name
#. ``icon`` (string) - Contact icon
#. ``jid`` ( :ref:`tdproto-JID` ) - Contact id
#. ``muted`` (boolean) - Microphone muted. Computed from devices muted states
#. ``role`` (string) - Contact role

.. _tdproto-Chat:

Chat
-------------------------------------------------------------

Chat (direct, group, task) representation

**Fields**:

#. ``assignee`` ( :ref:`tdproto-JID` ) - Assignee contact id. Tasks only

    **Maybe omitted**
#. ``autocleanup_age`` (number) - Delete messages in this chat in seconds. Experimental function

    **Maybe omitted**

    **Might be null**
#. ``base_gentime`` (number) - Base fields (not related to concrete participant) version

    **Maybe omitted**
#. ``can_change_member_status`` (boolean) - Can I change member status in this group chat

    **Maybe omitted**
#. ``can_call`` (boolean) - Can I call to this chat

    **Maybe omitted**
#. ``can_add_member`` (boolean) - Can I add member to this group chat

    **Maybe omitted**
#. ``can_delete`` (boolean) - Can I delete this chat

    **Maybe omitted**
#. ``can_set_important_any_message`` (boolean) - Can I change Important flag in any message in this chat

    **Maybe omitted**
#. ``can_send_message`` (boolean) - Can I send message to this chat

    **Maybe omitted**
#. ``can_remove_member`` (boolean) - Can I remove member from this group chat

    **Maybe omitted**
#. ``can_join`` (boolean) - Can I join to this public group/task

    **Maybe omitted**
#. ``can_change_settings`` (boolean) - deprecated: use changeable fields

    **Maybe omitted**
#. ``can_delete_any_message`` (boolean) - Can I delete any message in this chat

    **Maybe omitted**
#. ``cant_send_message_reason`` (string) - Why I can't send message to this chat (if can't)

    **Maybe omitted**
#. ``changeable_fields`` (string) - List of editable fields

    **Maybe omitted**
#. ``chat_type`` ( :ref:`tdproto-ChatType` ) - Chat type
#. ``collapsed`` (boolean) - Description collapsed. Used for tasks only

    **Maybe omitted**
#. ``color_index`` (number) - Custom color index from table of colors. Tasks only

    **Maybe omitted**

    **Might be null**
#. ``complexity`` (number) - Task complexity, number

    **Maybe omitted**

    **Might be null**
#. ``counters_enabled`` (boolean) - Include unread messages to counters

    **Maybe omitted**
#. ``created`` (string) - Creation date, iso datetime
#. ``deadline`` (string) - Task deadline in iso format, if any

    **Maybe omitted**
#. ``deadline_expired`` (boolean) - Is task deadline expired

    **Maybe omitted**
#. ``default_for_all`` (boolean) - Any new team member will be added to this group chat

    **Maybe omitted**
#. ``description`` (string) - Group or task description

    **Maybe omitted**
#. ``display_name`` (string) - Title
#. ``done`` (string) - Task done date in iso format, if any

    **Maybe omitted**
#. ``done_reason`` (string) - Task done reason, if any

    **Maybe omitted**
#. ``draft`` (string) - Last message draft, if any

    **Maybe omitted**
#. ``draft_num`` (number) - Last message draft version , if any

    **Maybe omitted**
#. ``feed`` (boolean) - Present in feed (main screen)

    **Maybe omitted**
#. ``gentime`` (number) - Chat fields related to concrete participant) version
#. ``hidden`` (boolean) - Hidden chat

    **Maybe omitted**
#. ``icons`` ( :ref:`tdproto-IconData` ) - Icons info

    **Might be null**
#. ``importance`` (number) - Task importance, if available in team

    **Maybe omitted**

    **Might be null**
#. ``items`` ( :ref:`tdproto-TaskItem` ) - Checklist items. Task only

    **Maybe omitted**
#. ``jid`` ( :ref:`tdproto-JID` ) - Group/Task/Contact id
#. ``last_read_message_id`` (string) - Last read message id, if any

    **Maybe omitted**
#. ``last_message`` ( :ref:`tdproto-Message` ) - Last message object

    **Maybe omitted**

    **Might be null**
#. ``last_activity`` (string) - Date of the last message sent even if it was deleted

    **Maybe omitted**
#. ``linked_messages`` (any) - Used for "Create task from messages..."

    **Maybe omitted**
#. ``links`` ( :ref:`tdproto-MessageLinks` ) - Links in description

    **Maybe omitted**
#. ``markup`` ( :ref:`tdproto-MarkupEntity` ) - Markup entities for description field. Experimental

    **Maybe omitted**
#. ``members`` ( :ref:`tdproto-GroupMembership` ) - Group chat members

    **Maybe omitted**
#. ``notifications_enabled`` (boolean) - Push notifications enabled

    **Maybe omitted**
#. ``num`` (number) - Task number in this team

    **Maybe omitted**
#. ``num_unread_notices`` (number) - Mentions (@) counter

    **Maybe omitted**
#. ``num_unread`` (number) - Unread counter

    **Maybe omitted**
#. ``num_members`` (number) - Non-archive participants number

    **Maybe omitted**

    **Might be null**
#. ``num_items`` (number) - Items in checklist. Tasks only

    **Maybe omitted**

    **Might be null**
#. ``num_importants`` (number) - Number of important messages

    **Maybe omitted**
#. ``num_checked_items`` (number) - Checked items in checklist. Tasks only

    **Maybe omitted**

    **Might be null**
#. ``observers`` ( :ref:`tdproto-JID` ) - Task followers id's. TODO: rename to "followers"

    **Maybe omitted**
#. ``owner`` ( :ref:`tdproto-JID` ) - Task creator

    **Maybe omitted**
#. ``parents`` ( :ref:`tdproto-Subtask` ) - Parent tasks

    **Maybe omitted**
#. ``pinned`` (boolean) - Is chat pinned on top

    **Maybe omitted**
#. ``pinned_sort_ordering`` (number) - Sort ordering for pinned chat

    **Maybe omitted**
#. ``pinned_message`` ( :ref:`tdproto-Message` ) - Pinned message for this chat

    **Maybe omitted**

    **Might be null**
#. ``public`` (boolean) - Can other team member see this task/group chat

    **Maybe omitted**
#. ``readonly_for_members`` (boolean) - Readonly for non-admins group chat (Like Channels in Telegram bug switchable)

    **Maybe omitted**
#. ``section`` (string) - Project / section id, if any

    **Maybe omitted**
#. ``spent_time`` (number) - Task spent time, number

    **Maybe omitted**

    **Might be null**
#. ``status`` ( :ref:`tdproto-GroupStatus` ) - My status in group chat

    **Maybe omitted**

    **Might be null**
#. ``tabs`` ( :ref:`tdproto-TaskTabKey` ) - Tab names

    **Maybe omitted**
#. ``tags`` (string) - Task tags list, if any

    **Maybe omitted**
#. ``task_status`` (string) - Task status. May be custom

    **Maybe omitted**
#. ``title`` (string) - Task title. Generated from number and description

    **Maybe omitted**
#. ``uploads`` ( :ref:`tdproto-Upload` ) - Upload uids for request, upload objects for response

    **Maybe omitted**
#. ``urgency`` (number) - Task urgency, if available in team

    **Maybe omitted**

    **Might be null**

.. _tdproto-ChatCounters:

ChatCounters
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``chat_type`` ( :ref:`tdproto-ChatType` ) - DOCUMENTATION MISSING
#. ``gentime`` (number) - DOCUMENTATION MISSING
#. ``jid`` ( :ref:`tdproto-JID` ) - DOCUMENTATION MISSING
#. ``last_read_message_id`` (string) - DOCUMENTATION MISSING

    **Might be null**
#. ``last_activity`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``num_unread_notices`` (number) - DOCUMENTATION MISSING
#. ``num_unread`` (number) - DOCUMENTATION MISSING

.. _tdproto-ChatMessages:

ChatMessages
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``messages`` ( :ref:`tdproto-Message` ) - DOCUMENTATION MISSING

.. _tdproto-ChatShort:

ChatShort
-------------------------------------------------------------

Minimal chat representation

**Fields**:

#. ``chat_type`` ( :ref:`tdproto-ChatType` ) - Chat type
#. ``display_name`` (string) - Title
#. ``icons`` ( :ref:`tdproto-IconData` ) - Icon data

    **Might be null**
#. ``jid`` ( :ref:`tdproto-JID` ) - Group/Task/Contact id

.. _tdproto-ClientActivity:

ClientActivity
-------------------------------------------------------------

Change AFK (away from keyboard) status

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-clientActivityParams` ) - DOCUMENTATION MISSING

.. _tdproto-clientActivityParams:

clientActivityParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``afk`` (boolean) - Is away from keyboard

.. _tdproto-ClientCallBuzzCancel:

ClientCallBuzzCancel
-------------------------------------------------------------

Call buzzing cancelled

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-clientCallBuzzCancelParams` ) - DOCUMENTATION MISSING

.. _tdproto-clientCallBuzzCancelParams:

clientCallBuzzCancelParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``jid`` ( :ref:`tdproto-JID` ) - Chat or contact id

.. _tdproto-clientCallBuzzParams:

clientCallBuzzParams
-------------------------------------------------------------

Call buzzing

**Fields**:

#. ``jid`` ( :ref:`tdproto-JID` ) - Chat or contact id
#. ``members`` ( :ref:`tdproto-JID` ) - List of call participants

.. _tdproto-ClientCallLeave:

ClientCallLeave
-------------------------------------------------------------

Leave call

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-clientCallLeaveParams` ) - DOCUMENTATION MISSING

.. _tdproto-clientCallLeaveParams:

clientCallLeaveParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``jid`` ( :ref:`tdproto-JID` ) - Chat or contact id
#. ``reason`` (string) - Reason, if any

.. _tdproto-ClientCallMuteAll:

ClientCallMuteAll
-------------------------------------------------------------

Mute all other call participants

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-clientCallMuteAllParams` ) - DOCUMENTATION MISSING

.. _tdproto-clientCallMuteAllParams:

clientCallMuteAllParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``jid`` ( :ref:`tdproto-JID` ) - Chat or contact id

.. _tdproto-ClientCallOffer:

ClientCallOffer
-------------------------------------------------------------

Start a call

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-clientCallOfferParams` ) - DOCUMENTATION MISSING

.. _tdproto-clientCallOfferParams:

clientCallOfferParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``jid`` ( :ref:`tdproto-JID` ) - Chat or contact id
#. ``muted`` (boolean) - Mute state
#. ``sdp`` (string) - SDP (session description protocol) data
#. ``trickle`` (boolean) - Is trickle mode enabled

.. _tdproto-ClientCallReject:

ClientCallReject
-------------------------------------------------------------

Reject the call

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-clientCallRejectParams` ) - DOCUMENTATION MISSING

.. _tdproto-clientCallRejectParams:

clientCallRejectParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``jid`` ( :ref:`tdproto-JID` ) - Chat or contact id
#. ``reason`` (string) - Reason, if any

.. _tdproto-ClientCallSound:

ClientCallSound
-------------------------------------------------------------

Change mute state in call

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-clientCallSoundParams` ) - DOCUMENTATION MISSING

.. _tdproto-clientCallSoundParams:

clientCallSoundParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``jid`` ( :ref:`tdproto-JID` ) - Chat or contact id
#. ``muted`` (boolean) - Mute state

.. _tdproto-ClientCallTrickle:

ClientCallTrickle
-------------------------------------------------------------

Send trickle candidate for webrtc connection

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-clientCallTrickleParams` ) - DOCUMENTATION MISSING

.. _tdproto-clientCallTrickleParams:

clientCallTrickleParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``candidate`` (string) - Trickle candidate
#. ``jid`` ( :ref:`tdproto-JID` ) - Chat or contact id
#. ``sdp_mline_index`` (number) - SDP index
#. ``sdp_mid`` (string) - SDP mid

.. _tdproto-ClientChatComposing:

ClientChatComposing
-------------------------------------------------------------

Typing or recording audiomessage

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-clientChatComposingParams` ) - DOCUMENTATION MISSING

.. _tdproto-clientChatComposingParams:

clientChatComposingParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``composing`` (boolean) - true = start typing / audio recording, false = stop

    **Maybe omitted**
#. ``draft`` (string) - Message draft data

    **Maybe omitted**

    **Might be null**
#. ``is_audio`` (boolean) - true = audiomessage, false = text typing

    **Maybe omitted**
#. ``jid`` ( :ref:`tdproto-JID` ) - Chat or contact id

.. _tdproto-ClientChatLastread:

ClientChatLastread
-------------------------------------------------------------

Last read message in chat changed

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-clientChatLastreadParams` ) - DOCUMENTATION MISSING

.. _tdproto-clientChatLastreadParams:

clientChatLastreadParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``jid`` ( :ref:`tdproto-JID` ) - Chat or contact id
#. ``last_read_message_id`` (string) - Last read message id. Omitted = last message in chat

    **Maybe omitted**

    **Might be null**

.. _tdproto-ClientConfirm:

ClientConfirm
-------------------------------------------------------------

Client confirmed server message

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-clientConfirmParams` ) - DOCUMENTATION MISSING

.. _tdproto-clientConfirmParams:

clientConfirmParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``confirm_id`` (string) - Unique identifier generated by client

.. _tdproto-ClientMessageDeleted:

ClientMessageDeleted
-------------------------------------------------------------

Message deleted

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-clientMessageDeletedParams` ) - DOCUMENTATION MISSING

.. _tdproto-clientMessageDeletedParams:

clientMessageDeletedParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``message_id`` (string) - Message id

    **Maybe omitted**

.. _tdproto-ClientMessageUpdated:

ClientMessageUpdated
-------------------------------------------------------------

Message created or changed

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-ClientMessageUpdatedParams` ) - DOCUMENTATION MISSING

.. _tdproto-ClientMessageUpdatedParams:

ClientMessageUpdatedParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``comment`` (string) - Deprecated

    **Maybe omitted**
#. ``content`` ( :ref:`tdproto-MessageContent` ) - Message content. Required
#. ``important`` (boolean) - Important flag. Not required. Default: false

    **Maybe omitted**
#. ``linked_messages`` (string) - Forwarded messages (previously was for reply too). Not required

    **Maybe omitted**
#. ``message_id`` (string) - Uid created by client. Recommended

    **Maybe omitted**
#. ``nopreview`` (boolean) - Disable links preview generation. Not required. Default: false

    **Maybe omitted**
#. ``old_style_attachment`` (boolean) - Backward compatibility mode

    **Maybe omitted**
#. ``reply_to`` (string) - Replied to message id. Not required

    **Maybe omitted**
#. ``to`` ( :ref:`tdproto-JID` ) - Chat, task or contact jid. Required
#. ``uploads`` (string) - Message attachments

    **Maybe omitted**

.. _tdproto-ClientPing:

ClientPing
-------------------------------------------------------------

Empty message for checking server connection

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING

.. _tdproto-ColorRule:

ColorRule
-------------------------------------------------------------

Set of rules to apply to tasks for coloring

**Fields**:

#. ``color_index`` (number) - DOCUMENTATION MISSING
#. ``description`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``priority`` (number) - DOCUMENTATION MISSING
#. ``section`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``section_enabled`` (boolean) - DOCUMENTATION MISSING

    **Maybe omitted**

    **Might be null**
#. ``tags`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``tags_enabled`` (boolean) - DOCUMENTATION MISSING

    **Maybe omitted**

    **Might be null**
#. ``task_urgency_enabled`` (boolean) - DOCUMENTATION MISSING

    **Maybe omitted**

    **Might be null**
#. ``task_urgency`` (number) - DOCUMENTATION MISSING

    **Maybe omitted**

    **Might be null**
#. ``task_status`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``task_importance_enabled`` (boolean) - DOCUMENTATION MISSING

    **Maybe omitted**

    **Might be null**
#. ``task_importance`` (number) - DOCUMENTATION MISSING

    **Maybe omitted**

    **Might be null**
#. ``uid`` (string) - DOCUMENTATION MISSING

.. _tdproto-Contact:

Contact
-------------------------------------------------------------

Contact

**Fields**:

#. ``add_to_team_rights`` (boolean) - Can contact add users to this team

    **Maybe omitted**
#. ``alt_send`` (boolean) - Use Ctrl/Cmd + Enter instead Enter

    **Maybe omitted**

    **Might be null**
#. ``always_send_pushes`` (boolean) - Send push notifications even contact is online

    **Maybe omitted**

    **Might be null**
#. ``asterisk_mention`` (boolean) - Use * as @ for mentions

    **Maybe omitted**

    **Might be null**
#. ``auth_2fa_enabled`` (boolean) - Two-factor authentication is configured and confirmed

    **Maybe omitted**
#. ``auth_2fa_status`` (string) - Two-factor authentication status

    **Maybe omitted**
#. ``botname`` (string) - Bot name. Empty for users

    **Maybe omitted**
#. ``can_create_task`` (boolean) - Can I call create task for this contact

    **Maybe omitted**
#. ``can_manage_tags`` (boolean) - Can I manage tags in this team

    **Maybe omitted**
#. ``can_manage_integrations`` (boolean) - Can I manage integrations in this team

    **Maybe omitted**
#. ``can_join_public_tasks`` (boolean) - Can I view/join public tasks in this team

    **Maybe omitted**
#. ``can_delete`` (boolean) - Can I remove this contact from team

    **Maybe omitted**
#. ``can_delete_any_message`` (boolean) - Deprecated: use CanDeleteAnyMessage in chat object

    **Maybe omitted**
#. ``can_join_public_groups`` (boolean) - Can I view/join public group in this team

    **Maybe omitted**
#. ``can_manage_color_rules`` (boolean) - Can I manage color rules in this team

    **Maybe omitted**
#. ``can_add_to_team`` (boolean) - Can I add new members to this team

    **Maybe omitted**
#. ``can_manage_sections`` (boolean) - Can I manage sections in this team

    **Maybe omitted**
#. ``can_call`` (boolean) - Can I call to this contact

    **Maybe omitted**
#. ``can_send_message`` (boolean) - Can I send message to this contact

    **Maybe omitted**
#. ``can_create_group`` (boolean) - Can I create group chats in this team

    **Maybe omitted**
#. ``can_add_to_group`` (boolean) - Can I add this contact to group chats

    **Maybe omitted**
#. ``cant_send_message_reason`` (string) - Why I can't send message to this chat (if can't)

    **Maybe omitted**
#. ``changeable_fields`` (string) - Changeable fields

    **Maybe omitted**
#. ``contact_show_archived`` (boolean) - Show archived contacts in contact list

    **Maybe omitted**

    **Might be null**
#. ``contact_short_view`` (boolean) - Short view in contact list

    **Maybe omitted**

    **Might be null**
#. ``contact_phone`` (string) - Contact phone in this team
#. ``contact_mshort_view`` (boolean) - Short view in contact list in mobile app

    **Maybe omitted**

    **Might be null**
#. ``contact_email`` (string) - Contact email in this team
#. ``custom_fields`` ( :ref:`tdproto-ContactCustomFields` ) - Extra contact fields

    **Maybe omitted**

    **Might be null**
#. ``debug_show_activity`` (boolean) - Enable debug messages in UI

    **Maybe omitted**

    **Might be null**
#. ``default_lang`` (string) - Default language code

    **Maybe omitted**

    **Might be null**
#. ``display_name`` (string) - Full name in chats
#. ``dropall_enabled`` (boolean) - Enable remove all messages experimental features

    **Maybe omitted**

    **Might be null**
#. ``family_name`` (string) - Family name

    **Maybe omitted**
#. ``given_name`` (string) - Given name

    **Maybe omitted**
#. ``group_short_view`` (boolean) - Short view in group list

    **Maybe omitted**

    **Might be null**
#. ``group_mshort_view`` (boolean) - Short view in group list in mobile app

    **Maybe omitted**

    **Might be null**
#. ``group_notifications_enabled`` (boolean) - Push notifications for group chats

    **Maybe omitted**

    **Might be null**
#. ``icons`` ( :ref:`tdproto-IconData` ) - Icons data

    **Might be null**
#. ``is_archive`` (boolean) - Contact deleted

    **Maybe omitted**
#. ``jid`` ( :ref:`tdproto-JID` ) - Contact Id
#. ``last_activity`` (string) - Last activity in this team (iso datetime)

    **Maybe omitted**
#. ``mood`` (string) - Mood in this team

    **Maybe omitted**
#. ``munread_first`` (boolean) - Show unread chats first in feed in mobile app

    **Maybe omitted**

    **Might be null**
#. ``patronymic`` (string) - Patronymic, if any

    **Maybe omitted**
#. ``quiet_time_start`` (string) - Quiet time start

    **Maybe omitted**

    **Might be null**
#. ``quiet_time_finish`` (string) - Quiet time finish

    **Maybe omitted**

    **Might be null**
#. ``role`` (string) - Role in this team
#. ``sections`` (string) - Section ids
#. ``short_name`` (string) - Short name in chats
#. ``status`` ( :ref:`tdproto-TeamStatus` ) - Status in this team
#. ``task_short_view`` (boolean) - Short view in task list

    **Maybe omitted**

    **Might be null**
#. ``task_notifications_enabled`` (boolean) - Push notifications for task chats

    **Maybe omitted**

    **Might be null**
#. ``task_mshort_view`` (boolean) - Short view in task list in mobile app

    **Maybe omitted**

    **Might be null**
#. ``timezone`` (string) - Timezone, if any

    **Maybe omitted**

    **Might be null**
#. ``unread_first`` (boolean) - Show unread chats first in feed

    **Maybe omitted**

    **Might be null**

.. _tdproto-ContactCustomFields:

ContactCustomFields
-------------------------------------------------------------

Extra contact fields

**Fields**:

#. ``company`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``department`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``mobile_phone`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``source`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``title`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**

.. _tdproto-ContactPreview:

ContactPreview
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``_error`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``family_name`` (string) - DOCUMENTATION MISSING
#. ``given_name`` (string) - DOCUMENTATION MISSING
#. ``patronymic`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``phone`` (string) - DOCUMENTATION MISSING
#. ``role`` (string) - DOCUMENTATION MISSING
#. ``section`` (string) - DOCUMENTATION MISSING

.. _tdproto-ContactShort:

ContactShort
-------------------------------------------------------------

Short contact representation

**Fields**:

#. ``display_name`` (string) - Full name in chats
#. ``icons`` ( :ref:`tdproto-IconData` ) - Icons data

    **Might be null**
#. ``jid`` ( :ref:`tdproto-JID` ) - Contact Id
#. ``short_name`` (string) - Short name in chats

.. _tdproto-Country:

Country
-------------------------------------------------------------

Country for phone numbers selection on login screen

**Fields**:

#. ``code`` (string) - Country code
#. ``default`` (boolean) - Selected by default

    **Maybe omitted**
#. ``name`` (string) - Country name
#. ``popular`` (boolean) - Is popular, need to cache

    **Maybe omitted**

.. _tdproto-DeletedChat:

DeletedChat
-------------------------------------------------------------

Minimal chat representation for deletion

**Fields**:

#. ``chat_type`` ( :ref:`tdproto-ChatType` ) - Chat type
#. ``gentime`` (number) - Chat fields (related to concrete participant) version
#. ``is_archive`` (boolean) - Archive flag. Always true for this structure
#. ``jid`` ( :ref:`tdproto-JID` ) - Group/Task/Contact id

.. _tdproto-DeletedRemind:

DeletedRemind
-------------------------------------------------------------

Remind deleted message

**Fields**:

#. ``uid`` (string) - Remind id

.. _tdproto-DeletedSection:

DeletedSection
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``gentime`` (number) - Object version
#. ``uid`` (string) - Section uid

.. _tdproto-DeletedTag:

DeletedTag
-------------------------------------------------------------

Delete tag message

**Fields**:

#. ``uid`` (string) - Tag id

.. _tdproto-DeletedTeam:

DeletedTeam
-------------------------------------------------------------

Team deletion message. Readonly

**Fields**:

#. ``gentime`` (number) - Object version
#. ``is_archive`` (boolean) - Team deleted
#. ``uid`` (string) - Team id

.. _tdproto-Dist:

Dist
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``type`` (string) - DOCUMENTATION MISSING
#. ``url`` (string) - DOCUMENTATION MISSING

.. _tdproto-Features:

Features
-------------------------------------------------------------

Server information. Readonly

**Fields**:

#. ``afk_age`` (number) - Max inactivity seconds
#. ``allow_admin_mute`` (boolean) - Wiki pages in chats. Experimental

    **Maybe omitted**
#. ``android_app`` (string) - Link to Google Play
#. ``app_title`` (string) - Application title
#. ``app_schemes`` (string) - Local applications urls
#. ``auth_2fa`` (boolean) - Two-factor authentication (2FA) enabled

    **Maybe omitted**
#. ``auth_by_qr_code`` (boolean) - QR-code / link authentication enabled

    **Maybe omitted**
#. ``auth_by_sms`` (boolean) - SMS authentication enabled

    **Maybe omitted**
#. ``auth_by_password`` (boolean) - Password authentication enabled

    **Maybe omitted**
#. ``background`` (string) - Background image url, if any

    **Maybe omitted**
#. ``build`` (string) - Build/revision of server side
#. ``calls`` (boolean) - Calls functions enabled
#. ``calls_record`` (boolean) - Calls record enabled
#. ``custom_server`` (boolean) - True for premise installation
#. ``default_wallpaper`` ( :ref:`tdproto-Wallpaper` ) - Default wallpaper url for mobile apps, if any

    **Maybe omitted**

    **Might be null**
#. ``desktop_version`` (string) - Desktop application version
#. ``firebase_api_key`` (string) - Firebase settings for web-push notifications
#. ``firebase_sender_id`` (string) - Firebase settings for web-push notifications
#. ``firebase_project_id`` (string) - Firebase settings for web-push notifications
#. ``firebase_database_url`` (string) - Firebase settings for web-push notifications
#. ``firebase_auth_domain`` (string) - Firebase settings for web-push notifications
#. ``firebase_app_id`` (string) - Firebase settings for web-push notifications
#. ``firebase_storage_bucket`` (string) - Firebase settings for web-push notifications
#. ``free_registration`` (boolean) - Free registration allowed
#. ``front_version`` (string) - Webclient version
#. ``host`` (string) - Current host
#. ``ice_servers`` ( :ref:`tdproto-ICEServer` ) - ICE servers for WebRTC
#. ``installation_type`` (string) - Name of installation
#. ``installation_title`` (string) - Installation title, used on login screen

    **Maybe omitted**
#. ``ios_app`` (string) - Link to AppStore
#. ``is_testing`` (boolean) - Testing installation
#. ``landing_url`` (string) - Landing page address, if any

    **Maybe omitted**
#. ``max_teams`` (number) - Maximum teams for one account
#. ``max_linked_messages`` (number) - Maximum number of forwarded messages
#. ``max_username_part_length`` (number) - Maximum chars for: family_name, given_name, patronymic if any
#. ``max_mood_length`` (number) - Maximum chars for mood in team
#. ``max_message_search_limit`` (number) - Maximum search result
#. ``max_message_uploads`` (number) - Maximum number of message uploads
#. ``max_participants_per_call`` (number) - Maximum number of participants per call

    **Maybe omitted**
#. ``max_color_rule_description_length`` (number) - Maximum length for ColorRule description
#. ``max_section_length`` (number) - Maximum length for project and contact's sections names
#. ``max_group_title_length`` (number) - Maximum chars for group chat name
#. ``max_task_title_length`` (number) - Maximum length for task title
#. ``max_integration_comment_length`` (number) - Maximum length for Integration comment
#. ``max_upload_mb`` (number) - Maximum size of user's upload
#. ``max_role_length`` (number) - Maximum chars for role in team
#. ``max_url_length`` (number) - Maximum length for urls
#. ``max_message_length`` (number) - Maximum chars for text message
#. ``max_tag_length`` (number) - Maximum length for tags
#. ``message_uploads`` (boolean) - Multiple message uploads
#. ``metrika`` (string) - Yandex metrika counter id
#. ``min_search_length`` (number) - Minimal chars number for starting global search
#. ``min_app_version`` (string) - Minimal application version required for this server. Used for breaking changes
#. ``mobile_calls`` (boolean) - Calls functions enabled for mobile applications
#. ``oauth_services`` ( :ref:`tdproto-OAuthService` ) - External services

    **Maybe omitted**
#. ``only_one_device_per_call`` (boolean) - Disallow call from multiply devices. Experimental

    **Maybe omitted**
#. ``readonly_groups`` (boolean) - Deprecated
#. ``resend_timeout`` (number) - Resend message in n seconds if no confirmation from server given
#. ``safari_push_id`` (string) - Safari push id for web-push notifications
#. ``sentry_dsn_js`` (string) - Frontend sentry.io settings
#. ``server_drafts`` (boolean) - Message drafts saved on server
#. ``single_group_teams`` (boolean) - Cross team communication. Experimental
#. ``task_messages`` (boolean) - Deprecated
#. ``task_tags`` (boolean) - Deprecated
#. ``task_public`` (boolean) - Deprecated
#. ``task_checklist`` (boolean) - Deprecated
#. ``task_dashboard`` (boolean) - Deprecated
#. ``terms`` ( :ref:`tdproto-Terms` ) - Team entity naming. Experimental
#. ``theme`` (string) - Default UI theme
#. ``userver`` (string) - Static files server address
#. ``wiki_pages`` (boolean) - Wiki pages in chats. Experimental

.. _tdproto-FontColors:

FontColors
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``brand_button`` (string) - DOCUMENTATION MISSING
#. ``bubble_sent`` (string) - DOCUMENTATION MISSING
#. ``bubble_received`` (string) - DOCUMENTATION MISSING
#. ``simple_button`` (string) - DOCUMENTATION MISSING
#. ``sub`` (string) - DOCUMENTATION MISSING
#. ``text`` (string) - DOCUMENTATION MISSING
#. ``title`` (string) - DOCUMENTATION MISSING

.. _tdproto-GroupAccessRequest:

GroupAccessRequest
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``created`` (string) - DOCUMENTATION MISSING
#. ``subject`` ( :ref:`tdproto-JID` ) - DOCUMENTATION MISSING
#. ``uid`` (string) - DOCUMENTATION MISSING

.. _tdproto-GroupMembership:

GroupMembership
-------------------------------------------------------------

Group chat membership status

**Fields**:

#. ``can_remove`` (boolean) - Can I remove this member

    **Maybe omitted**
#. ``jid`` ( :ref:`tdproto-JID` ) - Contact id
#. ``status`` ( :ref:`tdproto-GroupStatus` ) - Status in group

.. _tdproto-ICEServer:

ICEServer
-------------------------------------------------------------

Interactive Connectivity Establishment Server for WEB Rtc connection. Readonly

**Fields**:

#. ``urls`` (string) - URls

.. _tdproto-IconColors:

IconColors
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``brand`` (string) - DOCUMENTATION MISSING
#. ``other`` (string) - DOCUMENTATION MISSING
#. ``title`` (string) - DOCUMENTATION MISSING

.. _tdproto-IconData:

IconData
-------------------------------------------------------------

Icon data. For icon generated from display name contains Letters + Color fields

**Fields**:

#. ``blurhash`` (string) - Compact representation of a placeholder for an image (experimental)

    **Maybe omitted**
#. ``color`` (string) - Icon background color (only for stub icon)

    **Maybe omitted**
#. ``letters`` (string) - Letters (only for stub icon)

    **Maybe omitted**
#. ``lg`` ( :ref:`tdproto-SingleIcon` ) - Large image
#. ``sm`` ( :ref:`tdproto-SingleIcon` ) - Small icon
#. ``stub`` (string) - Deprecated

    **Maybe omitted**

.. _tdproto-InputColors:

InputColors
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``active`` (string) - DOCUMENTATION MISSING
#. ``disable`` (string) - DOCUMENTATION MISSING
#. ``error`` (string) - DOCUMENTATION MISSING
#. ``static`` (string) - DOCUMENTATION MISSING

.. _tdproto-Integration:

Integration
-------------------------------------------------------------

Integration for concrete chat

**Fields**:

#. ``-`` (string) - DOCUMENTATION MISSING
#. ``comment`` (string) - Comment, if any
#. ``created`` (string) - Creation datetime, iso

    **Maybe omitted**
#. ``enabled`` (boolean) - Integration enabled
#. ``form`` ( :ref:`tdproto-IntegrationForm` ) - Integration form
#. ``group`` ( :ref:`tdproto-JID` ) - Chat id
#. ``help`` (string) - Full description

    **Maybe omitted**
#. ``kind`` (string) - Unique integration name
#. ``uid`` (string) - Id

    **Maybe omitted**

.. _tdproto-IntegrationField:

IntegrationField
-------------------------------------------------------------

Integration form field

**Fields**:

#. ``label`` (string) - Label
#. ``readonly`` (boolean) - Is field readonly
#. ``value`` (string) - Current value

.. _tdproto-IntegrationForm:

IntegrationForm
-------------------------------------------------------------

Integration form

**Fields**:

#. ``api_key`` ( :ref:`tdproto-IntegrationField` ) - Api key field, if any

    **Maybe omitted**

    **Might be null**
#. ``url`` ( :ref:`tdproto-IntegrationField` ) - Url, if any

    **Maybe omitted**

    **Might be null**
#. ``webhook_url`` ( :ref:`tdproto-IntegrationField` ) - Webhook url, if any

    **Maybe omitted**

    **Might be null**

.. _tdproto-IntegrationKind:

IntegrationKind
-------------------------------------------------------------

Integration kind

**Fields**:

#. ``description`` (string) - Plugin description
#. ``icon`` (string) - Path to icon
#. ``kind`` (string) - Integration unique name
#. ``template`` ( :ref:`tdproto-Integration` ) - Integration template
#. ``title`` (string) - Plugin title

.. _tdproto-Integrations:

Integrations
-------------------------------------------------------------

Complete integrations data, as received from server

**Fields**:

#. ``integrations`` ( :ref:`tdproto-Integration` ) - Currently existing integrations
#. ``kinds`` ( :ref:`tdproto-IntegrationKind` ) - Types of integrations available for setup

.. _tdproto-Invitation:

Invitation
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``created`` (string) - DOCUMENTATION MISSING
#. ``qr`` (string) - DOCUMENTATION MISSING
#. ``token`` (string) - DOCUMENTATION MISSING
#. ``uid`` (string) - DOCUMENTATION MISSING

.. _tdproto-JSEP:

JSEP
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``sdp`` (string) - DOCUMENTATION MISSING
#. ``type`` (string) - DOCUMENTATION MISSING

.. _tdproto-MarkupEntity:

MarkupEntity
-------------------------------------------------------------

Markup entity. Experimental

**Fields**:

#. ``childs`` ( :ref:`tdproto-MarkupEntity` ) - List of internal markup entities

    **Maybe omitted**
#. ``cllen`` (number) - Close marker length

    **Maybe omitted**
#. ``cl`` (number) - Close marker offset
#. ``op`` (number) - Open marker offset
#. ``oplen`` (number) - Open marker length

    **Maybe omitted**
#. ``repl`` (string) - Text replacement

    **Maybe omitted**
#. ``time`` (string) - Time, for Time type

    **Maybe omitted**
#. ``typ`` ( :ref:`tdproto-MarkupType` ) - Marker type
#. ``url`` (string) - Url, for Link type

    **Maybe omitted**

.. _tdproto-Message:

Message
-------------------------------------------------------------

Chat message

**Fields**:

#. ``_debug`` (string) - Debug information, if any

    **Maybe omitted**
#. ``chat`` ( :ref:`tdproto-JID` ) - Chat id
#. ``chat_type`` ( :ref:`tdproto-ChatType` ) - Chat type
#. ``content`` ( :ref:`tdproto-MessageContent` ) - Message content struct
#. ``created`` (string) - Message creation datetime (set by server side) or sending datetime in future for draft messages
#. ``drafted`` (string) - Creation datetime for draft messages

    **Maybe omitted**
#. ``editable_until`` (string) - Author can change this message until date. Can be null

    **Maybe omitted**
#. ``edited`` (string) - ISODateTimeString of message modification or deletion

    **Maybe omitted**
#. ``from`` ( :ref:`tdproto-JID` ) - Sender contact id
#. ``gentime`` (number) - Object version
#. ``has_previews`` (boolean) - Has link previews. True or null

    **Maybe omitted**
#. ``important`` (boolean) - Importance flag

    **Maybe omitted**
#. ``is_last`` (boolean) - This message is first in this chat. True or null

    **Maybe omitted**
#. ``is_first`` (boolean) - This message is first in this chat. True or null

    **Maybe omitted**
#. ``is_archive`` (boolean) - This message is archive. True or null

    **Maybe omitted**
#. ``linked_messages`` ( :ref:`tdproto-Message` ) - Forwarded messages. Can be null. Also contains double of ReplyTo for backward compatibility

    **Maybe omitted**
#. ``links`` ( :ref:`tdproto-MessageLinks` ) - External/internals links

    **Maybe omitted**
#. ``markup`` ( :ref:`tdproto-MarkupEntity` ) - Markup entities. Experimental

    **Maybe omitted**
#. ``message_id`` (string) - Message uid
#. ``nopreview`` (boolean) - Disable link previews. True or null

    **Maybe omitted**
#. ``notice`` (boolean) - Has mention (@). True or null

    **Maybe omitted**
#. ``num`` (number) - Index number of this message. Starts from 0. Null for deleted messages. Changes when any previous message wad deleted

    **Maybe omitted**

    **Might be null**
#. ``num_received`` (number) - Unused yet

    **Maybe omitted**
#. ``prev`` (string) - Previous message id in this chat. Uid or null

    **Maybe omitted**
#. ``push_text`` (string) - Simple plaintext message representation

    **Maybe omitted**
#. ``reactions`` ( :ref:`tdproto-MessageReaction` ) - Message reactions struct. Can be null

    **Maybe omitted**
#. ``received`` (boolean) - Message was seen by anybody in chat. True or null

    **Maybe omitted**
#. ``reply_to`` ( :ref:`tdproto-Message` ) - Message that was replied to, if any

    **Maybe omitted**

    **Might be null**
#. ``silently`` (boolean) - Message has no pushes and did not affect any counters

    **Maybe omitted**
#. ``to`` ( :ref:`tdproto-JID` ) - Recipient id (group, task or contact)
#. ``uploads`` ( :ref:`tdproto-Upload` ) - Message uploads

    **Maybe omitted**

.. _tdproto-MessageColors:

MessageColors
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``allocated`` (string) - DOCUMENTATION MISSING
#. ``bubble_sent`` (string) - DOCUMENTATION MISSING
#. ``bubble_received`` (string) - DOCUMENTATION MISSING
#. ``bubble_important`` (string) - DOCUMENTATION MISSING
#. ``status_feed`` (string) - DOCUMENTATION MISSING
#. ``status_bubble`` (string) - DOCUMENTATION MISSING

.. _tdproto-MessageContent:

MessageContent
-------------------------------------------------------------

Chat message content

**Fields**:

#. ``actor`` ( :ref:`tdproto-JID` ) - Change actor contact id (for "change" mediatype)

    **Maybe omitted**
#. ``animated`` (boolean) - Upload is animated image, if any. Deprecated: use Uploads instead

    **Maybe omitted**
#. ``blurhash`` (string) - Compact representation of a placeholder for an image. Deprecated: use Uploads instead

    **Maybe omitted**
#. ``comment`` (string) - Comment (for "audiomsg" mediatype)

    **Maybe omitted**
#. ``duration`` (number) - Upload duration, if any. Deprecated: use Uploads instead

    **Maybe omitted**

    **Might be null**
#. ``emails`` (string) - Emails list (for "contact" mediatype)

    **Maybe omitted**
#. ``family_name`` (string) - Family name (for "contact" mediatype)

    **Maybe omitted**
#. ``given_name`` (string) - Given name (for "contact" mediatype)

    **Maybe omitted**
#. ``mediaURL`` (string) - Upload url, if any. Deprecated: use Uploads instead

    **Maybe omitted**
#. ``name`` (string) - Upload name, if any. Deprecated: use Uploads instead

    **Maybe omitted**
#. ``new`` (string) - Change new value (for "change" mediatype)

    **Maybe omitted**

    **Might be null**
#. ``old`` (string) - Change old value (for "change" mediatype)

    **Maybe omitted**

    **Might be null**
#. ``patronymic`` (string) - Patronymic name (for "contact" mediatype)

    **Maybe omitted**
#. ``pdf_version`` ( :ref:`tdproto-PdfVersion` ) - Pdf version, if any

    **Maybe omitted**

    **Might be null**
#. ``phones`` (string) - Contact phones list (for "contact" mediatype)

    **Maybe omitted**
#. ``preview2xURL`` (string) - Upload high resolution preview absolute url, if any. Deprecated: use Uploads instead

    **Maybe omitted**
#. ``previewHeight`` (number) - Upload preview height, in pixels, if any. Deprecated: use Uploads instead

    **Maybe omitted**
#. ``previewURL`` (string) - Upload preview absolute url, if any. Deprecated: use Uploads instead

    **Maybe omitted**
#. ``previewWidth`` (number) - Upload width, in pixels, if any. Deprecated: use Uploads instead

    **Maybe omitted**
#. ``processing`` (boolean) - Upload still processing, if any. Deprecated: use Uploads instead

    **Maybe omitted**
#. ``size`` (number) - Upload size, if any. Deprecated: use Uploads instead

    **Maybe omitted**
#. ``stickerpack`` (string) - Stickerpack name (for "sticker" subtype)

    **Maybe omitted**
#. ``subtype`` ( :ref:`tdproto-Mediasubtype` ) - Message subtype, if any

    **Maybe omitted**
#. ``text`` (string) - Text representation of message
#. ``title`` (string) - Change title (for "change" mediatype)

    **Maybe omitted**
#. ``type`` ( :ref:`tdproto-Mediatype` ) - Message type
#. ``upload`` (string) - Upload id, if any. Deprecated: use Uploads instead

    **Maybe omitted**

.. _tdproto-MessageLink:

MessageLink
-------------------------------------------------------------

Checked message links. In short: "Click here: {link.Pattern}" => "Click here: <a href='{link.Url}'>{link.Text}</a>"

**Fields**:

#. ``nopreview`` (boolean) - Website previews disabled

    **Maybe omitted**
#. ``pattern`` (string) - Text fragment that should be replaced by link
#. ``preview`` ( :ref:`tdproto-MessageLinkPreview` ) - Optional preview info, for websites

    **Maybe omitted**

    **Might be null**
#. ``text`` (string) - Text replacement
#. ``uploads`` ( :ref:`tdproto-Upload` ) - Optional upload info

    **Maybe omitted**
#. ``url`` (string) - Internal or external link
#. ``youtube_id`` (string) - Optional youtube movie id

    **Maybe omitted**

.. _tdproto-MessageLinkPreview:

MessageLinkPreview
-------------------------------------------------------------

Website title and description

**Fields**:

#. ``description`` (string) - Website description

    **Maybe omitted**
#. ``title`` (string) - Website title or og:title content

.. _tdproto-MessagePush:

MessagePush
-------------------------------------------------------------

Push message over websockets. Readonly

**Fields**:

#. ``chat`` ( :ref:`tdproto-JID` ) - Chat id
#. ``click_action`` (string) - Url opened on click
#. ``created`` (string) - Message creation iso datetime
#. ``icon_url`` (string) - Absolute url to push icon
#. ``message`` (string) - Push body
#. ``message_id`` (string) - Message id
#. ``sender`` ( :ref:`tdproto-JID` ) - Sender contact id
#. ``subtitle`` (string) - Push subtitle
#. ``tag`` (string) - Push tag (for join pushes)
#. ``team`` (string) - Team uid
#. ``title`` (string) - Push title

.. _tdproto-MessageReaction:

MessageReaction
-------------------------------------------------------------

Message emoji reaction

**Fields**:

#. ``counter`` (number) - Number of reactions
#. ``details`` ( :ref:`tdproto-MessageReactionDetail` ) - Details
#. ``name`` (string) - Emoji

.. _tdproto-MessageReactionDetail:

MessageReactionDetail
-------------------------------------------------------------

Message reaction detail

**Fields**:

#. ``created`` (string) - When reaction added, iso datetime
#. ``name`` (string) - Reaction emoji
#. ``sender`` ( :ref:`tdproto-JID` ) - Reaction author

.. _tdproto-OAuthService:

OAuthService
-------------------------------------------------------------

OAuth service

**Fields**:

#. ``name`` (string) - Integration title
#. ``url`` (string) - Redirect url

.. _tdproto-OnlineCall:

OnlineCall
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``jid`` ( :ref:`tdproto-JID` ) - Chat or contact id
#. ``online_count`` (number) - Number participants in call

    **Maybe omitted**
#. ``start`` (string) - Call start

    **Maybe omitted**

    **Might be null**
#. ``uid`` (string) - Call id

.. _tdproto-OnlineContact:

OnlineContact
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``afk`` (boolean) - Is away from keyboard

    **Maybe omitted**
#. ``jid`` ( :ref:`tdproto-JID` ) - Contact id
#. ``mobile`` (boolean) - Is mobile client

.. _tdproto-PaginatedChats:

PaginatedChats
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``contacts`` ( :ref:`tdproto-Contact` ) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``count`` (number) - DOCUMENTATION MISSING
#. ``limit`` (number) - DOCUMENTATION MISSING
#. ``objects`` ( :ref:`tdproto-Chat` ) - DOCUMENTATION MISSING
#. ``offset`` (number) - DOCUMENTATION MISSING

.. _tdproto-PaginatedContacts:

PaginatedContacts
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``count`` (number) - DOCUMENTATION MISSING
#. ``limit`` (number) - DOCUMENTATION MISSING
#. ``objects`` ( :ref:`tdproto-Contact` ) - DOCUMENTATION MISSING
#. ``offset`` (number) - DOCUMENTATION MISSING

.. _tdproto-PaginatedMessages:

PaginatedMessages
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``count`` (number) - DOCUMENTATION MISSING
#. ``limit`` (number) - DOCUMENTATION MISSING
#. ``objects`` ( :ref:`tdproto-Message` ) - DOCUMENTATION MISSING
#. ``offset`` (number) - DOCUMENTATION MISSING

.. _tdproto-PaginatedUploadShortMessages:

PaginatedUploadShortMessages
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``count`` (number) - DOCUMENTATION MISSING
#. ``limit`` (number) - DOCUMENTATION MISSING
#. ``objects`` ( :ref:`tdproto-UploadShortMessage` ) - DOCUMENTATION MISSING
#. ``offset`` (number) - DOCUMENTATION MISSING

.. _tdproto-PdfVersion:

PdfVersion
-------------------------------------------------------------

PDF preview of mediafile. Experimental

**Fields**:

#. ``text_preview`` (string) - First string of text content

    **Maybe omitted**
#. ``url`` (string) - Absolute url

.. _tdproto-PushDevice:

PushDevice
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``allowed_notifications`` (boolean) - DOCUMENTATION MISSING
#. ``data_pushes`` (boolean) - DOCUMENTATION MISSING
#. ``data_badges`` (boolean) - DOCUMENTATION MISSING
#. ``device_id`` (string) - DOCUMENTATION MISSING
#. ``name`` (string) - DOCUMENTATION MISSING
#. ``notification_token`` (string) - DOCUMENTATION MISSING
#. ``type`` (string) - DOCUMENTATION MISSING
#. ``voip_notification_token`` (string) - DOCUMENTATION MISSING

.. _tdproto-ReceivedMessage:

ReceivedMessage
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``_debug`` (string) - Debug message, if any

    **Maybe omitted**
#. ``chat`` ( :ref:`tdproto-JID` ) - Chat or contact id
#. ``message_id`` (string) - Message id
#. ``num_received`` (number) - Number of contacts received this message. Experimental

    **Maybe omitted**
#. ``received`` (boolean) - Is received

.. _tdproto-Remind:

Remind
-------------------------------------------------------------

Remind

**Fields**:

#. ``chat`` ( :ref:`tdproto-JID` ) - Chat id
#. ``comment`` (string) - Comment, if any

    **Maybe omitted**
#. ``fire_at`` (string) - Activation time, iso
#. ``uid`` (string) - Remind id

.. _tdproto-Section:

Section
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``description`` (string) - Description, if any

    **Maybe omitted**
#. ``gentime`` (number) - Object version
#. ``is_archive`` (boolean) - Is deleted

    **Maybe omitted**
#. ``name`` (string) - Name
#. ``sort_ordering`` (number) - Sort ordering
#. ``uid`` (string) - Section uid

.. _tdproto-ServerCallAnswer:

ServerCallAnswer
-------------------------------------------------------------

Call parameters

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverCallAnswerParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverCallAnswerCandidate:

serverCallAnswerCandidate
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``candidate`` (string) - DOCUMENTATION MISSING
#. ``sdpMLineIndex`` (number) - DOCUMENTATION MISSING

.. _tdproto-serverCallAnswerParams:

serverCallAnswerParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``candidates`` ( :ref:`tdproto-serverCallAnswerCandidate` ) - List of ICE candidates (when trickle = false)
#. ``jid`` ( :ref:`tdproto-JID` ) - Chat or contact id
#. ``jsep`` ( :ref:`tdproto-JSEP` ) - SDP data
#. ``onliners`` ( :ref:`tdproto-CallOnliner` ) - Current call participants

    **Maybe omitted**
#. ``uid`` (string) - Call id

.. _tdproto-ServerCallBuzz:

ServerCallBuzz
-------------------------------------------------------------

Call buzzing

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverCallBuzzParams` ) - DOCUMENTATION MISSING

.. _tdproto-ServerCallBuzzcancel:

ServerCallBuzzcancel
-------------------------------------------------------------

Call cancelled on buzzing

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverCallBuzzcancelParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverCallBuzzcancelParams:

serverCallBuzzcancelParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``jid`` ( :ref:`tdproto-JID` ) - Chat or contact id
#. ``team`` (string) - Team id
#. ``uid`` (string) - Call id

.. _tdproto-serverCallBuzzParams:

serverCallBuzzParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``actor`` ( :ref:`tdproto-ContactShort` ) - Short call creator information
#. ``buzz_timeout`` (number) - Number of seconds for stop buzzing
#. ``chat`` ( :ref:`tdproto-ChatShort` ) - Short chat information
#. ``display_name`` (string) - Chat title
#. ``icons`` ( :ref:`tdproto-IconData` ) - Chat icons

    **Might be null**
#. ``jid`` ( :ref:`tdproto-JID` ) - Chat or contact id
#. ``team`` (string) - Deprecated
#. ``teaminfo`` ( :ref:`tdproto-TeamShort` ) - Short team information
#. ``uid`` (string) - Call id

.. _tdproto-ServerCallCheckFingerprint:

ServerCallCheckFingerprint
-------------------------------------------------------------

Experimental function

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverCallCheckFingerprintParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverCallCheckFingerprintParams:

serverCallCheckFingerprintParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``fingerprint`` (string) - DOCUMENTATION MISSING

.. _tdproto-ServerCallLeave:

ServerCallLeave
-------------------------------------------------------------

Participant leave a call

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverCallLeaveParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverCallLeaveParams:

serverCallLeaveParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``jid`` ( :ref:`tdproto-JID` ) - Chat or contact id
#. ``uid`` (string) - Call uid

.. _tdproto-ServerCallMuteall:

ServerCallMuteall
-------------------------------------------------------------

All participants in call muted

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverCallMuteallParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverCallMuteallParams:

serverCallMuteallParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``jid`` ( :ref:`tdproto-JID` ) - Chat or contact id
#. ``muted`` (boolean) - Mute state

.. _tdproto-ServerCallReject:

ServerCallReject
-------------------------------------------------------------

Call rejected

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverCallRejectParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverCallRejectParams:

serverCallRejectParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``jid`` ( :ref:`tdproto-JID` ) - Chat or contact id
#. ``reason`` (string) - Reason, if any
#. ``uid`` (string) - Call id

.. _tdproto-ServerCallRestart:

ServerCallRestart
-------------------------------------------------------------

Call restarted

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverCallRestartParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverCallRestartParams:

serverCallRestartParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``jid`` ( :ref:`tdproto-JID` ) - Chat or contact id
#. ``team`` (string) - Team id
#. ``uid`` (string) - Call id

.. _tdproto-ServerCallSound:

ServerCallSound
-------------------------------------------------------------

Mute/unmute call participant

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-ServerCallSoundParams` ) - DOCUMENTATION MISSING

.. _tdproto-ServerCallSoundParams:

ServerCallSoundParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``jid`` ( :ref:`tdproto-JID` ) - Chat or contact id
#. ``muted`` (boolean) - Mute state

.. _tdproto-ServerCallState:

ServerCallState
-------------------------------------------------------------

Call participant number or parameters changed

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverCallStateParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverCallStateParams:

serverCallStateParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``audiorecord`` (boolean) - Call record enabled
#. ``buzz`` (boolean) - Call buzzing

    **Maybe omitted**
#. ``finish`` (string) - Call finish, if any

    **Might be null**
#. ``jid`` ( :ref:`tdproto-JID` ) - Chat or contact id
#. ``onliners`` ( :ref:`tdproto-CallOnliner` ) - Call participants

    **Maybe omitted**
#. ``start`` (string) - Call start, if any

    **Might be null**
#. ``timestamp`` (number) - Event start. FIXME: why not gentime?
#. ``uid`` (string) - Call id

.. _tdproto-ServerCallTalking:

ServerCallTalking
-------------------------------------------------------------

Someone talks in call

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverCallTalkingParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverCallTalkingParams:

serverCallTalkingParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``actor`` ( :ref:`tdproto-JID` ) - Actor id
#. ``jid`` ( :ref:`tdproto-JID` ) - Chat or contact id
#. ``talking`` (boolean) - Is talking

.. _tdproto-ServerChatComposing:

ServerChatComposing
-------------------------------------------------------------

Someone typing or recording audiomessage in chat

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverChatComposingParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverChatComposingParams:

serverChatComposingParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``actor`` ( :ref:`tdproto-JID` ) - Actor id
#. ``composing`` (boolean) - true = start typing / audio recording, false = stop
#. ``is_audio`` (boolean) - true = audiomessage, false = text typing

    **Maybe omitted**
#. ``jid`` ( :ref:`tdproto-JID` ) - Chat or contact id
#. ``valid_until`` (string) - Composing event max lifetime

    **Maybe omitted**

.. _tdproto-ServerChatDeleted:

ServerChatDeleted
-------------------------------------------------------------

Chat deleted

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverChatDeletedParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverChatDeletedParams:

serverChatDeletedParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``badge`` (number) - Total number of unreads
#. ``chats`` ( :ref:`tdproto-DeletedChat` ) - List of deleted chats
#. ``team_unread`` ( :ref:`tdproto-TeamUnread` ) - Current team counters

    **Might be null**

.. _tdproto-ServerChatDraft:

ServerChatDraft
-------------------------------------------------------------

Changed draft message in chan

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverChatDraftParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverChatDraftParams:

serverChatDraftParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``draft`` (string) - Draft text
#. ``draft_num`` (number) - Draft version. TODO: use gentime instead
#. ``jid`` ( :ref:`tdproto-JID` ) - Chat or contact id

.. _tdproto-ServerChatLastread:

ServerChatLastread
-------------------------------------------------------------

Changed last read message in chat

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverChatLastreadParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverChatLastreadParams:

serverChatLastreadParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``badge`` (number) - Total number of unreads
#. ``chats`` ( :ref:`tdproto-ChatCounters` ) - Chat counters
#. ``team_unread`` ( :ref:`tdproto-TeamUnread` ) - Current team counters

    **Might be null**

.. _tdproto-ServerChatUpdated:

ServerChatUpdated
-------------------------------------------------------------

Chat created or updated

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverChatUpdatedParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverChatUpdatedParams:

serverChatUpdatedParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``badge`` (number) - Total number of unreads
#. ``chats`` ( :ref:`tdproto-Chat` ) - Chat counters
#. ``team_unread`` ( :ref:`tdproto-TeamUnread` ) - Current team counters

    **Might be null**

.. _tdproto-ServerConfirm:

ServerConfirm
-------------------------------------------------------------

Server confirmed client message

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverConfirmParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverConfirmParams:

serverConfirmParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``confirm_id`` (string) - Unique id generated by server

.. _tdproto-ServerContactUpdated:

ServerContactUpdated
-------------------------------------------------------------

Contact created or updated

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverContactUpdatedParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverContactUpdatedParams:

serverContactUpdatedParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``contacts`` ( :ref:`tdproto-Contact` ) - Contact info

.. _tdproto-ServerDebug:

ServerDebug
-------------------------------------------------------------

Debug message

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverDebugParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverDebugParams:

serverDebugParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``text`` (string) - Debug message

.. _tdproto-ServerLogin:

ServerLogin
-------------------------------------------------------------

Login from other device

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverLoginParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverLoginParams:

serverLoginParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``device_name`` (string) - Device name

.. _tdproto-ServerMessagePush:

ServerMessagePush
-------------------------------------------------------------

Push replacement for desktop application

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-MessagePush` ) - DOCUMENTATION MISSING

.. _tdproto-ServerMessageReceived:

ServerMessageReceived
-------------------------------------------------------------

Message received by someone in chat

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverMessageReceivedParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverMessageReceivedParams:

serverMessageReceivedParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``messages`` ( :ref:`tdproto-ReceivedMessage` ) - received message data

.. _tdproto-ServerMessageUpdated:

ServerMessageUpdated
-------------------------------------------------------------

Chat message created, updated or deleted

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverMessageUpdatedParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverMessageUpdatedParams:

serverMessageUpdatedParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``badge`` (number) - Total number of unreads, if changed

    **Might be null**
#. ``chat_counters`` ( :ref:`tdproto-ChatCounters` ) - Chat counters
#. ``delayed`` (boolean) - true = silently message update, false = new message
#. ``messages`` ( :ref:`tdproto-Message` ) - Messages data
#. ``team_unread`` ( :ref:`tdproto-TeamUnread` ) - Current team counters

    **Might be null**

.. _tdproto-ServerOnline:

ServerOnline
-------------------------------------------------------------

Online team members and current active calls

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverOnlineParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverOnlineParams:

serverOnlineParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``calls`` ( :ref:`tdproto-OnlineCall` ) - Active calls

    **Maybe omitted**
#. ``contacts`` ( :ref:`tdproto-OnlineContact` ) - Online team members

.. _tdproto-ServerPanic:

ServerPanic
-------------------------------------------------------------

Critical server error

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverPanicParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverPanicParams:

serverPanicParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``code`` (string) - Error code
#. ``debug`` (string) - Debug message

    **Maybe omitted**

.. _tdproto-ServerProcessing:

ServerProcessing
-------------------------------------------------------------

Status of background operation

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverProcessingParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverProcessingParams:

serverProcessingParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``action`` (string) - Action name
#. ``has_error`` (boolean) - Has error
#. ``message`` (string) - Message
#. ``num`` (number) - Current processing item
#. ``total`` (number) - Total processing items

.. _tdproto-ServerRemindDeleted:

ServerRemindDeleted
-------------------------------------------------------------

Task or group remind deleted

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverRemindDeletedParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverRemindDeletedParams:

serverRemindDeletedParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``reminds`` ( :ref:`tdproto-DeletedRemind` ) - Remind information

.. _tdproto-ServerRemindFired:

ServerRemindFired
-------------------------------------------------------------

Task or group remind fired

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverRemindFiredParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverRemindFiredParams:

serverRemindFiredParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``reminds`` ( :ref:`tdproto-Remind` ) - Remind information

.. _tdproto-ServerRemindUpdated:

ServerRemindUpdated
-------------------------------------------------------------

Task/group remind created or changed

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverRemindUpdatedParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverRemindUpdatedParams:

serverRemindUpdatedParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``reminds`` ( :ref:`tdproto-Remind` ) - Remind information

.. _tdproto-ServerSectionDeleted:

ServerSectionDeleted
-------------------------------------------------------------

Contact section or task project deleted

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverSectionDeletedParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverSectionDeletedParams:

serverSectionDeletedParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``chat_type`` ( :ref:`tdproto-ChatType` ) - Chat type
#. ``gentime`` (number) - Deprecated
#. ``sections`` ( :ref:`tdproto-DeletedSection` ) - Section/project info

.. _tdproto-ServerSectionUpdated:

ServerSectionUpdated
-------------------------------------------------------------

Contact section or task project created or changed

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverSectionUpdatedParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverSectionUpdatedParams:

serverSectionUpdatedParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``chat_type`` ( :ref:`tdproto-ChatType` ) - Chat type
#. ``gentime`` (number) - deprecated
#. ``sections`` ( :ref:`tdproto-Section` ) - Section/project info

.. _tdproto-ServerTagDeleted:

ServerTagDeleted
-------------------------------------------------------------

Tag deleted

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverTagDeletedParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverTagDeletedParams:

serverTagDeletedParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``tags`` ( :ref:`tdproto-DeletedTag` ) - Tags info

.. _tdproto-ServerTagUpdated:

ServerTagUpdated
-------------------------------------------------------------

Tag created or changed

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverTagUpdatedParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverTagUpdatedParams:

serverTagUpdatedParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``tags`` ( :ref:`tdproto-Tag` ) - Tags info

.. _tdproto-ServerTeamCounters:

ServerTeamCounters
-------------------------------------------------------------

Counters form other teams

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverTeamCountersParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverTeamCountersParams:

serverTeamCountersParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``badge`` (number) - Total number of unreads
#. ``teams`` ( :ref:`tdproto-TeamCounter` ) - Counters

.. _tdproto-ServerTeamDeleted:

ServerTeamDeleted
-------------------------------------------------------------

Team archived

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverTeamDeletedParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverTeamDeletedParams:

serverTeamDeletedParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``teams`` ( :ref:`tdproto-DeletedTeam` ) - Teams info

.. _tdproto-ServerTeamUpdated:

ServerTeamUpdated
-------------------------------------------------------------

Team created or changed

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverTeamUpdatedParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverTeamUpdatedParams:

serverTeamUpdatedParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``teams`` ( :ref:`tdproto-Team` ) - DOCUMENTATION MISSING

.. _tdproto-ServerTime:

ServerTime
-------------------------------------------------------------

Current server time

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverTimeParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverTimeParams:

serverTimeParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``time`` (string) - Current time

.. _tdproto-ServerUiSettings:

ServerUiSettings
-------------------------------------------------------------

Part of UI settings changed

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-UiSettings` ) - DOCUMENTATION MISSING

    **Might be null**

.. _tdproto-ServerUploadUpdated:

ServerUploadUpdated
-------------------------------------------------------------

Upload object created or changed

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverUploadUpdatedParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverUploadUpdatedParams:

serverUploadUpdatedParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``uploads`` ( :ref:`tdproto-Upload` ) - Uploads data

.. _tdproto-ServerWarning:

ServerWarning
-------------------------------------------------------------

Something went wrong with client message

**Fields**:

#. ``confirm_id`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``event`` (string) - DOCUMENTATION MISSING
#. ``params`` ( :ref:`tdproto-serverWarningParams` ) - DOCUMENTATION MISSING

.. _tdproto-serverWarningParams:

serverWarningParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``message`` (string) - Message
#. ``orig`` (any) - Debug information

.. _tdproto-Session:

Session
-------------------------------------------------------------

Websocket session

**Fields**:

#. ``addr`` (string) - IP address

    **Maybe omitted**
#. ``afk`` (boolean) - Away from keyboard

    **Maybe omitted**
#. ``created`` (string) - Creation datetime
#. ``is_mobile`` (boolean) - Mobile

    **Maybe omitted**
#. ``lang`` (string) - Language code

    **Maybe omitted**
#. ``team`` (string) - Team id

    **Maybe omitted**
#. ``uid`` (string) - Session id
#. ``useragent`` (string) - User agent

    **Maybe omitted**

.. _tdproto-ShortMessage:

ShortMessage
-------------------------------------------------------------

Short message based on chat message

**Fields**:

#. ``chat`` ( :ref:`tdproto-JID` ) - Chat id
#. ``chat_type`` ( :ref:`tdproto-ChatType` ) - Chat type
#. ``created`` (string) - Message creation datetime (set by server side) or sending datetime in future for draft messages
#. ``from`` ( :ref:`tdproto-JID` ) - Sender contact id
#. ``gentime`` (number) - Object version
#. ``is_archive`` (boolean) - This message is archive. True or null

    **Maybe omitted**
#. ``message_id`` (string) - Message uid
#. ``to`` ( :ref:`tdproto-JID` ) - Recipient id (group, task or contact)

.. _tdproto-SingleIcon:

SingleIcon
-------------------------------------------------------------

Small or large icon

**Fields**:

#. ``height`` (number) - Icon height, in pixels
#. ``url`` (string) - absolute url to icon
#. ``width`` (number) - Icon width, in pixels

.. _tdproto-Sticker:

Sticker
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``icon100`` (string) - DOCUMENTATION MISSING
#. ``icon128`` (string) - DOCUMENTATION MISSING
#. ``icon200`` (string) - DOCUMENTATION MISSING
#. ``icon64`` (string) - DOCUMENTATION MISSING
#. ``message_content`` ( :ref:`tdproto-MessageContent` ) - DOCUMENTATION MISSING
#. ``uid`` (string) - DOCUMENTATION MISSING

.. _tdproto-Stickerpack:

Stickerpack
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``author`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``author_link`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``name`` (string) - DOCUMENTATION MISSING
#. ``stickers`` ( :ref:`tdproto-Sticker` ) - DOCUMENTATION MISSING
#. ``title`` (string) - DOCUMENTATION MISSING
#. ``uid`` (string) - DOCUMENTATION MISSING

.. _tdproto-Subtask:

Subtask
-------------------------------------------------------------

Link to sub/sup task

**Fields**:

#. ``assignee`` ( :ref:`tdproto-JID` ) - Assignee contact id. Tasks only
#. ``display_name`` (string) - Title
#. ``jid`` ( :ref:`tdproto-JID` ) - Task id
#. ``num`` (number) - Task number in this team
#. ``public`` (boolean) - Can other team member see this task/group chat

    **Maybe omitted**
#. ``title`` (string) - Task title. Generated from number and description

.. _tdproto-SwitcherColors:

SwitcherColors
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``off`` (string) - DOCUMENTATION MISSING
#. ``on`` (string) - DOCUMENTATION MISSING

.. _tdproto-Tag:

Tag
-------------------------------------------------------------

Task tag

**Fields**:

#. ``name`` (string) - Tag name
#. ``uid`` (string) - Tag id

.. _tdproto-TaskColor:

TaskColor
-------------------------------------------------------------

Task color rules color

**Fields**:

#. ``dark`` (string) - DOCUMENTATION MISSING
#. ``light`` (string) - DOCUMENTATION MISSING
#. ``regular`` (string) - DOCUMENTATION MISSING

.. _tdproto-TaskCounters:

TaskCounters
-------------------------------------------------------------

Tasks counters

**Fields**:

#. ``jid`` ( :ref:`tdproto-JID` ) - Task jid
#. ``num_unread_notices`` (number) - Mentions (@) counter

    **Maybe omitted**
#. ``num_unread`` (number) - Unreads counter

    **Maybe omitted**

.. _tdproto-TaskFilter:

TaskFilter
-------------------------------------------------------------

Task filter

**Fields**:

#. ``field`` ( :ref:`tdproto-TaskFilterKey` ) - Task filter field
#. ``title`` (string) - Filter title

.. _tdproto-TaskItem:

TaskItem
-------------------------------------------------------------

Task checklist item

**Fields**:

#. ``can_toggle`` (boolean) - Can I toggle this item

    **Maybe omitted**
#. ``checked`` (boolean) - Item checked

    **Maybe omitted**
#. ``sort_ordering`` (number) - Sort ordering

    **Maybe omitted**
#. ``subtask`` ( :ref:`tdproto-Subtask` ) - Link to subtask. Optional

    **Maybe omitted**

    **Might be null**
#. ``text`` (string) - Text or "#{OtherTaskNumber}"
#. ``uid`` (string) - Id

    **Maybe omitted**

.. _tdproto-TaskItems:

TaskItems
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``checked`` (boolean) - DOCUMENTATION MISSING
#. ``name`` (string) - DOCUMENTATION MISSING

.. _tdproto-TaskPreview:

TaskPreview
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``_error`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``assignee`` ( :ref:`tdproto-JID` ) - DOCUMENTATION MISSING
#. ``deadline`` (string) - DOCUMENTATION MISSING

    **Might be null**
#. ``description`` (string) - DOCUMENTATION MISSING
#. ``items`` ( :ref:`tdproto-TaskItems` ) - DOCUMENTATION MISSING
#. ``public`` (boolean) - DOCUMENTATION MISSING
#. ``section`` (string) - DOCUMENTATION MISSING
#. ``tags`` (string) - DOCUMENTATION MISSING

.. _tdproto-TaskSort:

TaskSort
-------------------------------------------------------------

Task sort type

**Fields**:

#. ``key`` ( :ref:`tdproto-TaskSortKey` ) - Field
#. ``title`` (string) - Sort title

.. _tdproto-TaskStatus:

TaskStatus
-------------------------------------------------------------

Custom task status

**Fields**:

#. ``is_archive`` (boolean) - Status not used anymore

    **Maybe omitted**
#. ``name`` (string) - Status internal name
#. ``sort_ordering`` (number) - Status sort ordering
#. ``title`` (string) - Status localized name
#. ``uid`` (string) - Status id

    **Maybe omitted**

.. _tdproto-TaskTab:

TaskTab
-------------------------------------------------------------

Task tab

**Fields**:

#. ``filters`` ( :ref:`tdproto-TaskFilter` ) - Filters inside tab
#. ``hide_empty`` (boolean) - Disable this tab when it has no contents
#. ``key`` ( :ref:`tdproto-TaskTabKey` ) - Tab name
#. ``pagination`` (boolean) - Enable pagination
#. ``show_counter`` (boolean) - Show unread badge
#. ``sort`` ( :ref:`tdproto-TaskSort` ) - Sort available in tab
#. ``title`` (string) - Tab title
#. ``unread_tasks`` ( :ref:`tdproto-TaskCounters` ) - Unread tasks with jid and counters

.. _tdproto-Team:

Team
-------------------------------------------------------------

Team

**Fields**:

#. ``bad_profile`` (boolean) - My profile in this team isn't full

    **Maybe omitted**
#. ``changeable_statuses`` ( :ref:`tdproto-TeamStatus` ) - What status I can set to other team members

    **Maybe omitted**
#. ``contacts`` ( :ref:`tdproto-Contact` ) - Team contacts. Used only for team creation

    **Maybe omitted**
#. ``default_task_deadline`` (string) - Default task deadline

    **Maybe omitted**
#. ``display_family_name_first`` (boolean) - Family name should be first in display name

    **Maybe omitted**
#. ``gentime`` (number) - Object version
#. ``hide_archived_users`` (boolean) - Don't show archived users by default

    **Maybe omitted**
#. ``icons`` ( :ref:`tdproto-IconData` ) - Team icons
#. ``is_archive`` (boolean) - Team deleted

    **Maybe omitted**
#. ``last_active`` (boolean) - User last activity was in this team
#. ``max_message_update_age`` (number) - Max message update/deletion age, in seconds
#. ``me`` ( :ref:`tdproto-Contact` ) - My profile in this team
#. ``name`` (string) - Team name
#. ``need_confirmation`` (boolean) - Need confirmation after invite to this team
#. ``single_group`` ( :ref:`tdproto-JID` ) - For single group teams, jid of chat

    **Maybe omitted**
#. ``task_importance_rev`` (boolean) - Bigger number = bigger importance. Default: lower number = bigger importance

    **Maybe omitted**
#. ``task_importance_min`` (number) - Minimal value of task importance. Default is 1

    **Maybe omitted**
#. ``task_importance_max`` (number) - Maximum value of task importance. Default is 5

    **Maybe omitted**
#. ``theme`` ( :ref:`tdproto-Theme` ) - Color theme, if any

    **Maybe omitted**

    **Might be null**
#. ``uid`` (string) - Team id
#. ``unread`` ( :ref:`tdproto-TeamUnread` ) - Unread message counters

    **Might be null**
#. ``uploads_size`` (number) - Total uploads size, bytes

    **Maybe omitted**
#. ``uploads_size_limit`` (number) - Maximum uploads size, bytes, if any

    **Maybe omitted**
#. ``use_task_urgency`` (boolean) - Use urgency field in task

    **Maybe omitted**
#. ``use_task_spent_time`` (boolean) - Use spent time field in task

    **Maybe omitted**
#. ``use_task_importance`` (boolean) - Use importance field in task

    **Maybe omitted**
#. ``use_task_complexity`` (boolean) - Use complexity field in task

    **Maybe omitted**
#. ``use_patronymic`` (boolean) - Patronymic in usernames for this team

    **Maybe omitted**
#. ``user_fields`` (string) - Username fields ordering

.. _tdproto-TeamCounter:

TeamCounter
-------------------------------------------------------------

Unread message counters

**Fields**:

#. ``uid`` (string) - Team id
#. ``unread`` ( :ref:`tdproto-TeamUnread` ) - Unread message counters

.. _tdproto-TeamShort:

TeamShort
-------------------------------------------------------------

Short team representation. For invites, push notifications, etc. Readonly

**Fields**:

#. ``icons`` ( :ref:`tdproto-IconData` ) - Team icons
#. ``name`` (string) - Team name
#. ``uid`` (string) - Team id

.. _tdproto-Terms:

Terms
-------------------------------------------------------------

Experimental translation fields for "team" entity renaming. Readonly

**Fields**:

#. ``EnInTeam`` (string) - DOCUMENTATION MISSING
#. ``EnTeam`` (string) - DOCUMENTATION MISSING
#. ``EnTeamAccess`` (string) - DOCUMENTATION MISSING
#. ``EnTeamAdmin`` (string) - DOCUMENTATION MISSING
#. ``EnTeamAdmins`` (string) - DOCUMENTATION MISSING
#. ``EnTeamGuest`` (string) - DOCUMENTATION MISSING
#. ``EnTeamMember`` (string) - DOCUMENTATION MISSING
#. ``EnTeamMembers`` (string) - DOCUMENTATION MISSING
#. ``EnTeamOwner`` (string) - DOCUMENTATION MISSING
#. ``EnTeams`` (string) - DOCUMENTATION MISSING
#. ``EnTeamSettings`` (string) - DOCUMENTATION MISSING
#. ``EnToTeam`` (string) - DOCUMENTATION MISSING
#. ``RuInTeam`` (string) - DOCUMENTATION MISSING
#. ``RuTeam`` (string) - DOCUMENTATION MISSING
#. ``RuTeamAccess`` (string) - DOCUMENTATION MISSING
#. ``RuTeamAdmin`` (string) - DOCUMENTATION MISSING
#. ``RuTeamAdmins`` (string) - DOCUMENTATION MISSING
#. ``RuTeamD`` (string) - DOCUMENTATION MISSING
#. ``RuTeamGuest`` (string) - DOCUMENTATION MISSING
#. ``RuTeamMember`` (string) - DOCUMENTATION MISSING
#. ``RuTeamMembers`` (string) - DOCUMENTATION MISSING
#. ``RuTeamOwner`` (string) - DOCUMENTATION MISSING
#. ``RuTeamP`` (string) - DOCUMENTATION MISSING
#. ``RuTeamR`` (string) - DOCUMENTATION MISSING
#. ``RuTeams`` (string) - DOCUMENTATION MISSING
#. ``RuTeamsD`` (string) - DOCUMENTATION MISSING
#. ``RuTeamSettings`` (string) - DOCUMENTATION MISSING
#. ``RuTeamsP`` (string) - DOCUMENTATION MISSING
#. ``RuTeamsR`` (string) - DOCUMENTATION MISSING
#. ``RuTeamsT`` (string) - DOCUMENTATION MISSING
#. ``RuTeamsV`` (string) - DOCUMENTATION MISSING
#. ``RuTeamT`` (string) - DOCUMENTATION MISSING
#. ``RuTeamV`` (string) - DOCUMENTATION MISSING
#. ``RuToTeam`` (string) - DOCUMENTATION MISSING

.. _tdproto-Theme:

Theme
-------------------------------------------------------------

Color theme

**Fields**:

#. ``AccentColor`` (string) - DOCUMENTATION MISSING
#. ``AccentHoverColor`` (string) - DOCUMENTATION MISSING
#. ``AppAccentColor`` (string) - Deprecated
#. ``AppPrimaryColor`` (string) - Deprecated
#. ``attention`` (string) - DOCUMENTATION MISSING
#. ``attention_light`` (string) - DOCUMENTATION MISSING
#. ``back`` (string) - DOCUMENTATION MISSING
#. ``back_light`` (string) - DOCUMENTATION MISSING
#. ``back_dark`` (string) - DOCUMENTATION MISSING
#. ``background`` (string) - DOCUMENTATION MISSING
#. ``BgColor`` (string) - Web colors
#. ``BgHoverColor`` (string) - DOCUMENTATION MISSING
#. ``brand`` (string) - App colors
#. ``brand_light`` (string) - DOCUMENTATION MISSING
#. ``brand_dark`` (string) - DOCUMENTATION MISSING
#. ``button`` ( :ref:`tdproto-ButtonColors` ) - DOCUMENTATION MISSING

    **Might be null**
#. ``chat_input_background`` (string) - DOCUMENTATION MISSING
#. ``error`` (string) - DOCUMENTATION MISSING
#. ``error_light`` (string) - DOCUMENTATION MISSING
#. ``font`` ( :ref:`tdproto-FontColors` ) - DOCUMENTATION MISSING

    **Might be null**
#. ``ic`` ( :ref:`tdproto-IconColors` ) - DOCUMENTATION MISSING

    **Might be null**
#. ``input`` ( :ref:`tdproto-InputColors` ) - DOCUMENTATION MISSING

    **Might be null**
#. ``MainAccent`` (string) - DOCUMENTATION MISSING
#. ``MainAccentHover`` (string) - DOCUMENTATION MISSING
#. ``MainLightAccent`` (string) - DOCUMENTATION MISSING
#. ``MainLink`` (string) - DOCUMENTATION MISSING
#. ``message`` ( :ref:`tdproto-MessageColors` ) - DOCUMENTATION MISSING

    **Might be null**
#. ``modal_background`` (string) - DOCUMENTATION MISSING
#. ``MutedTextColor`` (string) - DOCUMENTATION MISSING
#. ``substrate_background`` (string) - DOCUMENTATION MISSING
#. ``success`` (string) - DOCUMENTATION MISSING
#. ``success_light`` (string) - DOCUMENTATION MISSING
#. ``switcher`` ( :ref:`tdproto-SwitcherColors` ) - DOCUMENTATION MISSING

    **Might be null**
#. ``tab_background`` (string) - DOCUMENTATION MISSING
#. ``TextColor`` (string) - DOCUMENTATION MISSING
#. ``TextOnAccentHoverColor`` (string) - DOCUMENTATION MISSING
#. ``title_background`` (string) - DOCUMENTATION MISSING

.. _tdproto-Unread:

Unread
-------------------------------------------------------------

Unread message counters

**Fields**:

#. ``notice_messages`` (number) - Total unread messages with mentions
#. ``messages`` (number) - Total unread messages
#. ``chats`` (number) - Total chats with unread messages

.. _tdproto-Upload:

Upload
-------------------------------------------------------------

Uploaded media

**Fields**:

#. ``animated`` (boolean) - Is animated (images only)

    **Maybe omitted**
#. ``blurhash`` (string) - Compact representation of a placeholder for an image (images only)

    **Maybe omitted**
#. ``content_type`` (string) - Content type
#. ``created`` (string) - Uploaded at
#. ``duration`` (number) - Mediafile duration (for audio/video only)

    **Maybe omitted**
#. ``type`` ( :ref:`tdproto-UploadMediaType` ) - ?type=file,image,audio,video
#. ``name`` (string) - Filename
#. ``pdf_version`` ( :ref:`tdproto-PdfVersion` ) - PDF version of file. Experimental

    **Maybe omitted**

    **Might be null**
#. ``preview`` ( :ref:`tdproto-UploadPreview` ) - Preview details

    **Maybe omitted**

    **Might be null**
#. ``processing`` (boolean) - File still processing (video only)

    **Maybe omitted**
#. ``size`` (number) - Upload size in bytes
#. ``uid`` (string) - Upload id
#. ``url`` (string) - Absolute url

.. _tdproto-UploadPreview:

UploadPreview
-------------------------------------------------------------

Upload preview

**Fields**:

#. ``height`` (number) - Height in pixels
#. ``url`` (string) - Absolute url to image
#. ``url_2x`` (string) - Absolute url to high resolution image (retina)
#. ``width`` (number) - Width in pixels

.. _tdproto-UploadShortMessage:

UploadShortMessage
-------------------------------------------------------------

Upload + ShortMessage

**Fields**:

#. ``message`` ( :ref:`tdproto-ShortMessage` ) - DOCUMENTATION MISSING
#. ``upload`` ( :ref:`tdproto-Upload` ) - DOCUMENTATION MISSING

.. _tdproto-User:

User
-------------------------------------------------------------

Account data

**Fields**:

#. ``alt_send`` (boolean) - Use Ctrl/Cmd + Enter instead Enter
#. ``always_send_pushes`` (boolean) - Send pushes even user is online
#. ``asterisk_mention`` (boolean) - Use * as @ for mentions
#. ``default_lang`` (string) - Default language code

    **Maybe omitted**
#. ``email`` (string) - Email for login

    **Maybe omitted**
#. ``family_name`` (string) - Family name

    **Maybe omitted**
#. ``given_name`` (string) - Given name

    **Maybe omitted**
#. ``munread_first`` (boolean) - Show unread chats in chat list first on mobiles
#. ``patronymic`` (string) - Patronymic, if any

    **Maybe omitted**
#. ``phone`` (string) - Phone for login

    **Maybe omitted**
#. ``quiet_time_start`` (string) - Start silently time (no pushes, no sounds)

    **Might be null**
#. ``quiet_time_finish`` (string) - Finish silently time (no pushes, no sounds)

    **Might be null**
#. ``timezone`` (string) - Timezone
#. ``unread_first`` (boolean) - Show unread chats in chat list first

.. _tdproto-UserAuth:

UserAuth
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

#. ``_age`` (number) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``addr`` (string) - ip address

    **Maybe omitted**
#. ``country`` (string) - name of country

    **Maybe omitted**
#. ``created`` (string) - DOCUMENTATION MISSING
#. ``device`` ( :ref:`tdproto-PushDevice` ) - info about device (struct)

    **Maybe omitted**

    **Might be null**
#. ``kind`` (string) - type of auth
#. ``last_access`` (string) - DOCUMENTATION MISSING

    **Maybe omitted**
#. ``region`` (string) - name of region

    **Maybe omitted**
#. ``uid`` (string) - DOCUMENTATION MISSING
#. ``user_agent`` (string) - info about useragent

    **Maybe omitted**

.. _tdproto-UserWithMe:

UserWithMe
-------------------------------------------------------------

Accouint data with extra information

**Fields**:

#. ``alt_send`` (boolean) - Use Ctrl/Cmd + Enter instead Enter
#. ``always_send_pushes`` (boolean) - Send pushes even user is online
#. ``asterisk_mention`` (boolean) - Use * as @ for mentions
#. ``default_lang`` (string) - Default language code

    **Maybe omitted**
#. ``devices`` ( :ref:`tdproto-PushDevice` ) - Registered push devices
#. ``email`` (string) - Email for login

    **Maybe omitted**
#. ``family_name`` (string) - Family name

    **Maybe omitted**
#. ``given_name`` (string) - Given name

    **Maybe omitted**
#. ``inviter`` ( :ref:`tdproto-JID` ) - Inviter id, if any

    **Maybe omitted**
#. ``munread_first`` (boolean) - Show unread chats in chat list first on mobiles
#. ``patronymic`` (string) - Patronymic, if any

    **Maybe omitted**
#. ``phone`` (string) - Phone for login

    **Maybe omitted**
#. ``quiet_time_start`` (string) - Start silently time (no pushes, no sounds)

    **Might be null**
#. ``quiet_time_finish`` (string) - Finish silently time (no pushes, no sounds)

    **Might be null**
#. ``teams`` ( :ref:`tdproto-Team` ) - Available teams
#. ``timezone`` (string) - Timezone
#. ``unread_first`` (boolean) - Show unread chats in chat list first

.. _tdproto-Wallpaper:

Wallpaper
-------------------------------------------------------------

Chat wallpaper

**Fields**:

#. ``key`` (string) - Unique identifier
#. ``name`` (string) - Localized description
#. ``url`` (string) - Url to jpg or png

.. _tdproto-WikiPage:

WikiPage
-------------------------------------------------------------

Wiki page. Experimental

**Fields**:

#. ``editor`` ( :ref:`tdproto-JID` ) - Last editor contact id
#. ``gentime`` (number) - Object version
#. ``text`` (string) - Page text
#. ``updated`` (string) - Update time
