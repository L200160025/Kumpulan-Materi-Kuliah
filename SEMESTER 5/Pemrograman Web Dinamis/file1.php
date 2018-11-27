<?php
session_start();
$mhs = "Dina";
echo $mhs;
$_SESSION['mhs']=$mhs;
$_SESSION['status']="Admin";
?>