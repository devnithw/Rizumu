music_name = "music.mp3"
let play_btn = document.querySelector("#play");
let prev_btn = document.querySelector("#pre");
let next_btn = document.querySelector("#next");
let isPlaying = false;
let song = new Audio();
window.onload = playSong;

function playSong(){
    song.src = music_name;
    console.log(song)
    
    
    play_btn.addEventListener('click',function(){
        if(!isPlaying){
            song.play();
            isPlaying = true;
            document.getElementById("playpause").className = "fas fa-pause fa-lg";
        }
        else{
            song.pause();
            isPlaying = false;
            document.getElementById("playpause").className = "fas fa-play fa-lg";
        }
        song.addEventListener('ended',function(){
            song.pause();
            isPlaying = false;
            document.getElementById("playpause").className = "fas fa-play fa-lg";
        })
        
    
    })
}