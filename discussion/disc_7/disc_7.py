
#page4
class MinList:

	def __init__(self):
	self.size = 0
	self.items = []

	def append(self, item):
		self.items.append(item)
		self.size += 1

	def pop(self):
		min_elem = min(self.items)
		self.items.remove(min_elem)
		self.size -= 1
		return min_elem

#page5
class Email:
    """Every email object has 3 instance attributes:
    the message, the sender name, and the recipient name.
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name


class Server:
    
    def __init__(self):
        self.clients = {}
        
    
    def send(self, email): #這個函數的body,都不會寫
        #拿到email後，放置到收信client的inbox裡面
        recipient = email.recipient_name
        client = self.clients[recipient]
        client.receive(email)
        

    def register_client(self, client, client_name):  ##一開始錯
        self.clients[client_name] = client





class Client:

    def __init__(self, server, name):
        self.inbox = []
        self.server = serve
        self.name = name
        self.server.register_client(self, self.name) ##不懂為何要加這行

    def compose(self, msg, recipient_name):
        
        email = Email(msg,self.name, recipient_name)
        self.server.send(email)

    def receive(self, email):
        self.inbox.append(email)
        

#page8

class Cat(Pet):
    def __init__(self, name, owner, lives= 9):
        super().__init__(name, owner)
        self.lives = lives
        self.is_alive = True if self.lives > 0 else False #不要忘記加
        
    def talk(self):
        print(self.name + 'says meow!')


    def lose_life(self):
        
        if self.is_alive == False:
            print (self.name +  "has no more lives to lose.")
            
            
        else:
            self.lives -= 1
            self.is_alive = True if self.lives > 0 else False #不要忘記加

#page9

class NoisyCat(Cat):
    "__init__ method is not necessary
    "because it is same as superclass init method"
    super().__init__(name, owner, lives)

    def talk(self):
        for _ in range(2): #很好用的用法
            super().talk()


    def __repr__(self):

        return "NoisyCat ('{}', '{}')".format(self.name, self.owner) #注意引號
















    
        
    
        
