def hello(event, context):
    event['data'] += " test"
    return event['data']
