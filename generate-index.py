import os
import sys
from natsort import os_sorted

indexTextStart = """<!DOCTYPE html>
<html>
<head><title>Index of KindleBooks</title></head>
<link rel="stylesheet" href="assets/mystyle.css">
<script src="assets/search.js"></script>
<body>
    <h2>KindleBooks</h2>
<input type="text" id="searchInput" onkeyup="searchFunction()" placeholder="Search for books..">
    <ul id="myUL">
		<li>
			<a href="https://horrible-duck-6.telebit.io/hindu">TheHindu</a>
		</li>
		<li>
			<a href="https://horrible-duck-6.telebit.io/ie">IndianExpress</a>
		</li>		
"""
indexTextEnd = """
	</ul>
</body>
</html>
"""
# take Folder path
Dir = sys.argv[1]
def index_folder(folderPath):
	print("Indexing: " + folderPath)
	#Getting the content of the folder
	files = os_sorted(os.listdir(folderPath))
	#If Root folder, correcting folder name
	root = folderPath
	if folderPath == '.':
		root = 'Root'
	indexText = indexTextStart.format(folderPath=root)
	for file in files:
		#Avoiding index.html files
		if file != 'index.html':
			indexText += '\t\t<li>\n\t\t\t<a href="' + Dir + "/" + file + '">' + file + "</a>\n\t\t</li>\n"
		#Recursive call to continue indexing
		if os.path.isdir(folderPath+'/'+file):
			index_folder(folderPath + '/' + file)
	indexText += indexTextEnd
	#Create or override previous index.html
	index = open("."+'/index.html', "w")
	#Save indexed content to file
	index.write(indexText)

#Indexing root directory (Script position)
index_folder(Dir)
