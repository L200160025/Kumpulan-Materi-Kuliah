<?php
include "koneksi.php";
session_start();
$username = $_POST['username'];
$password = $_POST['password'];
$submit = $_POST['submit'];
if($submit){
	$sql = "select * from user where username='$username' and password='$password' ";
	$query=mysqli_query($conn,$sql);
	$hasil = mysqli_fetch_array($query);
	if($hasil['status']=="Admin"){
		$_SESSION['username']= $hasil[username];
		$_SESSION['nama']= $hasil[nama];
		$_SESSION['status']= $hasil[status];
		?>
		<script>alert("Selamat Datang Admin");document.location='admin.php';</script>
		<?php
	}else if($hasil[status]=="Pengunjung"){
		$_SESSION['username']= $hasil[username];
		$_SESSION['nama']= $hasil[nama];
		$_SESSION['status']= $hasil[status];
		?>
		<script>alert("Selamat Datang Pengunjung");document.location='pengunjung.php';</script>
		<?php
	}else{
		?>
		<script>alert("Username dan Password Salah Coy!");document.location='login.php';</script>
		<?php
	}
}
?>