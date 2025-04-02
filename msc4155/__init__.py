class Filter:
    @staticmethod
    def parse_config(config):
        return config # not parsed/used

    def __init__(self, config, api):
        api.register_spam_checker_callbacks(
            user_may_invite=self.user_may_invite
        )

    async def user_may_invite(self, inviter_userid, invitee_userid, room_id):
        return synapse.module_api.NOT_SPAM