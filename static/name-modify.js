var main = {
  init: function () {
    var _this = this;
    var oldName;
    var oldInput;
    $(".name-modify").on("click", function (e) {
      console.log(oldName);
      //   _this.cancel();
      _this.modify(e, oldName, oldInput);
    });
  },
  modify: function (e, oldName, oldInput) {
    var targets = $(e.target).parent().prev();
    oldName = targets.html();
    oldInput = targets.html(
      '<input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="addon-wrapping">'
    );
  },
};
main.init();
