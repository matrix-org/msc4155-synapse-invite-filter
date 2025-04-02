from matrix_common.regex import glob_to_regex
from synapse.module_api import NOT_SPAM, UserID
from synapse.module_api.errors import Codes

STATE_UNCHANGED = 0
STATE_ALLOWED = 1
STATE_BLOCKED = 2

SPAM = Codes.FORBIDDEN

class Filter:
    @staticmethod
    def parse_config(config):
        return config # not parsed/used

    def __init__(self, config, api):
        self.api = api
        api.register_spam_checker_callbacks(
            user_may_invite=self.user_may_invite
        )

    async def user_may_invite(self, inviter_userid, invitee_userid, room_id):
        config = await self.api.account_data_manager.get_global(invitee_userid, "org.matrix.msc4155.invite_permission_config")
        if not config:
            return NOT_SPAM

        # TODO: Support `ignored_users` and `ignored_servers` (once the module API also supports ignores)

        state = STATE_UNCHANGED

        # check users first, because that's faster
        allowed_users = config.get("allowed_users", [])
        blocked_users = config.get("blocked_users", [])
        state = self._tristate_of(invitee_userid, allowed_users, blocked_users)
        if state == STATE_ALLOWED:
            return NOT_SPAM

        # check servers second
        allowed_servers = config.get("allowed_servers", [])
        blocked_servers = config.get("blocked_servers", [])
        val = self._tristate_of(UserID.from_string(inviter_userid).domain, allowed_servers, blocked_servers)
        if val != STATE_UNCHANGED:
            state = val
        if state == STATE_ALLOWED:
            return NOT_SPAM

        if state == STATE_ALLOWED:
            return NOT_SPAM
        elif state == STATE_BLOCKED:
            return SPAM
        else:
            return NOT_SPAM # default/unchanged


    def _tristate_of(self, entity, allow_list, block_list):
        if len(allow_list) == 0 and len(block_list) == 0:
            return STATE_UNCHANGED

        for glob in allow_list:
            if glob_to_regex(glob).match(entity):
                return STATE_ALLOWED

        for glob in block_list:
            if glob_to_regex(glob).match(entity):
                return STATE_BLOCKED

        return STATE_UNCHANGED
