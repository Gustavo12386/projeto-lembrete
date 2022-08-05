$( document ).ready(function() {
    var deleteBtn = $('.delete-btn');
    $(deleteBtn).on('click', function(e) {

        e.preventDefault();
        var dellink = $(this).attr('href');
        var result = confirm('Quer deletar essa tarefa?'); 
        
        if(result){
           window.location.href = dellink
        }

    });
});
