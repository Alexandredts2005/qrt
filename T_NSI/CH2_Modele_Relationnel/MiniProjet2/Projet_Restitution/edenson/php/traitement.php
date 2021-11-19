<!DOCTYPE html>
<html lang="fr">
	<head>
		<meta charset="utf-8">
		<title>Retour de formulaire</title>
		<link rel="stylesheet" href="../css/style.css">
	</head>
	
	<body>
		<?php
		$nom = $_POST['NOM'];
		$prenom = $_POST['PRENOM'];
		$genre = $_POST['GENRE'];
		$adresse = $_POST['ADRESSE'];
		$code_postal = $_POST['CODEPOSTAL'];
		$telephone = $_POST['TELEPHONE'];
		$email = $_POST['EMAIL'];
		$heure_arrivee = $_POST['HEUREARRIVEE'];
		$heure_depart = $_POST['HEUREDEPART'];
		$dort_sur_place = $_POST['DORTSURPLACE'];
		$alergie_1 = $_POST['ALLERGIE'];
		$alergie_2 = $_POST['ALLERGIE2'];
		$musique_fav = $_POST['MUSIQUEFAVORITE'];
		$aprt_jus = $_POST['JUS'];
		$aprt_soda = $_POST['SODA'];
		$aprt_gateau = $_POST['GATEAU'];
		$aprt_biscuit = $_POST['BISCUIT'];
		$aprt_cookie = $_POST['COOKIE'];
		$aprt_brioche = $_POST['BRIOCHE'];
		$aprt_confiserie = $_POST['CONFISERIE'];
		?>
		<div class="hblock">

			<h1>Bonjour <?php echo $prenom; ?></h1>

			<br>

			<p>
				Formulaire remplis le <?php echo date('d/m/Y'); ?> !
			</p>

			<br>

			<?php 
				$date = date('d/m/Y');
				$heure = date("h:i:s a");
				$intro = "\nFormulaire de ".$nom." entré le ".$date." à ".$heure." :";
				//file_put_contents('donnees.txt', $intro, FILE_APPEND);
			?>

			<div class="block">
				<h2>Voici votre formulaire :</h2>
				<p>
					Nom : 
					<?php 
						echo $nom; 
						//file_put_contents('donnees.txt', "\n Nom : ".$nom, FILE_APPEND);
						file_put_contents('donnees.txt', $nom.",", FILE_APPEND);
					?>
					<br><br>

					Prénom : 
					<?php 
						echo $prenom; 
						//if ($prenom != "") {file_put_contents('donnees.txt', "\n Prénom : ".$prenom, FILE_APPEND);}
						file_put_contents('donnees.txt', $prenom.",", FILE_APPEND);
							
					?>
					<br><br>

					Genre : 
					<?php 
						echo $genre; 
						//if ($genre != "") {file_put_contents('donnees.txt', "\n Genre : ".$genre, FILE_APPEND);}
						file_put_contents('donnees.txt', $genre.",", FILE_APPEND);
					?>
					<br><br>

					Adresse : 
					<?php 
						echo $adresse; 
						//if ($adresse != "") {file_put_contents('donnees.txt', "\n Adresse : ".$adresse, FILE_APPEND);}
						file_put_contents('donnees.txt', $adresse.",", FILE_APPEND);
					?>
					<br><br>
					
					Code postal : 
					<?php 
						echo $code_postal; 
						//if ($code_postal != "") {file_put_contents('donnees.txt', "\n Code postal : ".$code_postal, FILE_APPEND);}
						file_put_contents('donnees.txt', $code_postal.",", FILE_APPEND);
					?>
					<br><br>
					
					Téléphone : 
					<?php 
						echo $telephone; 
						//if ($telephone != "") {file_put_contents('donnees.txt', "\n Téléphone : ".$telephone, FILE_APPEND);}
						file_put_contents('donnees.txt', $telephone.",", FILE_APPEND);
					?>
					<br><br>
					
					Email : 
					<?php 
						echo $email; 
						//if ($email != "") {file_put_contents('donnees.txt', "\n Email : ".$email, FILE_APPEND);}
						file_put_contents('donnees.txt', $email.",", FILE_APPEND);
					?>
					<br><br>
					
					Heure d'arrivée : 
					<?php 
						echo $heure_arrivee; 
						//if ($heure_arrivée != "") {file_put_contents('donnees.txt', "\n Heure d'arrivée : ".$heure_arrivée, FILE_APPEND);}
						file_put_contents('donnees.txt', $heure_arrivee.",", FILE_APPEND);
					?>
					<br><br>
					
					Heure de depart : 
					<?php 
						echo $heure_depart; 
						//if ($heure_depart != "") {file_put_contents('donnees.txt', "\n Heure de depart : ".$heure_depart, FILE_APPEND);}
						file_put_contents('donnees.txt', $heure_depart.",", FILE_APPEND);
					?>
					<br><br>

					Dort sur place : 
					<?php 
						echo $dort_sur_place; 
						//if ($dort_sur_place != "") {file_put_contents('donnees.txt', "\n Dort sur place : ".$dort_sur_place, FILE_APPEND);}
						file_put_contents('donnees.txt', $dort_sur_place.",", FILE_APPEND);
					?>
					<br><br>
					
					Allergie : 
					<?php 
						echo $alergie_1; 
						file_put_contents('donnees.txt', $alergie_1.",", FILE_APPEND);
						//if ($alergie_2 != ""){ 
						//	echo(", ".$alergie_2); 44860
						//	if ($alergie_1 != "") {file_put_contents('donnees.txt', "\n Allergies : ".$alergie_1." et ".$alergie_2, FILE_APPEND);}
						//	else{file_put_contents('donnees.txt', "\n Allergie : ".$alergie_2, FILE_APPEND);}
						//}
						//else{ if ($alergie_1 != "") {file_put_contents('donnees.txt', "\n Allergie : ".$alergie_1, FILE_APPEND);} }
						
						file_put_contents('donnees.txt', $alergie_2.",", FILE_APPEND);
					?>
					<br><br>
					
					Musique Favorite : 
					<?php 
						echo $musique_fav; 
						//if ($musique_fav != "") {file_put_contents('donnees.txt', "\n Musique Favorite : ".$musique_fav, FILE_APPEND);}
						file_put_contents('donnees.txt', $musique_fav.",", FILE_APPEND);
					?>
					Plat ou boisson apportés : 44860
					<?php 
						$plat_et_boisson = "";

						if ($aprt_biscuit != ""){ $plat_et_boisson = "{$plat_et_boisson}Biscuit ";}
						if ($aprt_brioche != ""){ $plat_et_boisson = "{$plat_et_boisson}Brioche ";}
						if ($aprt_confiserie != ""){ $plat_et_boisson = "{$plat_et_boisson}Confiserie ";}
						if ($aprt_cookie != ""){ $plat_et_boisson = "{$plat_et_boisson}Cookie ";}
						if ($aprt_gateau != ""){ $plat_et_boisson = "{$plat_et_boisson}Gateau ";}
						if ($aprt_jus != ""){ $plat_et_boisson = "{$plat_et_boisson}Jus ";}
						if ($aprt_soda != ""){ $plat_et_boisson = "{$plat_et_boisson}Soda ";}
						
						echo $plat_et_boisson; 
						//if ($plat_et_boisson != "") {file_put_contents('donnees.txt', "\n Plat ou boisson apportés : ".$plat_et_boisson, FILE_APPEND);}
						file_put_contents('donnees.txt', $plat_et_boisson.",", FILE_APPEND);
					?>
					<br><br>
					
					Commentaire : 
					<?php 
						echo $commentaire; 
						//if ($commentaire != "") {file_put_contents('donnees.txt', "\n Commentaire : ".$commentaire, FILE_APPEND);}
						file_put_contents('donnees.txt', $commentaire."\n", FILE_APPEND);
					?>
					<br><br>

			</div>
		</div>
		<?php //file_put_contents('donnees.txt', "\n\n\n", FILE_APPEND); ?>
	</body>
</html>