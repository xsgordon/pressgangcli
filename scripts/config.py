import ConfigParser

class PressgangConfig:
    def __init__(self, conf_file):
       self.config = ConfigParser.RawConfigParser()
       self.config.read(conf_file)

    def get_user(self):
       return self.config.get("Required", "USER")

    def get_location(self):
       return self.config.get("Required", "LOCATION")

    def get_public_dtd(self):
       return self.config.get("Required", "PUBLIC_DTD")

    def get_system_dtd(self):
       return self.config.get("Required", "SYSTEM_DTD")

    def get_editor(self):
       return self.config.get("Required", "EDITOR")
