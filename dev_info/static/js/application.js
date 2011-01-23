var gAnimationSpeed = "fast";
var gAnimationSpeedSlow = "slow";
var gShowNoticeTime = 2000;

$(document).ready(function() {
	$("#dev_select").change(function() {
		if ($("#display form#add_dev").length > 0) {
			$("form#add_dev").remove();
			$("a#add").click();
		}
		if ($("#display form#edit_dev").length > 0) {
			$("form#edit_dev").remove();
		}
		getDevList();
	});
	$("#dev_select").change();

	$("a#add").click(function() {
		var type = $("#dev_select option:selected").val();
		$.getJSON("/dev_info/add/", {"type": type}, function(data) {
			if (data.success == "True") {
				if ($("#display form#add_dev").length == 0) {
					$("#display").prepend(data.html);
					$("form#add_dev").hide().show(gAnimationSpeed);
				} else {
					clear_form_elements($("form#add_dev"));
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
								$("#notice").html(data.notice).hide()
									.show(gAnimationSpeed).delay(gShowNoticeTime)
									.hide(gAnimationSpeed);
								$("table#" + type + "_dev tbody tr:first").after(data.row);
								var id = $(data.row).attr("id");
								$("tr#" + id).fadeOut(gAnimationSpeedSlow)
									.fadeIn(gAnimationSpeedSlow);
								actionAddEdit();
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
					getDevList();					
					return false;
				});
			};
		});
		
		return false;
	});
	
	$("a#remove").click(function() {
		$("#display").each(function(i) {
			alert($(this).html());
		});
		
		return false;
	});
	
});

function getDevList() {
	var type = $("#dev_select option:selected").val();
	$.getJSON("/dev_info/", { 'type': type }, function(data) {
		if (data.success) {
			if ($("#dev_list").length > 0) {
				$("#dev_list").remove();
			} 
			$("#display").append(data.html);

			$("input#all").change(function() {
				if ($("input#all").is(":checked")) {
					$("input").each(function(i) {
						$(this).attr("checked", "yes");
					});
				} else {
					$("input").each(function() {
						$(this).removeAttr("checked");
					});
				};
			});
			actionAddEdit();
		};
	});
};

function actionAddEdit() {
	$("a.edit").click(function () {
		var id = $(this).attr("id");
		var type = $("#dev_select option:selected").val();
		$.getJSON("/dev_info/edit/", 
			{"type": type, "dev_id": id}, 
			function(data) {
				if (data.success == "True") {
					if ($("#display form#add_dev").length > 0) {
						$("form#add_dev").remove();
					}
					if ($("#display form#edit_dev").length == 0) {
						$("#display").prepend(data.html);
						$("form#edit_dev").hide().show(gAnimationSpeed);
					} else {
						$("#display form#edit_dev").remove();
						$("#display").prepend(data.html);
					};
					
					$("#edit_dev").submit(function(e) {
						var form = $(e.target);
						$.post("/dev_info/edit/", 
							{"type": type, "dev_id": id, "form": form.serialize()},
							function(data) {
								if (data.success == "True") {
									$("form#edit_dev").hide(gAnimationSpeed).queue(function() {
										$(this).remove();
									});
									$("#notice").html(data.notice).hide()
										.show(gAnimationSpeed).delay(gShowNoticeTime)
										.hide(gAnimationSpeed);
									$("tr#" + id).replaceWith(data.row);
									$("tr#" + id).fadeOut(gAnimationSpeedSlow)
										.fadeIn(gAnimationSpeedSlow);
									actionAddEdit();
								} else {
									$("#edit_errors").html(data.errors).hide()
										.show(gAnimationSpeed);
								}
						}, "json");
						
						return false;
					});

					$("a#cancel_edit").click(function() {
						$("form#edit_dev").hide(gAnimationSpeed).queue(function() {
							$(this).remove();
						});
						getDevList();					
						return false;
					});
			};
		});
		
		return false;
	});
	
	$("a.delete").click(function() {
		var id = $(this).attr("id");
		var type = $("#dev_select option:selected").val();
		if ($("#display form#edit_dev").length > 0) {
			$("form#edit_dev").hide(gAnimationSpeed).queue(function() {
				$(this).remove();
			});
		};
		$.post("/dev_info/delete/", 
			{"type": type, "dev_id": id},
			function(data) {
				$.noticeAdd({text: data});
//				$("#notice").html(data).hide().show(gAnimationSpeed).delay(gShowNoticeTime)
//					.fadeOut(gAnimationSpeed);
				$("tr#" + id).fadeOut(gAnimationSpeed);
			}
		);
		
		return false;
	});
}

function clear_form_elements(ele) {
    $(ele).find(':input').each(function() {
        switch(this.type) {
            case 'password':
            case 'select-multiple':
            case 'select-one':
            case 'text':
            case 'textarea':
                $(this).val('');
                break;
            case 'checkbox':
            case 'radio':
                this.checked = false;
        }
    });
}
