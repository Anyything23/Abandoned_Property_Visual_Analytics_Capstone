<?php 
  set_time_limit(0);
  //ini_set('display_errors',1); 
  //error_reporting(E_ALL);
  error_reporting(0);
  $address = $_POST['address'];
  shell_exec("python get_image.py $address");
  shell_exec("python object_detection.py");
  $file = file_get_contents('plywood.txt');
  echo $file;
?>
