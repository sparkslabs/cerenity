#!/usr/bin/env python

import os.path

class tagHandler(object):

      def doRoundBox(bunch, text, env):
         "roundedbox"
         template = """\
<div class="rbroundbox_%(colour)s">
    <div class="rbtop_%(colour)s">
        <div></div>
    </div>
    <div class="rbcontent_%(colour)s">
  <div class="sectionheader"> %(heading)s </div>
  <div class="sectioncontent">
%(content)s
</div>
    </div>
    <div class="rbbottom_%(colour)s">
        <div class="rbbot_%(colour)s"><div></div></div>
    </div>
</div>
"""
         foo = {
             "colour" : bunch.get("colour", "green"),
             "heading" : bunch.get("heading", env.get("heading", "")),
             "content" : text,
         }
         
         return template % foo;

      def doSectionHeading(bunch, text, env):
         "sectionheading"
         env["heading"]=text
         return ""

      mapping = {
                 "sectionheading" : doSectionHeading,
                 "roundedbox" : doRoundBox,
      }
      
mapping = tagHandler.mapping

if __name__ == "__main__":
   print "TAG HANDLER", tagHandler
   print "MAPPING", tagHandler.mapping
   
   print "HMM", tagHandler.mapping["href"]({"location":"bingle"}, "hello world", {})