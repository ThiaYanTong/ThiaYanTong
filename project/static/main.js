// run this only when the DOM is loaded
$(document).ready(function() {
    var max_fields = 10;
    var wrapper = $(".container1");
    var add_button = $("#add");

    var x = 1;
    $(add_button).click(function(e) {
        e.preventDefault();
        console.log("hello")
        if (x < max_fields) {
            x++;
            append_input() //add input box
        } else {
            alert('You Reached the limits')
        }
    });

    $(wrapper).on("click", ".delete", function(e) {
        e.preventDefault();
        $(this).parent('div').remove();
        x--;
    })
});

function append_input() {
    console.log("hello1")
    var wrapper = $(".container1");
    $.ajax({
        type: "GET",
        url: "/query",
        success: function(data) {
            var div = document.createElement("div");
            console.log("This is the returned data: " + data.success);
            var items = data.success;
            var select = document.createElement("select");
            select.name = "input";
            select.id = "input";
            var option = document.createElement("option");
            option.setAttribute("disabled", "disabled");
            option.defaultSelected = true;
            option.value = "";
            option.text = "Code";
            select.appendChild(option);
            for (const val of items)
            {
                var option = document.createElement("option");
                option.value = val;
                option.text = val.charAt(0).toUpperCase() + val.slice(1);
                select.appendChild(option);
            }
            var createA = document.createElement('a');
            var createAText = document.createTextNode("Delete");
            createA.setAttribute("class", "delete");
            createA.setAttribute('href', "#");
            createA.appendChild(createAText);
            div.appendChild(select);
            var blank = document.createTextNode( '\u00A0' );
            div.append(blank);
            div.append(blank);
            div.append(createA);
            $(wrapper).append(div);

        },
        error: function(error){
            console.log("Here is the error res: " + JSON.stringify(error));
        }
    });

    };


$(document).ready(function() {
    $("#form").submit(function(e) {
        e.preventDefault();
    });
});

function create_table(data) {
    var output = data.success;
    var current_index = data.current_index;
    var length = data.length;
    output = JSON.parse(output);
    console.log(output.length);
    console.log(output);

    console.log(output[0]);
    var test = output[0];
    console.log(test.length);

    var table = document.createElement('table');
    table.setAttribute("class","my-table-created");
    var first_column = ['0730 - 0830', '0830 - 0930', '0930 - 1030', '1030 - 1130', '1130 - 1230', '1230 - 1330', '1330 - 1430', '1430 - 1530', '1530 - 1630', '1630 - 1730', '1730 - 1830', '1830 - 1930', '1930 - 2030', '2030 - 2130', '2130 - 2230', '2230 - 2330'];
    var first_row = ['Time / Day','Mon','Tue','Wed','Thu','Fri','Sat'];

    console.log(first_row.length);
    var tr = document.createElement('tr');
    for (var k = 0; k < first_row.length; k++) {
        var td = document.createElement('td');
        var text = document.createTextNode(first_row[k]);
        td.appendChild(text);
        tr.appendChild(td);
    }
    table.appendChild(tr);

    for(var i = 0; i < output.length; i++) {
        var single_output = output[i];
        console.log(single_output)
        var tr = document.createElement('tr');
        for(var j = 0; j < single_output.length; j++) {

            if (j == 0) {
                var td = document.createElement('td');
                var text = document.createTextNode(first_column[i]);
                td.appendChild(text);
                tr.appendChild(td);

                if (single_output[j] === null) {
                    var td = document.createElement('td');
                    var text = document.createTextNode(" ");
                    td.appendChild(text);
                    tr.appendChild(td);
                }
                else {
                    var td = document.createElement('td');
                    var text = document.createTextNode(single_output[j]);
                    td.appendChild(text);
                    tr.appendChild(td);
                }

            }
            else {
                if (single_output[j] === null) {
                    var td = document.createElement('td');
                    var text = document.createTextNode(" ");
                    td.appendChild(text);
                    tr.appendChild(td);
                }
                else {
                    var td = document.createElement('td');
                    var text = document.createTextNode(single_output[j]);
                    td.appendChild(text);
                    tr.appendChild(td);
                }
            }
        }
        table.appendChild(tr);
    }
    $("#my-table-div").html('');
    $("#my-table-div").append(table);
    $("#start").html('');
    $("#start").append(current_index + 1);
    $("#end").html('');
    $("#end").append(length);
}


function create_paragraphs(data) {
    var code = data.code;
    var name = data.name;
    var course_index = data.course_index;
    var length = name.length;
    var div = document.createElement('div');
    var table = document.createElement('table');
    var tr = document.createElement('tr');
    var first_row = ['Course Code',"Course Title","Course Index"];
    for (var i = 0; i < first_row.length; i++) {
        var td = document.createElement('td');
        var text = document.createTextNode(first_row[i]);
        td.appendChild(text);
        tr.appendChild(td);
    }
    table.appendChild(tr);

    for (var j = 0; j < length; j++) {
        var tr = document.createElement('tr');
        for (var k = 0; k < first_row.length; k++) {
            var td = document.createElement('td');
            if (k === 0) {
                var text = document.createTextNode(code[j]);
            }
            if (k === 1) {
                var text = document.createTextNode(name[j]);
            }
            if (k === 2) {
                var text = document.createTextNode(course_index[j]);
            }
            td.appendChild(text);
            tr.appendChild(td);
        }
        table.appendChild(tr);
    }
    div.append(table);
    $("#paragraphs").html('');
    $("#paragraphs").append(table);
}



function myfunction(e) {

    var result = Array.from(document.querySelectorAll("#input"), ({ value }) => value);
    var query_all_input = document.querySelectorAll("#input");
    var results = {};
    var x = 0
    query_all_input.forEach((each_input) => {
        results[x]=each_input.value;
        x++;
    });
    

    $.ajax({
        type : 'POST',
        url : "/input_checking",
        contentType: 'application/json;charset=UTF-8',
        data : JSON.stringify(results),
        success: function(data) {
            if (data.status === 'pass') {
                $.ajax({
                    type : 'POST',
                    url : "/processing",
                    contentType: 'application/json;charset=UTF-8',
                    data : JSON.stringify(results),
                    success: function(data) {

                        $("#error_empty").html('');
                        $("#error_dup").html('');
                        create_table(data);
                        console.log("create new table");
                        create_paragraphs(data);
                        console.log("create new paragraphs");
                    }
                });
            }
            if (data.reason === 'empty and dup') {
                var span_empty = document.createElement('span');
                span_empty.setAttribute("style","color: red");
                var text_empty = document.createTextNode("Fields cannot be empty.");
                span_empty.appendChild(text_empty);
                $("#error_empty").html('');
                $("#error_empty").append(span_empty);

                var span_dup = document.createElement('span');
                span_dup.setAttribute("style","color: red");
                var text_dup = document.createTextNode("Fields cannot be duplicated.");
                span_dup.appendChild(text_dup);
                $("#error_dup").html('');
                $("#error_dup").append(span_dup);
            }
            if (data.reason === 'empty') {
                var span = document.createElement('span');
                span.setAttribute("style","color: red");
                var text = document.createTextNode("Fields cannot be empty.");
                span.appendChild(text);
                $("#error_empty").html('');
                $("#error_empty").append(span);

            }
            if (data.reason === 'dup') {
                var span = document.createElement('span');
                span.setAttribute("style","color: red");
                var text = document.createTextNode("Fields cannot be duplicated.");
                span.appendChild(text);
                $("#error_dup").html('');
                $("#error_dup").append(span);

            }

        }
    });
};

$(document).ready(function() {
    $("#form").submit(function(e) {
        e.preventDefault();
    });
});


$(document).ready(function() {
    $("#decrement").click(function(e) {
        e.preventDefault();
        console.log(document.querySelector("table").getAttribute('class'))
        if (document.querySelector("table").getAttribute('class') == 'my-table-created') {
            console.log("decrement");
            $.ajax({
                type : 'POST',
                url : "/increment_decrement",
                contentType: 'application/json;charset=UTF-8',
                data : JSON.stringify('decrement'),
                success: function(data) {
                    create_table(data);
                    create_paragraphs(data)
                    console.log("create decrement table");
                }
            });
        }
    });

    $("#increment").click(function(e) {
        e.preventDefault();
        if (document.querySelector("table").getAttribute('class') == 'my-table-created') {
            console.log("increment");
            $.ajax({
                type : 'POST',
                url : "/increment_decrement",
                contentType: 'application/json;charset=UTF-8',
                data : JSON.stringify('increment'),
                success: function(data) {
                    create_table(data);
                    create_paragraphs(data)
                    console.log("create increment table");
                }
            });
        }
    });
});

