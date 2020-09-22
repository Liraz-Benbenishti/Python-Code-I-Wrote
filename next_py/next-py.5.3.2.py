class MusicNotes():
	def __init__(self):
		self._index = -1
		self._freqs = [55, 61.74, 65.41, 73.42, 82.41, 87.31, 98]
	
	def __next__(self):
		if self._index >= len(self._freqs) * 5 - 1:
			raise StopIteration
			
		self._index += 1
			
		return self._freqs[self._index % 7] * 2 ** int(self._index / 7)
	
	def __iter__(self):
		return self
		
notes_iter = iter(MusicNotes())
for freq in notes_iter:
    print(freq)