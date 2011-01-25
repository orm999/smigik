$(document).ready(function() {
	$("#subj_select").change(function() {
		if ($("#subj_select option:selected").attr("id") == "") {
			var new_val = "";
		} else {
			var new_val = $("#subj_select option:selected").val()
		}
		$("#id_subject:text").val(new_val);
	});
	$("#subj_select").change();
	
	$("#save_subj").submit(function() {
		var subject = $("input:text").val();
		var id = $("#subj_select option:selected").attr("id");
		$.post("/img_subj/", {"subj_id": id, "subject": subject}, function(data) {
			$.noticeAdd({text: data.msg});
			if (data.option) {
				var new_id = $(data.option).attr("id");
				if (new_id == id) {
					$("#subj_select option#" + id).replaceWith(data.option)
				} else {
					$("#subj_select").append(data.option);
				}
				$("#id_subject:text").val("");
			} else {
				$("#subj_select option:selected").remove();
			}
		}, "json");
		
		return false;
	});
});
