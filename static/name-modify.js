var main = {
  init: function () {
    var _this = this;
    this.targets;
    var par;
    $(".name-modify").on("click", function (e) {
      _this.modify(e);
    });
  },
  modify: function (e) {
    var par = $(e.target).parent();
    var oldTag = $(e.target).parent().prev().html();
    par = par
      .prev()
      .html(
        '<input type="text" class="form-control" placeholder="이름을 적어주세요" aria-label="Username" aria-describedby="addon-wrapping">'
      )
      .children()
      .html();
    console.log("par : ", par, "oldTag : ", oldTag);
    return oldTag, par;
  },
};
main.init();
