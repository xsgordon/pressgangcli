import requests
import json

class TopicServer:

    _base_uri = "https://127.0.0.1:8443/TopicIndex/"
    _get_uri = "seam/resource/rest/1/topic/get/json/"
    _put_uri = "seam/resource/rest/1/topic/update/json/"

    def __init__(self, uri):
        self.set_uri(uri)

    def set_uri(self, uri):
        self._base_uri = "%s/TopicIndex/" % uri

    def get_save_uri(self, ID=None):
        return "%s%s" % (self._base_uri, self._put_uri)

    def get_load_uri(self, ID=None):
        if ID is None:
            return "%s%s" % (self._base_uri, self._get_uri)
        else:
            return "%s%s%s" % (self._base_uri, self._get_uri, str(ID))


class Topic:

    _srv = None
    _id = 0

    def __init__(self, server, ID):
        self._srv = server
        self._id = ID

    def get_html(self):
        json = self.get_json()
        return json["html"]

    def get_xml(self):
        json = self.get_json()
        return json["xml"]

    def get_json(self):
        resp = requests.get(self._srv.get_load_uri(self._id),
                            verify=False)
        return resp.json
        

    def set_xml(self, xml, title=None):
        payload = {}
        if title is None:
            payload = {"id" : self._id, "xml" : xml}
        else:
            payload = {"id" : self._id, "title": title, "xml" : xml}
        resp = requests.post(self._srv.get_save_uri(self._id),
                             data=json.dumps(payload),
                             headers={"content-type": "application/json",
                                      "Accept": "application/json"},
                             verify=False)
        return resp

    def revision(self):
        print ""

    def revisions(self):
        print ""
