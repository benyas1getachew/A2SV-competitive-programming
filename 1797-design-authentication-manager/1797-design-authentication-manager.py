class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tim=timeToLive
        self.token={}
        
        
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token[tokenId]=currentTime
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.token.keys():
            a=self.token[tokenId]
            if currentTime-a<self.tim:
                self.token[tokenId]=currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        cnto=0
        
        for k in self.token.keys():
            a =self.token[k]
            if currentTime-a <self.tim:
                cnto+=1
        return cnto
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)