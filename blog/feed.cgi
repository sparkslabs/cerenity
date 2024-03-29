#!/usr/bin/python


from __future__ import generators
import cgitb; cgitb.enable()
import cgi
import time
import os

config = (__import__("config")).config
Posts = (__import__("Posts")).Posts

posts = Posts()

print """\
Content-Type: application/xml

<?xml version="1.0"?>
<rss version="2.0">
   <channel>
      <title>%s</title>
      <link>%s</link>
      <description>%s</description>
      <language>en-uk</language>
      <pubDate> %s </pubDate>
      <lastBuildDate> %s </lastBuildDate>
      <docs>http://blogs.law.harvard.edu/tech/rss</docs>
      <generator>Kamaelia 0.1</generator>
      <managingEditor>%s</managingEditor>
      <webMaster>%s</webMaster>
""" % (config.v["blogname"],
       config.v["fullurl"],
       config.v["description"],
       time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()),
       time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()), 
       config.v["contact"],
       config.v["contact"], )
#for postid in posts.allNodes()[:7]:

nodes = list(posts.allNodes())
nodes = [ (    os.stat(os.path.join("posts", nodeid))  , nodeid ) for nodeid in nodes ]
nodes.sort()
nodes = [ nodeid for ts,nodeid in nodes ]

for postid in nodes[:10]:
   post = posts.readNode(postid)
   if post.get("Visible", "0") == "1":
      subject = cgi.escape(post.get("Subject","No subject"))
      description = cgi.escape(post.get("__SUMMARY__","No summary"))
      author = cgi.escape(post.get("From","Guest"))
      pid = postid +".0"

      filestat = os.stat(os.path.join("posts", postid))
      t = time.gmtime(filestat.st_mtime)                  # |    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
      date = time.strftime("%a, %d %b %Y %H:%M:%S +0000", t)
      posturl = config.v["fullurl"]+"?rm=viewpost&amp;nodeid="+postid
      link = cgi.escape( posturl )
      print """\
      <item>
         <title>%(subject)s</title>
         <link>%(link)s</link>
         <author>%(author)s</author>
         <description>%(description)s</description>
         <pubDate>%(date)s</pubDate>
         <guid>%(link)s</guid>
      </item>
""" % {
   "subject" : subject,
   "description" : description,
   "date" : date,
   "author" : author,
   "link" : link,
}
print """\
   </channel>
</rss>
"""
