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
<div class="wrap">
	<div class="search">
	   <input type="text" id="searchInput" onkeyup="searchFunction()" placeholder="What are you looking for?">
	   <button type="submit" class="searchButton"></button>
		 <i class="fa fa-search"></i>
	  </button>
	</div>
 </div>
 <div class="items">
    <ul id="myUL">
"""
indexTextEnd = """
	</ul>
	</div>
</body>
</html>
"""
# take Folder path
Dir = sys.argv[1]


def index_folder(folderPath):
    print("Indexing: " + folderPath)
    # Getting the content of the folder
    files = os_sorted(os.listdir(folderPath))
    # If Root folder, correcting folder name
    root = folderPath
    if folderPath == '.':
        root = 'Root'
    indexText = indexTextStart.format(folderPath=root)
    for file in files:
        # Avoiding index.html files
        if file != 'index.html':
            indexText += '\t\t<li>\n\t\t\t<a href="' + Dir + \
                "/" + file + '">' + file + "</a>\n\t\t</li>\n"
        # Recursive call to continue indexing
        if os.path.isdir(folderPath+'/'+file):
            index_folder(folderPath + '/' + file)
    indexText += indexTextEnd
    # Create or override previous index.html
    index = open("."+'/index.html', "w")
    # Save indexed content to file
    index.write(indexText)


# Indexing root directory (Script position)
index_folder(Dir)
