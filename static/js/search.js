var index = lunr(function() {

    this.field('title', {boost: 10});
    this.field('content');
    this.field('slug');
});
index.ref('slug');


window.data = {};
$.getJSON('/js/api/cases.json').done(function(item) {
    item.cases.forEach(function(d) {
        index.add(d);
        data[d.slug] = d;
    });
}).fail(function(jqxhr, textStatus, error) {
    var err = textStatus + ', ' + error;
    console.error('Error getting Hugo index flie:', err);
});

var doSearch = function() {
    var q = $('#q').val();
    window.results = index.search(q);
    var $el = $('#search-results');
    
    $el.empty();
    $el.show();
    if (results.length == 0) {
        $el.html('Sorry, no results matching your query were found.');
    } else {
        $el.append(
           $('<h2 class="results-title">Search Results: "' + q + '"</h2>')
        );

        for (r in results.slice(0, 10)) {
            if (results.hasOwnProperty(r)) {

                var d = results[r].ref;
                var title = window.data[d]['title'];
                var slug = window.data[d]['slug'];

                var $result = $('<div class="result-link">');
                var html_convert = $('<div>');

                html_convert.append(title);
                var text = html_convert.text();
                html_convert.html(text)
                $result.append('<a target="_blank "href="'+
                    slug+'">' + html_convert.html() + '</a>');
                
                $el.append($result);
            }
        }
    }
    return false;
}

$(document).ready(function() {
    $('#q').on('keydown', function(event) {
       var x = event.which;
       if (x === 13) {
           event.preventDefault();
       }
    });
    $('#q').keyup(function() {
        $('#search-results').empty();
        if ($(this).val().length < 2) {
            return;
        }
        $('#clear-search').show();
        return doSearch();
    });
    $('#clear-search').click(function(){
        $('#search-results').empty();
        $('#search-results').hide();
        $('#clear-search').hide();
    });
});