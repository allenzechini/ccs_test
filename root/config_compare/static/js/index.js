function compareFiles() {
	console.log("Compare Files button was clicked")
	/*
		Eventually will have a call to config_diff.py with two files passed in by user
		e.g.
		"C:\Program Files\Python39\python.exe" 
			config_diff.py -f1 TEST_filesystem_reader.js -f2 TEST_mfx_tools.js	*/
	const firstFile = document.getElementById("first-file").files[0],
		  secondFile = document.getElementById("second-file").files[0]
	console.log("First file is " + firstFile.name)
	console.log("Seocnd file is " + secondFile.name)
	//	  "C:\Program Files\Python39\python.exe" config_diff.py -f1 firstFile -f2 secondFile
}

function uploadFiles() {
	console.log("Upload File(s) button was clicked")
	const fileList = document.getElementById("upload-files").files
	for (let i=0; i<fileList.length; i++) {
		console.log("File " + i + ": " + fileList[i])
	}
}

var cmpButton = document.getElementById("cmp-butt")
var upButton = document.getElementById("up-butt")
console.log(cmpButton)
console.log(upButton)

cmpButton.addEventListener("click", compareFiles)
upButton.addEventListener("click", uploadFiles)