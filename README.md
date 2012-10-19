# Pressgang CCMS Command Line Tools #

## pressgang-config ##

The *pressgang-config* command is used to set configuration keys in the ~/.pressgangcli.conf file. These configuration keys are used by the other scripts when interacting with Pressgang.

### Syntax ###

   pressgang-config [-h] [-u USER] [-l LOCATION] [-p PUBLIC_DTD] [-s SYSTEM_DTD] [-e EDITOR]

### Options ###

 * *-h* - Display help.
 * *--user | -u*  - Update the USER configuration key with the Pressgang user name to use for authentication.
 * *--location | -l* - Update the LOCATION configuration key with the URL of the Pressgang server (e.g. https://localhost:8443/).
 * *--public_dtd | -p* - Update the PUBLIC_DTD configuration key with the public identifier of the DTD to use for validation.
 * *--system_dtd | -s* - Update the SYSTEM_DTD configuration key with the systen identifier of the DTD to use for validation.
 * *--editor | -e* - Update the EDITOR configuration key with the path to the editor to use for topic manipulation.

## pressgang-get ##

The *pressgang-get* script gets the XML for a topic from the Pressgang CCMS. Output is sent to stdout.

### Syntax ###

    pressgang-get [-h] [--diff | -d] [--json | -j] [--revision|-r=REVISION] <TOPIC> 

### Options ###

 * *-h* - Display help.
 * *--diff | -d* - Performs a diff operation. Where no revision is specified, the latest revision is treated as the 'new' revision and the previous revision is treated as the 'old' revision for the purposes of the diff. Where one revision is specified then it is treated as the 'new' revision and the previious revision is treated as the 'old' revision. Where two revisions are specified then the first is treated as the 'old' revision and the second as the 'new' revision.
 * *--json | -j* - Instead of returning the topic XML, returns the JSON representation of the topic. This option is not compatible with the *--diff* and *-d* options.
 * *--revision | -r* - Specifies a specific revision to retrieve or, when combined with the *--diff* or *-d* options, the revisions to perform a diff operation on. To specify two revisions, separate them with a colon (:).
 * *TOPIC* - Specifies the identifier of the topic to be retrieved. This must be either the numeric identifier of the topic or its short URL title.
  
## pressgang-put ##

The *pressgang-put* script updates a topic in the Pressgang CCMS.  On successful completion skynet-put displays the topic identifier and the revision information for the change.

### Syntax ###

	pressgang-put [-h] [--title|-t=TITLE] [--file|-f=FILE]  <topic>

### Options ###

 * *-h* - Display help.
 * *--title | -t* - Changes the title of the topic to the specified value.
 * *--file | -f* - Specifies the file to read the topic XML from. If no file is specified then the XML is read from standard input.
 * *TOPIC*  - Specifies the identifier of the topic to be retrieved. This must be either the numeric identifier of the topic or its short URL title.

