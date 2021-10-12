# from urllib import request
# import ssl
# import json
# import atexit
# import time
# import datetime
# import pytz

# #problemId : [str] 문제번호
# #problemName : [str] 문제이름
# #problemTier : [int] 문제 난이도
# #lastupdate : [float] 업데이트 로그

# def changeLevel(level):
#     ALPHA = [ 'EASY','MEDIUM','HARD' ]
#     level -= 1
#     return f"{ALPHA[level // 3]}{3 - level % 3}"


# class SolvedAPI:
#     def __init__(self,config):
#         assert type(config) == dict
#         self.ssl_context = ssl._create_unverified_context()
#         self.config = config
#         self.database = dict()
#         self.changeLevelLog = list()

#         #Load database
#         self.__Load_database()
#         self.__all_update()



#     def __all_update(self):
#         problemList = list()
#         problemIds = list(self.database.keys())
        

#         #update
#         # URL = f"https://leetcode.com/problems/"
#         # req         = request.Request(URL, headers = {'User-Agent': 'Mozilla/5.0'})
#         # response    = request.urlopen(req, context=self.ssl_context)





# #Example
# if __name__=="__main__":
#     config = dict()