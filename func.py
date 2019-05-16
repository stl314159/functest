def hello(event, context):
  print event
  print "Hello World"
  return event['data']
