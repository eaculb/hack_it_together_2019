function isEmptySubmition(name, seat) {
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

	// checks to see if client requested something else
	if(document.getElementById("other-request").value.length != 0) {
		selected = true;
	}

	// if there was a selection made, confirm submission
	if(selected == true) {
		var crewmember = document.getElementById("helper").value;

		// for readability purposes
		if(crewmember == "AnyMember") {
			crewmember = "Someone";
		}

		alert("Your request has been submitted, " + name + "! \n" +
			crewmember + " will be over in seat " + seat + " soon!");
	}
	else {
		alert("You are trying to submit an empty form. Please make a selection.");
	}

	return selected;
}