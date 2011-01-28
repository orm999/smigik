function init_state() {
	$("#subj_select option#0").attr("selected", "selected");
	$("#id_subject:text").val("");
}

$(document).ready(function() {
	$("#subj_select").change(function() {
		if ($("#subj_select option:selected").attr("id") == "") {
			var new_val = "";
		} else {
			var new_val = $("#subj_select option:selected").val()
		}
		$("#id_subject:text").val(new_val);
	});
	init_state();
	
	$("#save_subj").submit(function() {
		var subject = $("input:text").val();
		var id = $("#subj_select option:selected").attr("id");
		var answer = true;
		if (subject) {
			if (id != "0") {
				answer = confirm("Принять изменения в названии тематики?");
			}
		} else {
			answer = confirm("Вы действительно хотите уделить тематику?");
		}
		if (answer) {
			$.post("/img_subj/", {"subj_id": id, "subject": subject}, function(data) {
				$.noticeAdd({text: data.msg});
				if (data.action == "added") {
					$("#subj_select").append(data.option);
				} else if (data.action == "updated") {
					var new_id = $(data.option).attr("id");
					$("#subj_select option#" + id).replaceWith(data.option)
				} else if (data.action == "deleted") {
					$("#subj_select option:selected").remove();
				} else if (data.action == "exists" || data.action == "doesnotexist") {
				}
				
				init_state();
			}, "json");
		} else {
			init_state();
		};
	
		return false;
	});
});
