from wtforms import Form


class BaseFrom(Form):
    @property
    def messages(self):
        message_list = []
        for errors in self.errors.values():
            message_list.extend(errors)
        return message_list

