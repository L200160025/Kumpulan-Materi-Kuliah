<?php
include "koneksi.php";

$insert = "insert into mahasiswa(nim,nama,alamat) 
values('L200','Fafah','Ujung Kulon')";
mysqli_query($conn,$insert);

$update = "update mahasiswa
set nim='L300',nama='Fafah Hanifah',
alamat = 'Ujung Kulon Jawa Barat'
where nim='L200' ";
mysqli_query($conn,$update);
?>