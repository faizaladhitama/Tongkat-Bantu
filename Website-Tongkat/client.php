<?php
$host    = "169.254.146.6";
$port    = 12345;
$message = "Hello Server";
// create socket
$socket = socket_create(AF_INET, SOCK_STREAM, 0);
if ($socket === false) {
    // Using die() here because we really don't want to continue on while in an error condition.
    die('socket_create() failed: reason: ' . socket_strerror(socket_last_error($socket)));
}

// connect to server
if (socket_connect($socket, $host, $port) === false) { 
     die('socket_connect() failed: reason: ' . socket_strerror(socket_last_error($socket)));
}

socket_write($socket, $message);
$read = socket_read($socket,$port);
socket_close($socket);
echo $read;
/**
$host= gethostname();
$ip = gethostbyname($host);
echo $ip;
*/
?>
