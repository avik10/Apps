def reply(message):
    get_req = ''
    requests = list(data['req'])
    for req in requests:
        if message == req:
            get_req = req
        else :
                get_req = 'No Reuest Found..!!'
    print(get_req)