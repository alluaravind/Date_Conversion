$(document).ready(function(){
	$('form').on('submit',function(event){
		$.ajax({
			data:{
				date:$('#date').val()
			},
			type : 'POST',
			url: '/getday1/'
		})
		.done(function (data) {
			if(data.error){
				$('#error').text(data.error).show();
				$('#successAlert').hide();
			}
			else{
				$('#successAlert').text(data.name1).show();
				$('#error').hide();

			}
		});

		event.preventDefault();
	});
});