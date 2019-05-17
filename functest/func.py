def hello(event, context):
    event['data'] += " test1"
    return event['data']
