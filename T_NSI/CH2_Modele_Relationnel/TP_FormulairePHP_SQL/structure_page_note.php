<?php 
 $id = $_GET['id'];   // Récupération de l'id
?>

<!--la page html formulaire-->  
<!DOCTYPE html>
 <html lang="fr">
     <head>
         <meta charset="utf-8">
         <title>Notation</title>
         <link rel="stylesheet" href="css/style.css">
      </head>
      <body > 
         <form id="formNote" method="post" action="">
             <div class="formulaire">
                 <h1> Notez votre film  !</h1>
                 <div> <h2>"film N°1"</h2>
                     <div>
                        
                     </div>
                 </div>
 
                 <div> <h2>"film N°2"</h2>
                     <div>
                        <label class="label"> 1 </label> 
                         <input type="radio" name="note2" valeur="1">
                         <input type="radio" name="note2" valeur="2">
                         <input type="radio" name="note2" valeur="3">
                         <input type="radio" name="note2" valeur="4">
                         <input type="radio" name="note2" valeur="5">
                         <label class="label"> 5 </label> 
                     </div>
                 </div>
 
                 <div class="bouton">
                     <input type="submit" value="Envoyer" />
                 </div>
             </div>
             
         </form>
         
     </body>
 </html>
