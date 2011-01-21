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
			
			$("input.input#all").change(function(e) {
				if ($("input.input#all").is(":checked")) {
					$("input.input").each(function(i) {
						$(this).attr("checked", "yes");
					});
				} else {
					$("input.input").each(function(i) {
						$(this).removeAttr("checked");
					});
				};
			});
			
			$("a.input.edit").click(function () {
				var id = $(this).attr("id");
				$.getJSON("/dev_info/edit/", {"type": "input", "dev_id": id}, function(data) {
					if (data.success == "True") {
						$("#display").html(data.html);
						
						$("#edit_dev").submit(function(e) {
							var form = $(e.target);
							$.post("/dev_info/edit/", {"type": type, "dev_id": id, "form": form.serialize()},
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
		};
	});
};