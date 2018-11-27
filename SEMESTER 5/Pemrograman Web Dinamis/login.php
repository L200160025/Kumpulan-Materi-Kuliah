<?php
error_reporting(E_ALL ^ E_NOTICE ^ E_DEPRECATED);
session_start();
$status = $_SESSION['status'];
if($status=="Admin"){
	?>
	<script>document.location='admin.php';</script>
	<?php
}else if($status=="Pengunjung"){
	?>
	<script>document.location='pengunjung.php';</script>
	<?php
}
?>
<form method='post' name='login' action='ceklogin.php'>
<p>Username : <input type='text' name='username'></p>
<p>Password : <input type='password' name='password'></p>
<p><input type='submit' name='submit' value="LOGIN"></p>
</form>