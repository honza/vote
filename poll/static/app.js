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

  $(function() {

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
