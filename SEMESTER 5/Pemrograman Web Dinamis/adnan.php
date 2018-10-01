<html>
	<head>
		<title>Adnan Ganteng!</title>
	</head>
	<body>
	<form name='formulir' method='get' action='index.php' >
	Username : 
	<input type='text' name='user' value='adnan' size='15' maxlength='6'  >
	<input type='hidden' name='id' value='S11'>
	<hr>
	Nama : <input type='text' name='nama' placeholder='Masukkan Nama...'>
	<hr>
	Password :
	<input type='password' name='pass' placeholder='Masukkan Password...'>
	<hr>
	Upload Foto :  
	<input type='file' name='foto' >
	<hr>
	Jenis Kelamin :
	<input type='radio' name='jk' value='Laki'> Laki-Laki
	<input type='radio' name='jk' value='Wanita' checked>Perempuan
	<hr>
	Hobby :
	<input type='checkbox' name='hb' value='Intip Orang'> Membaca Buku
	<input type='checkbox' name='hb2' value='Renang' checked> Berenang
	<hr>
	Motivasi :
	<textarea name='motivasi' cols='25' rows='10'>Ini Isi Defaultnya</textarea>
	<hr>
	Fakultas :
	<select name='fakultas'>
		<option hidden>--Pilih Fakultas--</option>
		<option value='F KI'>FKI</option>
		<option value='F Kedok'>Kedokteran</option>
		<option value='F Hukum'>Hukum</option>
	</select>
	<hr>
	<input type='submit' name='register' value='Daftar'>
	<input type='reset' name='reset' value='Reset'>
	</form>
	
	<h1>Heading 1</h1>
	<h2>Heading 2</h2>
	<h3>Heading 3</h3>
	<h4>Heading 4</h4>
	<h5>Heading 5</h5>
	<h6>Heading 6</h6>
	<h7>Heading 7</h7>
	Tulisan Standar
	<font size='18' face='Arial' color='red' >Adnan</font>
	<b>Adnan Bold</b>
	<strong>Adnan Strong</strong>
	<i>Adnan Miring</i>
	<em>Adnan &nbsp;&nbsp;&nbsp;  Em</em>
	
	H<sub>2</sub>SO<sub>4</sub>
	Cm<sup>3</sup>
	25 <sup>1/2</sup>
	
	<ol type='1'>
		<li>Aul</li>
		<li>Adnan
			<ol type='a'>
				<li>Kelas A</li>
				<li>Kelas C</li>
			</ol>
		</li>
		<li>Dina</li>
	</ol>

	<hr>
	</body>
</html>