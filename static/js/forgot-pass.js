$("#forgot-pass-button").click(function(){
	var email = $("#forgot-email").val();

	Parse.User.requestPasswordReset(email, {
  success: function() {
  	$("#message").html("An email has been sent to your email address with instructions on how to change your password.");

  	$("#message").css("color", "green");
  	$(".forgot-pass").css("text-align", "center");
  	$("#forgot-email").css("display", "none");
  	$("#forgot-pass-button").css("display", "none");
  },
  error: function(error) {
    // Show the error message somewhere
    $("#message").html("This email is not registered with us. Please try again!");
  	$("#message").css("color", "red");
  	$(".forgot-pass").css("text-align", "center");
  }
});
});