function adicionarClasseParaParagrafos() {
    var paragrafos = document.querySelectorAll('p');
    let img = document.querySelectorAll('img');
    
    for (var i = 0; i < paragrafos.length; i++) {
        if ('text-white' != paragrafos[i].classList){
          paragrafos[i].classList.add('text-secondary');
        }
    }      
      
}

function adicionarClassesParaSpans(){
  var spans = document.querySelectorAll('span');

  for (var i = 0; i < spans.length; i++) {
    if ('text-white' != spans[i].classList){
      spans[i].classList.add('text-secondary');
    }
  }
}

function adicionarClassesParaH(){
  var h1 = document.querySelectorAll('h1');
  var h2 = document.querySelectorAll('h2');
  var h3 = document.querySelectorAll('h3');
  // var h4 = document.querySelectorAll('h4');
  var h5 = document.querySelectorAll('h5');

  for (var i = 0; i < h1.length; i++) {
    if ('text-white' != h1[i].classList){
      h1[i].classList.add('text-secondary');
    }
  }

  for (var i = 0; i < h2.length; i++) {
    if ('text-white' != h2[i].classList){
      h2[i].classList.add('text-secondary');
    }
  }

  for (var i = 0; i < h3.length; i++) {
    if ('text-white' != h3[i].classList){
      h3[i].classList.add('text-secondary');
    }
  }

  // for (var i = 0; i < h4.length; i++) {
  //   if ('text-white' != h4[i].classList){
  //     h4[i].classList.add('text-secondary');
  //   }
  // }

  // for (var i = 0; i < h5.length; i++) {
  //   if ('text-white' != h5[i].classList){
  //     h5[i].classList.add('text-secondary');
  //   }
  // }
}

window.onload = function() {
    adicionarClasseParaParagrafos();
    adicionarClassesParaSpans();
    adicionarClassesParaH();
};