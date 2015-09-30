var CaseFunctions = function () {
	var setTableHeaders = function ()
	{
        jQuery('#results').prepend('<thead>' +
                '<tr>' +
                    '<th class="case_id_head">Case Number</th>' +
                    '<th class="case_title_head">Title</th>' +
                    '<th class="case_topics_head">Category</th>' +
                '</tr>' +
               '</thead>');
    };
    
    var drawActiveFacetsDiv = function ()
		{
    	$('.active-facets').html(
                '<span class="category" data-facetname="category" style="display:none">Category: </span>' +
                '<span class="topics" data-facetname="topics" style="display:none">Topics: </span>' +
                '<span class="related_cases" data-facetname="related_cases" style="display:none">Related Cases: </span>');
		};
		
    var unescapeHtml = function ()
	{
		jQuery('.unescape').each(function(){
            var text = jQuery(this).text();
            jQuery(this).html(text);
		});
	};
    
	var clearQueryParams =  function() {
        var new_path = "/case/";
        var stateObj = { currentUrl: new_path };
        window.history.pushState(stateObj, "case-search", new_path);
    };
        
    var switchKeywordSearchPath = function() {
        var new_path = "/case/?search=keyword";
        var stateObj = { currentUrl: new_path };
        window.history.replaceState(stateObj, "case-search", new_path);
    };
    
    var switchFilterSearchPath = function(){
        var new_path = "/case/?search=filter";
        var stateObj = { currentUrl: new_path };
        window.history.replaceState(stateObj, "case-search", new_path);
    };
    
    var updateFilterSearchPath = function(){
        var new_path = "/case/?search=filter";
        var stateObj = { currentUrl: new_path };
        _.each(settings.state.filters, function(filter, facetname) 
        {
            for(var x=0; x < filter.length; x++)
            {
                new_path = new_path + "&" + facetname + "=" + filter[x];
            }
        });
        window.history.replaceState(stateObj, "case-search", new_path);
    };
    
    var displayActiveBreadcrumbs = function(){
        // add tags under search bar for active filters
        _.each(settings.state.filters, function(filter, facetname) 
        {   
           $('.active-facets .'+facetname+'').show();
            for(var x=0; x < filter.length; x++)
            {
                $('.active-facets .'+facetname+'').append("<span class='active-search-term' data-filtername='"+filter[x]+"'>"+filter[x]+"<span class='glyphicon glyphicon-remove'></span></span>");
            }
        });
    };
    
    var reconstructFilterSearch = function () {
        // first check if there is a '?search=filter' in the link
        // if it is recreate search from url params
            setTableHeaders();
            unescapeHtml();
            drawActiveFacetsDiv();

            try 
            {
                var qry_params = window.location.href.split('?search=filter&');
                var params = qry_params[1];

                // first check which facets are in url
                if (params.indexOf('category') !== -1)
                {
                  $.extend(settings.state.filters, {'category': []});
                }
                if (params.indexOf('topics') !== -1)
                {
                  $.extend(settings.state.filters, {'topics': []});
                }
                if (params.indexOf('related_cases') !== -1)
                {
                  $.extend(settings.state.filters, {'related_cases': []});
                }

                var active_facets = params.split('&');

                // go over url parameters and re create search results
                for(var count_params=0; count_params < active_facets.length; count_params++)
                {   
                    //count_params = count_params - 1;
                    var find_facet = String(active_facets[count_params]).split('=');
                    var facet = find_facet[0]; //category/related topics/
                    var search_term = find_facet[1];
                    settings.state.filters[facet].push(decodeURI(search_term));
                }

                displayActiveBreadcrumbs();
                
            }
            catch(error)
            {
              console.log(error);
            }

    };
    
    var updateFilterQueryParamsBreadCrumbs = function () {
    	drawActiveFacetsDiv();
    	displayActiveBreadcrumbs();
    	updateFilterSearchPath();
    	unescapeHtml();

    };
    
    var updateFilterSearch = function () {
    	updateFilterSearchPath();
    	unescapeHtml();
        drawActiveFacetsDiv();
    	
    };
        
    var resetSearchFacetTableBreadcrumbsPath = function ()
    {
 		/* Reset entire interface --> reset facets, bread crumbs, and table*/
    	//this.
		switchFilterSearchPath();
		
 	};
 	
    var resetSearchKeywordTablePath = function ()
 	{
    	switchKeywordSearchPath();
		
 	};
        	
	return {
		
		setTableHeaders: setTableHeaders,
        drawActiveFacetsDiv: drawActiveFacetsDiv,
 		unescapeHtml: unescapeHtml,
 		clearQueryParams: clearQueryParams,
 		switchKeywordSearchPath : switchKeywordSearchPath,
        switchFilterSearchPath : switchFilterSearchPath,
        displayActiveBreadcrumbs: displayActiveBreadcrumbs,
        updateFilterSearchPath: updateFilterSearchPath,
 		resetSearchFacetTableBreadcrumbsPath: resetSearchFacetTableBreadcrumbsPath,
 		resetSearchKeywordTablePath: resetSearchKeywordTablePath,
 		reconstructFilterSearch: reconstructFilterSearch,
 		updateFilterQueryParamsBreadCrumbs: updateFilterQueryParamsBreadCrumbs,

	};
	
	
}();