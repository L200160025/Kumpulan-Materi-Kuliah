<?php
session_start();
error_reporting(E_ALL ^ E_NOTICE);
echo $_SESSION['mhs'];
echo "<br>";
echo $_SESSION['status'];
?>