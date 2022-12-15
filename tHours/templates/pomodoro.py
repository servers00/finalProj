{% extends 'base.html' %}

{% block body %}
<!DOCTYPE html>
<html>
  <head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>
        <script>
          var started = false;
var work = 25;
var sBreak = 5;
var lBreak = 10;
let isPaused = true;
let second = 0;
let min = 0;
let myTimer;
let dispSeconds = 0;
let duration = 0;
let timeDisp = 0;
function timer(dur) {
  duration = dur;
}
myTimer = setInterval(function() {
  console.log("run1");

  if (!isPaused && duration != 0) {
    console.log("run");
    bar();
    second += 1;
    dispSeconds += 1;
    console.log(second);
    document.getElementById("timerDur").innerHTML = min + ":" + dispSeconds;
    if (second % 60 == 0) {
      min += 1;
      console.log(min);
      dispSeconds = 0;
      document.getElementById("timerDur").innerHTML = min + ":" + dispSeconds;
    }

    if (min == duration) {
      min = 0;
      second = 0;
      isPaused = true;
      $(document).ready(function(){
        $("#pausestart").html("start");
      });
      //clearInterval(myTimer);
    }

  }
}, 100);

$(document).ready(function() {

  $('#pausestart').on('click', function(e) {
    e.preventDefault();
    if (isPaused == false) {
      isPaused = true;
      $("#pausestart").html("start");
      console.log("clicking");
    }
    else if (isPaused == true) {
      isPaused = false;
      $("#pausestart").html("pause");
      console.log("clicking0");
    }

    //display amount of time
    $("#timerDur").html(duration);
  });

  //$('#start').on('click', function(e){
  //e.preventDefault();
  //isPaused = false;
  //console.log("blah", isPaused);
  //});
});

function bar() {
  $(document).ready(function() {
    width = Math.round((second / (duration * 60)) * 100)
    $(".progressBar").css('width', width*3);
    console.log(width);
  });
}

          
        </script>
         <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">


</head>
<body style="background: #ffc971;">


<div class="text-center container shadow p-3 mb-5 bg-white rounded">
<h1>Pomodoro Timer</h1>
<div class="row">
  <p id="timerDur">0:00</p>
</div>
<div class="row">
  <div class="col">
  <button type="button" class="btn btn-primary start" onclick="timer(25)">start 25</button>
  <button type="button" class="btn btn-primary start" onclick="timer(5)">start 5</button>
  <button type="button" class="btn btn-primary start" onclick="timer(10)">start 10</button>
  <button type="button" class="btn btn-primary start" id="pausestart">start</button>
  </div>
</div>
<div class="row">
  <div class="col align-self-center">
<div style="width: 0%; background-color: white; justify-content: center; margin-left: 38%;" class="progressBar"><p class="text-warning">time</p></div>
  </div>
</div>
</div>
</body>
</html>
{% endblock %}