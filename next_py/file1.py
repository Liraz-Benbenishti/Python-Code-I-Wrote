class GreetingCard:
	def __init__(self, recipient="Dana Ev", sender="Eyal Ch"):
		self._recipient = recipient
		self._sender = sender
	
	def greeting_msg(self):
		print("Sender: %s Recipient: %s" % (self._sender, self._recipient))
		