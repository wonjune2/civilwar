var main = {
  init: function () {
    var _this = this;
    var test;
    $(".name-modify").on("click", function (e) {
      //   _this.cancel();
      if (test) _this.cancel(test);
      test = _this.modify(e);
    });
    $(".cancelBtn").on("click", function (e) {
      _this.btnCancel(e);
    });
  },
  modify: function (e) {
    var targets = $(e.target).parent().prev();
    console.log("targets:", targets);
    var oldName = targets.html();
    targets.html(
      '<input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="addon-wrapping">'
    );
    var btntarget = $(e.target).parent();
    console.log(btntarget.text());
    btntarget.html(
      '<button type="button" class="btn btn-outline-dark btn-sm cancelBtn">취소</button>'
    );
    return { oldName: oldName, targets: targets, btntarget: btntarget };
  },
  cancel: function (test) {
    test.targets.html(test.oldName);
  },
};
main.init();
