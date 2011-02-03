$(document).ready(function() {
	$("div.req_proc").hide();

	$("a.request").click(function() {
		$("div.req_proc").hide();

		var div_id = $(this).attr("id").split("_")[1];
		$("div#req_proc_" + div_id).show(gAnimationSpeed);
		return false;
	})
	
	$("a.upload_img").click(function() {
		var div_id = $(this).attr("id").split("_")[2];
		$.ajax({url: "/req_proc/upload_img/", 
			success: function(data) {
				if (data.success == "True") {
					$("div#req_proc_" + div_id).append(data.html);
					
					if ($("#display form#add_dev").length == 0) {
						$("#display").prepend(data.html);
						$("form#add_dev").hide().show(gAnimationSpeed);
					} else {
						$.clear_form_elements($("form#add_dev"));
					};
					if ($("#display form#edit_dev").length > 0) {
						$("form#edit_dev").remove();
					}
	
					$("#add_dev").submit(function(e) {
						var form = $(e.target);
						$.post("/dev_info/add/", {"type": type, "form": form.serialize()},
							function(data) {
								if (data.success == "True") {
									$("form#add_dev").hide(gAnimationSpeed).queue(function() {
										$(this).remove();
									});
									$.noticeAdd({text: data.notice});
									$("table#" + type + "_dev tbody tr:first").after(data.row);
									var id = $(data.row).attr("id");
									$("tr#" + id).fadeOut(gAnimationSpeedSlow)
										.fadeIn(gAnimationSpeedSlow);
									actionEditDelete();
								} else {
									$("#add_errors").html(data.errors).hide().show(gAnimationSpeed);
								}
						}, "json");
						
						return false;
					});
	
					$("a#cancel_add").click(function() {
						$("form#add_dev").hide(gAnimationSpeed).queue(function() {
							$(this).remove();
						});
						return false;
					})
				}
			},
			
			type: "GET",
			dataType: "json",
			
			singleton: true,
			delay: gRequestDelay,
		});

		return false;
	})
	
	$("a.upload_cert").click(function() {
		return false;
	})
});
