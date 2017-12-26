function startSensor(){
}

function stopSensor(){
}

function getLog(){
	$.ajax({
        type: "POST",
        url: "client.php",
        data: "getLog",
        success: function (data) {
			console.log(data);
			$("#log-table").empty();
			$("#log-table").append(
			"<thead>\
			  <tr>\
				<th>#</th>\
				<th>Range</th>\
				<th>Time</th>\
				<th>LED</th>\
			  </tr>\
			 </thead>");
			$("#log-table").append(
			"<tbody>");
			var obj = JSON.parse(data);
			for(var i = 0; i < obj.length;i++){
				var x = i+1;
				$("tbody").append("<tr id=" + x + ">");
				for (var prop in obj[i]) {
					if (obj[i].hasOwnProperty(prop)) {
						var id = "#"+x;
						$(id).append("<td>"+obj[i][prop]+"</td>");							
					}
				}
				
				$("tbody").append("</tr>");
			}
			$("#log-table").append(
			"</tbody>");
        }
    });
}
