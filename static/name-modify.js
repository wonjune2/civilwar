var main = {
  init : function() {
    var _this = this;
    $('.name-modify').on('click', function(e){
      var oldTag = _this.modify(e);
      cancel.init(oldTag);
    })
  },
  modify : function(e) {
    console.log("진입!!");
    var oldTag = $('.name-place').html();
    $('.name-place').html('<div class="input-group mb-3">\
    <input type="text" class="form-control" name="name" placeholder="수정할 이름을 적어주세요" aria-describedby="button-addon2">\
    <button class="btn btn-outline-secondary cancel" type="button" id="button-addon2">취소</button>\
  </div>');
    return oldTag;
  },
  cancel : function() {
    cancel.cancel();
  }
}
var cancel = {
  init: function(oldTag) {
    var _this = this;
    $('.cancel').on('click', function() {
      _this.cancel(oldTag);
      main.init();
    })
  },
  cancel : function(oldTag) {
    $('.name-place').html(oldTag);
  }
};

main.init();
