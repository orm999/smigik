$(document).ready(function() {
	$("div.req_proc").hide();
	$("div.req_proc#req_proc_2205").show();

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
					var form_upload_cert = $("div#req_proc_" + div_id + " form#upload_cert");
					if (form_upload_cert.length > 0) {
						form_upload_cert.remove();
					}
	
					var form_upload_img = $("div#req_proc_" + div_id + " form#upload_img");
					if (form_upload_img.length == 0) {
						$("div#req_proc_" + div_id).append(data.html);
						$("form#upload_img").hide().show(gAnimationSpeed);
//						$("form#upload_img fieldset").append("<input type=\"hidden\" name=\"X-Requested-With\" value=\"XMLHttpRequest\" />");
//						$("form#upload_img fieldset").append("<input type=\"hidden\" name=\"X_REQUESTED_WITH\" value=\"XMLHttpRequest\" />");
					} else {
						$.clear_form_elements(form_upload_img);
					}

					$("#upload_img").ajaxForm({
						url: "/req_proc/upload_img/",
						beforeSend: function(xhr) {
							alert(xhr.status);
							xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
							xhr.setRequestHeader("X_REQUESTED_WITH", "XMLHttpRequest");
						},
						success: function(data) {
							alert('success');
							alert(data);
							
							return false;
						},
						error: function(xhr) {
							alert('error');
							alert(xhr.error);
						},
						type: "POST"
					});
//					$("#upload_img").submit(function(e) {
//						$(this).ajaxSubmit({
//							data: {"X_REQUESTED_WITH": "XMLHttpRequest"},
//							url: "/req_proc/upload_img/",
//							success: function(data) {
//								alert('success');
//								alert(data);
//								
//								return false;
//							}, 
//							error: function(xhr) {
//								alert('error');
//								alert(xhr.error);
//							},
//							type: "POST"
//						});
//
//						return false;
//					});
	
					$("a#cancel").click(function() {
						$("form#upload_img").hide(gAnimationSpeed).queue(function() {
							$(this).remove();
						});
						return false;
					})
				}
				
				return false;
			},
			
			type: "GET",
			dataType: "json",
			
			singleton: true,
			delay: gRequestDelay,
		});

		return false;
	})
	
	$("a.upload_cert").click(function() {
		var div_id = $(this).attr("id").split("_")[2];
		$.ajax({url: "/req_proc/upload_cert/",
			success: function(data) {
				if (data.success == "True") {
					var form_upload_cert = $("div#req_proc_" + div_id + " form#upload_img");
					if (form_upload_cert.length > 0) {
						form_upload_cert.remove();
					}
	
					var form_upload_img = $("div#req_proc_" + div_id + " form#upload_cert");
					if (form_upload_img.length == 0) {
						$("div#req_proc_" + div_id).append(data.html);
						$("form#upload_cert").hide().show(gAnimationSpeed);
					} else {
						$.clear_form_elements(form_upload_img);
					}
					
					$("#upload_cert").submit(function(e) {
						var form = $(e.target);
						$.post("/req_proc/upload_cert/", {"form": form.serialize()},
							function(data) {
								if (data.success == "True") {
									$("form#upload_cert").hide(gAnimationSpeed).queue(function() {
										$(this).remove();
									});
									$.noticeAdd({text: data.notice});
								} else {
									$("#errors").html(data.errors).hide().show(gAnimationSpeed);
								}
						}, "json");
						
						return false;
					});
	
					$("a#cancel").click(function() {
						$("form#upload_cert").hide(gAnimationSpeed).queue(function() {
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
});
