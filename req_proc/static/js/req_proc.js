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
					var form_upload_cert = $("div#req_proc_" + div_id + " form#upload_cert");
					if (form_upload_cert.length > 0) {
						form_upload_cert.remove();
					}
	
					var form_upload_img = $("div#req_proc_" + div_id + " form#upload_img");
					if (form_upload_img.length == 0) {
						$("div#req_proc_" + div_id).append(data.html);
						$("form#upload_img").hide().show(gAnimationSpeed);
					} else {
						$.clear_form_elements(form_upload_img);
					}

//					$("#upload_img").ajaxForm({
//						url: "/req_proc/upload_img/",
//						type: "POST",
////						dataType: "json",
//						beforeSubmit: function(formData, jqForm, options) {
//							var qString = $.param(formData);
//							alert('About to submit: \n\n' + qString);
//							return true;
//						},
//						success: function(data) {
//							alert(data);
////								if (data.success == "True") {
////									$("form#upload_img").hide(gAnimationSpeed).queue(function() {
////										$(this).remove();
////									});
////									$.noticeAdd({text: data.notice});
////								} else {
////									$("#errors").html(data.errors).hide().show(gAnimationSpeed);
////								}
//						},
//						error: function(xhr) {
//							alert('error' + xhr.error);
//						},
//						resetForm: true
//					});

					$("#upload_img").submit(function(e) {
//						var form = $(e.target);
//						alert($("#upload_img input").attr("value"));
//						alert(form.serialize());
						$(this).ajaxSubmit({
							url: "/req_proc/upload_img/",
							success: function(data) {
								alert(data);
//								if (data.success == "True") {
//									$("form#upload_img").hide(gAnimationSpeed).queue(function() {
//										$(this).remove();
//									});
//									$.noticeAdd({text: data.notice});
//								} else {
//									$("#errors").html(data.errors).hide().show(gAnimationSpeed);
//								}
							}, 
							dataType: "json"
						});

						return false;
					});
	
					$("a#cancel").click(function() {
						$("form#upload_img").hide(gAnimationSpeed).queue(function() {
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
