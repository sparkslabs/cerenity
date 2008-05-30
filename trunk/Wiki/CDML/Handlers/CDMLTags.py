#!/usr/bin/env python

import os.path

class tagHandler(object):
      def doHTML(bunch, text, env):
         return "<html>%s</html>" % text

      def doBODY(bunch, text, env):
         "body"
         return "<body>%s</body>" % text
      
      def doLINK(bunch, text, env):
         "link"
         return "<a href='%s'>%s</body>" % text

      def doPRE(bunch, text, env):
         "pre"
         return "<pre>%s</pre>" % text

      def doTitle(bunch, text, env):
          "title"
          return env["pagename"]

      def doTT(bunch, text, env):
         "tt"
         return "<tt>%s</tt>" % text

      def doHref(bunch, text, env):
         "href"
         return "<a href='%s'>%s</a>" % (bunch["location"], text)

      def doAnchor(bunch, text, env):
         "anchor"
         return "<a name='%s'> </a>" % (bunch["name"], )

      def doGroup(bunch, text, env):
         "group"
         return "<table width='100%%' border='0'><tr><td>%s</td></tr></table>" % (text)

      def doBoxRight(bunch, text, env):
         "boxright"
#         return "<table width='40%%' border='2' align='right'><tr><td>%s</td></tr></table>" % (text)
         return '</div> <div class="boxright">%s</div><div class="bodytext">' % (text)

      def doOldBoxRight(bunch, text, env):
         "oldboxright"
         return "<table width='40%%' border='2' align='right'><tr><td align='centre'>%s</td></tr></table>" % (text)
      
      def doSystemNote(bunch, text, env):
         "systemnote"
         return env.get("systemnote","")+text


      def doImg(bunch, text, env):
         "img tag"
         if bunch.get("align", None) is not None:
            align = " align='%s'" % bunch["align"]
         else:
            align = ""
         if bunch.get("width", None) is not None:
            width = " width='%s'" % bunch["width"]
         else:
            width = ""
         return "<img src='%s'%s%s>%s" % (bunch["src"], align, width,text)
     
      def doScriptUrl(bunch, text, env):
         "scripturl"
         return env.get("root", "")+text

      def doPagename(bunch, text, env):
         "discuss"
         

         return "%s <a href='%s%s'> %s </a> %s " % (\
                                           "<b> Discussion </b> Please discuss this on",
                                           env.get("root", ""),
                                           env.get("pagename", "XXXXXX")+"Discuss",
                                           "the discussion page",
                                           "for this page")

      mapping = {
                 "group" : doGroup,
                 "img" : doImg,
                 "href": doHref,
                 "html": doHTML,
                 "body": doBODY,
                 "boxright" : doBoxRight,
                 "oldboxright" : doOldBoxRight,
                 "axon.interfacedef" : doBoxRight,
                 "pre" : doPRE,
                 "tt" : doTT,
                 "title" : doTitle,
                 "systemnote": doSystemNote,
                 "discuss" : doPagename,
                 "anchor" : doAnchor,
#                 "scripturl" : doScriptUrl,
      }
      
mapping = tagHandler.mapping

if __name__ == "__main__":
   print "TAG HANDLER", tagHandler
   print "MAPPING", tagHandler.mapping
   print "HMM", tagHandler.mapping["href"]({"location":"bingle"}, "hello world", {})
