function objects_generate_news(length){
    $("#more_news").click(function(event){
        var more = $(this);
        $.ajax(more.data('url'),{
            'type':'GET',
            'async':true,
            'dataType':'html',
            'data':{
                'start':more.data('length'),
                'length':length,
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            'success':function(data,status,xhr){
                $("#news-container").append(data);
                more.data("length", more.data('length') + length);
            },
            'error':function(xhr,status,error){
                //console.log(status);
            }
        });
    });
}


$(document).ready(function(){
    objects_generate_news(3);
});