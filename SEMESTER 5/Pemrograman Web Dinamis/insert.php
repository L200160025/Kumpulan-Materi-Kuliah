<center>
<form action='insert.php' method='post' name='insert'  enctype="multipart/form-data" >
	<p>NIM : <input type='text' name='nim'></p>
	<p>Nama : <input type='text' name='nm'></p>
	<p>Alamat : <textarea name='alamat'></textarea></p>
	<p>Upload Foto : <input type='file' name='foto'> </p>
	<p><input type='submit' name='input' value='Input Data'></p>
</form>
</center>
<?php
error_reporting(E_ALL ^ E_NOTICE ^ E_DEPRECATED);
$nim    = $_POST['nim'];
$nm     = $_POST['nm'];
$alamat = $_POST['alamat'];
$folder	= "img/";
$nama_foto = $_FILES['foto']['name'];
$foto 	= $folder.$nama_foto;
$input  = $_POST['input'];

if($input){
	include "koneksi.php";
	$sql = "insert into mahasiswa(nim,nama,alamat,foto)
	values('$nim','$nm','$alamat','$foto')";
	$run = mysqli_query($conn,$sql);
	move_uploaded_file($_FILES["foto"]["tmp_name"],$foto);
	if($run){
		?>
	<script>alert("Data Berhasil Dimasukkan");
	document.location='view.php'
	</script>
		<?php
	}
}
?>