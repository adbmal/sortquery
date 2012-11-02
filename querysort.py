import os
import os.path
import operator
import heapq

"""
sort users' queries by frequency
1. hashing queries and dividing into 10 files. (hash(query)%10)
2. counting the number queries and sorting in each file using hashtable.
3. merging files using heap queue algorithm.
"""

datadir  = "d:/querysort/data/"
tempdir  = "d:/querysort/temp/"
destfile = "d:/querysort/sorted.txt"

def hashfiles():
    fs = []
    if not os.path.exists(tempdir):
        os.makedirs(tempdir)
    for f in range(0,10):
        fs.append(open(tempdir + str(f), 'w'))
    
    for parent, dirnames, filenames in os.walk(datadir):
        for filename in filenames:
            f = open(os.path.join(parent, filename),'r')
            for query in f:
                fs[hash(query)%10].write(query)
            f.close()          

    for f in fs:
         f.close()
     
                
def sortqueryinfile():
    fs = []
    if not os.path.exists(tempdir):
        return
    for f in range(0,10):
        fs.append(open(tempdir + str(f), 'r+'))

    for f in fs:
        D = {}
        for query in f:
            if query in D:
                D[query] += 1
            else:
                D[query] = 1
        sorted_D = sorted(D.iteritems(), key=operator.itemgetter(1), reverse=True)
        f.seek(0,0)
        f.truncate()
        for item in sorted_D:
            f.write(str(item[1]) + "\t" + item[0])
        f.close()

def decorated_file(f):
    """ Yields an easily sortable tuple. 
    """
    for line in f:
        count, query = line.split('\t',2)
        yield (-int(count), query)

def mergefiles():
    fs = []
    if not os.path.exists(tempdir):
        return
    for f in range(0,10):
        fs.append(open(tempdir + str(f), 'r+'))
    f_dest = open(destfile,"w")
    lines_written = 0
    for line in heapq.merge(*[decorated_file(f) for f in fs]):
        f_dest.write(line[1])
        lines_written += 1
    return lines_written

     
if __name__ == '__main__':
    hashfiles()
    sortqueryinfile()
    print "sorting completed, total queries: ", mergefiles()
