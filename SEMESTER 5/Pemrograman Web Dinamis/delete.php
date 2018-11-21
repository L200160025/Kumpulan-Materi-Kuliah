<?php
include "koneksi.php";
$del = $_GET['del'];
$sql = "delete from mahasiswa where nim='$del' ";
$query = mysqli_query($conn,$sql);
if($query){
	?>
	<script>alert("Data Berhasil Dihapus");
	document.location='view.php'</script>
	<?php
}
?>