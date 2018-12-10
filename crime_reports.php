<?php 
  set_time_limit(0);
  //ini_set('display_errors',1); 
  //error_reporting(E_ALL);
  error_reporting(0);
  $address = $_POST['address'];
  shell_exec("python get_crimes.py $address");
  $file = fopen('crimes.txt','r');
  $hi = array();
  $higher = array();
   $i =0;
  while(! feof($file))
  {
  	  $i++;
	  $str = fgets($file);
	  array_push($hi,$str);

	  if($i == 7)
	  {
	  	  array_push($higher,$hi);
		  $i =0;
		  $hi =array();
	  }
  } 
  echo json_encode($higher);
?>
