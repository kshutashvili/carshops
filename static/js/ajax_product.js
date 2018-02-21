function objects_generate_comments(){
    $("#create_comment").off();
    $("#comment-form").on('submit', function(event){
        console.log('123');
        console.log('1233');
        console.log('1232');
        console.log('1213');
        console.log('12');
        var action = $('#create_comment');
        var name = $('#name').val();
        var msg = $('#message').val();
        $.ajax(action.data('url'),{
            'type':'POST',
            'async':true,
            'dataType':'html',
            'data':{
                'name':name,
                'msg':msg,
                'prod_id':action.data('id'),
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            'success':function(data,status,xhr){
                $("#comments-container").append(data);
                console.log(status);
            },
            'error':function(xhr,status,error){
                console.log(status);
            }
        });
    });
}


$(document).ready(function(){
    objects_generate_comments();
});
