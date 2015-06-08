find -type f -name '*.html' | xargs sed -i 's/Kirsten Lundberg, Director, Case Consortium @ Columbia//g';
find -type f -name '*.html' | xargs sed -i 's/Kirsten Lundberg, Director, KCSI//g';

find -type f -name '*.html' | xargs sed -i 's/<strong>For further information, please contact:<\/strong>//g';
find -type f -name '*.html' | xargs sed -i 's/For further information, please contact://g';

find -type f -name '*.html' | xargs sed -i 's/Tel: 857-259-2148//g';
find -type f -name '*.html' | xargs sed -i 's/Tel: 212-854-8398//g';
find -type f -name '*.html' | xargs sed -i 's/Fax: 212-854-7837//g';
find -type f -name '*.html' | xargs sed -i 's/Tel: 212-854-8398; Fax: 212-854-7837//g';

find -type f -name '*.html' | xargs sed -i 's/<a href="mailto:klundberg@columbia.edu" style="text-decoration: none; color: rgb(51, 102, 153); ">k<\/a><a href="mailto:Klundberg@columbia.edu" style="text-decoration: none; color: rgb(17, 85, 204); " target="_blank">lundberg@columbia.edu<\/a>//g';
find -type f -name '*.html' | xargs sed -i 's/<a href="mailto:klundberg@columbia.edu">klundberg@columbia.edu<\/a>//g';
find -type f -name '*.html' | xargs sed -i 's/<a href="mailto:kol2101@columbia.edu">kol2101@columbia.edu<\/a>//g';
find -type f -name '*.html' | xargs sed -i 's/<a href="mailto:klundberg@columbia.edu">k<\/a>//g';
find -type f -name '*.html' | xargs sed -i 's/<a href="mailto:Klundberg@columbia.edu" style="text-decoration: none; color: rgb(51, 102, 153);" target="_blank">lundberg@columbia.edu<\/a>//g';
find -type f -name '*.html' | xargs sed -i 's/<a href="mailto:klundberg@columbia.edu" style="text-decoration: none; color: rgb(51, 102, 153);">k<\/a>//g';
find -type f -name '*.html' | xargs sed -i 's/<a href="mailto:Klundberg@columbia.edu" style="color: rgb(17, 85, 204); " target="_blank">lundberg@columbia.edu<\/a>//g';
find -type f -name '*.html' | xargs sed -i 's/<a href="mailto:Klundberg@columbia.edu" style="color: rgb(17, 85, 204);" target="_blank">lundberg@columbia.edu<\/a>//g';
find -type f -name '*.html' | xargs sed -i 's/mailto:klundberg@columbia.edu//g';
find -type f -name '*.html' | xargs sed -i 's/mailto:Klundberg@columbia.edu//g';
find -type f -name '*.html' | xargs sed -i 's/>lundberg@columbia.edu<\/a>/><\/a>/g';
find -type f -name '*.html' | xargs sed -i 's/k<\/a>/<\/a>/g';


find -type f -name '*.html' | xargs sed -i 's/Email:&nbsp;//g';
find -type f -name '*.html' | xargs sed -i 's/Email: <\/div>/<\/div>/g';

find -type f -name '*.html' | xargs sed -i 's/<a href="http:\/\/casestudies.jrn.columbia.edu\/">https:\/\/casestudies.jrn.columbia.edu<\/a>//g';
find -type f -name '*.html' | xargs sed -i 's/Website:&nbsp;<a href="http:\/\/casestudies.jrn.columbia.edu\/" style="text-decoration: none; color: rgb(51, 102, 153); ">https:\/\/casestudies.jrn.columbia.edu<\/a><\/div>//g';
find -type f -name '*.html' | xargs sed -i 's/Website: <a href="https:\/\/casestudies.jrn.columbia.edu">https:\/\/casestudies.jrn.columbia.edu<\/a>//g';
find -type f -name '*.html' | xargs sed -i 's/<a href="http:\/\/casestudies.jrn.columbia.edu" target="_blank"><span class="extlink">http:\/\/casestudies.jrn.columbia.edu<\/span><\/a>//g';
find -type f -name '*.html' | xargs sed -i 's/Website:&nbsp;//g';
