#!/bin/python

import sys
import argparse
import requests
import os.path
from topic import Topic
from topic import TopicServer
from config import PressgangConfig


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


class Error(Exception):
    def __init__(self, msg):
        self.msg = msg


def parse_args(argv):
    parser = argparse.ArgumentParser(description="Retrieve a topic from the " +
                                                 "Pressgang CCMS.")
#    parser.add_argument("-d", "--diff", help="Performs a diff operation between " +
#                                             "either the specified topic " +
#                                             "revisions, or the latest revision " +
#                                             "and its predecessor.",
#                                             action="store_true")
    parser.add_argument("-j", "--json", help="Instead of returning the topic XML" +
                                             ", returns the JSON representation " +
                                             "of the topic. This option is not " +
                                             "compatible with the --diff and -d " +
                                             "options.", action="store_true")
    parser.add_argument("-H", "--html", help="Instead of returning the topic XML, " +
                                       "returns HTML representation.", action="store_true" )
    parser.add_argument("-r", "--revision", help="Specifies a specific revision " +
                                                 "to retrieve or.", action="store", default=0)
    parser.add_argument("TOPIC", help="Specifies the identifier of the topic to " +
                                      "be retrieved. This must be either the " +
                                      "numeric identifier of the topic or its " +
                                      "short URL title.")
    args = parser.parse_args()
    return args


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        args = parse_args(argv)
        config = PressgangConfig("%s/.pressgangcli.conf" %os.path.expanduser("~"))
#        if args.diff and args.json:
#            raise Usage("The --diff and --json arguments are mutually exclusive.")
        topic_server = TopicServer(config.get_location())
        topic = Topic(topic_server, args.TOPIC)
        output = None

        if args.json:
            output = topic.get_json(revision=int(args.revision))
        elif args.html:
            output = topic.get_html(revision=int(args.revision))
        else:
            output = topic.get_xml(revision=int(args.revision))
        
        if output is not None:
            print output

        return 0

    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "For help and usage information use the --help argument."
        return 2
    except Error, err:
        print >>sys.stderr, err.msg
        return 1


if __name__ == "__main__":
    sys.exit(main())
