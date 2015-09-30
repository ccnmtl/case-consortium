var index = lunr(function() {

    this.field('title', {boost: 10});
    this.field('content');
    this.field('slug');
    this.field('id');
});
index.ref('slug');


window.data = {};
$.getJSON('/js/api/cases.json').done(function(item) {
    item.cases.forEach(function(d) {
        var el = $('<div>' + d.title + '</div>');
        // convert encoded html to decoded text
        // then grab that text and insert it to 
        // the index
        el.html(el.text());
        d.title = el.text();
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
                // this is the drop down HTML you
            	// see appended to the search bar
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


var searchTable = function() {
	jQuery("#facets").hide();
    var q = $('#q').val();
    window.results = index.search(q);
    var $el = $('#results');
    $el.empty();
    $el.show();
    

    if (results.length == 0) {
        $el.html('Sorry, no results matching your query were found.');
    } else {
    	CaseFunctions.setTableHeaders();
        for (r in results.slice(0, 10)) {
            if (results.hasOwnProperty(r)) {

                var d = results[r].ref;
                var row = "";
                var case_category = window.data[d]['category'];
                var cat_url = window.data[d]['cat_url'];
                var case_number = window.data[d]['case_number'];
                var title = window.data[d]['title'];
                var slug = window.data[d]['slug'];

                var $result = $('<tr class="item">');
                var row_elements = '<td>' + case_number + '</td><td><a target="_blank "href="'+slug+'">'
                                   + title + '</a></td><td><a href="/category/'+cat_url+'">'
                                   + case_category + '</td>'
                $result.append(row_elements);
                $el.append($result);
            }
            jQuery("#results").tablesorter();
        }
    }
    return false;
}

var createSearchTable = function(q) {
	jQuery("#facets").hide();
    //var q = $('#q').val();
    window.results = index.search(q);
    var $el = $('#results');
    $el.empty();
    $el.show();
    

    if (results.length == 0) {
        $el.html('Sorry, no results matching your query were found.');
    } else {
    	CaseFunctions.setTableHeaders();
        for (r in results.slice(0, 10)) {
            if (results.hasOwnProperty(r)) {

                var d = results[r].ref;
                var row = "";
                var case_category = window.data[d]['category'];
                var cat_url = window.data[d]['cat_url'];
                var case_number = window.data[d]['case_number'];
                var title = window.data[d]['title'];
                var slug = window.data[d]['slug'];

                var $result = $('<tr class="item">');
                var row_elements = '<td>' + case_number + '</td><td><a target="_blank "href="'+slug+'">'
                                   + title + '</a></td><td><a href="/category/'+cat_url+'">'
                                   + case_category + '</td>'
                $result.append(row_elements);
                $el.append($result);
            }
            jQuery("#results").tablesorter();
        }
    }
    return false;
}
