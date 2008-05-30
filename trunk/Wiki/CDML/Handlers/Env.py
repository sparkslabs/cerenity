#!/usr/bin/env python

import os.path

class tagHandler(object):
      def doEnv(bunch, text, env):
         "Insert the value of an environment variable"
         try:
            variable = bunch["var"]
         except KeyError:
            return "WHICH VARIABLE?"

         try:
            return env[variable]
         except KeyError:
            if bunch.get("default", None) is None:
               return "variable not set"
            else:
               return bunch["default"]

      mapping = {
                 "env": doEnv,
      }
      
mapping = tagHandler.mapping

if __name__ == "__main__":
   print "TAG HANDLER", tagHandler
   print "MAPPING", tagHandler.mapping
   
