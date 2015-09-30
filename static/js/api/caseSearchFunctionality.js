var CaseFunctions = function () {
	
	return {
		
		setTableHeaders: function ()
		{
            jQuery('#results').prepend('<thead>' +
                    '<tr>' +
                        '<th class="case_id_head">Case Number</th>' +
                        '<th class="case_title_head">Title</th>' +
                        '<th class="case_topics_head">Category</th>' +
                    '</tr>' +
                   '</thead>');
        },
        drawActiveFacetsDiv: function ()
 		{
        	$('.active-facets').html(
                    '<span class="category" data-facetname="category" style="display:none">Category: </span>' +
                    '<span class="topics" data-facetname="topics" style="display:none">Topics: </span>' +
                    '<span class="related_cases" data-facetname="related_cases" style="display:none">Related Cases: </span>');
 		},
 		unescapeHtml: function ()
 		{
 			jQuery('.unescape').each(function(){
                var text = jQuery(this).text();
                jQuery(this).html(text);
 			});
 		},
 		toggleURLPath : function(){
        	if (window.location.href.indexOf('?search=filter') !== -1)
            {
        		var new_path = "/case/?search=keyword";
                var stateObj = { currentUrl: new_path };
        		window.history.replaceState(stateObj, "case-search", new_path);
            }
        	else if (window.location.href.indexOf('?search=keyword') !== -1)
            {
        		var new_path = "/case/?search=filter";
                var stateObj = { currentUrl: new_path };
        		window.history.replaceState(stateObj, "case-search", new_path);
            }
        	
        }
 		/*,
 		resetFacets: function ()
 		{
		
		
 		},
 		clearHistory: function ()
 		{
		
		
 		},
 		setTableHeaders: function ()
 		{
		
		
 		}*/
	};
	
	
}();