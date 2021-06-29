
Enums index
============================

.. _tdproto-ChatType:

ChatType
-------------------------------------------------------------
**Possible values**:

* direct
* group
* task


.. _tdproto-GroupStatus:

GroupStatus
-------------------------------------------------------------
**Possible values**:

* admin
* member


.. _tdproto-MarkupType:

MarkupType
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

Mediasubtype
-------------------------------------------------------------
**Possible values**:

* sticker
* newtask


.. _tdproto-Mediatype:

Mediatype
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

TeamStatus
-------------------------------------------------------------
**Possible values**:

* owner
* admin
* member
* guest


.. _tdproto-UploadMediaType:

UploadMediaType
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

ActiveUserDailyStatList
-------------------------------------------------------------

**Base Type**: ActiveUserDailyStat

**Is array**

.. _tdproto-ISODateTimeString:

ISODateTimeString
-------------------------------------------------------------

Date and time in RFC3339 format. Example: ``2019-09-18T00:00:07.435409Z``

**Base Type**: string

.. _tdproto-JID:

JID
-------------------------------------------------------------

**Base Type**: string

.. _tdproto-MessageLinks:

MessageLinks
-------------------------------------------------------------

**Base Type**: MessageLink

**Is array**

.. _tdproto-PushDeviceType:

PushDeviceType
-------------------------------------------------------------

**Base Type**: int

.. _tdproto-RGBColor:

RGBColor
-------------------------------------------------------------

Color in ``#rrggbb`` format where ``rr``, ``gg``, ``bb`` are hexadecimal numbers from 00 to ff of red, green and blue channels correspondingly. (yellow would be ``#ffff00``)

**Base Type**: string

.. _tdproto-TaskFilterKey:

TaskFilterKey
-------------------------------------------------------------

**Base Type**: string

.. _tdproto-TaskSortKey:

TaskSortKey
-------------------------------------------------------------

**Base Type**: string

.. _tdproto-TaskTabKey:

TaskTabKey
-------------------------------------------------------------

**Base Type**: string

JSON objects index
============================

.. _tdproto-ButtonColors:

ButtonColors
-------------------------------------------------------------

Button colors for app

**Fields**:

* ``brand_static`` (:ref:`tdproto-RGBColor`) - Brand static color
* ``brand_active`` (:ref:`tdproto-RGBColor`) - Brand active color
* ``brand_disable`` (:ref:`tdproto-RGBColor`) - Brand disable color
* ``simple_static`` (:ref:`tdproto-RGBColor`) - Simple static color
* ``simple_active`` (:ref:`tdproto-RGBColor`) - Simple active color
* ``simple_disable`` (:ref:`tdproto-RGBColor`) - Simple disable color

.. _tdproto-CallDevice:

CallDevice
-------------------------------------------------------------

Call participant device

**Fields**:

* ``muted`` (boolean) - Device muted
* ``useragent`` (string) - Device description

.. _tdproto-CallOnliner:

CallOnliner
-------------------------------------------------------------

Call participant

**Fields**:

* ``jid`` (:ref:`tdproto-JID`) - Contact id
* ``display_name`` (string) - Contact name
* ``role`` (string) - Contact role
* ``icon`` (string) - Contact icon
* ``muted`` (boolean) - Microphone muted. Computed from devices muted states
* ``devices`` (array[:ref:`tdproto-CallDevice`]) - Member devices, strictly one for now

.. _tdproto-Chat:

Chat
-------------------------------------------------------------

Chat (direct, group, task) representation

**Fields**:

* ``jid`` (:ref:`tdproto-JID`) - Group/Task/Contact id
* ``chat_type`` (:ref:`tdproto-ChatType`) - Chat type
* ``base_gentime`` (number) :abbr:`💥 (Maybe omitted)` - Base fields (not related to concrete participant) version
* ``gentime`` (number) - Chat fields related to concrete participant) version
* ``created`` (string) - Creation date, iso datetime
* ``display_name`` (string) - Title
* ``icons`` (:ref:`tdproto-IconData`) :abbr:`0️⃣ (Might be null)` - Icons info
* ``counters_enabled`` (boolean) :abbr:`💥 (Maybe omitted)` - Include unread messages to counters
* ``can_call`` (boolean) :abbr:`💥 (Maybe omitted)` - Can I call to this chat
* ``can_send_message`` (boolean) :abbr:`💥 (Maybe omitted)` - Can I send message to this chat
* ``cant_send_message_reason`` (string) :abbr:`💥 (Maybe omitted)` - Why I can't send message to this chat (if can't)
* ``collapsed`` (boolean) :abbr:`💥 (Maybe omitted)` - Description collapsed. Used for tasks only
* ``draft`` (string) :abbr:`💥 (Maybe omitted)` - Last message draft, if any
* ``draft_gentime`` (number) :abbr:`💥 (Maybe omitted)` - Last message draft version, if any
* ``hidden`` (boolean) :abbr:`💥 (Maybe omitted)` - Hidden chat
* ``notifications_enabled`` (boolean) :abbr:`💥 (Maybe omitted)` - Push notifications enabled
* ``num_importants`` (number) :abbr:`💥 (Maybe omitted)` - Number of important messages
* ``num_unread`` (number) :abbr:`💥 (Maybe omitted)` - Unread counter
* ``num_unread_notices`` (number) :abbr:`💥 (Maybe omitted)` - Mentions (@) counter
* ``last_message`` (:ref:`tdproto-Message`) :abbr:`💥 (Maybe omitted)` - Last message object
* ``last_read_message_id`` (string) :abbr:`💥 (Maybe omitted)` - Last read message id, if any
* ``section`` (string) :abbr:`💥 (Maybe omitted)` - Project / section id, if any
* ``changeable_fields`` (array[string]) :abbr:`💥 (Maybe omitted)` - List of editable fields
* ``pinned`` (boolean) :abbr:`💥 (Maybe omitted)` - Is chat pinned on top
* ``pinned_sort_ordering`` (number) :abbr:`💥 (Maybe omitted)` - Sort ordering for pinned chat
* ``num_members`` (number) :abbr:`💥 (Maybe omitted)` - Non-archive participants number
* ``can_delete`` (boolean) :abbr:`💥 (Maybe omitted)` - Can I delete this chat
* ``description`` (string) :abbr:`💥 (Maybe omitted)` - Group or task description
* ``markup`` (array[:ref:`tdproto-MarkupEntity`]) :abbr:`💥 (Maybe omitted)` - Markup entities for description field. Experimental
* ``feed`` (boolean) :abbr:`💥 (Maybe omitted)` - Present in feed (main screen)
* ``pinned_message`` (:ref:`tdproto-Message`) :abbr:`💥 (Maybe omitted)` - Pinned message for this chat
* ``color_index`` (number) :abbr:`💥 (Maybe omitted)` - Custom color index from table of colors. Tasks only
* ``num_items`` (number) :abbr:`💥 (Maybe omitted)` - Items in checklist. Tasks only
* ``num_checked_items`` (number) :abbr:`💥 (Maybe omitted)` - Checked items in checklist. Tasks only
* ``assignee`` (:ref:`tdproto-JID`) :abbr:`💥 (Maybe omitted)` - Assignee contact id. Tasks only
* ``num`` (number) :abbr:`💥 (Maybe omitted)` - Task number in this team
* ``observers`` (array[:ref:`tdproto-JID`]) :abbr:`💥 (Maybe omitted)` - Task followers id's. TODO: rename to "followers"
* ``owner`` (:ref:`tdproto-JID`) :abbr:`💥 (Maybe omitted)` - Task creator
* ``task_status`` (string) :abbr:`💥 (Maybe omitted)` - Task status. May be custom
* ``title`` (string) :abbr:`💥 (Maybe omitted)` - Task title. Generated from number and description
* ``done`` (string) :abbr:`💥 (Maybe omitted)` - Task done date in iso format, if any
* ``done_reason`` (string) :abbr:`💥 (Maybe omitted)` - Task done reason, if any
* ``deadline`` (string) :abbr:`💥 (Maybe omitted)` - Task deadline in iso format, if any
* ``deadline_expired`` (boolean) :abbr:`💥 (Maybe omitted)` - Is task deadline expired
* ``links`` (:ref:`tdproto-MessageLinks`) :abbr:`💥 (Maybe omitted)` - Links in description
* ``tags`` (array[string]) :abbr:`💥 (Maybe omitted)` - Task tags list, if any
* ``importance`` (number) :abbr:`💥 (Maybe omitted)` - Task importance, if available in team
* ``urgency`` (number) :abbr:`💥 (Maybe omitted)` - Task urgency, if available in team
* ``spent_time`` (number) :abbr:`💥 (Maybe omitted)` - Task spent time, number
* ``complexity`` (number) :abbr:`💥 (Maybe omitted)` - Task complexity, number
* ``linked_messages`` (array[any]) :abbr:`💥 (Maybe omitted)` - Used for "Create task from messages..."
* ``uploads`` (array[:ref:`tdproto-Upload`]) :abbr:`💥 (Maybe omitted)` - Upload uids for request, upload objects for response
* ``items`` (array[:ref:`tdproto-TaskItem`]) :abbr:`💥 (Maybe omitted)` - Checklist items. Task only
* ``parents`` (array[:ref:`tdproto-Subtask`]) :abbr:`💥 (Maybe omitted)` - Parent tasks
* ``tabs`` (array[:ref:`tdproto-TaskTabKey`]) :abbr:`💥 (Maybe omitted)` - Tab names
* ``status`` (:ref:`tdproto-GroupStatus`) :abbr:`💥 (Maybe omitted)` - My status in group chat
* ``members`` (array[:ref:`tdproto-GroupMembership`]) :abbr:`💥 (Maybe omitted)` - Group chat members
* ``can_add_member`` (boolean) :abbr:`💥 (Maybe omitted)` - Can I add member to this group chat
* ``can_remove_member`` (boolean) :abbr:`💥 (Maybe omitted)` - Can I remove member from this group chat
* ``can_change_member_status`` (boolean) :abbr:`💥 (Maybe omitted)` - Can I change member status in this group chat
* ``can_change_settings`` (boolean) :abbr:`💥 (Maybe omitted)` - deprecated: use changeable fields
* ``default_for_all`` (boolean) :abbr:`💥 (Maybe omitted)` - Any new team member will be added to this group chat
* ``readonly_for_members`` (boolean) :abbr:`💥 (Maybe omitted)` - Readonly for non-admins group chat (Like Channels in Telegram but switchable)
* ``autocleanup_age`` (number) :abbr:`💥 (Maybe omitted)` - Delete messages in this chat in seconds. Experimental function
* ``public`` (boolean) :abbr:`💥 (Maybe omitted)` - Can other team member see this task/group chat
* ``can_join`` (boolean) :abbr:`💥 (Maybe omitted)` - Can I join to this public group/task
* ``can_delete_any_message`` (boolean) :abbr:`💥 (Maybe omitted)` - Can I delete any message in this chat
* ``can_set_important_any_message`` (boolean) :abbr:`💥 (Maybe omitted)` - Can I change Important flag in any message in this chat
* ``last_activity`` (string) :abbr:`💥 (Maybe omitted)` - Date of the last message sent even if it was deleted
* ``draft_num`` (number) :abbr:`💥 (Maybe omitted)` - Deprecated

.. _tdproto-ChatShort:

ChatShort
-------------------------------------------------------------

Minimal chat representation

**Fields**:

* ``jid`` (:ref:`tdproto-JID`) - Group/Task/Contact id
* ``chat_type`` (:ref:`tdproto-ChatType`) - Chat type
* ``display_name`` (string) - Title
* ``icons`` (:ref:`tdproto-IconData`) :abbr:`0️⃣ (Might be null)` - Icon data

.. _tdproto-ColorRule:

ColorRule
-------------------------------------------------------------

Set of rules to apply to tasks for coloring

**Fields**:

* ``uid`` (string) - Rule id
* ``priority`` (number) - Rule priority
* ``description`` (string) :abbr:`💥 (Maybe omitted)` - Rule description
* ``color_index`` (number) - Color index
* ``section_enabled`` (boolean) :abbr:`💥 (Maybe omitted)` - Project filter enabled
* ``section`` (string) :abbr:`💥 (Maybe omitted)` - Project id if project filter enabled
* ``tags_enabled`` (boolean) :abbr:`💥 (Maybe omitted)` - Tags filter enabled
* ``tags`` (array[string]) :abbr:`💥 (Maybe omitted)` - Tag ids if tags filter enabled
* ``task_status`` (string) :abbr:`💥 (Maybe omitted)` - Task status
* ``task_importance_enabled`` (boolean) :abbr:`💥 (Maybe omitted)` - Task importance filter enabled
* ``task_importance`` (number) :abbr:`💥 (Maybe omitted)` - Task importance if task importance filter enabled
* ``task_urgency_enabled`` (boolean) :abbr:`💥 (Maybe omitted)` - Task urgency filter enabled
* ``task_urgency`` (number) :abbr:`💥 (Maybe omitted)` - Task urgency if task urgency filter enabled

.. _tdproto-Contact:

Contact
-------------------------------------------------------------

Contact

**Fields**:

* ``jid`` (:ref:`tdproto-JID`) - Contact Id
* ``display_name`` (string) - Full name in chats
* ``short_name`` (string) - Short name in chats
* ``contact_email`` (string) - Contact email in this team
* ``contact_phone`` (string) - Contact phone in this team
* ``icons`` (:ref:`tdproto-IconData`) :abbr:`0️⃣ (Might be null)` - Icons data
* ``role`` (string) - Role in this team
* ``mood`` (string) :abbr:`💥 (Maybe omitted)` - Mood in this team
* ``status`` (:ref:`tdproto-TeamStatus`) - Status in this team
* ``last_activity`` (string) :abbr:`💥 (Maybe omitted)` - Last activity in this team (iso datetime)
* ``is_archive`` (boolean) :abbr:`💥 (Maybe omitted)` - Contact deleted
* ``botname`` (string) :abbr:`💥 (Maybe omitted)` - Bot name. Empty for users
* ``sections`` (array[string]) - Section ids
* ``can_send_message`` (boolean) :abbr:`💥 (Maybe omitted)` - Can I send message to this contact
* ``cant_send_message_reason`` (string) :abbr:`💥 (Maybe omitted)` - Why I can't send message to this chat (if can't)
* ``can_call`` (boolean) :abbr:`💥 (Maybe omitted)` - Can I call to this contact
* ``can_create_task`` (boolean) :abbr:`💥 (Maybe omitted)` - Can I call create task for this contact
* ``can_import_tasks`` (boolean) :abbr:`💥 (Maybe omitted)` - Can I import tasks in this team
* ``can_add_to_group`` (boolean) :abbr:`💥 (Maybe omitted)` - Can I add this contact to group chats
* ``can_delete`` (boolean) :abbr:`💥 (Maybe omitted)` - Can I remove this contact from team
* ``changeable_fields`` (array[string]) :abbr:`💥 (Maybe omitted)` - Changeable fields
* ``family_name`` (string) :abbr:`💥 (Maybe omitted)` - Family name
* ``given_name`` (string) :abbr:`💥 (Maybe omitted)` - Given name
* ``patronymic`` (string) :abbr:`💥 (Maybe omitted)` - Patronymic, if any
* ``default_lang`` (string) :abbr:`💥 (Maybe omitted)` - Default language code
* ``debug_show_activity`` (boolean) :abbr:`💥 (Maybe omitted)` - Enable debug messages in UI
* ``dropall_enabled`` (boolean) :abbr:`💥 (Maybe omitted)` - Enable remove all messages experimental features
* ``alt_send`` (boolean) :abbr:`💥 (Maybe omitted)` - Use Ctrl/Cmd + Enter instead Enter
* ``asterisk_mention`` (boolean) :abbr:`💥 (Maybe omitted)` - Use * as @ for mentions
* ``always_send_pushes`` (boolean) :abbr:`💥 (Maybe omitted)` - Send push notifications even contact is online
* ``timezone`` (string) :abbr:`💥 (Maybe omitted)` - Timezone, if any
* ``quiet_time_start`` (string) :abbr:`💥 (Maybe omitted)` - Quiet time start
* ``quiet_time_finish`` (string) :abbr:`💥 (Maybe omitted)` - Quiet time finish
* ``group_notifications_enabled`` (boolean) :abbr:`💥 (Maybe omitted)` - Push notifications for group chats
* ``task_notifications_enabled`` (boolean) :abbr:`💥 (Maybe omitted)` - Push notifications for task chats
* ``contact_short_view`` (boolean) :abbr:`💥 (Maybe omitted)` - Short view in contact list
* ``group_short_view`` (boolean) :abbr:`💥 (Maybe omitted)` - Short view in group list
* ``task_short_view`` (boolean) :abbr:`💥 (Maybe omitted)` - Short view in task list
* ``contact_mshort_view`` (boolean) :abbr:`💥 (Maybe omitted)` - Short view in contact list in mobile app
* ``group_mshort_view`` (boolean) :abbr:`💥 (Maybe omitted)` - Short view in group list in mobile app
* ``auth_2fa_enabled`` (boolean) :abbr:`💥 (Maybe omitted)` - Two-factor authentication is configured and confirmed
* ``auth_2fa_status`` (string) :abbr:`💥 (Maybe omitted)` - Two-factor authentication status
* ``task_mshort_view`` (boolean) :abbr:`💥 (Maybe omitted)` - Short view in task list in mobile app
* ``contact_show_archived`` (boolean) :abbr:`💥 (Maybe omitted)` - Show archived contacts in contact list
* ``unread_first`` (boolean) :abbr:`💥 (Maybe omitted)` - Show unread chats first in feed
* ``munread_first`` (boolean) :abbr:`💥 (Maybe omitted)` - Show unread chats first in feed in mobile app
* ``can_add_to_team`` (boolean) :abbr:`💥 (Maybe omitted)` - Can I add new members to this team
* ``can_manage_sections`` (boolean) :abbr:`💥 (Maybe omitted)` - Can I manage contact sections in this team
* ``can_manage_projects`` (boolean) :abbr:`💥 (Maybe omitted)` - Can I manage task projects in this team
* ``can_manage_tags`` (boolean) :abbr:`💥 (Maybe omitted)` - Can I manage tags in this team
* ``can_manage_integrations`` (boolean) :abbr:`💥 (Maybe omitted)` - Can I manage integrations in this team
* ``can_manage_color_rules`` (boolean) :abbr:`💥 (Maybe omitted)` - Can I manage color rules in this team
* ``can_create_group`` (boolean) :abbr:`💥 (Maybe omitted)` - Can I create group chats in this team
* ``can_join_public_groups`` (boolean) :abbr:`💥 (Maybe omitted)` - Can I view/join public group in this team
* ``can_join_public_tasks`` (boolean) :abbr:`💥 (Maybe omitted)` - Can I view/join public tasks in this team
* ``can_delete_any_message`` (boolean) :abbr:`💥 (Maybe omitted)` - Deprecated: use CanDeleteAnyMessage in chat object
* ``custom_fields`` (:ref:`tdproto-ContactCustomFields`) :abbr:`💥 (Maybe omitted)` - Extra contact fields

.. _tdproto-ContactCustomFields:

ContactCustomFields
-------------------------------------------------------------

Extra contact fields

**Fields**:

* ``company`` (string) :abbr:`💥 (Maybe omitted)` - Company
* ``department`` (string) :abbr:`💥 (Maybe omitted)` - Department
* ``title`` (string) :abbr:`💥 (Maybe omitted)` - Title
* ``mobile_phone`` (string) :abbr:`💥 (Maybe omitted)` - MobilePhone
* ``source`` (string) :abbr:`💥 (Maybe omitted)` - Import source

.. _tdproto-ContactShort:

ContactShort
-------------------------------------------------------------

Short contact representation

**Fields**:

* ``jid`` (:ref:`tdproto-JID`) - Contact Id
* ``display_name`` (string) - Full name in chats
* ``short_name`` (string) - Short name in chats
* ``icons`` (:ref:`tdproto-IconData`) :abbr:`0️⃣ (Might be null)` - Icons data

.. _tdproto-Country:

Country
-------------------------------------------------------------

Country for phone numbers selection on login screen

**Fields**:

* ``code`` (string) - Phone code
* ``iso`` (string) - Country ISO code
* ``name`` (string) - Country name
* ``default`` (boolean) :abbr:`💥 (Maybe omitted)` - Selected by default
* ``popular`` (boolean) :abbr:`💥 (Maybe omitted)` - Is popular, need to cache

.. _tdproto-DeletedChat:

DeletedChat
-------------------------------------------------------------

Minimal chat representation for deletion

**Fields**:

* ``jid`` (:ref:`tdproto-JID`) - Group/Task/Contact id
* ``chat_type`` (:ref:`tdproto-ChatType`) - Chat type
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

Deleted task project or contact section

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

.. _tdproto-Emoji:

Emoji
-------------------------------------------------------------

Emoji

**Fields**:

* ``char`` (string) - Unicode symbol
* ``key`` (string) - Text representation

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
* ``landing_url`` (string) :abbr:`💥 (Maybe omitted)` - Landing page address, if any
* ``app_schemes`` (array[string]) - Local applications urls
* ``userver`` (string) - Static files server address
* ``ios_app`` (string) - Link to AppStore
* ``android_app`` (string) - Link to Google Play
* ``theme`` (string) - Default UI theme
* ``min_ios_version`` (string) - Minimal iOS application version required for this server. Used for breaking changes
* ``min_android_version`` (string) - Minimal android application version required for this server. Used for breaking changes
* ``min_corp_ios_version`` (string) - Minimal iOS corp application version required for this server. Used for breaking changes
* ``min_corp_android_version`` (string) - Minimal android corp application version required for this server. Used for breaking changes
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
* ``auth_by_password`` (boolean) :abbr:`💥 (Maybe omitted)` - Password authentication enabled
* ``auth_by_qr_code`` (boolean) :abbr:`💥 (Maybe omitted)` - QR-code / link authentication enabled
* ``auth_by_sms`` (boolean) :abbr:`💥 (Maybe omitted)` - SMS authentication enabled
* ``auth_2fa`` (boolean) :abbr:`💥 (Maybe omitted)` - Two-factor authentication (2FA) enabled
* ``oauth_services`` (array[:ref:`tdproto-OAuthService`]) :abbr:`💥 (Maybe omitted)` - External services
* ``ice_servers`` (array[:ref:`tdproto-ICEServer`]) - ICE servers for WebRTC
* ``custom_server`` (boolean) - True for premise installation
* ``installation_type`` (string) - Name of installation
* ``installation_title`` (string) :abbr:`💥 (Maybe omitted)` - Installation title, used on login screen
* ``app_login_background`` (string) :abbr:`💥 (Maybe omitted)` - AppBackground image url, if any
* ``web_login_background`` (string) :abbr:`💥 (Maybe omitted)` - WebBackground image url, if any
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
* ``calls_version`` (number) - Calls version. 0 = disabled, 1 = audio only, 2 = audio+video
* ``mobile_calls`` (boolean) - Calls functions enabled for mobile applications
* ``calls_record`` (boolean) - Calls record enabled
* ``only_one_device_per_call`` (boolean) :abbr:`💥 (Maybe omitted)` - Disallow call from multiply devices. Experimental
* ``max_participants_per_call`` (number) :abbr:`💥 (Maybe omitted)` - Maximum number of participants per call
* ``safari_push_id`` (string) - Safari push id for web-push notifications
* ``message_uploads`` (boolean) - Multiple message uploads
* ``terms`` (:ref:`tdproto-Terms`) - Team entity naming. Experimental
* ``single_group_teams`` (boolean) - Cross team communication. Experimental
* ``wiki_pages`` (boolean) - Wiki pages in chats. Experimental
* ``allow_admin_mute`` (boolean) :abbr:`💥 (Maybe omitted)` - Wiki pages in chats. Experimental
* ``default_wallpaper`` (:ref:`tdproto-Wallpaper`) :abbr:`💥 (Maybe omitted)` - Default wallpaper url for mobile apps, if any
* ``support_email`` (string) - Support email
* ``task_checklist`` (boolean) - Deprecated
* ``readonly_groups`` (boolean) - Deprecated
* ``task_dashboard`` (boolean) - Deprecated
* ``task_messages`` (boolean) - Deprecated
* ``task_public`` (boolean) - Deprecated
* ``task_tags`` (boolean) - Deprecated
* ``calls`` (boolean) - Deprecated
* ``min_app_version`` (string) - Deprecated

.. _tdproto-FontColors:

FontColors
-------------------------------------------------------------

Font colors for app

**Fields**:

* ``text`` (:ref:`tdproto-RGBColor`) - Text color
* ``title`` (:ref:`tdproto-RGBColor`) - Title color
* ``sub`` (:ref:`tdproto-RGBColor`) - Sub color
* ``brand_button`` (:ref:`tdproto-RGBColor`) - Brand button color
* ``simple_button`` (:ref:`tdproto-RGBColor`) - Simple button color
* ``bubble_sent`` (:ref:`tdproto-RGBColor`) - Bubble sent color
* ``bubble_received`` (:ref:`tdproto-RGBColor`) - Bubble received color

.. _tdproto-GroupMembership:

GroupMembership
-------------------------------------------------------------

Group chat membership status

**Fields**:

* ``jid`` (:ref:`tdproto-JID`) - Contact id
* ``status`` (:ref:`tdproto-GroupStatus`) :abbr:`💥 (Maybe omitted)` - Status in group
* ``can_remove`` (boolean) :abbr:`💥 (Maybe omitted)` - Can I remove this member

.. _tdproto-ICEServer:

ICEServer
-------------------------------------------------------------

Interactive Connectivity Establishment Server for WEB Rtc connection. Readonly

**Fields**:

* ``urls`` (string) - URls

.. _tdproto-IconColors:

IconColors
-------------------------------------------------------------

Icon colors for app

**Fields**:

* ``title`` (:ref:`tdproto-RGBColor`) - Title color
* ``brand`` (:ref:`tdproto-RGBColor`) - Brand color
* ``other`` (:ref:`tdproto-RGBColor`) - Other color

.. _tdproto-IconData:

IconData
-------------------------------------------------------------

Icon data. For icon generated from display name contains Letters + Color fields

**Fields**:

* ``sm`` (:ref:`tdproto-SingleIcon`) - Small icon
* ``lg`` (:ref:`tdproto-SingleIcon`) - Large image
* ``letters`` (string) :abbr:`💥 (Maybe omitted)` - Letters (only for stub icon)
* ``color`` (string) :abbr:`💥 (Maybe omitted)` - Icon background color (only for stub icon)
* ``blurhash`` (string) :abbr:`💥 (Maybe omitted)` - Compact representation of a placeholder for an image (experimental)
* ``stub`` (string) :abbr:`💥 (Maybe omitted)` - Deprecated

.. _tdproto-InputColors:

InputColors
-------------------------------------------------------------

Input colors for app

**Fields**:

* ``static`` (:ref:`tdproto-RGBColor`) - Static color
* ``active`` (:ref:`tdproto-RGBColor`) - Active color
* ``disable`` (:ref:`tdproto-RGBColor`) - Disable color
* ``error`` (:ref:`tdproto-RGBColor`) - Error color

.. _tdproto-Integration:

Integration
-------------------------------------------------------------

Integration for concrete chat

**Fields**:

* ``uid`` (string) :abbr:`💥 (Maybe omitted)` - Id
* ``comment`` (string) - Comment, if any
* ``created`` (string) :abbr:`💥 (Maybe omitted)` - Creation datetime, iso
* ``enabled`` (boolean) - Integration enabled
* ``form`` (:ref:`tdproto-IntegrationForm`) - Integration form
* ``group`` (:ref:`tdproto-JID`) - Chat id
* ``help`` (string) :abbr:`💥 (Maybe omitted)` - Full description
* ``kind`` (string) - Unique integration name

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

* ``api_key`` (:ref:`tdproto-IntegrationField`) :abbr:`💥 (Maybe omitted)` - Api key field, if any
* ``webhook_url`` (:ref:`tdproto-IntegrationField`) :abbr:`💥 (Maybe omitted)` - Webhook url, if any
* ``url`` (:ref:`tdproto-IntegrationField`) :abbr:`💥 (Maybe omitted)` - Url, if any

.. _tdproto-IntegrationKind:

IntegrationKind
-------------------------------------------------------------

Integration kind

**Fields**:

* ``kind`` (string) - Integration unique name
* ``title`` (string) - Plugin title
* ``template`` (:ref:`tdproto-Integration`) - Integration template
* ``icon`` (string) - Path to icon
* ``description`` (string) - Plugin description

.. _tdproto-Integrations:

Integrations
-------------------------------------------------------------

Complete integrations data, as received from server

**Fields**:

* ``integrations`` (array[:ref:`tdproto-Integration`]) - Currently existing integrations
* ``kinds`` (array[:ref:`tdproto-IntegrationKind`]) - Types of integrations available for setup

.. _tdproto-JSEP:

JSEP
-------------------------------------------------------------

JavaScript Session Establishment Protocol

**Fields**:

* ``sdp`` (string) - Session Description Protocol information
* ``type`` (string) - See https://rtcweb-wg.github.io/jsep/#rfc.section.4.1.8

.. _tdproto-MarkupEntity:

MarkupEntity
-------------------------------------------------------------

Markup entity. Experimental

**Fields**:

* ``op`` (number) - Open marker offset
* ``oplen`` (number) :abbr:`💥 (Maybe omitted)` - Open marker length
* ``cl`` (number) - Close marker offset
* ``cllen`` (number) :abbr:`💥 (Maybe omitted)` - Close marker length
* ``typ`` (:ref:`tdproto-MarkupType`) - Marker type
* ``url`` (string) :abbr:`💥 (Maybe omitted)` - Url, for Link type
* ``repl`` (string) :abbr:`💥 (Maybe omitted)` - Text replacement
* ``time`` (string) :abbr:`💥 (Maybe omitted)` - Time, for Time type
* ``childs`` (array[:ref:`tdproto-MarkupEntity`]) :abbr:`💥 (Maybe omitted)` - List of internal markup entities

.. _tdproto-Message:

Message
-------------------------------------------------------------

Chat message

**Fields**:

* ``content`` (:ref:`tdproto-MessageContent`) - Message content struct
* ``push_text`` (string) :abbr:`💥 (Maybe omitted)` - Simple plaintext message representation
* ``from`` (:ref:`tdproto-JID`) - Sender contact id
* ``to`` (:ref:`tdproto-JID`) - Recipient id (group, task or contact)
* ``message_id`` (string) - Message uid
* ``created`` (string) - Message creation datetime (set by server side) or sending datetime in future for draft messages
* ``drafted`` (string) :abbr:`💥 (Maybe omitted)` - Creation datetime for draft messages
* ``gentime`` (number) - Object version
* ``chat_type`` (:ref:`tdproto-ChatType`) - Chat type
* ``chat`` (:ref:`tdproto-JID`) - Chat id
* ``links`` (:ref:`tdproto-MessageLinks`) :abbr:`💥 (Maybe omitted)` - External/internals links
* ``markup`` (array[:ref:`tdproto-MarkupEntity`]) :abbr:`💥 (Maybe omitted)` - Markup entities. Experimental
* ``important`` (boolean) :abbr:`💥 (Maybe omitted)` - Importance flag
* ``edited`` (string) :abbr:`💥 (Maybe omitted)` - ISODateTimeString of message modification or deletion
* ``received`` (boolean) :abbr:`💥 (Maybe omitted)` - Message was seen by anybody in chat. True or null
* ``num_received`` (number) :abbr:`💥 (Maybe omitted)` - Unused yet
* ``nopreview`` (boolean) :abbr:`💥 (Maybe omitted)` - Disable link previews. True or null
* ``has_previews`` (boolean) :abbr:`💥 (Maybe omitted)` - Has link previews. True or null
* ``prev`` (string) :abbr:`💥 (Maybe omitted)` - Previous message id in this chat. Uid or null
* ``is_first`` (boolean) :abbr:`💥 (Maybe omitted)` - This message is first in this chat. True or null
* ``is_last`` (boolean) :abbr:`💥 (Maybe omitted)` - This message is last in this chat. True or null
* ``uploads`` (array[:ref:`tdproto-Upload`]) :abbr:`💥 (Maybe omitted)` - Message uploads
* ``reactions`` (array[:ref:`tdproto-MessageReaction`]) :abbr:`💥 (Maybe omitted)` - Message reactions struct. Can be null
* ``reply_to`` (:ref:`tdproto-Message`) :abbr:`💥 (Maybe omitted)` - Message that was replied to, if any
* ``linked_messages`` (array[:ref:`tdproto-Message`]) :abbr:`💥 (Maybe omitted)` - Forwarded messages. Can be null. Also contains double of ReplyTo for backward compatibility
* ``notice`` (boolean) :abbr:`💥 (Maybe omitted)` - Has mention (@). True or null
* ``silently`` (boolean) :abbr:`💥 (Maybe omitted)` - Message has no pushes and did not affect any counters
* ``editable_until`` (string) :abbr:`💥 (Maybe omitted)` - Author can change this message until date. Can be null
* ``num`` (number) :abbr:`💥 (Maybe omitted)` - Index number of this message. Starts from 0. Null for deleted messages. Changes when any previous message wad deleted
* ``is_archive`` (boolean) :abbr:`💥 (Maybe omitted)` - This message is archive. True or null
* ``_debug`` (string) :abbr:`💥 (Maybe omitted)` - Debug information, if any

.. _tdproto-MessageColors:

MessageColors
-------------------------------------------------------------

Message colors for app

**Fields**:

* ``bubble_sent`` (:ref:`tdproto-RGBColor`) - Bubble sent color
* ``bubble_received`` (:ref:`tdproto-RGBColor`) - Bubble received color
* ``bubble_important`` (:ref:`tdproto-RGBColor`) - Bubble important color
* ``status_feed`` (:ref:`tdproto-RGBColor`) - Status feed color
* ``status_bubble`` (:ref:`tdproto-RGBColor`) - Status bubble color
* ``allocated`` (:ref:`tdproto-RGBColor`) - Allocated color

.. _tdproto-MessageContent:

MessageContent
-------------------------------------------------------------

Chat message content

**Fields**:

* ``text`` (string) - Text representation of message
* ``type`` (:ref:`tdproto-Mediatype`) - Message type
* ``subtype`` (:ref:`tdproto-Mediasubtype`) :abbr:`💥 (Maybe omitted)` - Message subtype, if any
* ``upload`` (string) :abbr:`💥 (Maybe omitted)` - Upload id, if any. Deprecated: use Uploads instead
* ``mediaURL`` (string) :abbr:`💥 (Maybe omitted)` - Upload url, if any. Deprecated: use Uploads instead
* ``size`` (number) :abbr:`💥 (Maybe omitted)` - Upload size, if any. Deprecated: use Uploads instead
* ``duration`` (number) :abbr:`💥 (Maybe omitted)` - Upload duration, if any. Deprecated: use Uploads instead
* ``processing`` (boolean) :abbr:`💥 (Maybe omitted)` - Upload still processing, if any. Deprecated: use Uploads instead
* ``blurhash`` (string) :abbr:`💥 (Maybe omitted)` - Compact representation of a placeholder for an image. Deprecated: use Uploads instead
* ``previewHeight`` (number) :abbr:`💥 (Maybe omitted)` - Upload preview height, in pixels, if any. Deprecated: use Uploads instead
* ``previewWidth`` (number) :abbr:`💥 (Maybe omitted)` - Upload width, in pixels, if any. Deprecated: use Uploads instead
* ``previewURL`` (string) :abbr:`💥 (Maybe omitted)` - Upload preview absolute url, if any. Deprecated: use Uploads instead
* ``preview2xURL`` (string) :abbr:`💥 (Maybe omitted)` - Upload high resolution preview absolute url, if any. Deprecated: use Uploads instead
* ``name`` (string) :abbr:`💥 (Maybe omitted)` - Upload name, if any. Deprecated: use Uploads instead
* ``animated`` (boolean) :abbr:`💥 (Maybe omitted)` - Upload is animated image, if any. Deprecated: use Uploads instead
* ``title`` (string) :abbr:`💥 (Maybe omitted)` - Change title (for "change" mediatype)
* ``old`` (string) :abbr:`💥 (Maybe omitted)` - Change old value (for "change" mediatype)
* ``new`` (string) :abbr:`💥 (Maybe omitted)` - Change new value (for "change" mediatype)
* ``actor`` (:ref:`tdproto-JID`) :abbr:`💥 (Maybe omitted)` - Change actor contact id (for "change" mediatype)
* ``comment`` (string) :abbr:`💥 (Maybe omitted)` - Comment (for "audiomsg" mediatype)
* ``given_name`` (string) :abbr:`💥 (Maybe omitted)` - Given name (for "contact" mediatype)
* ``family_name`` (string) :abbr:`💥 (Maybe omitted)` - Family name (for "contact" mediatype)
* ``patronymic`` (string) :abbr:`💥 (Maybe omitted)` - Patronymic name (for "contact" mediatype)
* ``phones`` (array[string]) :abbr:`💥 (Maybe omitted)` - Contact phones list (for "contact" mediatype)
* ``emails`` (array[string]) :abbr:`💥 (Maybe omitted)` - Emails list (for "contact" mediatype)
* ``stickerpack`` (string) :abbr:`💥 (Maybe omitted)` - Stickerpack name (for "sticker" subtype)
* ``pdf_version`` (:ref:`tdproto-PdfVersion`) :abbr:`💥 (Maybe omitted)` - Pdf version, if any

.. _tdproto-MessageLink:

MessageLink
-------------------------------------------------------------

Checked message links. In short: "Click here: {link.Pattern}" => "Click here: <a href='{link.Url}'>{link.Text}</a>"

**Fields**:

* ``pattern`` (string) - Text fragment that should be replaced by link
* ``url`` (string) - Internal or external link
* ``text`` (string) - Text replacement
* ``preview`` (:ref:`tdproto-MessageLinkPreview`) :abbr:`💥 (Maybe omitted)` - Optional preview info, for websites
* ``uploads`` (array[:ref:`tdproto-Upload`]) :abbr:`💥 (Maybe omitted)` - Optional upload info
* ``nopreview`` (boolean) :abbr:`💥 (Maybe omitted)` - Website previews disabled
* ``youtube_id`` (string) :abbr:`💥 (Maybe omitted)` - Optional youtube movie id

.. _tdproto-MessageLinkPreview:

MessageLinkPreview
-------------------------------------------------------------

Website title and description

**Fields**:

* ``title`` (string) - Website title or og:title content
* ``description`` (string) :abbr:`💥 (Maybe omitted)` - Website description

.. _tdproto-MessageReaction:

MessageReaction
-------------------------------------------------------------

Message emoji reaction

**Fields**:

* ``name`` (string) - Emoji
* ``counter`` (number) - Number of reactions
* ``details`` (array[:ref:`tdproto-MessageReactionDetail`]) - Details

.. _tdproto-MessageReactionDetail:

MessageReactionDetail
-------------------------------------------------------------

Message reaction detail

**Fields**:

* ``created`` (string) - When reaction added, iso datetime
* ``sender`` (:ref:`tdproto-JID`) - Reaction author
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

Active call status

**Fields**:

* ``jid`` (:ref:`tdproto-JID`) - Chat or contact id
* ``uid`` (string) - Call id
* ``start`` (string) :abbr:`💥 (Maybe omitted)` - Call start
* ``online_count`` (number) :abbr:`💥 (Maybe omitted)` - Number participants in call

.. _tdproto-OnlineContact:

OnlineContact
-------------------------------------------------------------

Contact online status

**Fields**:

* ``jid`` (:ref:`tdproto-JID`) - Contact id
* ``afk`` (boolean) :abbr:`💥 (Maybe omitted)` - Is away from keyboard
* ``mobile`` (boolean) - Is mobile client

.. _tdproto-PdfVersion:

PdfVersion
-------------------------------------------------------------

PDF preview of mediafile. Experimental

**Fields**:

* ``url`` (string) - Absolute url
* ``text_preview`` (string) :abbr:`💥 (Maybe omitted)` - First string of text content

.. _tdproto-PushDevice:

PushDevice
-------------------------------------------------------------

Push device info

**Fields**:

* ``type`` (string) - Type: android, ios, web, safari
* ``device_id`` (string) - Device id generated by client library
* ``notification_token`` (string) - Notification token
* ``voip_notification_token`` (string) - Notification token for VOIP (iOS only)
* ``name`` (string) - Readable device name
* ``data_pushes`` (boolean) - Send silently data pushes that must be fully processed by app. Must be true for modern mobile clients
* ``data_badges`` (boolean) - Send badge value as data. Experimental
* ``allowed_notifications`` (boolean) - deprecated

.. _tdproto-Reaction:

Reaction
-------------------------------------------------------------

Emoji reaction

**Fields**:

* ``name`` (string) - Unicode symbol

.. _tdproto-ReceivedMessage:

ReceivedMessage
-------------------------------------------------------------

Message receiving status

**Fields**:

* ``chat`` (:ref:`tdproto-JID`) - Chat or contact id
* ``message_id`` (string) - Message id
* ``received`` (boolean) - Is received
* ``num_received`` (number) :abbr:`💥 (Maybe omitted)` - Number of contacts received this message. Experimental
* ``_debug`` (string) :abbr:`💥 (Maybe omitted)` - Debug message, if any

.. _tdproto-Remind:

Remind
-------------------------------------------------------------

Remind

**Fields**:

* ``uid`` (string) - Remind id
* ``chat`` (:ref:`tdproto-JID`) - Chat id
* ``fire_at`` (string) - Activation time, iso
* ``comment`` (string) :abbr:`💥 (Maybe omitted)` - Comment, if any

.. _tdproto-Section:

Section
-------------------------------------------------------------

Task project or contact section

**Fields**:

* ``uid`` (string) - Section uid
* ``sort_ordering`` (number) - Sort ordering
* ``name`` (string) - Name
* ``gentime`` (number) - Object version
* ``description`` (string) :abbr:`💥 (Maybe omitted)` - Description, if any
* ``is_archive`` (boolean) :abbr:`💥 (Maybe omitted)` - Is deleted

.. _tdproto-Session:

Session
-------------------------------------------------------------

Websocket session

**Fields**:

* ``uid`` (string) - Session id
* ``created`` (string) - Creation datetime
* ``lang`` (string) :abbr:`💥 (Maybe omitted)` - Language code
* ``team`` (string) :abbr:`💥 (Maybe omitted)` - Team id
* ``is_mobile`` (boolean) :abbr:`💥 (Maybe omitted)` - Mobile
* ``afk`` (boolean) :abbr:`💥 (Maybe omitted)` - Away from keyboard
* ``useragent`` (string) :abbr:`💥 (Maybe omitted)` - User agent
* ``addr`` (string) :abbr:`💥 (Maybe omitted)` - IP address

.. _tdproto-ShortMessage:

ShortMessage
-------------------------------------------------------------

Short message based on chat message

**Fields**:

* ``from`` (:ref:`tdproto-JID`) - Sender contact id
* ``to`` (:ref:`tdproto-JID`) - Recipient id (group, task or contact)
* ``message_id`` (string) - Message uid
* ``created`` (string) - Message creation datetime (set by server side) or sending datetime in future for draft messages
* ``gentime`` (number) - Object version
* ``chat_type`` (:ref:`tdproto-ChatType`) - Chat type
* ``chat`` (:ref:`tdproto-JID`) - Chat id
* ``is_archive`` (boolean) :abbr:`💥 (Maybe omitted)` - This message is archive. True or null

.. _tdproto-SingleIcon:

SingleIcon
-------------------------------------------------------------

Small or large icon

**Fields**:

* ``url`` (string) - absolute url to icon
* ``width`` (number) - Icon width, in pixels
* ``height`` (number) - Icon height, in pixels

.. _tdproto-Subtask:

Subtask
-------------------------------------------------------------

Link to sub/sup task

**Fields**:

* ``jid`` (:ref:`tdproto-JID`) - Task id
* ``assignee`` (:ref:`tdproto-JID`) - Assignee contact id. Tasks only
* ``title`` (string) - Task title. Generated from number and description
* ``num`` (number) - Task number in this team
* ``display_name`` (string) - Title
* ``public`` (boolean) :abbr:`💥 (Maybe omitted)` - Can other team member see this task/group chat

.. _tdproto-SwitcherColors:

SwitcherColors
-------------------------------------------------------------

Switcher colors for app

**Fields**:

* ``on`` (:ref:`tdproto-RGBColor`) - On color
* ``off`` (:ref:`tdproto-RGBColor`) - Off color

.. _tdproto-Tag:

Tag
-------------------------------------------------------------

Task tag

**Fields**:

* ``uid`` (string) - Tag id
* ``name`` (string) - Tag name

.. _tdproto-Task:

Task
-------------------------------------------------------------

Task

**Fields**:

* ``custom_color_index`` (number) :abbr:`💥 (Maybe omitted)` - Custom task color
* ``description`` (string) :abbr:`💥 (Maybe omitted)` - Task description
* ``tags`` (array[string]) :abbr:`💥 (Maybe omitted)` - Task tags
* ``section`` (string) :abbr:`💥 (Maybe omitted)` - Task section UID
* ``observers`` (array[:ref:`tdproto-JID`]) :abbr:`💥 (Maybe omitted)` - User who follow the task
* ``items`` (array[string]) :abbr:`💥 (Maybe omitted)` - Items of the task
* ``assignee`` (:ref:`tdproto-JID`) :abbr:`💥 (Maybe omitted)` - User who was assigned the task
* ``deadline`` (string) :abbr:`💥 (Maybe omitted)` - Deadline time, if any
* ``public`` (boolean) :abbr:`💥 (Maybe omitted)` - Is task public
* ``remind_at`` (string) :abbr:`💥 (Maybe omitted)` - Fire a reminder at this time
* ``task_status`` (string) :abbr:`💥 (Maybe omitted)` - Task status
* ``importance`` (number) :abbr:`💥 (Maybe omitted)` - Task importance
* ``urgency`` (number) :abbr:`💥 (Maybe omitted)` - Task urgency
* ``complexity`` (number) :abbr:`💥 (Maybe omitted)` - Task complexity
* ``spent_time`` (number) :abbr:`💥 (Maybe omitted)` - Time spent
* ``linked_messages`` (array[string]) :abbr:`💥 (Maybe omitted)` - Linked messages
* ``uploads`` (array[string]) :abbr:`💥 (Maybe omitted)` - Task uploads

.. _tdproto-TaskColor:

TaskColor
-------------------------------------------------------------

Task color rules color

**Fields**:

* ``regular`` (:ref:`tdproto-RGBColor`) - Regular color
* ``dark`` (:ref:`tdproto-RGBColor`) - Dark color
* ``light`` (:ref:`tdproto-RGBColor`) - Light color

.. _tdproto-TaskCounters:

TaskCounters
-------------------------------------------------------------

Tasks counters

**Fields**:

* ``jid`` (:ref:`tdproto-JID`) - Task jid
* ``num_unread`` (number) :abbr:`💥 (Maybe omitted)` - Unreads counter
* ``num_unread_notices`` (number) :abbr:`💥 (Maybe omitted)` - Mentions (@) counter

.. _tdproto-TaskFilter:

TaskFilter
-------------------------------------------------------------

Task filter

**Fields**:

* ``field`` (:ref:`tdproto-TaskFilterKey`) - Task filter field
* ``title`` (string) - Filter title

.. _tdproto-TaskItem:

TaskItem
-------------------------------------------------------------

Task checklist item

**Fields**:

* ``uid`` (string) :abbr:`💥 (Maybe omitted)` - Id
* ``sort_ordering`` (number) :abbr:`💥 (Maybe omitted)` - Sort ordering
* ``text`` (string) - Text or "#{OtherTaskNumber}"
* ``checked`` (boolean) :abbr:`💥 (Maybe omitted)` - Item checked
* ``can_toggle`` (boolean) :abbr:`💥 (Maybe omitted)` - Can I toggle this item
* ``subtask`` (:ref:`tdproto-Subtask`) :abbr:`💥 (Maybe omitted)` - Link to subtask. Optional

.. _tdproto-TaskSort:

TaskSort
-------------------------------------------------------------

Task sort type

**Fields**:

* ``key`` (:ref:`tdproto-TaskSortKey`) - Field
* ``title`` (string) - Sort title

.. _tdproto-TaskStatus:

TaskStatus
-------------------------------------------------------------

Custom task status

**Fields**:

* ``uid`` (string) :abbr:`💥 (Maybe omitted)` - Status id
* ``sort_ordering`` (number) - Status sort ordering
* ``name`` (string) - Status internal name
* ``title`` (string) - Status localized name
* ``is_archive`` (boolean) :abbr:`💥 (Maybe omitted)` - Status not used anymore

.. _tdproto-TaskTab:

TaskTab
-------------------------------------------------------------

Task tab

**Fields**:

* ``key`` (:ref:`tdproto-TaskTabKey`) - Tab name
* ``title`` (string) - Tab title
* ``hide_empty`` (boolean) - Disable this tab when it has no contents
* ``show_counter`` (boolean) - Show unread badge
* ``pagination`` (boolean) - Enable pagination
* ``filters`` (array[:ref:`tdproto-TaskFilter`]) - Filters inside tab
* ``sort`` (array[:ref:`tdproto-TaskSort`]) - Sort available in tab
* ``unread_tasks`` (array[:ref:`tdproto-TaskCounters`]) - Unread tasks with jid and counters

.. _tdproto-Team:

Team
-------------------------------------------------------------

Team

**Fields**:

* ``uid`` (string) - Team id
* ``is_archive`` (boolean) :abbr:`💥 (Maybe omitted)` - Team deleted
* ``gentime`` (number) - Object version
* ``name`` (string) - Team name
* ``default_task_deadline`` (string) :abbr:`💥 (Maybe omitted)` - Default task deadline
* ``max_message_update_age`` (number) - Max message update/deletion age, in seconds
* ``icons`` (:ref:`tdproto-IconData`) - Team icons
* ``last_active`` (boolean) - User last activity was in this team
* ``changeable_statuses`` (array[:ref:`tdproto-TeamStatus`]) :abbr:`💥 (Maybe omitted)` - What status I can set to other team members
* ``bad_profile`` (boolean) :abbr:`💥 (Maybe omitted)` - My profile in this team isn't full
* ``need_confirmation`` (boolean) - Need confirmation after invite to this team
* ``use_patronymic`` (boolean) :abbr:`💥 (Maybe omitted)` - Patronymic in usernames for this team
* ``user_fields`` (array[string]) - Username fields ordering
* ``display_family_name_first`` (boolean) :abbr:`💥 (Maybe omitted)` - Family name should be first in display name
* ``use_task_importance`` (boolean) :abbr:`💥 (Maybe omitted)` - Use importance field in task
* ``task_importance_min`` (number) :abbr:`💥 (Maybe omitted)` - Minimal value of task importance. Default is 1
* ``task_importance_max`` (number) :abbr:`💥 (Maybe omitted)` - Maximum value of task importance. Default is 5
* ``task_importance_rev`` (boolean) :abbr:`💥 (Maybe omitted)` - Bigger number = bigger importance. Default: lower number = bigger importance
* ``use_task_urgency`` (boolean) :abbr:`💥 (Maybe omitted)` - Use urgency field in task
* ``use_task_complexity`` (boolean) :abbr:`💥 (Maybe omitted)` - Use complexity field in task
* ``use_task_spent_time`` (boolean) :abbr:`💥 (Maybe omitted)` - Use spent time field in task
* ``uploads_size`` (number) :abbr:`💥 (Maybe omitted)` - Total uploads size, bytes
* ``uploads_size_limit`` (number) :abbr:`💥 (Maybe omitted)` - Maximum uploads size, bytes, if any
* ``unread`` (:ref:`tdproto-TeamUnread`) :abbr:`0️⃣ (Might be null)` - Unread message counters
* ``me`` (:ref:`tdproto-Contact`) - My profile in this team
* ``contacts`` (array[:ref:`tdproto-Contact`]) :abbr:`💥 (Maybe omitted)` - Team contacts. Used only for team creation
* ``single_group`` (:ref:`tdproto-JID`) :abbr:`💥 (Maybe omitted)` - For single group teams, jid of chat
* ``theme`` (:ref:`tdproto-Theme`) :abbr:`💥 (Maybe omitted)` - Color theme, if any
* ``hide_archived_users`` (boolean) :abbr:`💥 (Maybe omitted)` - Don't show archived users by default
* ``pinned`` (boolean) :abbr:`💥 (Maybe omitted)` - Team pinned

.. _tdproto-TeamCounter:

TeamCounter
-------------------------------------------------------------

Unread message counters

**Fields**:

* ``uid`` (string) - Team id
* ``unread`` (:ref:`tdproto-TeamUnread`) - Unread message counters

.. _tdproto-TeamShort:

TeamShort
-------------------------------------------------------------

Short team representation. For invites, push notifications, etc. Readonly

**Fields**:

* ``uid`` (string) - Team id
* ``name`` (string) - Team name
* ``icons`` (:ref:`tdproto-IconData`) - Team icons

.. _tdproto-Terms:

Terms
-------------------------------------------------------------

Experimental translation fields for "team" entity renaming. Readonly

**Fields**:

* ``EnInTeam`` (string) - "in team"
* ``EnTeam`` (string) - "team"
* ``EnTeamAccess`` (string) - "access to team"
* ``EnTeamAdmin`` (string) - "team admin"
* ``EnTeamAdmins`` (string) - "team admins"
* ``EnTeamGuest`` (string) - "team guest"
* ``EnTeamMember`` (string) - "team member"
* ``EnTeamMembers`` (string) - "team members"
* ``EnTeamOwner`` (string) - "team owner",
* ``EnTeamSettings`` (string) - "team settings"
* ``RuTeamSettings`` (string) - "настройки команды"
* ``EnTeams`` (string) - "teams"
* ``EnToTeam`` (string) - "to team"
* ``RuInTeam`` (string) - "в команде"
* ``RuTeam`` (string) - "команда"
* ``RuTeamAccess`` (string) - "доступ к команде"
* ``RuTeamAdmin`` (string) - "администратор команды"
* ``RuTeamAdmins`` (string) - "администраторы команды"
* ``RuTeamD`` (string) - "команде"
* ``RuTeamGuest`` (string) - "гость команды"
* ``RuTeamMember`` (string) - "участник команды"
* ``RuTeamMembers`` (string) - "участники команды"
* ``RuTeamOwner`` (string) - "владелец команды"
* ``RuTeamP`` (string) - "команде"
* ``RuTeamR`` (string) - "команды"
* ``RuTeams`` (string) - "команды"
* ``RuTeamsD`` (string) - "командам"
* ``RuTeamsP`` (string) - "командах"
* ``RuTeamsR`` (string) - "команд"
* ``RuTeamsT`` (string) - "командами"
* ``RuTeamsV`` (string) - "команды"
* ``RuTeamT`` (string) - "командой"
* ``RuTeamV`` (string) - "команду"
* ``RuToTeam`` (string) - "в команду"

.. _tdproto-Theme:

Theme
-------------------------------------------------------------

Color theme

**Fields**:

* ``BgColor`` (:ref:`tdproto-RGBColor`) - BgColor for web
* ``BgHoverColor`` (:ref:`tdproto-RGBColor`) - BgHoverColor for web
* ``TextColor`` (:ref:`tdproto-RGBColor`) - TextColor for web
* ``MutedTextColor`` (:ref:`tdproto-RGBColor`) - MutedTextColor for web
* ``AccentColor`` (:ref:`tdproto-RGBColor`) - AccentColor for web
* ``AccentHoverColor`` (:ref:`tdproto-RGBColor`) - AccentHoverColor for web
* ``TextOnAccentHoverColor`` (:ref:`tdproto-RGBColor`) - TextOnAccentHoverColor for web
* ``MainAccent`` (:ref:`tdproto-RGBColor`) - MainAccent for web
* ``MainAccentHover`` (:ref:`tdproto-RGBColor`) - MainAccentHover for web
* ``MainLightAccent`` (:ref:`tdproto-RGBColor`) - MainLightAccent for web
* ``MainLink`` (:ref:`tdproto-RGBColor`) - MainLink for web
* ``brand`` (:ref:`tdproto-RGBColor`) - Brand color for app
* ``brand_dark`` (:ref:`tdproto-RGBColor`) - BrandDark color for app
* ``brand_light`` (:ref:`tdproto-RGBColor`) - Brand light color for app
* ``back`` (:ref:`tdproto-RGBColor`) - Back light color for app
* ``back_light`` (:ref:`tdproto-RGBColor`) - Back light color for app
* ``back_dark`` (:ref:`tdproto-RGBColor`) - Back dark color for app
* ``success`` (:ref:`tdproto-RGBColor`) - Success color for app
* ``success_light`` (:ref:`tdproto-RGBColor`) - Success light color for app
* ``error`` (:ref:`tdproto-RGBColor`) - Error color for app
* ``error_light`` (:ref:`tdproto-RGBColor`) - Error light color for app
* ``background`` (:ref:`tdproto-RGBColor`) - Background color for app
* ``tab_background`` (:ref:`tdproto-RGBColor`) - Tab background color for app
* ``chat_input_background`` (:ref:`tdproto-RGBColor`) - Chat input background color for app
* ``substrate_background`` (:ref:`tdproto-RGBColor`) - Substrate background color for app
* ``modal_background`` (:ref:`tdproto-RGBColor`) - Modal background color for app
* ``title_background`` (:ref:`tdproto-RGBColor`) - Title background color for app
* ``attention`` (:ref:`tdproto-RGBColor`) - Attention color for app
* ``attention_light`` (:ref:`tdproto-RGBColor`) - Attention light color for app
* ``font`` (:ref:`tdproto-FontColors`) :abbr:`0️⃣ (Might be null)` - Font colors for app
* ``message`` (:ref:`tdproto-MessageColors`) :abbr:`0️⃣ (Might be null)` - Message colors for app
* ``switcher`` (:ref:`tdproto-SwitcherColors`) :abbr:`0️⃣ (Might be null)` - Switcher colors for app
* ``button`` (:ref:`tdproto-ButtonColors`) :abbr:`0️⃣ (Might be null)` - Button colors for app
* ``input`` (:ref:`tdproto-InputColors`) :abbr:`0️⃣ (Might be null)` - Input colors for app
* ``ic`` (:ref:`tdproto-IconColors`) :abbr:`0️⃣ (Might be null)` - Icon colors for app
* ``AppAccentColor`` (:ref:`tdproto-RGBColor`) - Deprecated
* ``AppPrimaryColor`` (:ref:`tdproto-RGBColor`) - Deprecated

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
* ``duration`` (number) :abbr:`💥 (Maybe omitted)` - Mediafile duration (for audio/video only)
* ``name`` (string) - Filename
* ``url`` (string) - Absolute url
* ``preview`` (:ref:`tdproto-UploadPreview`) :abbr:`💥 (Maybe omitted)` - Preview details
* ``content_type`` (string) - Content type
* ``animated`` (boolean) :abbr:`💥 (Maybe omitted)` - Is animated (images only)
* ``blurhash`` (string) :abbr:`💥 (Maybe omitted)` - Compact representation of a placeholder for an image (images only)
* ``processing`` (boolean) :abbr:`💥 (Maybe omitted)` - File still processing (video only)
* ``pdf_version`` (:ref:`tdproto-PdfVersion`) :abbr:`💥 (Maybe omitted)` - PDF version of file. Experimental
* ``type`` (:ref:`tdproto-UploadMediaType`) - ?type=file,image,audio,video

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

* ``upload`` (:ref:`tdproto-Upload`) - Upload information
* ``message`` (:ref:`tdproto-ShortMessage`) - Short message information

.. _tdproto-User:

User
-------------------------------------------------------------

Account data

**Fields**:

* ``phone`` (string) :abbr:`💥 (Maybe omitted)` - Phone for login
* ``email`` (string) :abbr:`💥 (Maybe omitted)` - Email for login
* ``family_name`` (string) :abbr:`💥 (Maybe omitted)` - Family name
* ``given_name`` (string) :abbr:`💥 (Maybe omitted)` - Given name
* ``patronymic`` (string) :abbr:`💥 (Maybe omitted)` - Patronymic, if any
* ``default_lang`` (string) :abbr:`💥 (Maybe omitted)` - Default language code
* ``alt_send`` (boolean) - Use Ctrl/Cmd + Enter instead Enter
* ``asterisk_mention`` (boolean) - Use * as @ for mentions
* ``always_send_pushes`` (boolean) - Send pushes even user is online
* ``unread_first`` (boolean) - Show unread chats in chat list first
* ``munread_first`` (boolean) - Show unread chats in chat list first on mobiles
* ``timezone`` (string) - Timezone
* ``quiet_time_start`` (string) :abbr:`0️⃣ (Might be null)` - Start silently time (no pushes, no sounds)
* ``quiet_time_finish`` (string) :abbr:`0️⃣ (Might be null)` - Finish silently time (no pushes, no sounds)

.. _tdproto-UserWithMe:

UserWithMe
-------------------------------------------------------------

Account data with extra information

**Fields**:

* ``inviter`` (:ref:`tdproto-JID`) :abbr:`💥 (Maybe omitted)` - Inviter id, if any
* ``teams`` (array[:ref:`tdproto-Team`]) - Available teams
* ``devices`` (array[:ref:`tdproto-PushDevice`]) - Registered push devices
* ``phone`` (string) :abbr:`💥 (Maybe omitted)` - Phone for login
* ``email`` (string) :abbr:`💥 (Maybe omitted)` - Email for login
* ``family_name`` (string) :abbr:`💥 (Maybe omitted)` - Family name
* ``given_name`` (string) :abbr:`💥 (Maybe omitted)` - Given name
* ``patronymic`` (string) :abbr:`💥 (Maybe omitted)` - Patronymic, if any
* ``default_lang`` (string) :abbr:`💥 (Maybe omitted)` - Default language code
* ``alt_send`` (boolean) - Use Ctrl/Cmd + Enter instead Enter
* ``asterisk_mention`` (boolean) - Use * as @ for mentions
* ``always_send_pushes`` (boolean) - Send pushes even user is online
* ``unread_first`` (boolean) - Show unread chats in chat list first
* ``munread_first`` (boolean) - Show unread chats in chat list first on mobiles
* ``timezone`` (string) - Timezone
* ``quiet_time_start`` (string) :abbr:`0️⃣ (Might be null)` - Start silently time (no pushes, no sounds)
* ``quiet_time_finish`` (string) :abbr:`0️⃣ (Might be null)` - Finish silently time (no pushes, no sounds)

.. _tdproto-Wallpaper:

Wallpaper
-------------------------------------------------------------

Chat wallpaper

**Fields**:

* ``key`` (string) - Unique identifier
* ``name`` (string) - Localized description
* ``url`` (string) - Url to jpg or png

HTTP Queries
============================

.. _tdproto-TaskFilterQuery:

TaskFilter
-------------------------------------------------------------

Query parameters for listing messages

* ``assignee`` - * ?assignee=jid,jid
* ``created_gte`` - * ?created_gte=<isodate>
* ``created_lte`` - * ?created_lte=<isodate>
* ``deadline_gte`` - * ?deadline_gte=<isodate>
* ``deadline_lte`` - * ?deadline_lte=<isodate>
* ``done_gte`` - * ?done_gte=<isodate>
* ``done_lte`` - * ?done_lte=<isodate>
* ``exclude_task_status`` - * ?exclude_task_status = new,done | new | any
* ``gentime_gt`` - gentime great than group/chat
* ``member`` - * ?member=jid,jid
* ``num`` - * ?num=num1,num2,num3..
* ``observer`` - * ?observer=jid,jid // TODO: rename to ?follower=
* ``owner`` - * ?owner=jid,jid
* ``public`` - * ?public=true|false
* ``q`` - * ?q=
* ``section`` - * ?section=[ uid,uid... | "-" ]
* ``short`` - * ?short=true|false
* ``sort`` - * ?sort = [ "created" | "-created" | "last_message" | "-last_message" | "deadline" | "-deadline" ]
* ``tag`` - * ?tag=[ tag,tag,tag... | "-" ]
* ``task_status`` - * ?task_status = new,done | new | any
