<?php 
  set_time_limit(0);
  //ini_set('display_errors',1); 
  //error_reporting(E_ALL);
  error_reporting(0);
  $address = $_POST['address'];
  shell_exec("python get_price.py $address");
  shell_exec("python create_chart.py");
  $file = file_get_contents('price_slopes.txt');
  echo $file;
?>
