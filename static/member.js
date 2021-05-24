var main = {
    init : function() {
        var _this = this;
        var list = [];
        
        $('.member').on('click', function(e){
            _this.addList(list,e);
            console.log(list.length);
            if(list.length == 10) _this.onSubmit(list);
        });
        $('.entry').on('click', function(e){
            _this.removeList(list,e);
        });
    },
    addList : function(list,e) {
        if(list.length < 10) {
            var data = {
                id : $(e.target).val(),
                name : $(e.target).text().trim(),
            };
            data.winrate = $('#' + data.id).val();
            list.push(data);
            $(e.target).attr('disabled', true);
            entry.in(data);
        } else {
            $('.alerts').html('<div class="alert alert-warning alert-dismissible fade show" role="alert w-75">\
                <strong>참가 인원은 10명이 최대입니다!!</strong>\
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>\
            </div>');
            // $(e.target).on('click', function() {
            //     console.log(e.target);
            //     
            // })
           
        }
    },
    removeList : function(list, e) {
        var data = {
            id : $(e.target).val(),
        }
        var index = list.findIndex(i => i.id == data.id);
        list.splice(index, 1);
        console.log(list);
        $(e.target).attr('disabled', true);
        entry.out(data, e);
    },
    onSubmit : function(list) {
        console.log(list)
        $('.balance').attr('disabled', false);
        // $('.random').attr('disabled', false);
    }
};

var entry = {
    in : function(data) {
        var etr = $('.entry:disabled');
        etr = etr.first().attr('disabled', false);
        var send = $('.sendId[value=""]');
        send.first().val(data.id);
        etr.val(data.id);
        etr.contents()[0].textContent = data.name;
        etr.contents()[1].textContent = Math.ceil(data.winrate * 100)  + "%";
    },
    out : function(data, e) {
        var member = $('.member[value='+data.id+']');
        member.attr('disabled', false);
        var etr = $(e.target);
        $('.sendId[value='+data.id+']').val('');
        etr.val('');
        etr.contents()[0].textContent = '참가자를 선택해 주세요';
        etr.contents()[1].textContent = '0%';
    }
};
main.init();
