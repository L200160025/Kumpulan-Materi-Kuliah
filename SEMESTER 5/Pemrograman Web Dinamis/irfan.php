<?php
error_reporting(E_ALL ^ E_NOTICE ^ E_DEPRECATED);
echo " <p align='center'>Tes</p>";
$nim = "L200140" ;
echo " $nim <br>";

$a = 10;
$b = "10 10angka20";
$hasil = $a + $b;
$hasil2 = $a.$b;

echo "$hasil2<br>";

$c=20;
$total = $a + $c;

if($total >= 10){
	echo "$total lebih dari 10";
}else{
	echo "$total Kurang dari 10";
}

$i = 1;
while ($i <= $total){
	echo "$i ";
	$i=$i+1;
}

for ($i=1;$i<=$total;$i++){
	echo "$i ";
}
?>