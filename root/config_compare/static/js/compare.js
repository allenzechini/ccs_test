function compareFiles() {
	console.log("Compare Files button was clicked")
	//
	// 	Eventually will have a call to config_diff.py with two files passed in by user
	// 	e.g.
	// 	"C:\Program Files\Python39\python.exe" 
    //         config_diff.py -f1 TEST_filesystem_reader.js -f2 TEST_mfx_tools.js	
    // */
	const firstFile = document.getElementById("first-file").files[0]
	const secondFile = document.getElementById("second-file").files[0]
	console.log("First file is " + firstFile.name)
	console.log("Seocnd file is " + secondFile.name)
    
    // var myURL = "../scripts/config_diff.py -f1 "+firstFile+" -f2 "+secondFile
    // $.ajax({
    //     type: "get",
    //     url: myURL,
    //     cache:false,
    //     async:'asynchronous',
    //     dataType:'json',
    //     success: function(data) { console.log(JSON.stringify(data)) },
    //     error: function(request, status, error) { console.log("Error: " + error) }
    // })
}

var cmpButton = document.getElementById("cmp-butt")
console.log(cmpButton)
cmpButton.addEventListener("click", compareFiles)
    
    /**
     * Cannot run Python in JS...
     * Need to make an AJAX request to a web server that then calls the Python script
     * via a GET or POST request handler
     * 
     * Example from Nadya Pena:
     * 
     * Client-side JS:
     * 
     * $("#target").click(function(){ 
     * 
     *     $.ajax({ 
     *         type:'get',
     *         url:'/URLToTriggerGetRequestHandler',
     *         cache:false,
     *         async:'asynchronous',
     *         dataType:'json',
     *         success: function(data) {
     *             console.log(JSON.stringify(data))
     *         },
     *         error: function(request, status, error) {
     *             console.log("Error: " + error)
     *         }
     *     })
     * })
     * 
     * Server-side Python in config_diff.py
}

var cmpButton = document.getElementById("cmp-butt")
console.log(cmpButton)
cmpButton.addEventListener("click", compareFiles)

/**
 * Drag and drop (test later)
 * 
 * function dragenter(e) {
 *   e.stopPropagation()
 *   e.preventDefault()
 * }
 * 
 * function dragover(e) {
 *   e.stopPropagation()
 *   e.preventDefault()
 * }
 * 
 * function drop(e) {
 *   e.stopPropagation()
 *   e.preventDefault()
 * 
 *   const dt = e.dataTransfer
 *   const files = dt.files
 * 
 *   handleFiles(files) // need to write
 * }
 * 
 * let dropbox
 * 
 * dropbox = document.getElementById("dropbox")
 * dropbox.addEventListener("dragover", dragover, false)
 * dropbox.addEventListener("drop", drop, false)
 * 
 */