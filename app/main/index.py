# file name : index.py
# pwd : /project_name/app/main/index.py
 
from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app
# 추가할 모듈이 있다면 추가
 
main= Blueprint('main', __name__, url_prefix='/')
 
@main.route('/', methods=['GET'])
def index():
      
      # /main/index.html은 사실 /project_name/app/templates/main/index.html을 가리킵니다.
      return render_template('/main/index.html')


@main.route('/image', methods=['GET'])
def image():
    # /main/index.html은 사실 /project_name/app/templates/main/index.html을 가리킵니다.
    print("image 함수 호출")
    #print(request.form)
    filename = "/static/img/"+request.args.get('filename')
    return render_template('/main/image.html', filename = filename)



