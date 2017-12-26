function sendToServer(){
	message="hello world";
	$.ajax({
        type: "POST",
        url: "client.php",
        success: function (data) {
        	//console.log(data);
        	console.log(data);
        	var obj = JSON.parse(data);
        	console.log(obj);
        }
    });
}