<h1 align='center'>Data Mahasiswa</h1>
<p align='center'><a href='insert.php'>Tambah Data</a></p>

<table border='1' align='center'>
	<tr>
		<th>No</th>
		<th>NIM</th>
		<th>Nama</th>
		<th>Alamat</th>
		<th>Foto</th>
		<th>Aksi</th>
	</tr>
<?php
include "koneksi.php";
$no = 1;
$sql ="select * from mahasiswa ";
$query = mysqli_query($conn,$sql);
while($data=mysqli_fetch_array($query)){
	echo "
	<tr>
		<td>$no</td>
		<td>$data[nim]</td>
		<td>$data[nama]</td>
		<td>$data[alamat]</td>
		<td><img src='$data[foto]' width='100' height='100'></td>
		<td>
		<a href='delete.php?del=$data[nim]'>Hapus</a> 
		| 
		<a href='update.php?upd=$data[nim]'>Ubah</a>
		</td>
	</tr>
	";
	$no++;
}
?>	
</table>