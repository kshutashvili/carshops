function basket_session(name, id){
    if (id){
        var element = "#" + name;    
    }
    else{
        var element = "." + name;
    }
    $(element).click(function(event){
        var basket_template = $("#basket_template");
        var product = $(this)
        $.ajax(product.data('url'),{
            'type':'POST',
            'async':true,
            'data':{
                'pk':product.data('product'),
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            'success':function(data,status,xhr){
                $("#basket_template").html(data.amount + ' товаров на сумму ' + data.sum + ' грн');
                $("#basket_number").html(data.amount);
            },
            'error':function(xhr,status,error){

            }
        });
    });
}


function objects_generate_block(length){
    $("#more_prod").click(function(event){
        var more = $(this);
        $.ajax(more.data('url'),{
            'type':'GET',
            'async':true,
            'dataType':'html',
            'data':{
                'start':more.data('length'),
                'length':length,
                'container':'block',
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            'success':function(data,status,xhr){
                $("#tovar-list-block").append(data);
                for(var i=more.data('length')+1;i<more.data('length')+length;i++){
                    basket_session('tovar__basket'+i, true);
                }
            },
            'error':function(xhr,status,error){
                //console.log(status);
            }
        });
    });
}


function objects_generate_view(length){
    $("#more_prod").click(function(event){
        var more = $(this);
        $.ajax(more.data('url'),{
            'type':'GET',
            'async':true,
            'dataType':'html',
            'data':{
                'start':more.data('length'),
                'length':length,
                'container':'view',
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            'success':function(data,status,xhr){
                $("#tovar-list-view").append(data);
                for(var i=more.data('length')+1;i<more.data('length')+length;i++){
                    basket_session('basket'+i, true);
                }
                more.data("length", more.data('length') + length);
            },
            'error':function(xhr,status,error){
                //console.log(status);
            }
        });
    });
}


function cars_generate(container_changed, container, optional_container_to_clean){
    $("#" + container_changed).click(function(event){
        var select = $("#" + container_changed);
        $.ajax(select.data('url'),{
            'type':'GET',
            'async':true,
            'dataType':'html',
            'data':{
                'name':select.data('name'),
                'id':select.val(),
                'container':container,
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            'success':function(data,status,xhr){
                $("#" + container).empty();
                $("#" + container).html(data);
                $("#" + optional_container_to_clean).empty();
                var html = '<option value="0">Год выпуска автомобиля</option>'
                $("#" + optional_container_to_clean).html(html);
                //console.log(status);
            },
            'error':function(xhr,status,error){
                //console.log(status);
            }
        });
    });
}


$(document).ready(function(){
    var lastPathSegment = location.pathname.split('/').slice(-3)[0];
    console.log(lastPathSegment);
    if (lastPathSegment != 'product'){
        basket_session('buy',false);
        basket_session('tovar__basket',false);
        basket_session('basket',false);        
    }

    objects_generate_block(2);
    objects_generate_view(2);
    cars_generate('stamp_cars', 'model_cars', 'year_cars');
    cars_generate('model_cars', 'year_cars');
});
