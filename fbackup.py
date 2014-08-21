#! /usr/bin/env python
##
 # This file is under MIT Licence
 # Copyright (C) 2014 Alexandre BM <s@rednaks.tn>
 #   
 # Permission is hereby granted, free of charge, to any person obtaining a copy of
 # this software and associated documentation files (the "Software"),
 # to deal in the Software without restriction, including without limitation
 # the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
 # sell copies of the Software, and to permit persons to whom the Software is
 # furnished to do so, subject to the following conditions:
 #   
 # The above copyright notice and this permission notice shall be included in all copies
 # or substantial portions of the Software.
 #   
 # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
 # INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE
 # AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
 # DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 # ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import facebook

import requests
import sys
import json

facebook_access_token = ''
facebook_message_id = ''


def show_help(program):
  print "Usage: {} access_token message_id".format(program)


def get_root_message(api, message_id):
  return api.get_object(message_id)


def fetch_discussion(root):
 
  data = root['data']

  if(len(data) == 0):
    print "No more pages!"
    return data # emptry list

  next_url = root['paging']['next']
#  print next_url

  res = requests.get(next_url)
  if(res.ok):
    root = json.loads(res.content)
  else:
    print 'Error :s {}'.format(res.status_code)
    return []

  print "Next page ..."
  d = fetch_discussion(root)
  return d + data


if __name__ == '__main__':
  if(len(sys.argv)) < 2:
    show_help(sys.argv[0])
    sys.exit(-1)

  facebook_access_token = sys.argv[1]
  facebook_message_id = sys.argv[2]

  graph = facebook.GraphAPI(facebook_access_token)

  root_msg = get_root_message(graph, facebook_message_id)


  discussion_data = fetch_discussion(root_msg['comments'])

  fp = open('{}.json'.format(facebook_message_id), 'w+')
  json.dump(discussion_data, fp)
  fp.close()

  print "Finished work ! :)"

