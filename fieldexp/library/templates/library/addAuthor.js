$(function () {
    var authorCount = 1;
    var addAuthorForm = function(){
        authorCount++;

    };

    var renderForm = function(count){
        var formstring =
            ['<div class="form-group" id="author' + count + '">',
             '<label class="control-label col-lg-2" for="firstname' + count + '" name="author' + count + '">Author ' + count + '</label>',
             '<div class="col-lg-3">',
             '<input type="text" class="form-control" id="firstname' + count + '" name="firstname' + count + '" placeholder="First name">',
             '</div>',
             '<div class="col-lg-1">',
             '<input type="text" class="form-control" id="mi' + count + '" name="mi' + count + '" placeholder="MI">',
             '</div>',
             '<div class="col-lg-3">',
             '<input type="text" class="form-control" id="lastname' + count + '" name="lastname' + count + '" placeholder="Last name">',
             '</div>',
             '<div id="buttons' + count + '">',
             '<div class="col-lg-1">',
             '<button type="button" class="btn btn-success" id="author_button' + count + '">',
             '<span class=" glyphicon glyphicon-plus-sign"></span> Add',
             '</button>',
             '</div>',
             '<div class="col-lg-1">',
             '<button type="button" class="btn btn-danger" id="author_remove_button' + count + '">',
             '<span class=" glyphicon glyphicon-minus-sign"></span> Remove',
             '</button>',
             '</div>',
             '</div>',
             '</div>'].join('');
        return $.parseHTML(formstring);
    };

    var buttonRemoveFunction = function(count)
    {
        $("div#author" + count).hide();
        $("div#buttons" + (count-1)).show();
    }

    var buttonFunction = function(count){
        $("div#authors_div").append(function(){return renderForm(count+1);});
        $("div#buttons" + (count)).hide();
        $("button#author_button" + (count+1)).on("click", function() {buttonFunction(count+1);});
        $("button#author_remove_button" + (count+1)).on("click", function() {buttonRemoveFunction(count+1);});
    };


    $("button#author_button1").on("click", function() {
        buttonFunction(1);
    });
});
