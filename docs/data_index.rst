Enums index
============================

.. _tdproto-ChatType:

ChatType enum
-------------------------------------------------------------
**Possible values**:

* direct
* group
* task


.. _tdproto-GroupStatus:

GroupStatus enum
-------------------------------------------------------------
**Possible values**:

* admin
* member


.. _tdproto-MarkupType:

MarkupType enum
-------------------------------------------------------------
**Possible values**:

* bold
* italic
* underscore
* strike
* code
* codeblock
* quote
* link
* time
* unsafe


.. _tdproto-Mediasubtype:

Mediasubtype enum
-------------------------------------------------------------
**Possible values**:

* sticker
* newtask


.. _tdproto-Mediatype:

Mediatype enum
-------------------------------------------------------------
**Possible values**:

* plain
* change
* deleted
* file
* image
* video
* audiomsg
* contact
* pdf


.. _tdproto-TeamStatus:

TeamStatus enum
-------------------------------------------------------------
**Possible values**:

* owner
* admin
* member
* guest


.. _tdproto-UploadMediaType:

UploadMediaType enum
-------------------------------------------------------------
**Possible values**:

* file
* image
* video
* audio
* imagefile

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

* ``day`` (string) - DOCUMENTATION MISSING
* ``user_id`` (number) - DOCUMENTATION MISSING
* ``family_name`` (string) - DOCUMENTATION MISSING. Maybe omitted. Might be null
* ``given_name`` (string) - DOCUMENTATION MISSING. Maybe omitted. Might be null
* ``patronymic`` (string) - DOCUMENTATION MISSING. Maybe omitted. Might be null
* ``phone`` (string) - DOCUMENTATION MISSING. Maybe omitted. Might be null
* ``messages_count`` (number) - DOCUMENTATION MISSING. Maybe omitted. Might be null
* ``calls_count`` (number) - DOCUMENTATION MISSING. Maybe omitted. Might be null
* ``call_seconds_total`` (number) - DOCUMENTATION MISSING. Maybe omitted. Might be null

.. _tdproto-ButtonColors:

ButtonColors
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``brand_static`` (string) - DOCUMENTATION MISSING
* ``brand_active`` (string) - DOCUMENTATION MISSING
* ``brand_disable`` (string) - DOCUMENTATION MISSING
* ``simple_static`` (string) - DOCUMENTATION MISSING
* ``simple_active`` (string) - DOCUMENTATION MISSING
* ``simple_disable`` (string) - DOCUMENTATION MISSING

.. _tdproto-CallDevice:

CallDevice
-------------------------------------------------------------

Call participant device

**Fields**:

* ``muted`` (boolean) - Device muted
* ``useragent`` (string) - Device description

.. _tdproto-CallEvent:

CallEvent
-------------------------------------------------------------

Audio call information

**Fields**:

* ``start`` (string) - Call start. Might be null
* ``finish`` (string) - Call finish. Might be null
* ``audiorecord`` (boolean) - Call record enabled
* ``onliners`` ( :ref:`tdproto-CallOnliner` ) - Call participants. Maybe omitted

.. _tdproto-CallOnliner:

CallOnliner
-------------------------------------------------------------

Call participant

**Fields**:

* ``jid`` ( :ref:`tdproto-JID` ) - Contact id
* ``display_name`` (string) - Contact name
* ``role`` (string) - Contact role
* ``icon`` (string) - Contact icon
* ``muted`` (boolean) - Microphone muted. Computed from devices muted states
* ``devices`` ( :ref:`tdproto-CallDevice` ) - Member devices, strictly one for now

.. _tdproto-Chat:

Chat
-------------------------------------------------------------

Chat (direct, group, task) representation

**Fields**:

* ``jid`` ( :ref:`tdproto-JID` ) - Group/Task/Contact id
* ``chat_type`` ( :ref:`tdproto-ChatType` ) - Chat type
* ``base_gentime`` (number) - Base fields (not related to concrete participant) version. Maybe omitted
* ``gentime`` (number) - Chat fields related to concrete participant) version
* ``created`` (string) - Creation date, iso datetime
* ``display_name`` (string) - Title
* ``icons`` ( :ref:`tdproto-IconData` ) - Icons info. Might be null
* ``counters_enabled`` (boolean) - Include unread messages to counters. Maybe omitted
* ``can_call`` (boolean) - Can I call to this chat. Maybe omitted
* ``can_send_message`` (boolean) - Can I send message to this chat. Maybe omitted
* ``cant_send_message_reason`` (string) - Why I can't send message to this chat (if can't). Maybe omitted
* ``collapsed`` (boolean) - Description collapsed. Used for tasks only. Maybe omitted
* ``draft`` (string) - Last message draft, if any. Maybe omitted
* ``draft_num`` (number) - Last message draft version , if any. Maybe omitted
* ``hidden`` (boolean) - Hidden chat. Maybe omitted
* ``notifications_enabled`` (boolean) - Push notifications enabled. Maybe omitted
* ``num_importants`` (number) - Number of important messages. Maybe omitted
* ``num_unread`` (number) - Unread counter. Maybe omitted
* ``num_unread_notices`` (number) - Mentions (@) counter. Maybe omitted
* ``last_message`` ( :ref:`tdproto-Message` ) - Last message object. Maybe omitted. Might be null
* ``last_read_message_id`` (string) - Last read message id, if any. Maybe omitted
* ``section`` (string) - Project / section id, if any. Maybe omitted
* ``changeable_fields`` (string) - List of editable fields. Maybe omitted
* ``pinned`` (boolean) - Is chat pinned on top. Maybe omitted
* ``pinned_sort_ordering`` (number) - Sort ordering for pinned chat. Maybe omitted
* ``num_members`` (number) - Non-archive participants number. Maybe omitted. Might be null
* ``can_delete`` (boolean) - Can I delete this chat. Maybe omitted
* ``description`` (string) - Group or task description. Maybe omitted
* ``markup`` ( :ref:`tdproto-MarkupEntity` ) - Markup entities for description field. Experimental. Maybe omitted
* ``feed`` (boolean) - Present in feed (main screen). Maybe omitted
* ``pinned_message`` ( :ref:`tdproto-Message` ) - Pinned message for this chat. Maybe omitted. Might be null
* ``color_index`` (number) - Custom color index from table of colors. Tasks only. Maybe omitted. Might be null
* ``num_items`` (number) - Items in checklist. Tasks only. Maybe omitted. Might be null
* ``num_checked_items`` (number) - Checked items in checklist. Tasks only. Maybe omitted. Might be null
* ``assignee`` ( :ref:`tdproto-JID` ) - Assignee contact id. Tasks only. Maybe omitted
* ``num`` (number) - Task number in this team. Maybe omitted
* ``observers`` ( :ref:`tdproto-JID` ) - Task followers id's. TODO: rename to "followers". Maybe omitted
* ``owner`` ( :ref:`tdproto-JID` ) - Task creator. Maybe omitted
* ``task_status`` (string) - Task status. May be custom. Maybe omitted
* ``title`` (string) - Task title. Generated from number and description. Maybe omitted
* ``done`` (string) - Task done date in iso format, if any. Maybe omitted
* ``done_reason`` (string) - Task done reason, if any. Maybe omitted
* ``deadline`` (string) - Task deadline in iso format, if any. Maybe omitted
* ``deadline_expired`` (boolean) - Is task deadline expired. Maybe omitted
* ``links`` ( :ref:`tdproto-MessageLinks` ) - Links in description. Maybe omitted
* ``tags`` (string) - Task tags list, if any. Maybe omitted
* ``importance`` (number) - Task importance, if available in team. Maybe omitted. Might be null
* ``urgency`` (number) - Task urgency, if available in team. Maybe omitted. Might be null
* ``spent_time`` (number) - Task spent time, number. Maybe omitted. Might be null
* ``complexity`` (number) - Task complexity, number. Maybe omitted. Might be null
* ``linked_messages`` (any) - Used for "Create task from messages...". Maybe omitted
* ``uploads`` ( :ref:`tdproto-Upload` ) - Upload uids for request, upload objects for response. Maybe omitted
* ``items`` ( :ref:`tdproto-TaskItem` ) - Checklist items. Task only. Maybe omitted
* ``parents`` ( :ref:`tdproto-Subtask` ) - Parent tasks. Maybe omitted
* ``tabs`` ( :ref:`tdproto-TaskTabKey` ) - Tab names. Maybe omitted
* ``status`` ( :ref:`tdproto-GroupStatus` ) - My status in group chat. Maybe omitted. Might be null
* ``members`` ( :ref:`tdproto-GroupMembership` ) - Group chat members. Maybe omitted
* ``can_add_member`` (boolean) - Can I add member to this group chat. Maybe omitted
* ``can_remove_member`` (boolean) - Can I remove member from this group chat. Maybe omitted
* ``can_change_member_status`` (boolean) - Can I change member status in this group chat. Maybe omitted
* ``can_change_settings`` (boolean) - deprecated: use changeable fields. Maybe omitted
* ``default_for_all`` (boolean) - Any new team member will be added to this group chat. Maybe omitted
* ``readonly_for_members`` (boolean) - Readonly for non-admins group chat (Like Channels in Telegram bug switchable). Maybe omitted
* ``autocleanup_age`` (number) - Delete messages in this chat in seconds. Experimental function. Maybe omitted. Might be null
* ``public`` (boolean) - Can other team member see this task/group chat. Maybe omitted
* ``can_join`` (boolean) - Can I join to this public group/task. Maybe omitted
* ``can_delete_any_message`` (boolean) - Can I delete any message in this chat. Maybe omitted
* ``can_set_important_any_message`` (boolean) - Can I change Important flag in any message in this chat. Maybe omitted
* ``last_activity`` (string) - Date of the last message sent even if it was deleted. Maybe omitted

.. _tdproto-ChatCounters:

ChatCounters
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``jid`` ( :ref:`tdproto-JID` ) - DOCUMENTATION MISSING
* ``chat_type`` ( :ref:`tdproto-ChatType` ) - DOCUMENTATION MISSING
* ``gentime`` (number) - DOCUMENTATION MISSING
* ``num_unread`` (number) - DOCUMENTATION MISSING
* ``num_unread_notices`` (number) - DOCUMENTATION MISSING
* ``last_read_message_id`` (string) - DOCUMENTATION MISSING. Might be null
* ``last_activity`` (string) - DOCUMENTATION MISSING. Maybe omitted

.. _tdproto-ChatMessages:

ChatMessages
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``messages`` ( :ref:`tdproto-Message` ) - DOCUMENTATION MISSING

.. _tdproto-ChatShort:

ChatShort
-------------------------------------------------------------

Minimal chat representation

**Fields**:

* ``jid`` ( :ref:`tdproto-JID` ) - Group/Task/Contact id
* ``chat_type`` ( :ref:`tdproto-ChatType` ) - Chat type
* ``display_name`` (string) - Title
* ``icons`` ( :ref:`tdproto-IconData` ) - Icon data. Might be null

.. _tdproto-ClientMessageUpdatedParams:

ClientMessageUpdatedParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``to`` ( :ref:`tdproto-JID` ) - Chat, task or contact jid. Required
* ``content`` ( :ref:`tdproto-MessageContent` ) - Message content. Required
* ``message_id`` (string) - Uid created by client. Recommended. Maybe omitted
* ``reply_to`` (string) - Replied to message id. Not required. Maybe omitted
* ``linked_messages`` (string) - Forwarded messages (previously was for reply too). Not required. Maybe omitted
* ``important`` (boolean) - Important flag. Not required. Default: false. Maybe omitted
* ``nopreview`` (boolean) - Disable links preview generation. Not required. Default: false. Maybe omitted
* ``uploads`` (string) - Message attachments. Maybe omitted
* ``old_style_attachment`` (boolean) - Backward compatibility mode. Maybe omitted
* ``comment`` (string) - Deprecated. Maybe omitted

.. _tdproto-ColorRule:

ColorRule
-------------------------------------------------------------

Set of rules to apply to tasks for coloring

**Fields**:

* ``uid`` (string) - DOCUMENTATION MISSING
* ``priority`` (number) - DOCUMENTATION MISSING
* ``color_index`` (number) - DOCUMENTATION MISSING
* ``section`` (string) - DOCUMENTATION MISSING. Maybe omitted
* ``tags`` (string) - DOCUMENTATION MISSING. Maybe omitted
* ``description`` (string) - DOCUMENTATION MISSING. Maybe omitted
* ``task_status`` (string) - DOCUMENTATION MISSING. Maybe omitted
* ``task_importance`` (number) - DOCUMENTATION MISSING. Maybe omitted. Might be null
* ``task_urgency`` (number) - DOCUMENTATION MISSING. Maybe omitted. Might be null
* ``section_enabled`` (boolean) - DOCUMENTATION MISSING. Maybe omitted. Might be null
* ``task_importance_enabled`` (boolean) - DOCUMENTATION MISSING. Maybe omitted. Might be null
* ``task_urgency_enabled`` (boolean) - DOCUMENTATION MISSING. Maybe omitted. Might be null
* ``tags_enabled`` (boolean) - DOCUMENTATION MISSING. Maybe omitted. Might be null

.. _tdproto-Contact:

Contact
-------------------------------------------------------------

Contact

**Fields**:

* ``jid`` ( :ref:`tdproto-JID` ) - Contact Id
* ``display_name`` (string) - Full name in chats
* ``short_name`` (string) - Short name in chats
* ``contact_email`` (string) - Contact email in this team
* ``contact_phone`` (string) - Contact phone in this team
* ``icons`` ( :ref:`tdproto-IconData` ) - Icons data. Might be null
* ``role`` (string) - Role in this team
* ``mood`` (string) - Mood in this team. Maybe omitted
* ``status`` ( :ref:`tdproto-TeamStatus` ) - Status in this team
* ``last_activity`` (string) - Last activity in this team (iso datetime). Maybe omitted
* ``add_to_team_rights`` (boolean) - Can contact add users to this team. Maybe omitted
* ``is_archive`` (boolean) - Contact deleted. Maybe omitted
* ``botname`` (string) - Bot name. Empty for users. Maybe omitted
* ``sections`` (string) - Section ids
* ``can_send_message`` (boolean) - Can I send message to this contact. Maybe omitted
* ``cant_send_message_reason`` (string) - Why I can't send message to this chat (if can't). Maybe omitted
* ``can_call`` (boolean) - Can I call to this contact. Maybe omitted
* ``can_create_task`` (boolean) - Can I call create task for this contact. Maybe omitted
* ``can_add_to_group`` (boolean) - Can I add this contact to group chats. Maybe omitted
* ``can_delete`` (boolean) - Can I remove this contact from team. Maybe omitted
* ``changeable_fields`` (string) - Changeable fields. Maybe omitted
* ``family_name`` (string) - Family name. Maybe omitted
* ``given_name`` (string) - Given name. Maybe omitted
* ``patronymic`` (string) - Patronymic, if any. Maybe omitted
* ``default_lang`` (string) - Default language code. Maybe omitted. Might be null
* ``debug_show_activity`` (boolean) - Enable debug messages in UI. Maybe omitted. Might be null
* ``dropall_enabled`` (boolean) - Enable remove all messages experimental features. Maybe omitted. Might be null
* ``alt_send`` (boolean) - Use Ctrl/Cmd + Enter instead Enter. Maybe omitted. Might be null
* ``asterisk_mention`` (boolean) - Use * as @ for mentions. Maybe omitted. Might be null
* ``always_send_pushes`` (boolean) - Send push notifications even contact is online. Maybe omitted. Might be null
* ``timezone`` (string) - Timezone, if any. Maybe omitted. Might be null
* ``quiet_time_start`` (string) - Quiet time start. Maybe omitted. Might be null
* ``quiet_time_finish`` (string) - Quiet time finish. Maybe omitted. Might be null
* ``group_notifications_enabled`` (boolean) - Push notifications for group chats. Maybe omitted. Might be null
* ``task_notifications_enabled`` (boolean) - Push notifications for task chats. Maybe omitted. Might be null
* ``contact_short_view`` (boolean) - Short view in contact list. Maybe omitted. Might be null
* ``group_short_view`` (boolean) - Short view in group list. Maybe omitted. Might be null
* ``task_short_view`` (boolean) - Short view in task list. Maybe omitted. Might be null
* ``contact_mshort_view`` (boolean) - Short view in contact list in mobile app. Maybe omitted. Might be null
* ``group_mshort_view`` (boolean) - Short view in group list in mobile app. Maybe omitted. Might be null
* ``auth_2fa_enabled`` (boolean) - Two-factor authentication is configured and confirmed. Maybe omitted
* ``auth_2fa_status`` (string) - Two-factor authentication status. Maybe omitted
* ``task_mshort_view`` (boolean) - Short view in task list in mobile app. Maybe omitted. Might be null
* ``contact_show_archived`` (boolean) - Show archived contacts in contact list. Maybe omitted. Might be null
* ``unread_first`` (boolean) - Show unread chats first in feed. Maybe omitted. Might be null
* ``munread_first`` (boolean) - Show unread chats first in feed in mobile app. Maybe omitted. Might be null
* ``can_add_to_team`` (boolean) - Can I add new members to this team. Maybe omitted
* ``can_manage_sections`` (boolean) - Can I manage sections in this team. Maybe omitted
* ``can_manage_tags`` (boolean) - Can I manage tags in this team. Maybe omitted
* ``can_manage_integrations`` (boolean) - Can I manage integrations in this team. Maybe omitted
* ``can_manage_color_rules`` (boolean) - Can I manage color rules in this team. Maybe omitted
* ``can_create_group`` (boolean) - Can I create group chats in this team. Maybe omitted
* ``can_join_public_groups`` (boolean) - Can I view/join public group in this team. Maybe omitted
* ``can_join_public_tasks`` (boolean) - Can I view/join public tasks in this team. Maybe omitted
* ``can_delete_any_message`` (boolean) - Deprecated: use CanDeleteAnyMessage in chat object. Maybe omitted
* ``custom_fields`` ( :ref:`tdproto-ContactCustomFields` ) - Extra contact fields. Maybe omitted. Might be null

.. _tdproto-ContactCustomFields:

ContactCustomFields
-------------------------------------------------------------

Extra contact fields

**Fields**:

* ``company`` (string) - DOCUMENTATION MISSING. Maybe omitted
* ``department`` (string) - DOCUMENTATION MISSING. Maybe omitted
* ``title`` (string) - DOCUMENTATION MISSING. Maybe omitted
* ``mobile_phone`` (string) - DOCUMENTATION MISSING. Maybe omitted
* ``source`` (string) - DOCUMENTATION MISSING. Maybe omitted

.. _tdproto-ContactPreview:

ContactPreview
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``_error`` (string) - DOCUMENTATION MISSING. Maybe omitted
* ``phone`` (string) - DOCUMENTATION MISSING
* ``given_name`` (string) - DOCUMENTATION MISSING
* ``family_name`` (string) - DOCUMENTATION MISSING
* ``patronymic`` (string) - DOCUMENTATION MISSING. Maybe omitted
* ``role`` (string) - DOCUMENTATION MISSING
* ``section`` (string) - DOCUMENTATION MISSING

.. _tdproto-ContactShort:

ContactShort
-------------------------------------------------------------

Short contact representation

**Fields**:

* ``jid`` ( :ref:`tdproto-JID` ) - Contact Id
* ``display_name`` (string) - Full name in chats
* ``short_name`` (string) - Short name in chats
* ``icons`` ( :ref:`tdproto-IconData` ) - Icons data. Might be null

.. _tdproto-Country:

Country
-------------------------------------------------------------

Country for phone numbers selection on login screen

**Fields**:

* ``code`` (string) - Country code
* ``name`` (string) - Country name
* ``default`` (boolean) - Selected by default. Maybe omitted
* ``popular`` (boolean) - Is popular, need to cache. Maybe omitted

.. _tdproto-DeletedChat:

DeletedChat
-------------------------------------------------------------

Minimal chat representation for deletion

**Fields**:

* ``jid`` ( :ref:`tdproto-JID` ) - Group/Task/Contact id
* ``chat_type`` ( :ref:`tdproto-ChatType` ) - Chat type
* ``gentime`` (number) - Chat fields (related to concrete participant) version
* ``is_archive`` (boolean) - Archive flag. Always true for this structure

.. _tdproto-DeletedRemind:

DeletedRemind
-------------------------------------------------------------

Remind deleted message

**Fields**:

* ``uid`` (string) - Remind id

.. _tdproto-DeletedSection:

DeletedSection
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``uid`` (string) - Section uid
* ``gentime`` (number) - Object version

.. _tdproto-DeletedTag:

DeletedTag
-------------------------------------------------------------

Delete tag message

**Fields**:

* ``uid`` (string) - Tag id

.. _tdproto-DeletedTeam:

DeletedTeam
-------------------------------------------------------------

Team deletion message. Readonly

**Fields**:

* ``uid`` (string) - Team id
* ``is_archive`` (boolean) - Team deleted
* ``gentime`` (number) - Object version

.. _tdproto-Dist:

Dist
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``type`` (string) - DOCUMENTATION MISSING
* ``url`` (string) - DOCUMENTATION MISSING

.. _tdproto-Features:

Features
-------------------------------------------------------------

Server information. Readonly

**Fields**:

* ``host`` (string) - Current host
* ``build`` (string) - Build/revision of server side
* ``desktop_version`` (string) - Desktop application version
* ``front_version`` (string) - Webclient version
* ``app_title`` (string) - Application title
* ``landing_url`` (string) - Landing page address, if any. Maybe omitted
* ``app_schemes`` (string) - Local applications urls
* ``userver`` (string) - Static files server address
* ``ios_app`` (string) - Link to AppStore
* ``android_app`` (string) - Link to Google Play
* ``theme`` (string) - Default UI theme
* ``min_app_version`` (string) - Minimal application version required for this server. Used for breaking changes
* ``free_registration`` (boolean) - Free registration allowed
* ``max_upload_mb`` (number) - Maximum size of user's upload
* ``max_linked_messages`` (number) - Maximum number of forwarded messages
* ``max_message_uploads`` (number) - Maximum number of message uploads
* ``max_username_part_length`` (number) - Maximum chars for: family_name, given_name, patronymic if any
* ``max_group_title_length`` (number) - Maximum chars for group chat name
* ``max_role_length`` (number) - Maximum chars for role in team
* ``max_mood_length`` (number) - Maximum chars for mood in team
* ``max_message_length`` (number) - Maximum chars for text message
* ``max_section_length`` (number) - Maximum length for project and contact's sections names
* ``max_tag_length`` (number) - Maximum length for tags
* ``max_task_title_length`` (number) - Maximum length for task title
* ``max_color_rule_description_length`` (number) - Maximum length for ColorRule description
* ``max_url_length`` (number) - Maximum length for urls
* ``max_integration_comment_length`` (number) - Maximum length for Integration comment
* ``max_teams`` (number) - Maximum teams for one account
* ``max_message_search_limit`` (number) - Maximum search result
* ``afk_age`` (number) - Max inactivity seconds
* ``auth_by_password`` (boolean) - Password authentication enabled. Maybe omitted
* ``auth_by_qr_code`` (boolean) - QR-code / link authentication enabled. Maybe omitted
* ``auth_by_sms`` (boolean) - SMS authentication enabled. Maybe omitted
* ``auth_2fa`` (boolean) - Two-factor authentication (2FA) enabled. Maybe omitted
* ``oauth_services`` ( :ref:`tdproto-OAuthService` ) - External services. Maybe omitted
* ``ice_servers`` ( :ref:`tdproto-ICEServer` ) - ICE servers for WebRTC
* ``custom_server`` (boolean) - True for premise installation
* ``installation_type`` (string) - Name of installation
* ``installation_title`` (string) - Installation title, used on login screen. Maybe omitted
* ``background`` (string) - Background image url, if any. Maybe omitted
* ``is_testing`` (boolean) - Testing installation
* ``metrika`` (string) - Yandex metrika counter id
* ``min_search_length`` (number) - Minimal chars number for starting global search
* ``resend_timeout`` (number) - Resend message in n seconds if no confirmation from server given
* ``sentry_dsn_js`` (string) - Frontend sentry.io settings
* ``server_drafts`` (boolean) - Message drafts saved on server
* ``firebase_app_id`` (string) - Firebase settings for web-push notifications
* ``firebase_sender_id`` (string) - Firebase settings for web-push notifications
* ``firebase_api_key`` (string) - Firebase settings for web-push notifications
* ``firebase_auth_domain`` (string) - Firebase settings for web-push notifications
* ``firebase_database_url`` (string) - Firebase settings for web-push notifications
* ``firebase_project_id`` (string) - Firebase settings for web-push notifications
* ``firebase_storage_bucket`` (string) - Firebase settings for web-push notifications
* ``calls`` (boolean) - Calls functions enabled
* ``mobile_calls`` (boolean) - Calls functions enabled for mobile applications
* ``calls_record`` (boolean) - Calls record enabled
* ``only_one_device_per_call`` (boolean) - Disallow call from multiply devices. Experimental. Maybe omitted
* ``max_participants_per_call`` (number) - Maximum number of participants per call. Maybe omitted
* ``safari_push_id`` (string) - Safari push id for web-push notifications
* ``message_uploads`` (boolean) - Multiple message uploads
* ``terms`` ( :ref:`tdproto-Terms` ) - Team entity naming. Experimental
* ``single_group_teams`` (boolean) - Cross team communication. Experimental
* ``wiki_pages`` (boolean) - Wiki pages in chats. Experimental
* ``allow_admin_mute`` (boolean) - Wiki pages in chats. Experimental. Maybe omitted
* ``default_wallpaper`` ( :ref:`tdproto-Wallpaper` ) - Default wallpaper url for mobile apps, if any. Maybe omitted. Might be null
* ``task_checklist`` (boolean) - Deprecated
* ``readonly_groups`` (boolean) - Deprecated
* ``task_dashboard`` (boolean) - Deprecated
* ``task_messages`` (boolean) - Deprecated
* ``task_public`` (boolean) - Deprecated
* ``task_tags`` (boolean) - Deprecated

.. _tdproto-FontColors:

FontColors
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``text`` (string) - DOCUMENTATION MISSING
* ``title`` (string) - DOCUMENTATION MISSING
* ``sub`` (string) - DOCUMENTATION MISSING
* ``brand_button`` (string) - DOCUMENTATION MISSING
* ``simple_button`` (string) - DOCUMENTATION MISSING
* ``bubble_sent`` (string) - DOCUMENTATION MISSING
* ``bubble_received`` (string) - DOCUMENTATION MISSING

.. _tdproto-GroupAccessRequest:

GroupAccessRequest
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``uid`` (string) - DOCUMENTATION MISSING
* ``created`` (string) - DOCUMENTATION MISSING
* ``subject`` ( :ref:`tdproto-JID` ) - DOCUMENTATION MISSING

.. _tdproto-GroupMembership:

GroupMembership
-------------------------------------------------------------

Group chat membership status

**Fields**:

* ``jid`` ( :ref:`tdproto-JID` ) - Contact id
* ``status`` ( :ref:`tdproto-GroupStatus` ) - Status in group
* ``can_remove`` (boolean) - Can I remove this member. Maybe omitted

.. _tdproto-ICEServer:

ICEServer
-------------------------------------------------------------

Interactive Connectivity Establishment Server for WEB Rtc connection. Readonly

**Fields**:

* ``urls`` (string) - URls

.. _tdproto-IconColors:

IconColors
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``title`` (string) - DOCUMENTATION MISSING
* ``brand`` (string) - DOCUMENTATION MISSING
* ``other`` (string) - DOCUMENTATION MISSING

.. _tdproto-IconData:

IconData
-------------------------------------------------------------

Icon data. For icon generated from display name contains Letters + Color fields

**Fields**:

* ``sm`` ( :ref:`tdproto-SingleIcon` ) - Small icon
* ``lg`` ( :ref:`tdproto-SingleIcon` ) - Large image
* ``letters`` (string) - Letters (only for stub icon). Maybe omitted
* ``color`` (string) - Icon background color (only for stub icon). Maybe omitted
* ``blurhash`` (string) - Compact representation of a placeholder for an image (experimental). Maybe omitted
* ``stub`` (string) - Deprecated. Maybe omitted

.. _tdproto-InputColors:

InputColors
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``static`` (string) - DOCUMENTATION MISSING
* ``active`` (string) - DOCUMENTATION MISSING
* ``disable`` (string) - DOCUMENTATION MISSING
* ``error`` (string) - DOCUMENTATION MISSING

.. _tdproto-Integration:

Integration
-------------------------------------------------------------

Integration for concrete chat

**Fields**:

* ``uid`` (string) - Id. Maybe omitted
* ``comment`` (string) - Comment, if any
* ``created`` (string) - Creation datetime, iso. Maybe omitted
* ``enabled`` (boolean) - Integration enabled
* ``form`` ( :ref:`tdproto-IntegrationForm` ) - Integration form
* ``group`` ( :ref:`tdproto-JID` ) - Chat id
* ``help`` (string) - Full description. Maybe omitted
* ``kind`` (string) - Unique integration name
* ``-`` (string) - DOCUMENTATION MISSING

.. _tdproto-IntegrationField:

IntegrationField
-------------------------------------------------------------

Integration form field

**Fields**:

* ``label`` (string) - Label
* ``readonly`` (boolean) - Is field readonly
* ``value`` (string) - Current value

.. _tdproto-IntegrationForm:

IntegrationForm
-------------------------------------------------------------

Integration form

**Fields**:

* ``api_key`` ( :ref:`tdproto-IntegrationField` ) - Api key field, if any. Maybe omitted. Might be null
* ``webhook_url`` ( :ref:`tdproto-IntegrationField` ) - Webhook url, if any. Maybe omitted. Might be null
* ``url`` ( :ref:`tdproto-IntegrationField` ) - Url, if any. Maybe omitted. Might be null

.. _tdproto-IntegrationKind:

IntegrationKind
-------------------------------------------------------------

Integration kind

**Fields**:

* ``kind`` (string) - Integration unique name
* ``title`` (string) - Plugin title
* ``template`` ( :ref:`tdproto-Integration` ) - Integration template
* ``icon`` (string) - Path to icon
* ``description`` (string) - Plugin description

.. _tdproto-Integrations:

Integrations
-------------------------------------------------------------

Complete integrations data, as received from server

**Fields**:

* ``integrations`` ( :ref:`tdproto-Integration` ) - Currently existing integrations
* ``kinds`` ( :ref:`tdproto-IntegrationKind` ) - Types of integrations available for setup

.. _tdproto-Invitation:

Invitation
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``uid`` (string) - DOCUMENTATION MISSING
* ``token`` (string) - DOCUMENTATION MISSING
* ``created`` (string) - DOCUMENTATION MISSING
* ``qr`` (string) - DOCUMENTATION MISSING

.. _tdproto-JSEP:

JSEP
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``sdp`` (string) - DOCUMENTATION MISSING
* ``type`` (string) - DOCUMENTATION MISSING

.. _tdproto-MarkupEntity:

MarkupEntity
-------------------------------------------------------------

Markup entity. Experimental

**Fields**:

* ``op`` (number) - Open marker offset
* ``oplen`` (number) - Open marker length. Maybe omitted
* ``cl`` (number) - Close marker offset
* ``cllen`` (number) - Close marker length. Maybe omitted
* ``typ`` ( :ref:`tdproto-MarkupType` ) - Marker type
* ``url`` (string) - Url, for Link type. Maybe omitted
* ``repl`` (string) - Text replacement. Maybe omitted
* ``time`` (string) - Time, for Time type. Maybe omitted
* ``childs`` ( :ref:`tdproto-MarkupEntity` ) - List of internal markup entities. Maybe omitted

.. _tdproto-Message:

Message
-------------------------------------------------------------

Chat message

**Fields**:

* ``content`` ( :ref:`tdproto-MessageContent` ) - Message content struct
* ``push_text`` (string) - Simple plaintext message representation. Maybe omitted
* ``from`` ( :ref:`tdproto-JID` ) - Sender contact id
* ``to`` ( :ref:`tdproto-JID` ) - Recipient id (group, task or contact)
* ``message_id`` (string) - Message uid
* ``created`` (string) - Message creation datetime (set by server side) or sending datetime in future for draft messages
* ``drafted`` (string) - Creation datetime for draft messages. Maybe omitted
* ``gentime`` (number) - Object version
* ``chat_type`` ( :ref:`tdproto-ChatType` ) - Chat type
* ``chat`` ( :ref:`tdproto-JID` ) - Chat id
* ``links`` ( :ref:`tdproto-MessageLinks` ) - External/internals links. Maybe omitted
* ``markup`` ( :ref:`tdproto-MarkupEntity` ) - Markup entities. Experimental. Maybe omitted
* ``important`` (boolean) - Importance flag. Maybe omitted
* ``edited`` (string) - ISODateTimeString of message modification or deletion. Maybe omitted
* ``received`` (boolean) - Message was seen by anybody in chat. True or null. Maybe omitted
* ``num_received`` (number) - Unused yet. Maybe omitted
* ``nopreview`` (boolean) - Disable link previews. True or null. Maybe omitted
* ``has_previews`` (boolean) - Has link previews. True or null. Maybe omitted
* ``prev`` (string) - Previous message id in this chat. Uid or null. Maybe omitted
* ``is_first`` (boolean) - This message is first in this chat. True or null. Maybe omitted
* ``is_last`` (boolean) - This message is first in this chat. True or null. Maybe omitted
* ``uploads`` ( :ref:`tdproto-Upload` ) - Message uploads. Maybe omitted
* ``reactions`` ( :ref:`tdproto-MessageReaction` ) - Message reactions struct. Can be null. Maybe omitted
* ``reply_to`` ( :ref:`tdproto-Message` ) - Message that was replied to, if any. Maybe omitted. Might be null
* ``linked_messages`` ( :ref:`tdproto-Message` ) - Forwarded messages. Can be null. Also contains double of ReplyTo for backward compatibility. Maybe omitted
* ``notice`` (boolean) - Has mention (@). True or null. Maybe omitted
* ``silently`` (boolean) - Message has no pushes and did not affect any counters. Maybe omitted
* ``editable_until`` (string) - Author can change this message until date. Can be null. Maybe omitted
* ``num`` (number) - Index number of this message. Starts from 0. Null for deleted messages. Changes when any previous message wad deleted. Maybe omitted. Might be null
* ``is_archive`` (boolean) - This message is archive. True or null. Maybe omitted
* ``_debug`` (string) - Debug information, if any. Maybe omitted

.. _tdproto-MessageColors:

MessageColors
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``bubble_sent`` (string) - DOCUMENTATION MISSING
* ``bubble_received`` (string) - DOCUMENTATION MISSING
* ``bubble_important`` (string) - DOCUMENTATION MISSING
* ``status_feed`` (string) - DOCUMENTATION MISSING
* ``status_bubble`` (string) - DOCUMENTATION MISSING
* ``allocated`` (string) - DOCUMENTATION MISSING

.. _tdproto-MessageContent:

MessageContent
-------------------------------------------------------------

Chat message content

**Fields**:

* ``text`` (string) - Text representation of message
* ``type`` ( :ref:`tdproto-Mediatype` ) - Message type
* ``subtype`` ( :ref:`tdproto-Mediasubtype` ) - Message subtype, if any. Maybe omitted
* ``upload`` (string) - Upload id, if any. Deprecated: use Uploads instead. Maybe omitted
* ``mediaURL`` (string) - Upload url, if any. Deprecated: use Uploads instead. Maybe omitted
* ``size`` (number) - Upload size, if any. Deprecated: use Uploads instead. Maybe omitted
* ``duration`` (number) - Upload duration, if any. Deprecated: use Uploads instead. Maybe omitted. Might be null
* ``processing`` (boolean) - Upload still processing, if any. Deprecated: use Uploads instead. Maybe omitted
* ``blurhash`` (string) - Compact representation of a placeholder for an image. Deprecated: use Uploads instead. Maybe omitted
* ``previewHeight`` (number) - Upload preview height, in pixels, if any. Deprecated: use Uploads instead. Maybe omitted
* ``previewWidth`` (number) - Upload width, in pixels, if any. Deprecated: use Uploads instead. Maybe omitted
* ``previewURL`` (string) - Upload preview absolute url, if any. Deprecated: use Uploads instead. Maybe omitted
* ``preview2xURL`` (string) - Upload high resolution preview absolute url, if any. Deprecated: use Uploads instead. Maybe omitted
* ``name`` (string) - Upload name, if any. Deprecated: use Uploads instead. Maybe omitted
* ``animated`` (boolean) - Upload is animated image, if any. Deprecated: use Uploads instead. Maybe omitted
* ``title`` (string) - Change title (for "change" mediatype). Maybe omitted
* ``old`` (string) - Change old value (for "change" mediatype). Maybe omitted. Might be null
* ``new`` (string) - Change new value (for "change" mediatype). Maybe omitted. Might be null
* ``actor`` ( :ref:`tdproto-JID` ) - Change actor contact id (for "change" mediatype). Maybe omitted
* ``comment`` (string) - Comment (for "audiomsg" mediatype). Maybe omitted
* ``given_name`` (string) - Given name (for "contact" mediatype). Maybe omitted
* ``family_name`` (string) - Family name (for "contact" mediatype). Maybe omitted
* ``patronymic`` (string) - Patronymic name (for "contact" mediatype). Maybe omitted
* ``phones`` (string) - Contact phones list (for "contact" mediatype). Maybe omitted
* ``emails`` (string) - Emails list (for "contact" mediatype). Maybe omitted
* ``stickerpack`` (string) - Stickerpack name (for "sticker" subtype). Maybe omitted
* ``pdf_version`` ( :ref:`tdproto-PdfVersion` ) - Pdf version, if any. Maybe omitted. Might be null

.. _tdproto-MessageLink:

MessageLink
-------------------------------------------------------------

Checked message links. In short: "Click here: {link.Pattern}" => "Click here: <a href='{link.Url}'>{link.Text}</a>"

**Fields**:

* ``pattern`` (string) - Text fragment that should be replaced by link
* ``url`` (string) - Internal or external link
* ``text`` (string) - Text replacement
* ``preview`` ( :ref:`tdproto-MessageLinkPreview` ) - Optional preview info, for websites. Maybe omitted. Might be null
* ``uploads`` ( :ref:`tdproto-Upload` ) - Optional upload info. Maybe omitted
* ``nopreview`` (boolean) - Website previews disabled. Maybe omitted
* ``youtube_id`` (string) - Optional youtube movie id. Maybe omitted

.. _tdproto-MessageLinkPreview:

MessageLinkPreview
-------------------------------------------------------------

Website title and description

**Fields**:

* ``title`` (string) - Website title or og:title content
* ``description`` (string) - Website description. Maybe omitted

.. _tdproto-MessagePush:

MessagePush
-------------------------------------------------------------

Push message over websockets. Readonly

**Fields**:

* ``title`` (string) - Push title
* ``subtitle`` (string) - Push subtitle
* ``message`` (string) - Push body
* ``icon_url`` (string) - Absolute url to push icon
* ``click_action`` (string) - Url opened on click
* ``tag`` (string) - Push tag (for join pushes)
* ``team`` (string) - Team uid
* ``sender`` ( :ref:`tdproto-JID` ) - Sender contact id
* ``chat`` ( :ref:`tdproto-JID` ) - Chat id
* ``message_id`` (string) - Message id
* ``created`` (string) - Message creation iso datetime

.. _tdproto-MessageReaction:

MessageReaction
-------------------------------------------------------------

Message emoji reaction

**Fields**:

* ``name`` (string) - Emoji
* ``counter`` (number) - Number of reactions
* ``details`` ( :ref:`tdproto-MessageReactionDetail` ) - Details

.. _tdproto-MessageReactionDetail:

MessageReactionDetail
-------------------------------------------------------------

Message reaction detail

**Fields**:

* ``created`` (string) - When reaction added, iso datetime
* ``sender`` ( :ref:`tdproto-JID` ) - Reaction author
* ``name`` (string) - Reaction emoji

.. _tdproto-OAuthService:

OAuthService
-------------------------------------------------------------

OAuth service

**Fields**:

* ``name`` (string) - Integration title
* ``url`` (string) - Redirect url

.. _tdproto-OnlineCall:

OnlineCall
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``jid`` ( :ref:`tdproto-JID` ) - Chat or contact id
* ``uid`` (string) - Call id
* ``start`` (string) - Call start. Maybe omitted. Might be null
* ``online_count`` (number) - Number participants in call. Maybe omitted

.. _tdproto-OnlineContact:

OnlineContact
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``jid`` ( :ref:`tdproto-JID` ) - Contact id
* ``afk`` (boolean) - Is away from keyboard. Maybe omitted
* ``mobile`` (boolean) - Is mobile client

.. _tdproto-PaginatedChats:

PaginatedChats
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``contacts`` ( :ref:`tdproto-Contact` ) - DOCUMENTATION MISSING. Maybe omitted
* ``objects`` ( :ref:`tdproto-Chat` ) - DOCUMENTATION MISSING
* ``count`` (number) - DOCUMENTATION MISSING
* ``limit`` (number) - DOCUMENTATION MISSING
* ``offset`` (number) - DOCUMENTATION MISSING

.. _tdproto-PaginatedContacts:

PaginatedContacts
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``objects`` ( :ref:`tdproto-Contact` ) - DOCUMENTATION MISSING
* ``count`` (number) - DOCUMENTATION MISSING
* ``limit`` (number) - DOCUMENTATION MISSING
* ``offset`` (number) - DOCUMENTATION MISSING

.. _tdproto-PaginatedMessages:

PaginatedMessages
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``objects`` ( :ref:`tdproto-Message` ) - DOCUMENTATION MISSING
* ``count`` (number) - DOCUMENTATION MISSING
* ``limit`` (number) - DOCUMENTATION MISSING
* ``offset`` (number) - DOCUMENTATION MISSING

.. _tdproto-PaginatedUploadShortMessages:

PaginatedUploadShortMessages
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``objects`` ( :ref:`tdproto-UploadShortMessage` ) - DOCUMENTATION MISSING
* ``count`` (number) - DOCUMENTATION MISSING
* ``limit`` (number) - DOCUMENTATION MISSING
* ``offset`` (number) - DOCUMENTATION MISSING

.. _tdproto-PdfVersion:

PdfVersion
-------------------------------------------------------------

PDF preview of mediafile. Experimental

**Fields**:

* ``url`` (string) - Absolute url
* ``text_preview`` (string) - First string of text content. Maybe omitted

.. _tdproto-PushDevice:

PushDevice
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``type`` (string) - DOCUMENTATION MISSING
* ``device_id`` (string) - DOCUMENTATION MISSING
* ``notification_token`` (string) - DOCUMENTATION MISSING
* ``voip_notification_token`` (string) - DOCUMENTATION MISSING
* ``allowed_notifications`` (boolean) - DOCUMENTATION MISSING
* ``name`` (string) - DOCUMENTATION MISSING
* ``data_pushes`` (boolean) - DOCUMENTATION MISSING
* ``data_badges`` (boolean) - DOCUMENTATION MISSING

.. _tdproto-ReceivedMessage:

ReceivedMessage
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``chat`` ( :ref:`tdproto-JID` ) - Chat or contact id
* ``message_id`` (string) - Message id
* ``received`` (boolean) - Is received
* ``num_received`` (number) - Number of contacts received this message. Experimental. Maybe omitted
* ``_debug`` (string) - Debug message, if any. Maybe omitted

.. _tdproto-Remind:

Remind
-------------------------------------------------------------

Remind

**Fields**:

* ``uid`` (string) - Remind id
* ``chat`` ( :ref:`tdproto-JID` ) - Chat id
* ``fire_at`` (string) - Activation time, iso
* ``comment`` (string) - Comment, if any. Maybe omitted

.. _tdproto-Section:

Section
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``uid`` (string) - Section uid
* ``sort_ordering`` (number) - Sort ordering
* ``name`` (string) - Name
* ``gentime`` (number) - Object version
* ``description`` (string) - Description, if any. Maybe omitted
* ``is_archive`` (boolean) - Is deleted. Maybe omitted

.. _tdproto-ServerCallSoundParams:

ServerCallSoundParams
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``jid`` ( :ref:`tdproto-JID` ) - Chat or contact id
* ``muted`` (boolean) - Mute state

.. _tdproto-Session:

Session
-------------------------------------------------------------

Websocket session

**Fields**:

* ``uid`` (string) - Session id
* ``created`` (string) - Creation datetime
* ``lang`` (string) - Language code. Maybe omitted
* ``team`` (string) - Team id. Maybe omitted
* ``is_mobile`` (boolean) - Mobile. Maybe omitted
* ``afk`` (boolean) - Away from keyboard. Maybe omitted
* ``useragent`` (string) - User agent. Maybe omitted
* ``addr`` (string) - IP address. Maybe omitted

.. _tdproto-ShortMessage:

ShortMessage
-------------------------------------------------------------

Short message based on chat message

**Fields**:

* ``from`` ( :ref:`tdproto-JID` ) - Sender contact id
* ``to`` ( :ref:`tdproto-JID` ) - Recipient id (group, task or contact)
* ``message_id`` (string) - Message uid
* ``created`` (string) - Message creation datetime (set by server side) or sending datetime in future for draft messages
* ``gentime`` (number) - Object version
* ``chat_type`` ( :ref:`tdproto-ChatType` ) - Chat type
* ``chat`` ( :ref:`tdproto-JID` ) - Chat id
* ``is_archive`` (boolean) - This message is archive. True or null. Maybe omitted

.. _tdproto-SingleIcon:

SingleIcon
-------------------------------------------------------------

Small or large icon

**Fields**:

* ``url`` (string) - absolute url to icon
* ``width`` (number) - Icon width, in pixels
* ``height`` (number) - Icon height, in pixels

.. _tdproto-Sticker:

Sticker
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``uid`` (string) - DOCUMENTATION MISSING
* ``icon64`` (string) - DOCUMENTATION MISSING
* ``icon100`` (string) - DOCUMENTATION MISSING
* ``icon128`` (string) - DOCUMENTATION MISSING
* ``icon200`` (string) - DOCUMENTATION MISSING
* ``message_content`` ( :ref:`tdproto-MessageContent` ) - DOCUMENTATION MISSING

.. _tdproto-Stickerpack:

Stickerpack
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``uid`` (string) - DOCUMENTATION MISSING
* ``name`` (string) - DOCUMENTATION MISSING
* ``title`` (string) - DOCUMENTATION MISSING
* ``author`` (string) - DOCUMENTATION MISSING. Maybe omitted
* ``author_link`` (string) - DOCUMENTATION MISSING. Maybe omitted
* ``stickers`` ( :ref:`tdproto-Sticker` ) - DOCUMENTATION MISSING

.. _tdproto-Subtask:

Subtask
-------------------------------------------------------------

Link to sub/sup task

**Fields**:

* ``jid`` ( :ref:`tdproto-JID` ) - Task id
* ``assignee`` ( :ref:`tdproto-JID` ) - Assignee contact id. Tasks only
* ``title`` (string) - Task title. Generated from number and description
* ``num`` (number) - Task number in this team
* ``display_name`` (string) - Title
* ``public`` (boolean) - Can other team member see this task/group chat. Maybe omitted

.. _tdproto-SwitcherColors:

SwitcherColors
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``on`` (string) - DOCUMENTATION MISSING
* ``off`` (string) - DOCUMENTATION MISSING

.. _tdproto-Tag:

Tag
-------------------------------------------------------------

Task tag

**Fields**:

* ``uid`` (string) - Tag id
* ``name`` (string) - Tag name

.. _tdproto-TaskColor:

TaskColor
-------------------------------------------------------------

Task color rules color

**Fields**:

* ``regular`` (string) - DOCUMENTATION MISSING
* ``dark`` (string) - DOCUMENTATION MISSING
* ``light`` (string) - DOCUMENTATION MISSING

.. _tdproto-TaskCounters:

TaskCounters
-------------------------------------------------------------

Tasks counters

**Fields**:

* ``jid`` ( :ref:`tdproto-JID` ) - Task jid
* ``num_unread`` (number) - Unreads counter. Maybe omitted
* ``num_unread_notices`` (number) - Mentions (@) counter. Maybe omitted

.. _tdproto-TaskFilter:

TaskFilter
-------------------------------------------------------------

Task filter

**Fields**:

* ``field`` ( :ref:`tdproto-TaskFilterKey` ) - Task filter field
* ``title`` (string) - Filter title

.. _tdproto-TaskItem:

TaskItem
-------------------------------------------------------------

Task checklist item

**Fields**:

* ``uid`` (string) - Id. Maybe omitted
* ``sort_ordering`` (number) - Sort ordering. Maybe omitted
* ``text`` (string) - Text or "#{OtherTaskNumber}"
* ``checked`` (boolean) - Item checked. Maybe omitted
* ``can_toggle`` (boolean) - Can I toggle this item. Maybe omitted
* ``subtask`` ( :ref:`tdproto-Subtask` ) - Link to subtask. Optional. Maybe omitted. Might be null

.. _tdproto-TaskItems:

TaskItems
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``name`` (string) - DOCUMENTATION MISSING
* ``checked`` (boolean) - DOCUMENTATION MISSING

.. _tdproto-TaskPreview:

TaskPreview
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``_error`` (string) - DOCUMENTATION MISSING. Maybe omitted
* ``assignee`` ( :ref:`tdproto-JID` ) - DOCUMENTATION MISSING
* ``deadline`` (string) - DOCUMENTATION MISSING. Might be null
* ``description`` (string) - DOCUMENTATION MISSING
* ``section`` (string) - DOCUMENTATION MISSING
* ``public`` (boolean) - DOCUMENTATION MISSING
* ``tags`` (string) - DOCUMENTATION MISSING
* ``items`` ( :ref:`tdproto-TaskItems` ) - DOCUMENTATION MISSING

.. _tdproto-TaskSort:

TaskSort
-------------------------------------------------------------

Task sort type

**Fields**:

* ``key`` ( :ref:`tdproto-TaskSortKey` ) - Field
* ``title`` (string) - Sort title

.. _tdproto-TaskStatus:

TaskStatus
-------------------------------------------------------------

Custom task status

**Fields**:

* ``uid`` (string) - Status id. Maybe omitted
* ``sort_ordering`` (number) - Status sort ordering
* ``name`` (string) - Status internal name
* ``title`` (string) - Status localized name
* ``is_archive`` (boolean) - Status not used anymore. Maybe omitted

.. _tdproto-TaskTab:

TaskTab
-------------------------------------------------------------

Task tab

**Fields**:

* ``key`` ( :ref:`tdproto-TaskTabKey` ) - Tab name
* ``title`` (string) - Tab title
* ``hide_empty`` (boolean) - Disable this tab when it has no contents
* ``show_counter`` (boolean) - Show unread badge
* ``pagination`` (boolean) - Enable pagination
* ``filters`` ( :ref:`tdproto-TaskFilter` ) - Filters inside tab
* ``sort`` ( :ref:`tdproto-TaskSort` ) - Sort available in tab
* ``unread_tasks`` ( :ref:`tdproto-TaskCounters` ) - Unread tasks with jid and counters

.. _tdproto-Team:

Team
-------------------------------------------------------------

Team

**Fields**:

* ``uid`` (string) - Team id
* ``is_archive`` (boolean) - Team deleted. Maybe omitted
* ``gentime`` (number) - Object version
* ``name`` (string) - Team name
* ``default_task_deadline`` (string) - Default task deadline. Maybe omitted
* ``max_message_update_age`` (number) - Max message update/deletion age, in seconds
* ``icons`` ( :ref:`tdproto-IconData` ) - Team icons
* ``last_active`` (boolean) - User last activity was in this team
* ``changeable_statuses`` ( :ref:`tdproto-TeamStatus` ) - What status I can set to other team members. Maybe omitted
* ``bad_profile`` (boolean) - My profile in this team isn't full. Maybe omitted
* ``need_confirmation`` (boolean) - Need confirmation after invite to this team
* ``use_patronymic`` (boolean) - Patronymic in usernames for this team. Maybe omitted
* ``user_fields`` (string) - Username fields ordering
* ``display_family_name_first`` (boolean) - Family name should be first in display name. Maybe omitted
* ``use_task_importance`` (boolean) - Use importance field in task. Maybe omitted
* ``task_importance_min`` (number) - Minimal value of task importance. Default is 1. Maybe omitted
* ``task_importance_max`` (number) - Maximum value of task importance. Default is 5. Maybe omitted
* ``task_importance_rev`` (boolean) - Bigger number = bigger importance. Default: lower number = bigger importance. Maybe omitted
* ``use_task_urgency`` (boolean) - Use urgency field in task. Maybe omitted
* ``use_task_complexity`` (boolean) - Use complexity field in task. Maybe omitted
* ``use_task_spent_time`` (boolean) - Use spent time field in task. Maybe omitted
* ``uploads_size`` (number) - Total uploads size, bytes. Maybe omitted
* ``uploads_size_limit`` (number) - Maximum uploads size, bytes, if any. Maybe omitted
* ``unread`` ( :ref:`tdproto-TeamUnread` ) - Unread message counters. Might be null
* ``me`` ( :ref:`tdproto-Contact` ) - My profile in this team
* ``contacts`` ( :ref:`tdproto-Contact` ) - Team contacts. Used only for team creation. Maybe omitted
* ``single_group`` ( :ref:`tdproto-JID` ) - For single group teams, jid of chat. Maybe omitted
* ``theme`` ( :ref:`tdproto-Theme` ) - Color theme, if any. Maybe omitted. Might be null
* ``hide_archived_users`` (boolean) - Don't show archived users by default. Maybe omitted

.. _tdproto-TeamCounter:

TeamCounter
-------------------------------------------------------------

Unread message counters

**Fields**:

* ``uid`` (string) - Team id
* ``unread`` ( :ref:`tdproto-TeamUnread` ) - Unread message counters

.. _tdproto-TeamShort:

TeamShort
-------------------------------------------------------------

Short team representation. For invites, push notifications, etc. Readonly

**Fields**:

* ``uid`` (string) - Team id
* ``name`` (string) - Team name
* ``icons`` ( :ref:`tdproto-IconData` ) - Team icons

.. _tdproto-Terms:

Terms
-------------------------------------------------------------

Experimental translation fields for "team" entity renaming. Readonly

**Fields**:

* ``EnInTeam`` (string) - DOCUMENTATION MISSING
* ``EnTeam`` (string) - DOCUMENTATION MISSING
* ``EnTeamAccess`` (string) - DOCUMENTATION MISSING
* ``EnTeamAdmin`` (string) - DOCUMENTATION MISSING
* ``EnTeamAdmins`` (string) - DOCUMENTATION MISSING
* ``EnTeamGuest`` (string) - DOCUMENTATION MISSING
* ``EnTeamMember`` (string) - DOCUMENTATION MISSING
* ``EnTeamMembers`` (string) - DOCUMENTATION MISSING
* ``EnTeamOwner`` (string) - DOCUMENTATION MISSING
* ``EnTeamSettings`` (string) - DOCUMENTATION MISSING
* ``RuTeamSettings`` (string) - DOCUMENTATION MISSING
* ``EnTeams`` (string) - DOCUMENTATION MISSING
* ``EnToTeam`` (string) - DOCUMENTATION MISSING
* ``RuInTeam`` (string) - DOCUMENTATION MISSING
* ``RuTeam`` (string) - DOCUMENTATION MISSING
* ``RuTeamAccess`` (string) - DOCUMENTATION MISSING
* ``RuTeamAdmin`` (string) - DOCUMENTATION MISSING
* ``RuTeamAdmins`` (string) - DOCUMENTATION MISSING
* ``RuTeamD`` (string) - DOCUMENTATION MISSING
* ``RuTeamGuest`` (string) - DOCUMENTATION MISSING
* ``RuTeamMember`` (string) - DOCUMENTATION MISSING
* ``RuTeamMembers`` (string) - DOCUMENTATION MISSING
* ``RuTeamOwner`` (string) - DOCUMENTATION MISSING
* ``RuTeamP`` (string) - DOCUMENTATION MISSING
* ``RuTeamR`` (string) - DOCUMENTATION MISSING
* ``RuTeams`` (string) - DOCUMENTATION MISSING
* ``RuTeamsD`` (string) - DOCUMENTATION MISSING
* ``RuTeamsP`` (string) - DOCUMENTATION MISSING
* ``RuTeamsR`` (string) - DOCUMENTATION MISSING
* ``RuTeamsT`` (string) - DOCUMENTATION MISSING
* ``RuTeamsV`` (string) - DOCUMENTATION MISSING
* ``RuTeamT`` (string) - DOCUMENTATION MISSING
* ``RuTeamV`` (string) - DOCUMENTATION MISSING
* ``RuToTeam`` (string) - DOCUMENTATION MISSING

.. _tdproto-Theme:

Theme
-------------------------------------------------------------

Color theme

**Fields**:

* ``BgColor`` (string) - Web colors
* ``BgHoverColor`` (string) - DOCUMENTATION MISSING
* ``TextColor`` (string) - DOCUMENTATION MISSING
* ``MutedTextColor`` (string) - DOCUMENTATION MISSING
* ``AccentColor`` (string) - DOCUMENTATION MISSING
* ``AccentHoverColor`` (string) - DOCUMENTATION MISSING
* ``TextOnAccentHoverColor`` (string) - DOCUMENTATION MISSING
* ``MainAccent`` (string) - DOCUMENTATION MISSING
* ``MainAccentHover`` (string) - DOCUMENTATION MISSING
* ``MainLightAccent`` (string) - DOCUMENTATION MISSING
* ``MainLink`` (string) - DOCUMENTATION MISSING
* ``AppAccentColor`` (string) - Deprecated
* ``AppPrimaryColor`` (string) - Deprecated
* ``brand`` (string) - App colors
* ``brand_dark`` (string) - DOCUMENTATION MISSING
* ``brand_light`` (string) - DOCUMENTATION MISSING
* ``back`` (string) - DOCUMENTATION MISSING
* ``back_light`` (string) - DOCUMENTATION MISSING
* ``back_dark`` (string) - DOCUMENTATION MISSING
* ``success`` (string) - DOCUMENTATION MISSING
* ``success_light`` (string) - DOCUMENTATION MISSING
* ``error`` (string) - DOCUMENTATION MISSING
* ``error_light`` (string) - DOCUMENTATION MISSING
* ``background`` (string) - DOCUMENTATION MISSING
* ``tab_background`` (string) - DOCUMENTATION MISSING
* ``chat_input_background`` (string) - DOCUMENTATION MISSING
* ``substrate_background`` (string) - DOCUMENTATION MISSING
* ``modal_background`` (string) - DOCUMENTATION MISSING
* ``title_background`` (string) - DOCUMENTATION MISSING
* ``attention`` (string) - DOCUMENTATION MISSING
* ``attention_light`` (string) - DOCUMENTATION MISSING
* ``font`` ( :ref:`tdproto-FontColors` ) - DOCUMENTATION MISSING. Might be null
* ``message`` ( :ref:`tdproto-MessageColors` ) - DOCUMENTATION MISSING. Might be null
* ``switcher`` ( :ref:`tdproto-SwitcherColors` ) - DOCUMENTATION MISSING. Might be null
* ``button`` ( :ref:`tdproto-ButtonColors` ) - DOCUMENTATION MISSING. Might be null
* ``input`` ( :ref:`tdproto-InputColors` ) - DOCUMENTATION MISSING. Might be null
* ``ic`` ( :ref:`tdproto-IconColors` ) - DOCUMENTATION MISSING. Might be null

.. _tdproto-Unread:

Unread
-------------------------------------------------------------

Unread message counters

**Fields**:

* ``messages`` (number) - Total unread messages
* ``notice_messages`` (number) - Total unread messages with mentions
* ``chats`` (number) - Total chats with unread messages

.. _tdproto-Upload:

Upload
-------------------------------------------------------------

Uploaded media

**Fields**:

* ``uid`` (string) - Upload id
* ``created`` (string) - Uploaded at
* ``size`` (number) - Upload size in bytes
* ``duration`` (number) - Mediafile duration (for audio/video only). Maybe omitted
* ``name`` (string) - Filename
* ``url`` (string) - Absolute url
* ``preview`` ( :ref:`tdproto-UploadPreview` ) - Preview details. Maybe omitted. Might be null
* ``content_type`` (string) - Content type
* ``animated`` (boolean) - Is animated (images only). Maybe omitted
* ``blurhash`` (string) - Compact representation of a placeholder for an image (images only). Maybe omitted
* ``processing`` (boolean) - File still processing (video only). Maybe omitted
* ``pdf_version`` ( :ref:`tdproto-PdfVersion` ) - PDF version of file. Experimental. Maybe omitted. Might be null
* ``type`` ( :ref:`tdproto-UploadMediaType` ) - ?type=file,image,audio,video

.. _tdproto-UploadPreview:

UploadPreview
-------------------------------------------------------------

Upload preview

**Fields**:

* ``url`` (string) - Absolute url to image
* ``url_2x`` (string) - Absolute url to high resolution image (retina)
* ``width`` (number) - Width in pixels
* ``height`` (number) - Height in pixels

.. _tdproto-UploadShortMessage:

UploadShortMessage
-------------------------------------------------------------

Upload + ShortMessage

**Fields**:

* ``upload`` ( :ref:`tdproto-Upload` ) - DOCUMENTATION MISSING
* ``message`` ( :ref:`tdproto-ShortMessage` ) - DOCUMENTATION MISSING

.. _tdproto-User:

User
-------------------------------------------------------------

Account data

**Fields**:

* ``phone`` (string) - Phone for login. Maybe omitted
* ``email`` (string) - Email for login. Maybe omitted
* ``family_name`` (string) - Family name. Maybe omitted
* ``given_name`` (string) - Given name. Maybe omitted
* ``patronymic`` (string) - Patronymic, if any. Maybe omitted
* ``default_lang`` (string) - Default language code. Maybe omitted
* ``alt_send`` (boolean) - Use Ctrl/Cmd + Enter instead Enter
* ``asterisk_mention`` (boolean) - Use * as @ for mentions
* ``always_send_pushes`` (boolean) - Send pushes even user is online
* ``unread_first`` (boolean) - Show unread chats in chat list first
* ``munread_first`` (boolean) - Show unread chats in chat list first on mobiles
* ``timezone`` (string) - Timezone
* ``quiet_time_start`` (string) - Start silently time (no pushes, no sounds). Might be null
* ``quiet_time_finish`` (string) - Finish silently time (no pushes, no sounds). Might be null

.. _tdproto-UserAuth:

UserAuth
-------------------------------------------------------------

MISSING CLASS DOCUMENTATION

**Fields**:

* ``created`` (string) - DOCUMENTATION MISSING
* ``last_access`` (string) - DOCUMENTATION MISSING. Maybe omitted
* ``_age`` (number) - DOCUMENTATION MISSING. Maybe omitted
* ``uid`` (string) - DOCUMENTATION MISSING
* ``kind`` (string) - type of auth
* ``addr`` (string) - ip address. Maybe omitted
* ``user_agent`` (string) - info about useragent. Maybe omitted
* ``country`` (string) - name of country. Maybe omitted
* ``region`` (string) - name of region. Maybe omitted
* ``device`` ( :ref:`tdproto-PushDevice` ) - info about device (struct). Maybe omitted. Might be null

.. _tdproto-UserWithMe:

UserWithMe
-------------------------------------------------------------

Accouint data with extra information

**Fields**:

* ``inviter`` ( :ref:`tdproto-JID` ) - Inviter id, if any. Maybe omitted
* ``teams`` ( :ref:`tdproto-Team` ) - Available teams
* ``devices`` ( :ref:`tdproto-PushDevice` ) - Registered push devices
* ``phone`` (string) - Phone for login. Maybe omitted
* ``email`` (string) - Email for login. Maybe omitted
* ``family_name`` (string) - Family name. Maybe omitted
* ``given_name`` (string) - Given name. Maybe omitted
* ``patronymic`` (string) - Patronymic, if any. Maybe omitted
* ``default_lang`` (string) - Default language code. Maybe omitted
* ``alt_send`` (boolean) - Use Ctrl/Cmd + Enter instead Enter
* ``asterisk_mention`` (boolean) - Use * as @ for mentions
* ``always_send_pushes`` (boolean) - Send pushes even user is online
* ``unread_first`` (boolean) - Show unread chats in chat list first
* ``munread_first`` (boolean) - Show unread chats in chat list first on mobiles
* ``timezone`` (string) - Timezone
* ``quiet_time_start`` (string) - Start silently time (no pushes, no sounds). Might be null
* ``quiet_time_finish`` (string) - Finish silently time (no pushes, no sounds). Might be null

.. _tdproto-Wallpaper:

Wallpaper
-------------------------------------------------------------

Chat wallpaper

**Fields**:

* ``key`` (string) - Unique identifier
* ``name`` (string) - Localized description
* ``url`` (string) - Url to jpg or png

.. _tdproto-WikiPage:

WikiPage
-------------------------------------------------------------

Wiki page. Experimental

**Fields**:

* ``gentime`` (number) - Object version
* ``updated`` (string) - Update time
* ``editor`` ( :ref:`tdproto-JID` ) - Last editor contact id
* ``text`` (string) - Page text
