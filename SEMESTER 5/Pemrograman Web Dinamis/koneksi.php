<?php
error_reporting(E_ALL ^ E_NOTICE ^ E_DEPRECATED);
$host = 'localhost';
$user = 'root';
$pass = '';
$db = 'kelasa_db';

$conn = mysqli_connect($host,$user,$pass,$db) or die();
?>