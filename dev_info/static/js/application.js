$(document).ready(function() {
	$("#dev_select").change(function() {
		if ($("#display form#add_dev").length > 0) {
			$("a#add").click();
		} else {
			getDevList();
		}
	});
	$("#dev_select").change();

	$("a#add").click(function() {
		var type = $("#dev_select option:selected").val();
		$.getJSON("/dev_info/add/", {"type": type}, function(data) {
			if (data.success == "True") {
				$("#display").html(data.html);

				$("#add_dev").submit(function(e) {
					var form = $(e.target);
					$.post("/dev_info/add/", {"type": type, "form": form.serialize()},
						function(data) {
							if (data.success == "True") {
								$("#display").html(data.html);
								
								$("a#dev_info").click(function() {
									getDevList();
									return false;
								});
							} else {
								$("#add_errors").html(data.html);
							}
					}, "json");
					
					return false;
				});

				$("a#cancel_add").click(function() {
					getDevList();					
					return false;
				});
			};
		});
		
		return false;
	});
	
	$("a#edit").click(function() {
		alert('hi');
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
			$("#display").html(data.html);
			
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
			
			$("a.edit").click(function () {
				var id = $(this).attr("id");
				var type = $("#dev_select option:selected").val();
				$.getJSON("/dev_info/edit/", 
					{"type": type, "dev_id": id}, 
					function(data) {
						if (data.success == "True") {
							$("#display").html(data.html);
	
							$("#edit_dev").submit(function(e) {
								var form = $(e.target);
								$.post("/dev_info/edit/", 
									{"type": type, "dev_id": id, "form": form.serialize()},
									function(data) {
										if (data.success == "True") {
											$("#display").html(data.html);
											
											$("a#dev_info").click(function() {
												getDevList();
												return false;
											});
										} else {
											$("#edit_errors").html(data.html);
										}
								}, "json");
								
								return false;
							});

							$("a#cancel_add").click(function() {
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
				$.post("/dev_info/delete/", 
					{"type": type, "dev_id": id},
					function(data) {
						$("#notice").html(data).hide().show("slow").delay(2000).hide("slow");
						$("tr#" + id).fadeOut(1000);
					}
				);
				
				return false;
			});
		};
	});
};