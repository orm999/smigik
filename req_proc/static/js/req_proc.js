function getDivHtml(user, obj) {
	$.post("/", {"who": user}, function(data) {
		obj.html(data.html);
	}, "json")
}

$(document).ready(function() {
	$("a#user_room").click(function() {
		$.cookie("who", "user");
		getDivHtml("user", $("div#user_room"));
		$("div#operator_room").html("");
		$("div#admin_room").html("");

		return false;
	});

	$("a#operator_room").click(function() {
		$.cookie("who", "operator");
		getDivHtml("user", $("div#user_room"));
		getDivHtml("operator", $("div#operator_room"));
		$("div#admin_room").html("");

		return false;
	});

	$("a#admin_room").click(function() {
		$.cookie("who", "admin");
		getDivHtml("user", $("div#user_room"));
		getDivHtml("operator", $("div#operator_room"));
		getDivHtml("admin", $("div#admin_room"));
		
		return false;
	});
	
	var who = $.cookie("who");
	if (who == null) {
		who = "user";
	}
	$("a#" + who + "_room").click();
});
