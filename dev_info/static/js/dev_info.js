var gAnimationSpeed = "fast";
var gAnimationSpeedSlow = "slow";
var gShowNoticeTime = 2000;
var gRequestDelay = 1000;


$.tr_type = function tr_type(type) {
	if (type == "input")
		return "ввода";
	else
		return  "вывода";
}

$.clear_form_elements = function clear_form_elements(ele) {
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
		$.ajax({url: "/dev_info/add/", 
			data: {"type": type}, 
			success: function(data) {
				if (data.success == "True") {
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
	//					getDevList();				
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
	});
	
	$("a#deleteChecked").click(function() {
		var checkboxes = $("input:checkbox:checked");
		if (checkboxes.size() > 0) {
			var answer = confirm("Удалить выбранные устройства?");
			if (answer) {
				checkboxes.each(function(i) {
					var id = $(this).attr("id");
					if (id != "all") {
						setTimeout(function() {
							a_delete($("tr#" + id + " a.delete"), false);
						}, i * 100);
					};
				});
				$("input#all:checkbox").removeAttr("checked");
			}
		} else {
			alert("Не выбрано ни одного устройства.")
		}
		
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

			$("input#all:checkbox").change(function() {
				if ($("input#all:checkbox").is(":checked")) {
					$("input:checkbox").each(function(i) {
						$(this).attr("checked", "yes");
					});
				} else {
					$("input:checkbox").each(function() {
						$(this).removeAttr("checked");
					});
				};
			});
			actionEditDelete();
		};
	});
};

function actionEditDelete() {
	$("a.edit").click(function () {
		var id = $(this).attr("id");
		var type = $("#dev_select option:selected").val();
		$.ajax({url: "/dev_info/edit/", 
			data: {"type": type, "dev_id": id}, 
			success: function(data) {
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
					
					$("a#cancel_edit").click(function() {
						$("form#edit_dev").hide(gAnimationSpeed).queue(function() {
							$(this).remove();
						});
//						getDevList();			
						return false;
					});

					$("#edit_dev").submit(function(e) {
						var answer = confirm("Сохранить изменения в устройстве " + $.tr_type(type) + " №" + id + "?");
						if (answer) {
							var form = $(e.target);
							$.post("/dev_info/edit/", 
								{"type": type, "dev_id": id, "form": form.serialize()},
								function(data) {
									if (data.success == "True") {
										$("form#edit_dev").hide(gAnimationSpeed).queue(function() {
											$(this).remove();
										});
										$.noticeAdd({text: data.notice});
										$("tr#" + id).replaceWith(data.row);
										$("tr#" + id).fadeOut(gAnimationSpeedSlow)
											.fadeIn(gAnimationSpeedSlow);
									} else {
										$("#edit_errors").html(data.errors).hide()
											.show(gAnimationSpeed);
									}
									actionEditDelete();
									
									return false;
							}, "json");
						} else {
							$("a#cancel_edit").click();
						}
						
						return false;
					});
				}
			},
			type: "GET",
			dataType: "json",
			
			singleton: true,
			delay: gRequestDelay
		});
		
		return false;
	});
	
	$("a.delete").click(function() {
		a_delete($(this));
//		getDevList();
		
		return false;
	});
}

function a_delete(obj, confm) {
	if (confm == undefined) {
		confm = true;
	}

	var id = obj.attr("id");
	var type = $("#dev_select option:selected").val();
	
	if (confm) {
		var answer = confirm("Удалить устройство " + $.tr_type(type) + " №" + id + "?");
	} else {
		var answer = true;
	}

	if (answer) {
		if ($("#display form#edit_dev").length > 0) {
			$("form#edit_dev").hide(gAnimationSpeed).queue(function() {
				obj.remove();
			});
		};
		$.post("/dev_info/delete/",
			{"type": type, "dev_id": id},
			function(data) {
				$.noticeAdd({text: data});
				$("tr#" + id).fadeOut(gAnimationSpeed);
				actionEditDelete();
			}
		);
	}
}
