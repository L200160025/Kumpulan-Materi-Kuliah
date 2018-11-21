<form action='mulyono.php' method='get' name='penjumlahan'>
Angka 1 : <input type='text' name='a1'><br>
Angka 2 : <input type='text' name='a2'><br>
<input type='submit' name='jumlah' value='Tambah'>
</form>

Tulis NIM, Nama, Kelas.
Dari Form di atas, buatlah php untuk melakukan operasi penjumlahan dua buah bilangan.
Sampai jam 07.45





<?php
error_reporting(E_ALL ^ E_NOTICE);
$a1 = $_GET['a1'];
$a2 = $_GET['a2'];
$jumlah = $_GET['jumlah'];

$total = $a1 + $a2;

if($jumlah){
	echo "Hasil Penjumlahan $a1 dan $a2 adalah $total ";
}


?>