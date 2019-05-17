def hello(event, context):
    event['data'] += "abcd"
    return event['data']
