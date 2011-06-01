(function($) {

  var actions = {
    'delete': 'Deleted',
    'no-member': 'Not a member',
    'duplicate': 'Duplicate'
  };

  var makeReq = function(id, action) {
    var data = {
      uid: id,
      action: action
    };
    $.get('/staff/ajax/', data, function(data) {
      var res = $.parseJSON(data);
      if (res.status == 'success') {
        // update first table cell
        var tr = $('#uid-' + id);
        tr.addClass(action);
        tr.children().first().html(actions[action]);
      } else {
        alert(status.message);
      }
    });
  };

  var makeChart = function() {

    if (typeof data === 'undefined')
      return;

    var canvas, colors, w, h;

    var total = data[0] + data[1];
    w = 300;
    h = 200;

    canvas = document.getElementById('canvas');
    colors = ["#0094ee", "#f02c02"];

    if (typeof canvas.getContext === 'undefined') {
        return;
    }

    var ctx = canvas.getContext('2d');
    var radius = Math.min(w/2, h/2);
    var center = [w/2, h/2];

    var sofar = 0;

    for (var piece in data) {

        var thisvalue = data[piece] / total;

        ctx.beginPath();
        ctx.moveTo(center[0], center[1]);
        ctx.arc(
            center[0],
            center[1],
            radius,
            Math.PI * (- 0.5 + 2 * sofar),
            Math.PI * (- 0.5 + 2 * (sofar + thisvalue)), false);

        ctx.lineTo(center[0], center[1]);
        ctx.closePath();
        ctx.fillStyle = colors[piece];
        ctx.fill();

        sofar += thisvalue;
    }

  };

  $(function() {

    makeChart();

    $('input.no-member').click(function() {
      var id = $(this).parent().parent().attr('id');
      id = id.substr(4, (id.length - 4));
      makeReq(id, 'no-member');
    });

    $('input.duplicate').click(function() {
      var id = $(this).parent().parent().attr('id');
      id = id.substr(4, (id.length - 4));
      makeReq(id, 'duplicate');
    });

    $('input.delete').click(function() {
      var id = $(this).parent().parent().attr('id');
      id = id.substr(4, (id.length - 4));
      makeReq(id, 'delete');
    });

  });

})(jQuery);
