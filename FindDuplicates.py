# -*- coding: utf-8 -*-
"""

@author: samantha (HireSamH@gmail.com)

Rudimentry commandline duplicate file finder.
Walk the directorries to find duplicates using MD5sum.

"""

import os.path
import sys
import os
import subprocess as sub

files = {}

def add_to_dic(file_name):
    """
        Adds file to dictionary as MD5Sum as the Key and
        file name as value (a list).
    """
    global files;
    #generate md5
    cmd = 'md5'+ ' ' + file_name
    # md5 = os.system(cmd)  # does not return the output
    #print file_name, '->', md5 , ', type = ', type(md5), ' hash=', hash(md5)
    p = sub.Popen(cmd, stdout = sub.PIPE, stderr = sub.PIPE)
    output, errors = p.communicate()
    print output, errors
    #print file_name, '->', md5

    # if this is the first file with this md5, create empty list
    #if md5 not in files.keys():
     #   files[md5] = []


    #(files[md5]).append(file_name)
    #print files, '\n'


def show_results():

    """ Produces final onscreen output
    """

    dup_grp_no = 0

    for k, v in files.iteritems():
        if len(v) >1:  # there are duplicates
            #print "Duplicates with MD5=", k
            dup_item_no = 0
            dup_grp_no += 1
            print '>>>> Duplicate Group #', dup_grp_no

            for i in v:
                dup_item_no += 1;
                print '\t', dup_item_no , ': ', i

    # if there were no duplicates
    if dup_grp_no == 0:
        print "Be happy! No duplicated found."


if __name__ == '__main__':
    print 'args ', sys.argv

    if len(sys.argv) != 2:
        print 'Only one argument, a directory, is expected!'
    else:
        #thisdirfiles = os.listdir(sys.argv[1])
        #print thisdirfiles

        for dirpath, dirnames, filenames in os.walk(os.curdir):
            for fp in filenames:
                thisfile = os.path.abspath(fp)
                #print thisfile
                add_to_dic(thisfile)

        show_results()


