class User:
    async def SendMessage(self, conn):
        data = await self.RecvProto(conn)
        ips = self.DB.Check(self.account, self.where[self.account._connection_ != None], fetch='*', columns=['_connection_'])
        for ip in ips:
            far_host = self.Connections[ip[0]]
            far_host_connection = await self.Communicate(far_host, "RecvMessage")
            await self.SendProto(far_host_connection, data)
    async def Login(self, conn):
        payload = await self.RecvProto(conn)
        if not self.DB.Check(self.account, self.where[self.account.username == payload['username']]):
            self.DB.Insert(self.account, {
                'username': payload['username'],
                'password': self.Crypto.Hash.Sha512(payload['password']),
                '_connection_': conn
            })
            await self.SendSignal(conn, 1)
        else: await self.SendSignal(conn, 0)
