
Enums index
============================

.. tdproto:enum:: ChatType
  :tdpackage: tdmodels

  **Possible values**:

  * direct
  * group
  * task


.. tdproto:enum:: GroupStatus
  :tdpackage: tdmodels

  **Possible values**:

  * admin
  * member


.. tdproto:enum:: MarkupType
  :tdpackage: tdmodels

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


.. tdproto:enum:: Mediasubtype
  :tdpackage: tdmodels

  **Possible values**:

  * sticker
  * newtask


.. tdproto:enum:: Mediatype
  :tdpackage: tdmodels

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


.. tdproto:enum:: TeamStatus
  :tdpackage: tdmodels

  **Possible values**:

  * owner
  * admin
  * member
  * guest


.. tdproto:enum:: UploadMediaType
  :tdpackage: tdmodels

  **Possible values**:

  * file
  * image
  * video
  * audio
  * imagefile


Type aliases
============================

.. tdproto:type:: ActiveUserDailyStatList
  :tdpackage: tdmodels

  
  **Base Type**: ActiveUserDailyStat

  **Is array**

.. tdproto:type:: BotCommands
  :tdpackage: tdmodels

  
  Bot commands list
  
  **Base Type**: BotCommand

  **Is array**

.. tdproto:type:: Err
  :tdpackage: tdmodels

  
  **Base Type**: string

.. tdproto:type:: ISODateTimeString
  :tdpackage: tdmodels

  
  Date and time in RFC3339 format. Example: ``2019-09-18T00:00:07.435409Z``
  
  **Base Type**: string

.. tdproto:type:: JID
  :tdpackage: tdmodels

  
  **Base Type**: string

.. tdproto:type:: MessageLinks
  :tdpackage: tdmodels

  
  **Base Type**: MessageLink

  **Is array**

.. tdproto:type:: PushDeviceType
  :tdpackage: tdmodels

  
  **Base Type**: int

.. tdproto:type:: RGBColor
  :tdpackage: tdmodels

  
  Color in ``#rrggbb`` format where ``rr``, ``gg``, ``bb`` are hexadecimal numbers from 00 to ff of red, green and blue channels correspondingly. (yellow would be ``#ffff00``)
  
  **Base Type**: string

.. tdproto:type:: SharpLinks
  :tdpackage: tdmodels

  
  #-links autocomplete response
  
  **Base Type**: SharpLink

  **Is array**

.. tdproto:type:: TaskFilterKey
  :tdpackage: tdmodels

  
  **Base Type**: string

.. tdproto:type:: TaskSortKey
  :tdpackage: tdmodels

  
  **Base Type**: string

.. tdproto:type:: TaskTabKey
  :tdpackage: tdmodels

  
  **Base Type**: string

JSON objects index
============================

.. tdproto:struct:: BotCommand
  :tdpackage: tdmodels

  Bot commands information

  :field key string: What should be inserted to the chat
  :field title string: What should be visible by user
  :field args array[string]: Command options, if any

.. tdproto:struct:: ButtonColors
  :tdpackage: tdmodels

  ButtonColors button colors for app

  :field brand_static `tdproto-RGBColor`: Brand static color
  :field brand_active `tdproto-RGBColor`: Brand active color
  :field brand_disable `tdproto-RGBColor`: Brand disable color
  :field simple_static `tdproto-RGBColor`: Simple static color
  :field simple_active `tdproto-RGBColor`: Simple active color
  :field simple_disable `tdproto-RGBColor`: Simple disable color

.. tdproto:struct:: CallDevice
  :tdpackage: tdmodels

  Call participant device

  :field muted boolean: Device muted
  :field useragent string: Device description

.. tdproto:struct:: CallOnliner
  :tdpackage: tdmodels

  Call participant

  :field jid `tdproto-JID`: Contact id
  :field display_name string: Contact name
  :field role string: Contact role
  :field icon string: Contact icon
  :field muted boolean: Microphone muted. Computed from devices muted states
  :field devices array[`tdproto-CallDevice`]: Member devices, strictly one for now

.. tdproto:struct:: Chat
  :tdpackage: tdmodels

  Chat (direct, group, task) representation

  :field jid `tdproto-JID`: Group/Task/Contact id
  :field chat_type `tdproto-ChatType`: Chat type
  :field base_gentime number omitempty: Base fields (not related to concrete participant) version
  :field gentime number: Chat fields related to concrete participant) version
  :field created string: Creation date, iso datetime
  :field display_name string: Title
  :field icons `tdproto-IconData`: Icons info
  :field counters_enabled boolean omitempty: Include unread messages to counters
  :field can_call boolean omitempty: Can I call to this chat
  :field can_send_message boolean omitempty: Can I send message to this chat
  :field cant_send_message_reason string omitempty: Why I can't send message to this chat (if can't)
  :field collapsed boolean omitempty: Description collapsed. Used for tasks only
  :field draft string omitempty: Last message draft, if any
  :field draft_gentime number omitempty: Last message draft version, if any
  :field hidden boolean omitempty: Hidden chat
  :field notifications_enabled boolean omitempty: Push notifications enabled
  :field num_importants number omitempty: Number of important messages
  :field num_unread number omitempty: Unread counter
  :field num_unread_notices number omitempty: Mentions (@) counter
  :field last_message `tdproto-Message` omitempty: Last message object
  :field last_read_message_id string omitempty: Last read message id, if any
  :field section string omitempty: Project / section id, if any
  :field changeable_fields array[string] omitempty: List of editable fields
  :field pinned boolean omitempty: Is chat pinned on top
  :field pinned_sort_ordering number omitempty: Sort ordering for pinned chat
  :field num_members number omitempty: Non-archive participants number
  :field can_delete boolean omitempty: Can I delete this chat
  :field description string omitempty: Group or task description
  :field markup array[`tdproto-MarkupEntity`] omitempty: Markup entities for description field. Experimental
  :field feed boolean omitempty: Present in feed (main screen)
  :field pinned_message `tdproto-Message` omitempty: Pinned message for this chat
  :field color_index number omitempty: Custom color index from table of colors. Tasks only
  :field num_items number omitempty: Items in checklist. Tasks only
  :field num_checked_items number omitempty: Checked items in checklist. Tasks only
  :field assignee `tdproto-JID` omitempty: Assignee contact id. Tasks only
  :field num number omitempty: Task number in this team
  :field observers array[`tdproto-JID`] omitempty: Task followers id's. TODO: rename to "followers"
  :field owner `tdproto-JID` omitempty: Task creator
  :field task_status string omitempty: Task status. May be custom
  :field title string omitempty: Task title. Generated from number and description
  :field done string omitempty: Task done date in iso format, if any
  :field done_reason string omitempty: Task done reason, if any
  :field deadline string omitempty: Task deadline in iso format, if any
  :field deadline_expired boolean omitempty: Is task deadline expired
  :field links `tdproto-MessageLinks` omitempty: Links in description
  :field tags array[string] omitempty: Task tags list, if any
  :field importance number omitempty: Task importance, if available in team
  :field urgency number omitempty: Task urgency, if available in team
  :field spent_time number omitempty: Task spent time, number
  :field complexity number omitempty: Task complexity, number
  :field linked_messages array[any] omitempty: Used for "Create task from messages..."
  :field uploads array[`tdproto-Upload`] omitempty: Upload uids for request, upload objects for response
  :field items array[`tdproto-TaskItem`] omitempty: Checklist items. Task only
  :field parents array[`tdproto-Subtask`] omitempty: Parent tasks
  :field tabs array[`tdproto-TaskTabKey`] omitempty: Tab names
  :field status `tdproto-GroupStatus` omitempty: My status in group chat
  :field members array[`tdproto-GroupMembership`] omitempty: Group chat members
  :field can_add_member boolean omitempty: Can I add member to this group chat
  :field can_remove_member boolean omitempty: Can I remove member from this group chat
  :field can_change_member_status boolean omitempty: Can I change member status in this group chat
  :field can_change_settings boolean omitempty: deprecated: use changeable fields
  :field default_for_all boolean omitempty: Any new team member will be added to this group chat
  :field readonly_for_members boolean omitempty: Readonly for non-admins group chat (Like Channels in Telegram but switchable)
  :field autocleanup_age number omitempty: Delete messages in this chat in seconds. Experimental function
  :field public boolean omitempty: Can other team member see this task/group chat
  :field can_join boolean omitempty: Can I join to this public group/task
  :field can_delete_any_message boolean omitempty: Can I delete any message in this chat
  :field can_set_important_any_message boolean omitempty: Can I change Important flag in any message in this chat
  :field last_activity string omitempty: Date of the last message sent even if it was deleted
  :field draft_num number omitempty: Deprecated

.. tdproto:struct:: ChatShort
  :tdpackage: tdmodels

  Minimal chat representation

  :field jid `tdproto-JID`: Group/Task/Contact id
  :field chat_type `tdproto-ChatType`: Chat type
  :field display_name string: Title
  :field icons `tdproto-IconData`: Icon data

.. tdproto:struct:: ColorRule
  :tdpackage: tdmodels

  Set of rules to apply to tasks for coloring

  :field uid string: Rule id
  :field priority number: Rule priority
  :field description string omitempty: Rule description
  :field color_index number: Color index
  :field section_enabled boolean omitempty: Project filter enabled
  :field section string omitempty: Project id if project filter enabled
  :field tags_enabled boolean omitempty: Tags filter enabled
  :field tags array[string] omitempty: Tag ids if tags filter enabled
  :field task_status string omitempty: Task status
  :field task_importance_enabled boolean omitempty: Task importance filter enabled
  :field task_importance number omitempty: Task importance if task importance filter enabled
  :field task_urgency_enabled boolean omitempty: Task urgency filter enabled
  :field task_urgency number omitempty: Task urgency if task urgency filter enabled

.. tdproto:struct:: Contact
  :tdpackage: tdmodels

  Contact

  :field jid `tdproto-JID`: Contact Id
  :field node string omitempty: Node uid for external users
  :field display_name string: Full name in chats
  :field short_name string: Short name in chats
  :field contact_email string: Contact email in this team
  :field contact_phone string: Contact phone in this team
  :field icons `tdproto-IconData`: Icons data
  :field gentime number: Object version
  :field role string: Role in this team
  :field mood string omitempty: Mood in this team
  :field status `tdproto-TeamStatus`: Status in this team
  :field last_activity string omitempty: Last activity in this team (iso datetime)
  :field is_archive boolean omitempty: Contact deleted
  :field botname string omitempty: Bot name. Empty for users
  :field sections array[string]: Section ids
  :field can_send_message boolean omitempty: Can I send message to this contact
  :field cant_send_message_reason string omitempty: Why I can't send message to this chat (if can't)
  :field can_call boolean omitempty: Can I call to this contact
  :field can_create_task boolean omitempty: Can I create task for this contact
  :field can_import_tasks boolean omitempty: Can I import tasks in this team
  :field can_add_to_group boolean omitempty: Can I add this contact to group chats
  :field can_delete boolean omitempty: Can I remove this contact from team
  :field changeable_fields array[string] omitempty: Changeable fields
  :field family_name string omitempty: Family name
  :field given_name string omitempty: Given name
  :field patronymic string omitempty: Patronymic, if any
  :field default_lang string omitempty: Default language code
  :field debug_show_activity boolean omitempty: Enable debug messages in UI
  :field dropall_enabled boolean omitempty: Enable remove all messages experimental features
  :field alt_send boolean omitempty: Use Ctrl/Cmd + Enter instead Enter
  :field asterisk_mention boolean omitempty: Use * as @ for mentions
  :field always_send_pushes boolean omitempty: Send push notifications even contact is online
  :field hide_pushes_content boolean omitempty: Hide pushes body
  :field timezone string omitempty: Timezone, if any
  :field quiet_time_start string omitempty: Quiet time start
  :field quiet_time_finish string omitempty: Quiet time finish
  :field focus_until string omitempty: Focus mode enabled until
  :field group_notifications_enabled boolean omitempty: Push notifications for group chats
  :field task_notifications_enabled boolean omitempty: Push notifications for task chats
  :field contact_short_view boolean omitempty: Short view in contact list
  :field group_short_view boolean omitempty: Short view in group list
  :field task_short_view boolean omitempty: Short view in task list
  :field contact_mshort_view boolean omitempty: Short view in contact list in mobile app
  :field group_mshort_view boolean omitempty: Short view in group list in mobile app
  :field auth_2fa_enabled boolean omitempty: Two-factor authentication is configured and confirmed
  :field auth_2fa_status string omitempty: Two-factor authentication status
  :field task_mshort_view boolean omitempty: Short view in task list in mobile app
  :field contact_show_archived boolean omitempty: Show archived contacts in contact list
  :field unread_first boolean omitempty: Show unread chats first in feed
  :field munread_first boolean omitempty: Show unread chats first in feed in mobile app
  :field can_add_to_team boolean omitempty: Can I add new members to this team
  :field can_manage_sections boolean omitempty: Can I manage contact sections in this team
  :field can_manage_projects boolean omitempty: Can I manage task projects in this team
  :field can_manage_tags boolean omitempty: Can I manage tags in this team
  :field can_manage_integrations boolean omitempty: Can I manage integrations in this team
  :field can_manage_color_rules boolean omitempty: Can I manage color rules in this team
  :field can_create_group boolean omitempty: Can I create group chats in this team
  :field can_join_public_groups boolean omitempty: Can I view/join public group in this team
  :field can_join_public_tasks boolean omitempty: Can I view/join public tasks in this team
  :field custom_fields `tdproto-ContactCustomFields` omitempty: Extra contact fields
  :field can_delete_any_message boolean omitempty: Deprecated

.. tdproto:struct:: ContactCustomFields
  :tdpackage: tdmodels

  Extra contact fields

  :field company string omitempty: Company
  :field department string omitempty: Department
  :field title string omitempty: Title
  :field mobile_phone string omitempty: MobilePhone
  :field source string omitempty: Import source
  :field ad_uid string omitempty: User UUID in Active Directory

.. tdproto:struct:: ContactShort
  :tdpackage: tdmodels

  Short contact representation

  :field jid `tdproto-JID`: Contact Id
  :field display_name string: Full name in chats
  :field short_name string: Short name in chats
  :field icons `tdproto-IconData`: Icons data
  :field gentime number: Object version

.. tdproto:struct:: Country
  :tdpackage: tdmodels

  Country for phone numbers selection on login screen

  :field code string: Phone code
  :field iso string: Country ISO code
  :field name string: Country name
  :field default boolean omitempty: Selected by default
  :field popular boolean omitempty: Is popular, need to cache

.. tdproto:struct:: DeletedChat
  :tdpackage: tdmodels

  Minimal chat representation for deletion

  :field jid `tdproto-JID`: Group/Task/Contact id
  :field chat_type `tdproto-ChatType`: Chat type
  :field gentime number: Chat fields (related to concrete participant) version
  :field is_archive boolean: Archive flag. Always true for this structure

.. tdproto:struct:: DeletedRemind
  :tdpackage: tdmodels

  Remind deleted message

  :field uid string: Remind id

.. tdproto:struct:: DeletedSection
  :tdpackage: tdmodels

  Deleted task project or contact section

  :field uid string: Section uid
  :field gentime number: Object version

.. tdproto:struct:: DeletedTag
  :tdpackage: tdmodels

  Delete tag message

  :field uid string: Tag id

.. tdproto:struct:: DeletedTeam
  :tdpackage: tdmodels

  Team deletion message. Readonly

  :field uid string: Team id
  :field is_archive boolean: Team deleted
  :field gentime number: Object version

.. tdproto:struct:: EasyApiMessage
  :tdpackage: tdmodels

  Simple api for integrations /api/message or /tasks/[team]/[num]/message

  :field key string: Comma separated api keys (for /api/message calls only)
  :field message string: Message text. Required
  :field message_id string: Message uuid. Optional
  :field nopreview boolean: Disable links preview
  :field important boolean: Mark message as important
  :field silently boolean: Disable counters and push notifications
  :field convert_linebreaks boolean: Convert "\\n" to "\n"

.. tdproto:struct:: Emoji
  :tdpackage: tdmodels

  Emoji

  :field char string: Unicode symbol
  :field key string: Text representation

.. tdproto:struct:: Features
  :tdpackage: tdmodels

  Server information. Readonly

  :field host string: Current host
  :field build string: Build/revision of server side
  :field desktop_version string: Desktop application version
  :field front_version string: Webclient version
  :field app_title string: Application title
  :field landing_url string omitempty: Landing page address, if any
  :field app_schemes array[string]: Local applications urls
  :field userver string: Static files server address
  :field ios_app string: Link to AppStore
  :field android_app string: Link to Google Play
  :field ios_corp_app string: Link to AppStore for corporate app
  :field android_corp_app string: Link to Google Play for corporate app
  :field theme string: Default UI theme
  :field min_ios_version string: Minimal iOS application version required for this server. Used for breaking changes
  :field min_android_version string: Minimal android application version required for this server. Used for breaking changes
  :field min_corp_ios_version string: Minimal iOS corp application version required for this server. Used for breaking changes
  :field min_corp_android_version string: Minimal android corp application version required for this server. Used for breaking changes
  :field free_registration boolean: Free registration allowed
  :field max_upload_mb number: Maximum size of user's upload
  :field max_linked_messages number: Maximum number of forwarded messages
  :field max_message_uploads number: Maximum number of message uploads
  :field max_username_part_length number: Maximum chars for: family_name, given_name, patronymic if any
  :field max_group_title_length number: Maximum chars for group chat name
  :field max_team_title_length number: Maximum chars for team name
  :field max_role_length number: Maximum chars for role in team
  :field max_mood_length number: Maximum chars for mood in team
  :field max_message_length number: Maximum chars for text message
  :field max_section_length number: Maximum length for contact's sections names
  :field max_project_length number: Maximum length for project
  :field max_tag_length number: Maximum length for tags
  :field max_task_title_length number: Maximum length for task title
  :field max_color_rule_description_length number: Maximum length for ColorRule description
  :field max_url_length number: Maximum length for urls
  :field max_integration_comment_length number: Maximum length for Integration comment
  :field max_teams number: Maximum teams for one account
  :field max_message_search_limit number: Maximum search result
  :field multi_nodes boolean omitempty: Multi nodes mode (federation) enabled
  :field afk_age number: Max inactivity seconds
  :field auth_by_password boolean omitempty: Password authentication enabled
  :field auth_by_qr_code boolean omitempty: QR-code / link authentication enabled
  :field auth_by_sms boolean omitempty: SMS authentication enabled
  :field auth_2fa boolean omitempty: Two-factor authentication (2FA) enabled
  :field is_pin_code_required boolean: Mandatory setting of the pin code in the application
  :field pin_code_wrong_limit number: Max number of attempts to enter an invalid PIN code
  :field oauth_services array[`tdproto-OAuthService`] omitempty: External services
  :field ice_servers array[`tdproto-ICEServer`]: ICE servers for WebRTC
  :field custom_server boolean: True for premise installation
  :field installation_type string: Name of installation
  :field installation_title string omitempty: Installation title, used on login screen
  :field custom_app_icon_name string omitempty: Custom application icon name, if any
  :field app_login_background string omitempty: AppBackground image url, if any
  :field web_login_background string omitempty: WebBackground image url, if any
  :field is_testing boolean: Testing installation
  :field metrika string: Yandex metrika counter id
  :field amplitude_api_key string omitempty: Amplitude api key
  :field min_search_length number: Minimal chars number for starting global search
  :field resend_timeout number: Resend message in n seconds if no confirmation from server given
  :field sentry_dsn_js string: Frontend sentry.io settings
  :field server_drafts boolean: Message drafts saved on server
  :field firebase_app_id string: Firebase settings for web-push notifications
  :field firebase_sender_id string: Firebase settings for web-push notifications
  :field firebase_api_key string: Firebase settings for web-push notifications
  :field firebase_auth_domain string: Firebase settings for web-push notifications
  :field firebase_database_url string: Firebase settings for web-push notifications
  :field firebase_project_id string: Firebase settings for web-push notifications
  :field firebase_storage_bucket string: Firebase settings for web-push notifications
  :field calls_version number: Calls version. 0 = disabled, 1 = audio only, 2 = audio+video
  :field mobile_calls boolean: Calls functions enabled for mobile applications
  :field calls_record boolean: Calls record enabled
  :field only_one_device_per_call boolean omitempty: Disallow call from multiple devices. Experimental
  :field max_participants_per_call number omitempty: Maximum number of participants per call
  :field safari_push_id string: Safari push id for web-push notifications
  :field message_uploads boolean: Multiple message uploads
  :field terms `tdproto-Terms`: Team entity naming. Experimental
  :field single_group_teams boolean: Cross team communication. Experimental
  :field wiki_pages boolean: Wiki pages in chats. Experimental
  :field allow_admin_mute boolean omitempty: Wiki pages in chats. Experimental
  :field default_wallpaper `tdproto-Wallpaper` omitempty: Default wallpaper url for mobile apps, if any
  :field support_email string: Support email
  :field custom_theme boolean: True if server has custom theme
  :field task_checklist boolean: Deprecated
  :field readonly_groups boolean: Deprecated
  :field task_dashboard boolean: Deprecated
  :field task_messages boolean: Deprecated
  :field task_public boolean: Deprecated
  :field task_tags boolean: Deprecated
  :field calls boolean: Deprecated
  :field min_app_version string: Deprecated
  :field file_extension_whitelist array[string]: File Extension Whitelist
  :field file_extension_blacklist array[string]: File Extension Blacklist
  :field file_extension_whitelist_priority boolean: File Extension Whitelist Priority

.. tdproto:struct:: FontColors
  :tdpackage: tdmodels

  FontColors font colors for app

  :field text `tdproto-RGBColor`: Text color
  :field title `tdproto-RGBColor`: Title color
  :field sub `tdproto-RGBColor`: Sub color
  :field brand_button `tdproto-RGBColor`: Brand button color
  :field simple_button `tdproto-RGBColor`: Simple button color
  :field bubble_sent `tdproto-RGBColor`: Bubble sent color
  :field bubble_received `tdproto-RGBColor`: Bubble received color

.. tdproto:struct:: GroupMembership
  :tdpackage: tdmodels

  Group chat membership status

  :field jid `tdproto-JID`: Contact id
  :field status `tdproto-GroupStatus` omitempty: Status in group
  :field can_remove boolean omitempty: Can I remove this member

.. tdproto:struct:: ICEServer
  :tdpackage: tdmodels

  Interactive Connectivity Establishment Server for WEB Rtc connection. Readonly

  :field urls string: URls

.. tdproto:struct:: IconColors
  :tdpackage: tdmodels

  IconColors icon colors for app

  :field title `tdproto-RGBColor`: Title color
  :field brand `tdproto-RGBColor`: Brand color
  :field other `tdproto-RGBColor`: Other color

.. tdproto:struct:: IconData
  :tdpackage: tdmodels

  Icon data. For icon generated from display name contains Letters + Color fields

  :field sm `tdproto-SingleIcon`: Small icon
  :field lg `tdproto-SingleIcon`: Large image
  :field letters string omitempty: Letters (only for stub icon)
  :field color string omitempty: Icon background color (only for stub icon)
  :field blurhash string omitempty: Compact representation of a placeholder for an image (experimental)
  :field stub string omitempty: Deprecated

.. tdproto:struct:: InputColors
  :tdpackage: tdmodels

  InputColors input colors for app

  :field static `tdproto-RGBColor`: Static color
  :field active `tdproto-RGBColor`: Active color
  :field disable `tdproto-RGBColor`: Disable color
  :field error `tdproto-RGBColor`: Error color

.. tdproto:struct:: Integration
  :tdpackage: tdmodels

  Integration for concrete chat

  :field uid string omitempty: Id
  :field comment string: Comment, if any
  :field created string omitempty: Creation datetime, iso
  :field enabled boolean: Integration enabled
  :field form `tdproto-IntegrationForm`: Integration form
  :field group `tdproto-JID`: Chat id
  :field help string omitempty: Full description
  :field kind string: Unique integration name

.. tdproto:struct:: IntegrationField
  :tdpackage: tdmodels

  Integration form field

  :field label string: Label
  :field readonly boolean: Is field readonly
  :field value string: Current value

.. tdproto:struct:: IntegrationForm
  :tdpackage: tdmodels

  Integration form

  :field api_key `tdproto-IntegrationField` omitempty: Api key field, if any
  :field webhook_url `tdproto-IntegrationField` omitempty: Webhook url, if any
  :field url `tdproto-IntegrationField` omitempty: Url, if any

.. tdproto:struct:: IntegrationKind
  :tdpackage: tdmodels

  Integration kind

  :field kind string: Integration unique name
  :field title string: Plugin title
  :field template `tdproto-Integration`: Integration template
  :field icon string: Path to icon
  :field description string: Plugin description

.. tdproto:struct:: Integrations
  :tdpackage: tdmodels

  Complete integrations data, as received from server

  :field integrations array[`tdproto-Integration`]: Currently existing integrations
  :field kinds array[`tdproto-IntegrationKind`]: Types of integrations available for setup

.. tdproto:struct:: InvitableUser
  :tdpackage: tdmodels

  Account from other team, Active Directory or node

  :field uid string: Account id
  :field node string omitempty: Node uid for external users
  :field display_name string: Full name
  :field icons `tdproto-IconData`: Icons
  :field teams array[string] omitempty: Common team uids, if any

.. tdproto:struct:: JSEP
  :tdpackage: tdmodels

  JavaScript Session Establishment Protocol

  :field sdp string: Session Description Protocol information
  :field type string: See https://rtcweb-wg.github.io/jsep/#rfc.section.4.1.8

.. tdproto:struct:: MarkupEntity
  :tdpackage: tdmodels

  Markup entity. Experimental

  :field op number: Open marker offset
  :field oplen number omitempty: Open marker length
  :field cl number: Close marker offset
  :field cllen number omitempty: Close marker length
  :field typ `tdproto-MarkupType`: Marker type
  :field url string omitempty: Url, for Link type
  :field repl string omitempty: Text replacement
  :field time string omitempty: Time, for Time type
  :field childs array[`tdproto-MarkupEntity`] omitempty: List of internal markup entities

.. tdproto:struct:: Message
  :tdpackage: tdmodels

  Chat message

  :field content `tdproto-MessageContent`: Message content struct
  :field push_text string omitempty: Simple plaintext message representation
  :field from `tdproto-JID`: Sender contact id
  :field to `tdproto-JID`: Recipient id (group, task or contact)
  :field message_id string: Message uid
  :field created string: Message creation datetime (set by server side) or sending datetime in future for draft messages
  :field drafted string omitempty: Creation datetime for draft messages
  :field gentime number: Object version
  :field chat_type `tdproto-ChatType`: Chat type
  :field chat `tdproto-JID`: Chat id
  :field links `tdproto-MessageLinks` omitempty: External/internals links
  :field markup array[`tdproto-MarkupEntity`] omitempty: Markup entities. Experimental
  :field important boolean omitempty: Importance flag
  :field edited string omitempty: ISODateTimeString of message modification or deletion
  :field received boolean omitempty: Message was seen by anybody in chat. True or null
  :field num_received number omitempty: Unused yet
  :field nopreview boolean omitempty: Disable link previews. True or null
  :field has_previews boolean omitempty: Has link previews. True or null
  :field prev string omitempty: Previous message id in this chat. Uid or null
  :field is_first boolean omitempty: This message is first in this chat. True or null
  :field is_last boolean omitempty: This message is last in this chat. True or null
  :field uploads array[`tdproto-Upload`] omitempty: Message uploads
  :field reactions array[`tdproto-MessageReaction`] omitempty: Message reactions struct. Can be null
  :field reply_to `tdproto-Message` omitempty: Message that was replied to, if any
  :field linked_messages array[`tdproto-Message`] omitempty: Forwarded messages. Can be null. Also contains double of ReplyTo for backward compatibility
  :field notice boolean omitempty: Has mention (@). True or null
  :field silently boolean omitempty: Message has no pushes and did not affect any counters
  :field editable_until string omitempty: Author can change this message until date. Can be null
  :field num number omitempty: Index number of this message. Starts from 0. Null for deleted messages. Changes when any previous message wad deleted
  :field is_archive boolean omitempty: This message is archive. True or null
  :field _debug string omitempty: Debug information, if any

.. tdproto:struct:: MessageColors
  :tdpackage: tdmodels

  MessageColors message colors for app

  :field bubble_sent `tdproto-RGBColor`: Bubble sent color
  :field bubble_received `tdproto-RGBColor`: Bubble received color
  :field bubble_important `tdproto-RGBColor`: Bubble important color
  :field status_feed `tdproto-RGBColor`: Status feed color
  :field status_bubble `tdproto-RGBColor`: Status bubble color
  :field allocated `tdproto-RGBColor`: Allocated color

.. tdproto:struct:: MessageContent
  :tdpackage: tdmodels

  Chat message content

  :field text string: Text representation of message
  :field type `tdproto-Mediatype`: Message type
  :field subtype `tdproto-Mediasubtype` omitempty: Message subtype, if any
  :field upload string omitempty: Upload id, if any. Deprecated: use Uploads instead
  :field mediaURL string omitempty: Upload url, if any. Deprecated: use Uploads instead
  :field size number omitempty: Upload size, if any. Deprecated: use Uploads instead
  :field duration number omitempty: Upload duration, if any. Deprecated: use Uploads instead
  :field processing boolean omitempty: Upload still processing, if any. Deprecated: use Uploads instead
  :field blurhash string omitempty: Compact representation of a placeholder for an image. Deprecated: use Uploads instead
  :field previewHeight number omitempty: Upload preview height, in pixels, if any. Deprecated: use Uploads instead
  :field previewWidth number omitempty: Upload width, in pixels, if any. Deprecated: use Uploads instead
  :field previewURL string omitempty: Upload preview absolute url, if any. Deprecated: use Uploads instead
  :field preview2xURL string omitempty: Upload high resolution preview absolute url, if any. Deprecated: use Uploads instead
  :field name string omitempty: Upload name, if any. Deprecated: use Uploads instead
  :field animated boolean omitempty: Upload is animated image, if any. Deprecated: use Uploads instead
  :field title string omitempty: Change title (for "change" mediatype)
  :field old string omitempty: Change old value (for "change" mediatype)
  :field new string omitempty: Change new value (for "change" mediatype)
  :field actor `tdproto-JID` omitempty: Change actor contact id (for "change" mediatype)
  :field comment string omitempty: Comment (for "audiomsg" mediatype)
  :field given_name string omitempty: Given name (for "contact" mediatype)
  :field family_name string omitempty: Family name (for "contact" mediatype)
  :field patronymic string omitempty: Patronymic name (for "contact" mediatype)
  :field phones array[string] omitempty: Contact phones list (for "contact" mediatype)
  :field emails array[string] omitempty: Emails list (for "contact" mediatype)
  :field stickerpack string omitempty: Stickerpack name (for "sticker" subtype)
  :field pdf_version `tdproto-PdfVersion` omitempty: Pdf version, if any

.. tdproto:struct:: MessageLink
  :tdpackage: tdmodels

  Checked message links. In short: "Click here: {link.Pattern}" => "Click here: <a href='{link.Url}'>{link.Text}</a>"

  :field pattern string: Text fragment that should be replaced by link
  :field url string: Internal or external link
  :field text string: Text replacement
  :field preview `tdproto-MessageLinkPreview` omitempty: Optional preview info, for websites
  :field uploads array[`tdproto-Upload`] omitempty: Optional upload info
  :field nopreview boolean omitempty: Website previews disabled
  :field youtube_id string omitempty: Optional youtube movie id

.. tdproto:struct:: MessageLinkPreview
  :tdpackage: tdmodels

  Website title and description

  :field title string: Website title or og:title content
  :field description string omitempty: Website description

.. tdproto:struct:: MessageReaction
  :tdpackage: tdmodels

  Message emoji reaction

  :field name string: Emoji
  :field counter number: Number of reactions
  :field details array[`tdproto-MessageReactionDetail`]: Details

.. tdproto:struct:: MessageReactionDetail
  :tdpackage: tdmodels

  Message reaction detail

  :field created string: When reaction added, iso datetime
  :field sender `tdproto-JID`: Reaction author
  :field name string: Reaction emoji

.. tdproto:struct:: MyReactions
  :tdpackage: tdmodels

  Reactions to messages: frequently used and all available

  :field top array[`tdproto-Reaction`]: My frequently used reactions
  :field all array[`tdproto-Reaction`]: All available reactions

.. tdproto:struct:: Node
  :tdpackage: tdmodels

  Node (for external users)

  :field uid string: Node uid
  :field title string: Node title
  :field enabled boolean: Synchronization with node works

.. tdproto:struct:: OAuthService
  :tdpackage: tdmodels

  OAuth service

  :field name string: Integration title
  :field url string: Redirect url

.. tdproto:struct:: OnlineCall
  :tdpackage: tdmodels

  Active call status

  :field jid `tdproto-JID`: Chat or contact id
  :field uid string: Call id
  :field start string omitempty: Call start
  :field online_count number omitempty: Number participants in call

.. tdproto:struct:: OnlineContact
  :tdpackage: tdmodels

  Contact online status

  :field jid `tdproto-JID`: Contact id
  :field afk boolean omitempty: Is away from keyboard
  :field focused boolean omitempty: Focus mode enabled
  :field mobile boolean: Is mobile client

.. tdproto:struct:: PdfVersion
  :tdpackage: tdmodels

  PDF preview of mediafile. Experimental

  :field url string: Absolute url
  :field text_preview string omitempty: First string of text content

.. tdproto:struct:: PushDevice
  :tdpackage: tdmodels

  Push device info

  :field type string: Type: android, ios, web, safari
  :field device_id string: Device id generated by client library
  :field notification_token string: Notification token
  :field voip_notification_token string: Notification token for VOIP (iOS only)
  :field name string: Readable device name
  :field data_pushes boolean: Send silently data pushes that must be fully processed by app. Must be true for modern mobile clients
  :field data_badges boolean: Send badge value as data. Experimental
  :field allowed_notifications boolean: deprecated

.. tdproto:struct:: Reaction
  :tdpackage: tdmodels

  Emoji reaction

  :field name string: Unicode symbol

.. tdproto:struct:: ReceivedMessage
  :tdpackage: tdmodels

  Message receiving status

  :field chat `tdproto-JID`: Chat or contact id
  :field message_id string: Message id
  :field received boolean: Is received
  :field num_received number omitempty: Number of contacts received this message. Experimental
  :field _debug string omitempty: Debug message, if any

.. tdproto:struct:: Remind
  :tdpackage: tdmodels

  Remind

  :field uid string: Remind id
  :field chat `tdproto-JID`: Chat id
  :field fire_at string: Activation time, iso
  :field comment string omitempty: Comment, if any

.. tdproto:struct:: Resp
  :tdpackage: tdmodels

  Server response

  :field _time string omitempty: Server side work time
  :field ok boolean: Request status
  :field result any omitempty: Result only if ok is true)
  :field error `tdproto-Err` omitempty: Error (only if ok is false)
  :field details string omitempty: Error (only if ok is false and Error is 'InvalidData')
  :field reason string omitempty: Reason (only if ok is false and Error is `AccessDenied`)
  :field markup array[`tdproto-MarkupEntity`] omitempty: Reason markup (only if ok is false and Error is `AccessDenied`)

.. tdproto:struct:: Section
  :tdpackage: tdmodels

  Task project or contact section

  :field uid string: Section uid
  :field sort_ordering number: Sort ordering
  :field name string: Name
  :field gentime number: Object version
  :field description string omitempty: Description, if any
  :field is_archive boolean omitempty: Is deleted

.. tdproto:struct:: Session
  :tdpackage: tdmodels

  Websocket session

  :field uid string: Session id
  :field created string: Creation datetime
  :field lang string omitempty: Language code
  :field team string omitempty: Team id
  :field is_mobile boolean omitempty: Mobile
  :field afk boolean omitempty: Away from keyboard
  :field useragent string omitempty: User agent
  :field addr string omitempty: IP address

.. tdproto:struct:: SharpLink
  :tdpackage: tdmodels

  #-link autocomplete information

  :field key string: What should be inserted to the chat
  :field title string: What should be visible by user
  :field icons `tdproto-IconData` omitempty: Icon data, if any
  :field meta `tdproto-SharpLinkMeta`: Internal details

.. tdproto:struct:: SharpLinkMeta
  :tdpackage: tdmodels

  #-link autocomplete details

  :field jid `tdproto-JID`: Chat id
  :field chat_type `tdproto-ChatType`: Chat type
  :field public boolean omitempty: Is task or group public for non-guests
  :field task_status string omitempty: Task status (for tasks)
  :field num number omitempty: Task number (for tasks)
  :field done boolean omitempty: Deprecated: use `TaskStatus == "done"` comparsion

.. tdproto:struct:: ShortMessage
  :tdpackage: tdmodels

  Short message based on chat message

  :field from `tdproto-JID`: Sender contact id
  :field to `tdproto-JID`: Recipient id (group, task or contact)
  :field message_id string: Message uid
  :field created string: Message creation datetime (set by server side) or sending datetime in future for draft messages
  :field gentime number: Object version
  :field chat_type `tdproto-ChatType`: Chat type
  :field chat `tdproto-JID`: Chat id
  :field is_archive boolean omitempty: This message is archive. True or null

.. tdproto:struct:: SingleIcon
  :tdpackage: tdmodels

  Small or large icon

  :field url string: absolute url to icon
  :field width number: Icon width, in pixels
  :field height number: Icon height, in pixels

.. tdproto:struct:: Subscription
  :tdpackage: tdmodels

  Subscription - an entity that signifies the fact of subscribing to the tariff of any team for a certain period (not defined, in the case of the default tariff)

  :field uid string: Subscription id
  :field activated string omitempty: Subscription activation time
  :field expires string omitempty: Subscription expiration time
  :field tariff_uid string omitempty: ID of the tariff for which the subscription is valid
  :field user_uid string omitempty: ID of the user who subscribed

.. tdproto:struct:: Subtask
  :tdpackage: tdmodels

  Link to sub/sup task

  :field jid `tdproto-JID`: Task id
  :field assignee `tdproto-JID`: Assignee contact id. Tasks only
  :field title string: Task title. Generated from number and description
  :field num number: Task number in this team
  :field display_name string: Title
  :field public boolean omitempty: Is task or group public for non-guests
  :field task_status string omitempty: Subtask task status

.. tdproto:struct:: SwitcherColors
  :tdpackage: tdmodels

  SwitcherColors switcher colors for app

  :field on `tdproto-RGBColor`: On color
  :field off `tdproto-RGBColor`: Off color

.. tdproto:struct:: Tag
  :tdpackage: tdmodels

  Task tag

  :field uid string: Tag id
  :field name string: Tag name

.. tdproto:struct:: Tariff
  :tdpackage: tdmodels

  Tariff for teams

  :field uid string: Tariff id
  :field title_en string: Title of tariff in enlish
  :field title_ru string: Title of tariff in russian
  :field price string omitempty: Price of tariff
  :field cloud_space number omitempty: Cloud space reserved for storing team users uploads in megabytes
  :field max_members_in_team number omitempty: Maximum allowed number of members in a team
  :field max_participants_per_call number omitempty: Maximum number of participants per call
  :field max_upload_filesize number omitempty: maximum file size for uploading

.. tdproto:struct:: Task
  :tdpackage: tdmodels

  Task

  :field custom_color_index number omitempty: Custom task color
  :field description string omitempty: Task description
  :field tags array[string] omitempty: Task tags
  :field section string omitempty: Task section UID
  :field observers array[`tdproto-JID`] omitempty: User who follow the task
  :field items array[string] omitempty: Items of the task
  :field assignee `tdproto-JID` omitempty: User who was assigned the task
  :field deadline string omitempty: Deadline time, if any
  :field public boolean omitempty: Is task or group public for non-guests
  :field remind_at string omitempty: Fire a reminder at this time
  :field task_status string omitempty: Task status
  :field importance number omitempty: Task importance
  :field urgency number omitempty: Task urgency
  :field complexity number omitempty: Task complexity
  :field spent_time number omitempty: Time spent
  :field linked_messages array[string] omitempty: Linked messages
  :field uploads array[string] omitempty: Task uploads

.. tdproto:struct:: TaskColor
  :tdpackage: tdmodels

  Task color rules color

  :field regular `tdproto-RGBColor`: Regular color
  :field dark `tdproto-RGBColor`: Dark color
  :field light `tdproto-RGBColor`: Light color

.. tdproto:struct:: TaskCounters
  :tdpackage: tdmodels

  Tasks counters

  :field jid `tdproto-JID`: Task jid
  :field num_unread number omitempty: Unreads counter
  :field num_unread_notices number omitempty: Mentions (@) counter

.. tdproto:struct:: TaskFilter
  :tdpackage: tdmodels

  Task filter

  :field field `tdproto-TaskFilterKey`: Task filter field
  :field title string: Filter title

.. tdproto:struct:: TaskItem
  :tdpackage: tdmodels

  Task checklist item

  :field uid string omitempty: Id
  :field gentime number: Object version
  :field sort_ordering number omitempty: Sort ordering
  :field text string: Text or "#{OtherTaskNumber}"
  :field checked boolean omitempty: Item checked
  :field can_toggle boolean omitempty: Can I toggle this item
  :field can_change boolean omitempty: Can I change this item
  :field subtask `tdproto-Subtask` omitempty: Link to subtask. Optional

.. tdproto:struct:: TaskSort
  :tdpackage: tdmodels

  Task sort type

  :field key `tdproto-TaskSortKey`: Field
  :field title string: Sort title

.. tdproto:struct:: TaskStatus
  :tdpackage: tdmodels

  Custom task status

  :field uid string omitempty: Status id
  :field sort_ordering number: Status sort ordering
  :field name string: Status internal name
  :field title string: Status localized name
  :field is_archive boolean omitempty: Status not used anymore

.. tdproto:struct:: TaskTab
  :tdpackage: tdmodels

  Task tab

  :field key `tdproto-TaskTabKey`: Tab name
  :field title string: Tab title
  :field hide_empty boolean: Disable this tab when it has no contents
  :field show_counter boolean: Show unread badge
  :field pagination boolean: Enable pagination
  :field filters array[`tdproto-TaskFilter`]: Filters inside tab
  :field sort array[`tdproto-TaskSort`]: Sort available in tab
  :field unread_tasks array[`tdproto-TaskCounters`]: Unread tasks with jid and counters

.. tdproto:struct:: Team
  :tdpackage: tdmodels

  Team

  :field uid string: Team id
  :field is_archive boolean omitempty: Team deleted
  :field gentime number: Object version
  :field name string: Team name
  :field default_task_deadline string omitempty: Default task deadline
  :field max_message_update_age number: Max message update/deletion age, in seconds
  :field icons `tdproto-IconData`: Team icons
  :field last_active boolean: User last activity was in this team
  :field changeable_statuses array[`tdproto-TeamStatus`] omitempty: What status I can set to other team members
  :field bad_profile boolean omitempty: My profile in this team isn't full
  :field need_confirmation boolean: Need confirmation after invite to this team
  :field use_patronymic boolean omitempty: Patronymic in usernames for this team
  :field user_fields array[string]: Username fields ordering. Possible values: "family_name", "given_name", "patronymic"
  :field display_family_name_first boolean omitempty: Family name should be first in display name
  :field use_task_importance boolean omitempty: Use importance field in task
  :field task_importance_min number omitempty: Minimal value of task importance. Default is 1
  :field task_importance_max number omitempty: Maximum value of task importance. Default is 5
  :field task_importance_rev boolean omitempty: Bigger number = bigger importance. Default: lower number = bigger importance
  :field use_task_urgency boolean omitempty: Use urgency field in task
  :field use_task_complexity boolean omitempty: Use complexity field in task
  :field use_task_spent_time boolean omitempty: Use spent time field in task
  :field uploads_size number omitempty: Total uploads size, bytes
  :field uploads_size_limit number omitempty: Maximum uploads size, bytes, if any
  :field unread `tdproto-TeamUnread` nullable: Unread message counters
  :field me `tdproto-Contact`: My profile in this team
  :field contacts array[`tdproto-Contact`] omitempty: Team contacts. Used only for team creation
  :field single_group `tdproto-JID` omitempty: For single group teams, jid of chat
  :field theme `tdproto-Theme` omitempty: Color theme, if any
  :field hide_archived_users boolean omitempty: Don't show archived users by default
  :field pinned boolean omitempty: Team pinned
  :field available_tariffs array[string] omitempty: Team's available tariff by includig archive ones
  :field subscription `tdproto-Subscription` omitempty: Сurrent team subscription

.. tdproto:struct:: TeamCounter
  :tdpackage: tdmodels

  Unread message counters

  :field uid string: Team id
  :field unread `tdproto-TeamUnread`: Unread message counters

.. tdproto:struct:: TeamShort
  :tdpackage: tdmodels

  Short team representation. For invites, push notifications, etc. Readonly

  :field uid string: Team id
  :field name string: Team name
  :field icons `tdproto-IconData`: Team icons

.. tdproto:struct:: Terms
  :tdpackage: tdmodels

  Experimental translation fields for "team" entity renaming. Readonly

  :field EnInTeam string: "in team"
  :field EnTeam string: "team"
  :field EnTeamAccess string: "access to team"
  :field EnTeamAdmin string: "team admin"
  :field EnTeamAdmins string: "team admins"
  :field EnTeamGuest string: "team guest"
  :field EnTeamMember string: "team member"
  :field EnTeamMembers string: "team members"
  :field EnTeamOwner string: "team owner",
  :field EnTeamSettings string: "team settings"
  :field RuTeamSettings string: "настройки команды"
  :field EnTeams string: "teams"
  :field EnToTeam string: "to team"
  :field RuInTeam string: "в команде"
  :field RuTeam string: "команда"
  :field RuTeamAccess string: "доступ к команде"
  :field RuTeamAdmin string: "администратор команды"
  :field RuTeamAdmins string: "администраторы команды"
  :field RuTeamD string: "команде"
  :field RuTeamGuest string: "гость команды"
  :field RuTeamMember string: "участник команды"
  :field RuTeamMembers string: "участники команды"
  :field RuTeamOwner string: "владелец команды"
  :field RuTeamP string: "команде"
  :field RuTeamR string: "команды"
  :field RuTeams string: "команды"
  :field RuTeamsD string: "командам"
  :field RuTeamsP string: "командах"
  :field RuTeamsR string: "команд"
  :field RuTeamsT string: "командами"
  :field RuTeamsV string: "команды"
  :field RuTeamT string: "командой"
  :field RuTeamV string: "команду"
  :field RuToTeam string: "в команду"

.. tdproto:struct:: Theme
  :tdpackage: tdmodels

  Color theme

  :field BgColor `tdproto-RGBColor`: BgColor for web
  :field BgHoverColor `tdproto-RGBColor`: BgHoverColor for web
  :field TextColor `tdproto-RGBColor`: TextColor for web
  :field MutedTextColor `tdproto-RGBColor`: MutedTextColor for web
  :field AccentColor `tdproto-RGBColor`: AccentColor for web
  :field AccentHoverColor `tdproto-RGBColor`: AccentHoverColor for web
  :field TextOnAccentHoverColor `tdproto-RGBColor`: TextOnAccentHoverColor for web
  :field MainAccent `tdproto-RGBColor`: MainAccent for web
  :field MainAccentHover `tdproto-RGBColor`: MainAccentHover for web
  :field MainLightAccent `tdproto-RGBColor`: MainLightAccent for web
  :field MainLink `tdproto-RGBColor`: MainLink for web
  :field brand `tdproto-RGBColor`: Brand color for app
  :field brand_dark `tdproto-RGBColor`: BrandDark color for app
  :field brand_light `tdproto-RGBColor`: Brand light color for app
  :field back `tdproto-RGBColor`: Back light color for app
  :field back_light `tdproto-RGBColor`: Back light color for app
  :field back_dark `tdproto-RGBColor`: Back dark color for app
  :field success `tdproto-RGBColor`: Success color for app
  :field success_light `tdproto-RGBColor`: Success light color for app
  :field error `tdproto-RGBColor`: Error color for app
  :field error_light `tdproto-RGBColor`: Error light color for app
  :field background `tdproto-RGBColor`: Background color for app
  :field tab_background `tdproto-RGBColor`: Tab background color for app
  :field chat_input_background `tdproto-RGBColor`: Chat input background color for app
  :field substrate_background `tdproto-RGBColor`: Substrate background color for app
  :field modal_background `tdproto-RGBColor`: Modal background color for app
  :field title_background `tdproto-RGBColor`: Title background color for app
  :field attention `tdproto-RGBColor`: Attention color for app
  :field attention_light `tdproto-RGBColor`: Attention light color for app
  :field font `tdproto-FontColors` nullable: Font colors for app
  :field message `tdproto-MessageColors` nullable: Message colors for app
  :field switcher `tdproto-SwitcherColors` nullable: Switcher colors for app
  :field button `tdproto-ButtonColors` nullable: Button colors for app
  :field input `tdproto-InputColors` nullable: Input colors for app
  :field ic `tdproto-IconColors` nullable: Icon colors for app
  :field web_base `tdproto-WebBase` nullable: WebBase colors for web
  :field AppAccentColor `tdproto-RGBColor`: Deprecated
  :field AppPrimaryColor `tdproto-RGBColor`: Deprecated

.. tdproto:struct:: Unread
  :tdpackage: tdmodels

  Unread message counters

  :field messages number: Total unread messages
  :field notice_messages number: Total unread messages with mentions
  :field chats number: Total chats with unread messages

.. tdproto:struct:: Upload
  :tdpackage: tdmodels

  Uploaded media

  :field uid string: Upload id
  :field created string: Uploaded at
  :field size number: Upload size in bytes
  :field duration number omitempty: Mediafile duration (for audio/video only)
  :field name string: Filename
  :field url string: Absolute url
  :field preview `tdproto-UploadPreview` omitempty: Preview details
  :field content_type string: Content type
  :field animated boolean omitempty: Is animated (images only)
  :field blurhash string omitempty: Compact representation of a placeholder for an image (images only)
  :field processing boolean omitempty: File still processing (video only)
  :field pdf_version `tdproto-PdfVersion` omitempty: PDF version of file. Experimental
  :field type `tdproto-UploadMediaType`: ?type=file,image,audio,video

.. tdproto:struct:: UploadPreview
  :tdpackage: tdmodels

  Upload preview

  :field url string: Absolute url to image
  :field url_2x string: Absolute url to high resolution image (retina)
  :field width number: Width in pixels
  :field height number: Height in pixels

.. tdproto:struct:: UploadShortMessage
  :tdpackage: tdmodels

  Upload + ShortMessage

  :field upload `tdproto-Upload`: Upload information
  :field message `tdproto-ShortMessage`: Short message information

.. tdproto:struct:: User
  :tdpackage: tdmodels

  Account data

  :field phone string omitempty: Phone for login
  :field email string omitempty: Email for login
  :field family_name string omitempty: Family name
  :field given_name string omitempty: Given name
  :field patronymic string omitempty: Patronymic, if any
  :field default_lang string omitempty: Default language code
  :field alt_send boolean: Use Ctrl/Cmd + Enter instead Enter
  :field asterisk_mention boolean: Use * as @ for mentions
  :field always_send_pushes boolean: Send pushes even user is online
  :field hide_pushes_content boolean: Hide pushes body
  :field unread_first boolean: Show unread chats in chat list first
  :field munread_first boolean: Show unread chats in chat list first on mobiles
  :field timezone string: Timezone
  :field quiet_time_start string nullable: Start silently time (no pushes, no sounds)
  :field quiet_time_finish string nullable: Finish silently time (no pushes, no sounds)
  :field icons `tdproto-IconData`: Icon data

.. tdproto:struct:: UserWithMe
  :tdpackage: tdmodels

  Account data with extra information

  :field inviter `tdproto-JID` omitempty: Inviter id, if any
  :field teams array[`tdproto-Team`]: Available teams
  :field devices array[`tdproto-PushDevice`]: Registered push devices
  :field phone string omitempty: Phone for login
  :field email string omitempty: Email for login
  :field family_name string omitempty: Family name
  :field given_name string omitempty: Given name
  :field patronymic string omitempty: Patronymic, if any
  :field default_lang string omitempty: Default language code
  :field alt_send boolean: Use Ctrl/Cmd + Enter instead Enter
  :field asterisk_mention boolean: Use * as @ for mentions
  :field always_send_pushes boolean: Send pushes even user is online
  :field hide_pushes_content boolean: Hide pushes body
  :field unread_first boolean: Show unread chats in chat list first
  :field munread_first boolean: Show unread chats in chat list first on mobiles
  :field timezone string: Timezone
  :field quiet_time_start string nullable: Start silently time (no pushes, no sounds)
  :field quiet_time_finish string nullable: Finish silently time (no pushes, no sounds)
  :field icons `tdproto-IconData`: Icon data

.. tdproto:struct:: Wallpaper
  :tdpackage: tdmodels

  Chat wallpaper

  :field key string: Unique identifier
  :field name string: Localized description
  :field url string: Url to jpg or png

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
