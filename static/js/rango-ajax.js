$('#likes').click(function(){
    var barid;
    barid = $(this).attr("data-catid");
    $.get('/rango/like_bares/', {bares_id: barid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
    });
  

});
