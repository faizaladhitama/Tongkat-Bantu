<?php
	require 'header.php';
?>

<div class="container-fluid text-center">    
  <div class="row content">
    <div class="col-sm-12 text-left"> 
      <h1>Welcome</h1>
      <p>Website ini dipergunakan untuk memberikan log data kepada user, mengaktifkan sensor, dan mematikan sensor</p>
      <hr>
      <button onclick="getLog()">Receive log data</button>
      <button onclick="startSensor()">Start sensor</button>
      <button onclick="stopSensor()">Stop sensor</button>
      <div class="table-responsive">
		<table id="log-table" class="table">
		</table>
      </div>
    </div>
  </div>
</div>

<?php
	require 'footer.php';
?>
