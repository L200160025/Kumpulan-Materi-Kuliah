<?php
session_start();
$status = $_SESSION['status'];
if($status!="Admin"){
	?>
	<script>alert("Anda Tidak Berhak Mengakses Halaman ini!"); document.location='login.php';</script>
	<?php
}

?>
Anda Admin
<br>
<a href='logout.php'>Log Out</a>