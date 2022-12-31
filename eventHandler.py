def eventHandler(sio, time):
    # all the msg in a list
    msgList = []
    # Socket server event handlers

    @sio.event
    def connect(sid, environ):
        print('connect ', sid)

    # receive message from client
    @sio.event
    def sendMsg(sid, data):
        print('message ', data)
        # get current time in ms for random and unique user id
        t_ms = int(round(time.time() * 1000))
        msgList.append({
            'id': t_ms,
            'uid': sid,
            'msg': data,
        })
        sio.emit('recvMsg', msgList)

    @sio.event
    def disconnect(sid):
        print('disconnect ', sid)
