function isEmptySubmition() {
	var selected = false;

	// checks to see if a drink was selected
	for(var j=1; j<21; j++) {
		if(document.getElementById("drink-" + j).checked == true)
			selected = true;
	}

	// checks to see if a snack was selected
	for(var i=1; i<6; i++) {
		if(document.getElementById("snack-" + i).checked == true)
			selected = true;
	}

	// checks to see if a purchase was selected
	for(var j=1; j<4; j++) {
		if(document.getElementById("purchase-" + j).checked == true)
			selected = true;
	}

	return selected;
}