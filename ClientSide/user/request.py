class Communication:
    def RecvMessage(self, conn):
        data = self.RecvProto(conn)
        self.button.data = [data['username'], data['message']]
        self.button.click()


class RequestsPanel:
    Communication = Communication()

    def SendMessage(self, conn, data):
        self.SendProto(conn, data)

    def Login(self, conn, data):
        self.SendProto(conn, data)
        code = self.RecvSignal(conn)
        if code != 0:
            return code
        else:
            raise NotImplementedError("Server Refused")
