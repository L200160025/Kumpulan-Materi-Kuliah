<?php
error_reporting(E_ALL ^ E_NOTICE ^ E_DEPRECATED);
include "koneksi.php";
$upd = $_GET['upd'];
$sql = "select * from mahasiswa where nim='$upd' ";
$query=mysqli_query($conn,$sql);
$hasil=mysqli_fetch_array($query);
?>
<center>
<form action='<?php $_SERVER['PHP_SELF'];?>' method='post' name='update'>
	<p>NIM : <input type='text' name='nim' value='<?php echo $hasil[nim]; ?>' ></p>
	<p>Nama : <input type='text' name='nm' value='<?php echo $hasil[nama]; ?>' ></p>
	<p>Alamat : <textarea name='alamat'><?php echo $hasil[alamat]; ?></textarea></p>
	<p>Upload Foto : <input type='file' name='foto'> </p>
	<p><input type='submit' name='input' value='Ubah Data'></p>
</form>
</center>
<?php
$nim	= $_POST['nim'];
$nm		= $_POST['nm'];
$alamat	= $_POST['alamat'];
$input	= $_POST['input'];
if($input){
	$sql = "update mahasiswa set nim='$nim', nama='$nm', alamat='$alamat' where nim='$upd' ";
	$query=mysqli_query($conn,$sql);
	if($query){
		?>
		<script>alert("Data Berhasil Diubah");
		document.location='view.php'</script>
		<?php
	}
}
?>