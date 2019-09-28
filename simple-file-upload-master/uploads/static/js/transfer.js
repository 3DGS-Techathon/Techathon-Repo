(function($) {
    
    $('#list1').sortable({
        connectWith: 'ul'
    });    
    
    $('#list2').sortable({
        connectWith: 'ul',
        receive: function(ev, ui) {
            if(ui.item.hasClass("number"))
              ui.sender.sortable("cancel");
        }
    });    
})(jQuery);