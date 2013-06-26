import requests
import json
import urllib


class TopicServer:

    _base_uri = "https://127.0.0.1:8443/"
    _get_uri = "rest/1/topic/get"
    _put_uri = "rest/1/topic/update/json/"

    def __init__(self, uri):
        self.set_uri(uri)

    def set_uri(self, uri):
        self._base_uri = "%s/" % uri

    def get_save_uri(self, ID=None):
        return "%s%s" % (self._base_uri, self._put_uri)

    def get_load_uri(self, ID, revision=0, fmt="json"):
        common_uri = "%s%s/%s" % (self._base_uri, self._get_uri, fmt)
        if revision == 0:
            if fmt == "json":
                return "%s/%s" % (common_uri,
                                  str(ID))
            else:
                return "%s/%s/%s" % (common_uri,
                                     str(ID), fmt)
        else:
            if fmt == "json":
                return "%s/%s/r/%s" % (common_uri,
                                       str(ID),
                                       str(revision))
            else:
                return "%s/%s/r/%s/%s" % (common_uri,
                                          str(ID),
                                          str(revision),
                                          fmt)


class Topic:

    _srv = None
    _id = 0

    def __init__(self, server, ID):
        self._srv = server
        self._id = ID

    def get_html(self, revision=0):
        url = self._srv.get_load_uri(ID=self._id,
                                     revision=revision,
                                     fmt="html")
        return requests.get(url, verify=False).text

    def get_xml(self, revision=0):
        url = self._srv.get_load_uri(ID=self._id,
                                     revision=revision,
                                     fmt="xml")
        return requests.get(url, verify=False).text

    def get_json(self, revision=0):
        url = self._srv.get_load_uri(ID=self._id,
                                     revision=revision,
                                     fmt="json")
        return requests.get(url, verify=False).json

    def set_xml(self, xml, title=None):
        payload = {}
        if title is None:
            payload = {"configuredParameters": ["xml"],
                       "id": self._id,
                       "xml": xml}
        else:
            payload = {"configuredParameters": ["xml"],
                       "id": self._id,
                       "title": title,
                       "xml": xml}

        resp = requests.post(self._srv.get_save_uri(self._id),
                             data=json.dumps(payload),
                             headers={"content-type": "application/json",
                                      "Accept": "application/json"},
                             verify=False)

        return resp
