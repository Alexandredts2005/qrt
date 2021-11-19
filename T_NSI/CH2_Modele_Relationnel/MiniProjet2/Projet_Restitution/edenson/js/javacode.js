let i = 0;

function EntreeSouris (event) {
	let texte = document.querySelector(".couleur");
	if (i==0) {
		texte.style.color="red";
	}
	if (i==1) {
		texte.style.color="blue";
	}
	if (i==2) {
		texte.style.color="green";
	}
	if (i==3) {
		texte.style.color="yellow";
	}
	if (i==4) {
		texte.style.color="purple";
	}
	if (i==5) {
		texte.style.color="cyan";
	}
	if (i==6) {
		texte.style.color="black";
	}
}

function SortieSouris(event){
	i = i + 1
	if (i>6) {
		i = 0
	}
}

let texte = document.querySelector(".couleur");
texte.addEventListener('mouseenter',EntreeSouris);
texte.addEventListener('mouseleave',SortieSouris);



function EntreeSouris2(event) {
	var elt = this;
	console.log("1");
	elt.style.backgroundColor='#ffb31a';
	elt.style.borderColor='#ffaa00';
}

function SortieSouris2(event){
	var elt = this;
	console.log("2");
	elt.style.backgroundColor='#ffd633';
	elt.style.borderColor='#ffcc00';
}

var arr = document.querySelectorAll(".changecoulevent");

for (var k=0; k<arr.length; k++) {
	arr[k].addEventListener('mouseenter',EntreeSouris2);
	arr[k].addEventListener('mouseleave',SortieSouris2);
}






