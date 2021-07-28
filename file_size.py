import os , sys , re
def sizeToReadableFormat(size):
	current_size = size
	for size_format in ["B","K","M","G","T","P"]:
		if current_size<1024:
			return "%s %sB"%(current_size , size_format)
		current_size/=(1024) 	

def getSize(root, files):
	for file in files:
		file_path=os.path.join(root,file)
		size = os.path.getsize(file_path)
		print(file_path , sizeToReadableFormat(size))

def getMovies(dir_path):
	mov_matcher = re.compile(r".*\.mp4$")
	for root , _ , files in os.walk(dir_path):
		if files:
			mov_files = list(filter(mov_matcher.match , files))
			if mov_files:
				getSize(root,mov_files)
if __name__ == "__main__":
	getMovies("C:/Users/Sahibealam/Documents")
