from bs4 import BeautifulSoup
import pdb

def write_html_file(html):
    out_file = open("../public/case/index_new.html", "w")
    out_file.write(html.prettify("utf-8"))
    out_file.close()

def export_js(script):
    ext = '.' + script.attrs['data-file-extension']
    directory = "../static/js/api/"
    out_filename = script.attrs['id'] + ext
    out_file = open(directory + out_filename, "w")
    out_file.write(script.string.encode('utf-8'))
    out_file.close()
    return out_filename

def main():
    bs_file = open("../public/case/index.html")
    html = BeautifulSoup(bs_file) 
    html_out = html
    for script in html.find_all('script'):
        try:
            if script.attrs['data-export'] == "true":
                jsfile = export_js(script)
                
                script_source = BeautifulSoup('<script></script>')
                #pdb.set_trace()
                script_tag = script_source.new_tag('script', src='/js/'+jsfile)
                html_out.find('footer').insert_after(script_tag)
                
                html_out.find('script', {'data-export':"true"}).decompose()
                print len(html_out.find_all('script', {'data-export':"true"}))
                
        except:
            pass

    bs_file.close
    write_html_file(html_out)

if __name__ == "__main__":
    main()