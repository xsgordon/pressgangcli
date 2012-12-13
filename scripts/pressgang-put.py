#!/bin/python

import sys
import argparse
import requests
import os.path
import codecs

from topic import Topic
from topic import TopicServer
from config import PressgangConfig


class Usage(Exception):
    def __init__(self, msg):
        self.msg = "USAGE: %s" % msg


class Error(Exception):
    def __init__(self, msg):
        self.msg = "ERROR: %s" % msg


def parse_args(argv):
    parser = argparse.ArgumentParser(description="Create or update a topic " +
                                                 "in the Pressgang CCMS.")
    parser.add_argument("-f", "--file", help="Specifies the XML file to save" +
                                             "otherwise reads from standard " +
                                             "input.")
    parser.add_argument("-t", "--title", help="Specifies title for the topic.")
    parser.add_argument("TOPIC", help="Specifies the identifier of the topic" +
                                      " to update. This must be the numeric " +
                                      "identifier of the topic.")
    args = parser.parse_args()
    return args


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        args = parse_args(argv)
        f = None
        if args.file:
            f = open(args.file, "rt")
        else:
            f = sys.stdin
        xml = ""
        data = f.readline()
        while data:
            xml = "%s%s" % (xml, data)
            data = f.readline()

        config = PressgangConfig("%s/.pressgangcli.conf" %
                                 os.path.expanduser("~"))
        topic_server = TopicServer(config.get_location())
        topic = Topic(topic_server, args.TOPIC).set_xml(xml)

        # Note that failure is considered non-fatal, just return the response
        # code for the calling script/user to deal with.
        if topic.status_code == 200:
            print "Topic %s, revision %s saved." % (args.TOPIC,
                                                    topic.json["revision"])
        else:
            print "HTTP status %s." % str(topic.status_code)

        return topic.status_code
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, ("For help and usage information use the --help " +
                            "argument.")
        return 2
    except Error, err:
        print >>sys.stderr, err.msg
        return 1


if __name__ == "__main__":
    sys.stdout = codecs.getwriter("UTF-8")(sys.stdout)
    sys.stderr = codecs.getwriter("UTF-8")(sys.stderr)
    sys.exit(main())
