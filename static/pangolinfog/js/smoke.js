$(function(){

 var ua = window.navigator.userAgent;
    var msie = ua.indexOf("MSIE ");

  if(!msie){
    var a=0;for(;a<15;a+=1){setTimeout(function b(){var a=Math.random()*2e3+4e3,c=$("<div />",{"class":"smoke", css:{opacity:0,left:Math.random()*100-35}});$(c).appendTo("#Carousel-intro");$.when($(c).animate({opacity: 1},{duration:a/4,easing:"linear",queue:false,complete:function(){$(c).animate({opacity:0},{duration:a/3,easing:"linear",queue:false})}}),$(c).animate({bottom:$("#Carousel-intro").height()},{duration:a,easing:"linear",queue:false})).then(function(){$(c).remove();b()})},Math.random()*3e3)}
  }else{    
  "use strict";var a=0;for(;a<15;a+=1){setTimeout(function b(){var a=Math.random()*2e3+4e3,c=$("<div />",{"class":"smoke",css:{left:Math.random()*100-35}});$(c).appendTo("#Carousel-intro");$.when($(c).animate({},{duration:a/4,easing:"linear",queue:false,complete:function(){$(c).animate({},{duration:a/3,easing:"linear",queue:false})}}),$(c).animate({bottom:$("#Carousel-intro").height()},{duration:a,easing:"linear",queue:false})).then(function(){$(c).remove();b()})},Math.random()*3e3)}}}())