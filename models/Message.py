class Message: 
    def __init__(self,messageID,author,dest,content,date):
        self.messageID = messageID
        self.author = author
        self.dest = dest
        self.content = content
        self.date = date 

    def get_message(self):
        return self.messageID
    
    def get_author(self):
        return self.author
    
    def get_dest(self):
        return self.dest
    
    def get_content(self):
        return self.content
    
    def get_date(self):
        return self.date
    
    def set_message(self, neWvalue):
       self.messageID = neWvalue

    def set_author(self, neWvalue):
        self.author = neWvalue
    
    def set_dest(self, neWvalue):
        self.dest = neWvalue

    def set_content(self, neWvalue):
        self.content = neWvalue

    def set_date(self, neWvalue):
        self.date = neWvalue