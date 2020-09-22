def my_mp4_playlist(file_path, new_song):
	"""
	:param file_path: path to the file. 
	:param new_song: name of a new song
	:type file_path: string
	:type new_song: string
	:return: 
	rtype:
	"""
	with open(file_path, 'r') as songs_file:
		file_contents_lines = songs_file.read().splitlines()
		file_songs_list = []
	
	for line in file_contents_lines:
		file_songs_list.append(line.split(";"))

	if (len(file_songs_list) < 3):
		file_songs_list.append([new_song, "Unknown", "4:15"])
	else:
		file_songs_list[2][0] = new_song
		file_songs_list[2][1] = "Unknown"
	
	with open(file_path, 'w') as song_file:
		if (len(file_songs_list) < 3):
			for row in range(3 - len(file_songs_list)):
				song_file.write("\n")
		for song in file_songs_list:
			if (len(song) < 3):
				song = ['', '', '']
			song_file.write("%s;%s;%s;\n" % tuple(song[0:3]))
			
	with open(file_path, 'r') as songs_file:
		file_contents_lines = songs_file.read()
	print (file_contents_lines)
	
	
def main():
	my_mp4_playlist(r"C:\Users\Liraz\Desktop\hangman\hangman-unit9\songs.txt", "Python Love Story")

if __name__ == "__main__":
	main()