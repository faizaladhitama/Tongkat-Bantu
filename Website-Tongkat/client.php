<?php
foreach($_POST as $key => $value){
	echo $key;
}
$str = file_get_contents('../data.json');
echo $str;
$json = json_decode($str,true);
$counter = 0;
$length = count($json)-1;
$limit = $length - 2;
/*
foreach ($json as $key => $value) {
	if($counter > $limit){
		echo $key;
	}
	$counter+=1;
}
*/
?>
