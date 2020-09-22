def my_mp3_playlist(file_path):
	"""
	:param file_path: path to file.
	:type file_path: string
	:return: returns a tuple where the first element is string that represent the longest song in the file (duration), the second element
	         is a number that represent the number of songs the file contains, the third element  is a string that represent the name of 
			 the artist that appear the most in the file.
	rtype: tuple
	"""
	with open(file_path) as songs_file:
		file_contents_lines = songs_file.read().splitlines()
		file_songs_list = []
		for line in file_contents_lines:
			file_songs_list.append(line.split(";"))

	longest_time = 0
	longest_song_name = ""
	artists_list = []
	artists_appearances = 0;
	artist_name = ""
	
	for song in file_songs_list:
		song_time = song[2].split(":")
		if (int(song_time[0]) * 60 + int(song_time[1]) > longest_time):
			longest_time = int(song_time[0]) * 60 + int(song_time[1])
			longest_name = song[0]
			
		artists_list.append(song[1])
		if artists_list.count(song[1]) > artists_appearances:
			artist_name = song[1]
			
	tuple_first_element = longest_name
	
	tuple_second_element = len(file_songs_list)
	
	tuple_third_element = artist_name
	return (tuple_first_element, tuple_second_element, tuple_third_element)
	
def main():
	print(my_mp3_playlist(r"C:\Users\Liraz\Desktop\hangman\hangman-unit9\songs.txt"))

if __name__ == "__main__":
	main()