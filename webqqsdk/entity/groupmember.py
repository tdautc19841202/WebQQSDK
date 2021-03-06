#coding=UTF8

class GroupMember(object):
    """
        self.uin: int, 群成员临时号码
        self.qq: int, 群成员的QQ号
        self.nick: string, 昵称
        self.card: string, 群名片，没有则为""
        self.isAdmin: bool, 是否是群管理员
        self.ip: int, 登录IP，只有群成员发送了消息才能获取
        self.status: 登录状态
    """

    def __init__(self):
        

        self.uin = 0
        self.nick = ""
        self.card = ""
        self.isAdmin = False
        self.ip = 0
        self.status = None

    def getName(self):
        """
        有群名片则返回群名片，
        无则返回昵称
        """
        return self.card or self.nick

    def __getattr__(self,name):

        if "qq" == name:
            return self.getQQ(self.uin)

    def getQQ(self,uin):
        """
        返回QQ号(int)
        """
