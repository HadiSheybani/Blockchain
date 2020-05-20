from entity.policy import Policy


class First3ZeroPolicy(Policy):

    def check(self, hash : str):
        if (hash[0] == '0' and hash[1] == '0' and hash[2] =='0'):
            return True
        return False
