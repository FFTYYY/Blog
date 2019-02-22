import os
import sys

os.chdir(sys.path[0])

def make_ignored_file(path , default_content):
	if os.path.exists(path):
		return
	with open(path , "w" , encoding = "utf-8") as fil:
		fil.write(default_content)


secret_key_path = "../YYYBlog/YYYBlog/setting_secret_key.py"
secret_key_content = '''
SECRET_KEY = '12345678901234567890123456789012345678901234567890'
'''

make_ignored_file(secret_key_path , secret_key_content)

disp_lis_path = "../YYYBlog/Article_Zone/static/Article_Zone/display_list.py"
disp_lis_content = '''
不可视的节点列表 = {
	("我本人") : [
	] , 

	("访客") : [
		"article_one" , 
	] , 

}
'''

make_ignored_file(disp_lis_path , disp_lis_content)