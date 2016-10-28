var cats = document.getElementsByClassName("tile");

if (true) {
	console.log("here");
	var emptyDiv = document.createElement("div")
	emptyDiv.className="tile empty";
	emptyDiv.id="overlay";
	emptyDiv.style.display="hidden"
	var emptyDivin = document.createElement("div")
	emptyDivin.className="tile empty";
	emptyDivin.id="category";
	emptyDivin.style.display="hidden"
	emptyDivin.style.border="transparent";
	emptyDiv.appendChild(emptyDivin);
	var cont =document.body.getElementsByClassName("container")[0];
	cont.appendChild(emptyDiv)
}