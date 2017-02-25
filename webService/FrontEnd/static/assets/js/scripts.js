
/*
    Small slider 1
*/
function small_slider_1(slider_container) {
	var img_index = 1;
	$('.' + slider_container + ' img').each(function(){
		$(this).addClass('slider-1-img-' + img_index);
		$('.' + slider_container + ' .slider-1-nav').append('<span class="slider-1-nav-item-' + img_index + '"></span>');
		if($(this).hasClass('slider-1-img-active')) {
			$('.' + slider_container + ' .slider-1-nav-item-' + img_index).addClass('slider-1-nav-item-active');
		}
		img_index++;
	});
	// change slide
	$(document).on('click', '.' + slider_container + ' .slider-1-nav span', function(){
		if(!($(this).hasClass('slider-1-nav-item-active'))) {
			$('.' + slider_container + ' .slider-1-nav span').removeClass('slider-1-nav-item-active');
			var clicked_nav_index = $(this).attr('class').replace('slider-1-nav-item-', '');
			$(this).addClass('slider-1-nav-item-active');
			$('.' + slider_container + ' img.slider-1-img-active').fadeOut(300, function(){
				$(this).removeClass('slider-1-img-active');
				$('.' + slider_container + ' img.slider-1-img-' + clicked_nav_index).fadeIn(400, function(){
					$(this).addClass('slider-1-img-active');
				});
			});
		}
	});
}


/*
	Scroll to (navigation)
*/
function scroll_to(clicked_link, nav_height) {
	var element_class = clicked_link.attr('href').replace('#', '.');
	var scroll_to = 0;
	if(element_class != '.top-content') {
		element_class += '-container';
		scroll_to = $(element_class).offset().top - nav_height;
	}
	if($(window).scrollTop() != scroll_to) {
		$('html, body').stop().animate({scrollTop: scroll_to}, 1000);
	}
}


jQuery(document).ready(function() {
    
    /*
        Wow
    */
    new WOW().init();
    
    /*
	    Navigation
	*/
	$('a.scroll-link').on('click', function(e) {
		e.preventDefault();
		scroll_to($(this), $('nav').height());
	});
	// show/hide menu
	$('.show-menu a').on('click', function(e) {
		e.preventDefault();
		$(this).fadeOut(100, function(){ $('nav').slideDown(); });
	});
	$('.hide-menu a').on('click', function(e) {
		e.preventDefault();
		$('nav').slideUp(function(){ $('.show-menu a').fadeIn(); });
	});
    
    /*
        Fullscreen backgrounds
    */
    $('.top-content').backstretch("assets/img/backgrounds/1.jpg");
    $('.counters-container').backstretch("assets/img/backgrounds/2.jpg");
    $('.our-motto-container').backstretch("assets/img/backgrounds/2.jpg");
	
	/*
	    Testimonials
	*/
	$('.testimonial-active').html('<p>' + $('.testimonial-single:first p').html() + '</p>');
	$('.testimonial-single:first .testimonial-single-image img').css('opacity', '1');
	
	$('.testimonial-single-image img').on('click', function() {
		$('.testimonial-single-image img').css('opacity', '0.5');
		$(this).css('opacity', '1');
		var new_testimonial_text = $(this).parent('.testimonial-single-image').siblings('p').html();
		$('.testimonial-active p').fadeOut(300, function() {
			$(this).html(new_testimonial_text);
			$(this).fadeIn(400);
		});
	});
	
	/*
	    Small slider 1
	*/
	small_slider_1('slider-1-our-process');
	
	/*
	    Contact form
	*/
	$('.contact-form form input[type="text"], .contact-form form textarea').on('focus', function() {
		$('.contact-form form input[type="text"], .contact-form form textarea').removeClass('contact-error');
	});

	$('.contact-form form').submit(function(e) {
		e.preventDefault();
	    $('.contact-form form input[type="text"], .contact-form form textarea').removeClass('contact-error');
	    var postdata = $('.contact-form form').serialize();
	    $.ajax({
	        type: 'POST',
	        url: 'assets/contact.php',
	        data: postdata,
	        dataType: 'json',
	        success: function(json) {
	            if(json.emailMessage != '') {
	                $('.contact-form form .contact-email').addClass('contact-error animated shake').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function(){
            			$(this).removeClass('animated shake');
            		});
	            }
	            if(json.subjectMessage != '') {
	                $('.contact-form form .contact-subject').addClass('contact-error animated shake').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function(){
            			$(this).removeClass('animated shake');
            		});
	            }
	            if(json.messageMessage != '') {
	                $('.contact-form form textarea').addClass('contact-error animated shake').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function(){
            			$(this).removeClass('animated shake');
            		});
	            }
	            if(json.emailMessage == '' && json.subjectMessage == '' && json.messageMessage == '') {
	                $('.contact-form form').fadeOut('fast', function() {
	                    $('.contact-form').append('<p>Thanks for contacting us! We will get back to you very soon.</p>');
	                });
	            }
	        }
	    });
	});
    
});



jQuery(window).load(function() {
	
	/*
		Loader
	*/
	$(".loader-img").fadeOut();
	$(".loader").delay(1000).fadeOut("slow");
	
	/*
	    Portfolio
	*/
	$('.portfolio-masonry').masonry({
		columnWidth: '.portfolio-box', 
		itemSelector: '.portfolio-box',
		transitionDuration: '0.5s'
	});
	
	$('.portfolio-filters a').on('click', function(e){
		e.preventDefault();
		if(!$(this).hasClass('active')) {
	    	$('.portfolio-filters a').removeClass('active');
	    	var clicked_filter = $(this).attr('class').replace('filter-', '');
	    	$(this).addClass('active');
	    	if(clicked_filter != 'all') {
	    		$('.portfolio-box:not(.' + clicked_filter + ')').css('display', 'none');
	    		$('.portfolio-box:not(.' + clicked_filter + ')').removeClass('portfolio-box');
	    		$('.' + clicked_filter).addClass('portfolio-box');
	    		$('.' + clicked_filter).css('display', 'block');
	    		$('.portfolio-masonry').masonry();
	    	}
	    	else {
	    		$('.portfolio-masonry > div').addClass('portfolio-box');
	    		$('.portfolio-masonry > div').css('display', 'block');
	    		$('.portfolio-masonry').masonry();
	    	}
		}
	});
	
	$(window).on('resize', function(){ $('.portfolio-masonry').masonry(); });
	
	// image popup	
	$('.portfolio-box-text').magnificPopup({
		type: 'image',
		gallery: {
			enabled: true,
			navigateByImgClick: true,
			preload: [0,1] // Will preload 0 - before current, and 1 after the current image
		},
		image: {
			tError: 'The image could not be loaded.',
			titleSrc: function(item) {
				return item.el.find('p').text();
			}
		},
		callbacks: {
			elementParse: function(item) {
				item.src = item.el.parent('.portfolio-box-text-container').siblings('img').attr('src');
			}
		}
	});
	
});

/*

//1. CALULATE INVENTORY


function */
/* constant */
var Z_MAX = 6;
var P=0;
/* function */
var avr = function(maxSale, probableSale, minSale) {
  return (maxSale+4*probableSale+minSale)/6;
};

var sd = function(maxSale, minSale) {
  return (maxSale-minSale)/6;
};
var criticalRatio = function(sellCost, buyCost) {
  return (sellCost-buyCost)/sellCost;
};

/*getting z from 누적p (2) */
var getZ = function( criticalRatio ) {
 var Zs = [-2.326347874,-2.053748911,-1.880793608,-1.750686071,-1.644853627,-1.554773595,-1.475791028,-1.40507156,-1.340755034,-1.281551566,-1.22652812,-1.174986792,-1.126391129,-1.080319341,-1.036433389,-0.994457883,-0.954165253,-0.915365088,
-0.877896295,-0.841621234,-0.806421247,-0.772193214,-0.738846849,-0.706302563,-0.67448975,-0.643345405,-0.612812991,-0.582841507,-0.55338472,-0.524400513,-0.495850347,-0.467698799,-0.439913166,-0.412463129,-0.385320466,
-0.358458793,-0.331853346,-0.305480788,-0.279319034,-0.253347103,-0.227544977,-0.201893479,-0.176374165,-0.150969215,-0.125661347,-0.100433721,-0.075269862,-0.050153583,-0.025068908,0];
 var result = Zs.concat(
   Zs.filter(v=>v<0)
   .map(v=>-v)
   .reverse()
 ).map((v,k)=>({
   idx:k*0.01+0.01,
   value:v
 })).find(v=>criticalRatio<=v.idx)
 return result && result.value;
};

var optimal = function(o) {
  return avr(o.maxSale, o.probableSale, o.minSale)+
    getZ(criticalRatio(o.sellCost, o.buyCost))*
    sd(o.maxSale, o.minSale);
};
// var maxstandard = function(o){
//   return (o.maxSale-
//           avr(o.maxSale,o.probaleSale, o.minSale))/
//     sd(o.maxSale,o.minSale);
// }

// var minstandard = function(o){
//   return (o.minSale-
//           avr(o.maxSale,o.probaleSale, o.minSale))/
//     sd(o.maxSale,o.minSale);
// }
document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('OptimalInventory').addEventListener('submit', calc);
});

function calc(event) {
  event.preventDefault();

  /* input from html */
  var fSell=document.getElementById('SellCost').value*1;
  var fBuy=document.getElementById('BuyCost').value*1;
  var fMin=document.getElementById('MinSale').value*1;
  var fMax=document.getElementById('MaxSale').value*1;
  var fProb=document.getElementById('ProbableSale').value*1;
//   var fOptimal= optimal(
//       {
//         maxSale:fMax,
//         minSale:fMin,
//         probableSale:fProb,
//         sellCost:fSell,
//         buyCost:fBuy
//       }
//   );
//   var fAvr=avr(fMax,fProb,fMin);
//   var fSd=sd(fMax,fMin);
//   var nMin=(fMin-fAvr)/fSd;
//   var nMax=(fMax-fAvr)/fSd;
//   var nOptimal=(fOptimal-fAvr)/fSd;
  var msgdiv = document.getElementById('msg');

  if (fMin>fMax) {
    document.getElementById('Optimal_output').innerHTML="";
	msgdiv.innerHTML += "최소값이 최대값보다 큽니다.<br>";
    return;
  }
  if(fSell<fBuy){
    document.getElementById('Optimal_output').innerHTML="";
    msgdiv.innerHTML += "구입가격이 판매가격보다 큽니다. 당신은 손해를 보고 있습니다.<br>";
    return;
   }
  if(fProb<fMin || fProb>fMax){
    document.getElementById('Optimal_output').innerHTML="";
    msgdiv.innerHTML +="예상판매량은 최소값과 최대값 사이여야 합니다.<br>";
    return;
  }
  msgdiv.innerHTML="";
  document.getElementById('Optimal_output').innerHTML = Math.round(optimal(
      {
        maxSale:fMax,
        minSale:fMin,
        probableSale:fProb,
        sellCost:fSell,
        buyCost:fBuy
      }
  ));
  /* 여기에서 marker 들을 지우고 다시 그리는 걸 넣어보아요 */
  /* clear all markers */
  d3.selectAll('#markers>g').remove();
  /* 100번째 라인을 보고 필요한 내용으로 바꿔서 startTransitions를 실행해봐요 */
  startTransitions([{
    "amount":  (document.getElementById('MinSale').value*1-
             (document.getElementById('MinSale').value*1+document.getElementById('MaxSale').value*1+document.getElementById('ProbableSale').value*4)/6)/
              (document.getElementById('MaxSale').value*1-document.getElementById('MinSale').value*1)*6,
    "type": "min",
    "value": document.getElementById('MinSale').value*1
  },
  {
    "amount":getZ(criticalRatio(document.getElementById('SellCost').value*1,document.getElementById('BuyCost').value*1)),
    "type": "optimal",
    "value": ""
//     avr(document.getElementById('MaxSale').value*1,document.getElementById('ProbalbeSale').value*1,document.getElementById('MinSale').value*1)+getZ(criticalRatio(document.getElementById('SellCost').value*1,document.getElementById('BuyCost').value*1))*
//              sd(document.getElementById('MaxSale').value*1,document.getElementById('MinSale').value*1)
  },
  {
    "amount":  (document.getElementById('MaxSale').value*1-
             (document.getElementById('MinSale').value*1+document.getElementById('MaxSale').value*1+document.getElementById('ProbableSale').value*4)/6)/
              (document.getElementById('MaxSale').value*1-document.getElementById('MinSale').value*1)*6,
    "type": "max",
    "value": document.getElementById('MaxSale').value*1
  }]);
}

/*

*/
