$(document).ready(function() {
	$("#devs").change(onSelectChange);
	$("#devs").change();
})

function onSelectChange() {
	var selected = $("#devs option:selected");
	if (selected.val() != 0) {
		var type = selected.val();
		$.get("/dev_info/", { 'type': type }, function(data) {
			$("#dev_list").html(data);
		})
	}
}