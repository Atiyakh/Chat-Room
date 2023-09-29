from Client.connection_vent import *
from request import RequestsPanel
from QDesign import GUI


class User:
    def __init__(self):
        self.server = ConnectionHandler(self)
        self.initiate()

    def send_msg(self, username, msg):
        self.server.PostRequest(RequestsPanel.SendMessage, data={
            'username': username,
            'message': msg
        })

    def login(self, username, password):
        return self.server.PostRequest(RequestsPanel.Login, data={
            'username': username,
            'password': password
        })

    def initiate(self):
        self.gui = GUI(self)


if __name__ == '__main__':
    user = User()
