<?php
foreach($_POST as $key => $value){
	if($key == "getJSON"){
		getJSON();
	}
	else if($key == "stop"){
		stopSensor();
	}
	else if($key == "start"){
		startSensor();
	}
}

function startSensor(){
	shell_exec(". ./sensor.py");
}

function stopSensor(){
	echo shell_exec("whoami");
	$proses1 = shell_exec("ps -ef | grep dummy.py | head -n 1 | awk '{print $2}'");
	$proses2 = (int)$proses1 + 1;
	$killCommand = "./kill.sh $proses1";
	echo $killCommand;
	$kill = exec($killCommand);
	echo $kill;
}

function getJson(){
	$str = file_get_contents('../data.json');
	$str2 = file_get_contents('../data2.json');
	$json = json_decode($str,true);
	$json2 = json_decode($str2,true);
	$merge = array_merge($json,$json2);
	$jsonMerge = json_encode($merge,true);
	echo $jsonMerge;
}
?>
