#!/bin/python

import sys
import argparse
import os.path
import ConfigParser
import codecs

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


class Error(Exception):
    def __init__(self, msg):
        self.msg = msg

def parse_args(argv):
    """
    Users can provide all, some, or none of the arguments. Arguments that are
    not supplied are taken from the existing configuration.
    """
    parser = argparse.ArgumentParser(description="Set configuration options " +
                                                 "for the Pressgang CCMS " +
                                                 "command line tools.")
    parser.add_argument("-u", "--user", help="User name to use.")
    parser.add_argument("-l", "--location", help="Pressgang CCMS URL.")
    parser.add_argument("-p", "--public_dtd", help="Public DTD ID.")
    parser.add_argument("-s", "--system_dtd", help="System DTD ID.")
    parser.add_argument("-e", "--editor", help="Topic editor.")

    return parser.parse_args()

def get_config():
    """
    Retrieve existing configuration from user's .pressgangcli.conf file. If it
    does not exist then check for .skynet-shell-tools as used by earlier 
    versions of these tools.

    Returns a dictionary of config keys, or none where no config could be found.
    """

    config_values = {}

    home = os.path.expanduser("~")

    pgang_config_exists = os.path.isfile("%s/.pressgangcli.conf" % home)
    skynet_config_exists = os.path.isfile("%s/.skynet-shell-tools" % home)

    if(pgang_config_exists):
        config = ConfigParser.RawConfigParser()
        config.read("%s/.pressgangcli.conf" % home)
        config_values["USER"] = config.get("Required", "USER")
        config_values["LOCATION"] = config.get("Required", "LOCATION")
        config_values["PUBLIC_DTD"] = config.get("Required", "PUBLIC_DTD")
        config_values["SYSTEM_DID"] = config.get("Required", "SYSTEM_DTD")
        config_values["EDITOR"] = config.get("Required", "EDITOR")
    elif(skynet_config_exists):
        f = open("%s/.skynet-shell-tools" % home, "r")
        f_keys = f.readlines()
        for key in f_keys:
            if(key[0:1] == "#"):
                continue
            key_split = key.split("=", 1)
            # We don't need the quotes that surround the values,
            config_values[key_split[0]] = key_split[1][1:len(key_split[1])-2]
        config_translated = {}
        for key, val in config_values.iteritems():
            if(key == "SKYNET_USER"):
                config_translated["USER"] = val
            elif(key == "SKYNET_URL"):
                config_translated["LOCATION"] = val
            elif(key == "SKYNET_PUBLIC_DTD"):
                config_translated["PUBLIC_DTD"] = val
            elif(key == "SKYNET_SYSTEM_DTD"):
                config_translated["SYSTEM_DTD"] = val
            elif(key == "SKYNET_EDITOR"):
                config_translated["EDITOR"] = val
            else:
                continue
        config_values = config_translated
    else:
        return None

    return config_values


def set_config(new, old=None):
    """
    Save configuration values to user's .pressgangcli.conf file. Expected 
    parameters are the dictionary of new configuration items and, optionally,
    a dictionary of old configuration options to be used if only a subset of
    values are being set.

    Note that if no old configuration options are provided and the new options
    dictionary does not contain all expected options then an exception will 
    result.
    """
    home = os.path.expanduser("~")

    config = ConfigParser.RawConfigParser()
    config.add_section("Required")

    if(new["USER"] is None):
        config.set("Required", "USER", old["USER"])
    else:
        config.set("Required", "USER", new["USER"])
   
    if(new["LOCATION"] is None):
        config.set("Required", "LOCATION", old["LOCATION"])
    else:
        config.set("Required", "LOCATION", new["LOCATION"])
    
    if(new["PUBLIC_DTD"] is None):
        config.set("Required", "PUBLIC_DTD", old["PUBLIC_DTD"])
    else:
        config.set("Required", "PUBLIC_DTD", new["PUBLIC_DTD"])
    
    if(new["SYSTEM_DTD"] is None):
        config.set("Required", "SYSTEM_DTD", old["SYSTEM_DTD"])
    else:
        config.set("Required", "SYSTEM_DTD", new["SYSTEM_DTD"])
    
    if(new["EDITOR"] is None):
        config.set("Required", "EDITOR", old["EDITOR"])
    else:
        config.set("Required", "EDITOR", new["EDITOR"])
    
    with open("%s/.pressgangcli.conf" % home, "wb") as configfile:
        config.write(configfile)

def main(argv=None):
    if argv is None:
        argv = sys.argv
    
    try:
        args = parse_args(argv)

        old_values = get_config()
        new_values = {"USER": args.user,
                      "LOCATION": args.location,
                      "PUBLIC_DTD": args.public_dtd,
                      "SYSTEM_DTD": args.system_dtd,
                      "EDITOR": args.editor}
        set_config(new_values, old_values)

    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "For help and usage information use the --help argument."
        return 2
    except Error, err:
        print >>sys.stderr, err.msg
        return 1


if __name__ == "__main__":
    sys.stdout = codecs.getwriter("UTF-8")(sys.stdout)
    sys.stderr = codecs.getwriter("UTF-8")(sys.stderr)
    sys.exit(main())
