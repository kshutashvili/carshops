function change_amount(container_class){
    $("." + container_class).click(function(event){
        var change = $(this);
        $.ajax(change.data('url'),{
            'type':'POST',
            'async':true,
            'data':{
                'id':change.data('id'),
                'action':change.data('action'),
                'amount':change.data('amount'),
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()   
            },
            'success':function(data,status,xhr){
                $("#amount" + change.data('id')).val(data.amount);
                $("#convert").html(data.sum + " грн");
                $("#sum").html(data.sum + " грн");
                var amount = parseInt($("#basket_number").text());
                if(change.data('action') == "-" && data.not_last){
                    amount--;
                }
                else if(change.data('action') == "+"){
                    amount++;
                }
                $("#basket_template").html(amount + ' товаров на сумму ' + data.sum + ' грн');
                $("#basket_number").html(amount);
            },
            'error':function(xhr,status,error){
                console.log(status);
            }
        });
    });
}


function clear_basket(button){
    $("#" + button).click(function(event){
        var clear = $(this);
        $.ajax(clear.data('url'),{
            'type':'POST',
            'async':true,
            'dataType':'html',
            'data':{
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()   
            },
            'success':function(data,status,xhr){
                $("#shopping-basket").html(data);
                $("#basket_template").html(0 + ' товаров на сумму ' + 0 + ' грн');
                $("#basket_number").html(0);
            },
            'error':function(xhr,status,error){
                console.log(status);
            }
        });
    });
}


$(document).ready(function(){
    change_amount('btn.plus');
    change_amount('btn.minus');
    clear_basket('clear-basket');
});