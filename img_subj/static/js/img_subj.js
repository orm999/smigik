var gAnimationSpeed = "fast";
var gAnimationSpeedSlow = "slow";
var gShowNoticeTime = 2000;

$(document).ready(function() {
	$("#subj_select").change(function() {
//		alert('hi');
	});
	$("#subj_select").change();
	
	$("#save_subj").submit(function() {
		var subject = $("input:text").val();
		var id = $("#subj_select option:selected").attr("id");
		$.post("/img_subj/", {"subj_id": id, "subject": subject}, function(data) {
			$.noticeAdd({text: data.msg});
			if (data.option) {
				alert(data.option);
			}
		}, "json");
		
		return false;
	});
});
