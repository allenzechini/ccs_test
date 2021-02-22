const uploadedFiles = []

async function uploadFiles() {
	console.log("Upload File(s) button was clicked")
	const fileList = document.getElementById("upload-files").files
	for (let i=0; i<fileList.length; i++) {
		console.log("File " + i + ": " + fileList[i].name)
	}
	// let uploadStatus = new Promise( (resolve, reject) => {
	// 	setTimeout ( () => {
	// 		uploadedFiles.push("New File")
	// 		resolve("File was uploaded successfully")
	// 	}, 3000)
	// })

	// // Await resolution from uploadStatus
	// let result = await uploadStatus

	// console.log(result)
	// console.log(uploadedFiles.length)
}

var upButton = document.getElementById("up-butt")
upButton.addEventListener("click", uploadFiles)