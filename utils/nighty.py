#!/usr/bin/env python

from optparse import OptionParser
import os.path
import shutil
import tempfile
import sys
import tarfile
import datetime
if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-s", "--skeleton", dest="skeleton", help="Location of skeleton directory")
    parser.add_option("-b", "--base", dest="base", help="location of the base directory")
    parser.add_option("-d", "--destination", dest="destination", help="where to copy our archive")
    options, args = parser.parse_args()

    if options.skeleton is None or options.base is None or options.destination is None:
        print "Need --skeleton argument as well as --base argument"
        parser.print_help()
        sys.exit()

    infoDict = {}
    info = execfile(os.path.expanduser(os.path.join(options.skeleton, "info.py")), infoDict)
    now = datetime.datetime.now()
    now = "%d%d%d" % (now.year, now.month, now.day)
    dirName = "nighty-build-%s" % now
    dst = os.path.join(tempfile.gettempdir(), dirName)
    tmpFile = os.path.join(tempfile.gettempdir(), "nighty-build-%s-%s.tar.bz2" % (now, infoDict["os"]))
    i = 0
    def loginfo(path, names):
        global i
        i += 1
        if i / 10.0 == int(i / 10):
            sys.stdout.write(".")
            sys.stdout.flush()
        return []

    try:
        print "copying skeleton to ", dst
        i = 0
        shutil.copytree(options.skeleton, dst, ignore=loginfo)
        print ""

        base = os.path.join(dst, infoDict["base"])
        print "copying base to ", base

        i = 0
        for stuff in os.listdir(options.base):
            currSource = os.path.join(options.base, stuff)
            currDest = os.path.join(base, stuff)
            if os.path.isdir(currSource):
                shutil.copytree(currSource, currDest, ignore=loginfo)
            else:
                shutil.copy2(currSource, currDest)

        print ""
        print "copying done, making archive: ", tmpFile
        archive = tarfile.open(tmpFile, "w:bz2")
        print "making archive"
        archive.add(dst)
        print "closing"
        archive.close()
        print "copying archive to ", options.destination
        shutil.copy(tmpFile, options.destination)
    except:
        print "encountered an error"
        raise
    finally:
        print "deleting tmp files"
        shutil.rmtree(dst)
        os.unlink(tmpFile)