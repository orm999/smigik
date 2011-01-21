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
	
	$("a#remove").click(function() {
//		alert('remove');
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
		};
	});
};