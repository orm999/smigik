$(document).ready(function() {
//	alert('hi');
//	$("#devs").change(onSelectChange);
})

function onSelectChange() {
//	alert("hi");
	var selected = $("#developer option:selected");
	var output = "sdf";
	if (selected.val() != 0) {
		output = "You selected " + selected.text(); 
	}
	$("#dev_output").html(output);
}