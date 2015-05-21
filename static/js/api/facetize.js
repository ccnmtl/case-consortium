
                    jQuery(document).ready(function(){
                        var item_template = 
                           '<div class="item">' +
                             '<img src="<%= obj.imageURL %>">' +
                             '<h4><%= obj.title %></h4>' + 
                             '<p class="tags">' + 
                             '<% if (obj.category) {  %><%= obj.category %><% } %>' +
                             '</p>' +
                             '<p class="desc"><%= obj.description %></p>' +
                             '<p class="item-id"><%= obj.id %></p>' +
                             '<p class="item-topics">Topics: </br><% for(var topic in obj.topics)' +
                             '{ %> <%= obj.topics[topic] %><span class="comma-sep">,</span> <% } %></p>' +
                           '</div>';
                        settings = { 
                          items            : Cases,
                          facets           : { 
                                              'topics'     : 'What topic',
                          },  
                          resultSelector   : '#results',
                          facetSelector    : '#facets',
                          resultTemplate   : item_template,
                          paginationCount  : 10,
                          orderByOptions   : {'topic': 'Topic', 'title': 'Title'},
                          
                        }   

                        
                        jQuery.facetelize(settings);

                    });
            