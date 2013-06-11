Question：

http://weibo.com/lirenchen @陈利人

有10个文件，每个文件1G，每个文件的每行存放的都是用户的query（请自己随机产生），每个文件的query都可能重复。要求你按照query的频度排序。

Solution:
sort users' queries by frequency

1. hashing queries and dividing into 10 files. (hash(query)%10)

2. counting the number queries and sorting in each file using hashtable.

3. merging files using heap queue algorithm.
