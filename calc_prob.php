<?php 
  set_time_limit(0);
  //ini_set('display_errors',1); 
  //error_reporting(E_ALL);
  error_reporting(0);
  
  if (!$crimes = file('crimes.txt', FILE_IGNORE_NEW_LINES)) 
    $crimes = [];  

  if (!$price =file('price_slopes.txt', FILE_IGNORE_NEW_LINES)) 
    $price = [0.0];
 
  if (!$plywood = file('plywood.txt', FILE_IGNORE_NEW_LINES)) 
    $plywood = [0.0];

  for($i = 0; $i < count($plywood); $i++)
	  $plywood[$i] = (int)substr($plywood[$i],9,2);
  rsort($plywood);
  if(count($plywood) >= 3)
    $pp = (($plywood[0] + $plywood[1] + $plywood[2])/3.0)*0.6; 
  if(count($plywood) == 2)
    $pp = (($plywood[0] + $plywood[1])/2.0)*0.4; 
  if(count($plywood) == 1)
    $pp = $plywood[0]*0.2; 
  if(count($plywood) < 1)
    $pp = 0.0; 

  $cp = count($crimes)/14.0;
  if($cp > 10.0)
	  $cp = 10.0;

  $sp = round((float)substr($price[2],0,-23)*0.3,1);
  $sp = round($sp,1);
  $pp = round($pp,1);
  $cp = round($cp,1);
  
  $fp = $pp + $cp + $sp; 
  
  $fp = round($fp,1);
  $arr = [$pp,$sp,$cp,$fp];
  echo json_encode($arr);
?>
