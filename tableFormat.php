#!/usr/bin/php

<?php

//Otvori datoteku i kreiraj niz linija.
$filename = $argv[1];//"data.txt"; //$argv[1] drugi unos s komandne linije - treba da bude putanja do datoteke

//Razdvoji linije.
$arrayStringova = explode("\n", file_get_contents($filename));

//Kreiraj niz nizova koji ce sadrzavati elemente iz datoteke...
$array = array();
foreach ($arrayStringova as $linija) {
		$array[] = str_split($linija, 2);
}
//print_r($array);

//Ovo ce nam dati najvecu liniju u fajlu - sirina matrice
$najduzaLinija = 0;
foreach ($array as $linija){
	if (count($linija) > $najduzaLinija){
		$najduzaLinija = count($linija);
	}
}

//Broj linija 
$brojLinija = count($array)-1; //Ovo radim jer explode doda u niz nizova na kraj jos jedan niz koji ne sadrzi nista 

//Kreiramo matrix koji ce sadrzavati finalni ispis i popunimo ga praznim mjestima
$matrix = array();
for ($i=0; $i < 2*$brojLinija+1; $i++){
	for ($j=0; $j < $najduzaLinija*4+1; $j++){
		$matrix[$i][$j]=" ";
	}
}

for ($i=0;$i<$brojLinija;$i++){
	for ($j=0;$j<count($array[$i]);$j++){
		
		if (substr($array[$i][$j],0,1) != " "){
			//var_dump($array[$i][$j]);
			//echo "karakter je: ".$array[$i][$j]."\n";
			$matrix[2*$i][4*($j)]='+';
			$matrix[2*$i][4*($j)+1]='-';
			$matrix[2*$i][4*($j)+2]='-';
			$matrix[2*$i][4*($j)+3]='-';
			$matrix[2*$i][4*($j)+4]='+';
			$matrix[2*$i+1][4*($j)]='|';
			$matrix[2*$i+1][4*($j)+2]=substr($array[$i][$j],0,1);
			$matrix[2*$i+1][4*($j)+4]='|';
			$matrix[2*$i+2][4*($j)]='+';
			$matrix[2*$i+2][4*($j)+1]='-';
			$matrix[2*$i+2][4*($j)+2]='-';
			$matrix[2*$i+2][4*($j)+3]='-';
			$matrix[2*$i+2][4*($j)+4]='+';
		}
	}
}

for ($i=0; $i < 2*$brojLinija+1; $i++){
	for ($j=0; $j < $najduzaLinija*4+1; $j++){
		echo $matrix[$i][$j];
	}
	echo("\n");
}

//print_r($matrix);
?>
