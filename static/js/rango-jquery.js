 $(document).ready( function() {

    $("#about-btn").click( function(event) {
        alert("You clicked the button using JQuery!");
    });

    $(".ouch").click( function(event) {
           alert("You clicked me! ouch!");
    });


    $("p").hover( function() {
            $(this).css('color', 'green');
    },
    function() {
            $(this).css('color', 'grey');
    });

    $("#about-btn").click( function(event) {
msgstr = $("#msg").html()
        msgstr = msgstr + "o"
        $("#msg").html(msgstr)
    });


     $(function(){ 
	$('#botones .boton').click(function(){   
		$('body').removeClass();     
			if(this.id == 'aumentar'){    
	    		$('body').addClass('grande');    
	    	}  
		else if(this.id == 'mas_grande'){  
	    		$('body').addClass('mas_grande');  
		}  
		$('#botones .boton').removeClass('seleccion'); 
   		$(this).addClass('seleccion');  
	});                             
  

     $(function(){  
      $('#botones .boton').hover(function() {  
        $(this).addClass('sobre');
      }, 
       function() {  
      $(this).removeClass('sobre');   
  	});  



    $(function(){  	 
    	 $.ajax({
		url: "/rango/reclama_datos",
		type: 'get',                        
		success: function(datos) {
			Visualiza_datos (datos);  
		},
		failure: function(datos) { 
			alert('esto no vá');
		}
	});
	
	function Visualiza_datos (datos) {
		
		var bares = []
		var views = []
		for (i=0; i<datos["length"]; i++){
			bares.push(datos[i])
			views.push(datos[datos[i]])
		}

    $(function () { 
         var chart = new Highcharts.Chart({
                chart: {
                    type: 'column',
                    renderTo: 'container'
		},
		title: {
			text: 'Grafica de Visitas'
		},
		xAxis: {
			categories: ['Bares']
		},		
		yAxis: {
			title: {
				text: 'Visitas'
			}
		},
		series: datos,
	});
		});
	};
	});	
	});
   });
});




