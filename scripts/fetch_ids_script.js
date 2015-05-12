var caseObjs = {};
jQuery('.list-group-item').each(function(){
    var title = jQuery(this).text();
    var href = jQuery(this).find('a').attr('href');
    id = href.split('case_id=')[1].split('.html')[0];
    caseObj = {
        "title": title,
        "id" : id
    };
    caseObjs[id] = caseObj;
})

for(var caseId in caseObjs){
    var id = caseObjs[caseId].id;
    var title = caseObjs[caseId].title;
    console.log('cases[' + id + ']=' + '"' + title + '"');
}
