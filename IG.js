

var totlikes= 0;

function doSomething(random) {
    var firstLike = document.querySelector('section.ltpMr.Slqrh > span.fr66n > button > div > span > svg[aria-label="Like"]');
    if(firstLike){
      firstLike.scrollIntoView({behavior: "smooth", block: "center", inline: "nearest"});
      var closestElement = firstLike.closest('button');
        console.log('clicked...\n');
        closestElement.click();
    }
    console.log('waiting for '+random+' miliseconds\n');
}

(function loop() {
    var min = 9000; // min 9 seconds
    var max = 12000; // max 12 seconds
    var random = Math.floor(Math.random() * (+max - +min)) + +min;
    var h = new Date().getHours();
    var m = new Date().getMinutes();
    console.log('current time: '+h+ ":" +m+ '\n');
    var start = 15; // start liking after this hour
    var end = 16; // stop liking after this hour
    if (h >= start && h < end) { // Between
      setTimeout(function() {doSomething(random);loop(); totlikes++ }, random);
    }
    else {
      // Off
      if (h< start) {
         var diff = start - h;
      } else if (h >= end) {
        var diff = h + start;
      }
      console.log('waiting for '+Math.abs(diff)+' hours until '+start+'\n');
      console.log("total likes:"+ totlikes)
      setTimeout(function() {
        loop();
      }, Math.abs(diff)*3600000);
    }
}());
