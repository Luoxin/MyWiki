#  Flask入门基础

### 第一个flask程序以及部分说明

```python
# 从flask这个框架中导入Flask这个类
from flask import Flask

# 初始化一个Flask对象
# Flaks()
# 需要传递一个参数__name__
# 1. 方便flask框架去寻找资源
# 2. 方便flask插件比如Flask-Sqlalchemy出现错误的时候，好去寻找问题所在的位置
app = Flask(__name__)


# @app.route是一个装饰器
# @开头，并且在函数的上面，说明是装饰器
# 这个装饰器的作用，是做一个url与视图函数的映射
# 127.0.0.1:5000/   ->  去请求hello_world这个函数，然后将结果返回给浏览器
@app.route('/')
def hello_world():
    return '我是第一个flask程序'


# 如果当前这个文件是作为入口程序运行，那么就执行app.run()
if __name__ == '__main__':
    # app.run()
    # 启动一个应用服务器，来接受用户的请求
    # while True:
    #   listen()
    app.run()
```

- debug模式

	- app.run(debug=True)

- 配置文件

	- 在主文件中导入包

	- ```python
		app.config.from_object()
		```

### URL与视图

- URL传参

  - ```python
      @app.route('/article/<id>')
      def article(id):
          return'您请求的参数是：%s' % id
      ```

- URL反转

  - ```python
    @app.route('/')
    def index():
    	print url_for('my_list')
    	print url_for('article',id='123')
    	return 'Hello World!'
    
    @app.route('/list/')
    def my_list():
        return 'list'
        
    @app.route('/article/<id>/')
    def article(id):
        return '您请求的id是：%s' % id
    ```

- 页面跳转重定向

  - ```python
    @app.route('/')
    def index():
        login_url = url_for('login')
        return redirect(login_url)  # 页面跳转
    
    @app.route('/login/')
    def login():
        return '这是登录页面'
    
    @app.route('/question/<is_login>/')
    def question(is_login):
        if is_login == '1':
            return '这是发布问答页面'
        else:
            return redirect(url_for('login'))
    
    ```


### Jinjia2模版

- 模版渲染与参数
       - Python代码
            ```Python
                
            ```

    ```python
        @app.route('/')
        def index():
            class Person(object):
                name = u'黄勇'
                age = 18
        
            p = Person()
            context = {
                'username': '知了课堂',
                'gender': '男',
                'age': 18,
                'person': p,
                'websites': {
                'baidu': 'www.baidu.com',
                'google': 'www.google.com'
                }
            }
            return render_template('anthoer/index.html',**context)
    ```

    - HTML代码
        ```jinja2
        <body>
            这是HTML文件中出现的文字
            <p>用户名：{{ username }}</p>
            <p>性别：{{ gender }}</p>
            <p>年龄：{{ age }}</p>

            <hr>
            <p>名字：{{ person['name'] }}</p>
            <p>年龄：{{ person.age }}</p>

            <hr>
            <p>百度：{{ websites.baidu }}</p>
            <p>谷歌：{{ websites['google'] }}</p>
        </body>
        ```

    - 在模板中，如果要使用一个变量，语法是：`{{params}}`

    - 访问模型中的属性或者是字典，可以通过`{{params.property}}`的形式，或者是使用`{{params['age']}}`

- if语句

    - ```jinja2
      <body>
          {% if user and user.age > 18 %}
              <a href="#">{{ user.username }}</a>
              <a href="#">注销</a>
          {% else %}
              <a href="#">登录</a>
              <a href="#">注册</a>
          {% endif %}
      </body>
      ```

    - 和Python中的if用法相似

- for循环遍历

    - HTML代码

        ```jinja2
        <body>
        <table>
            <thead>
                <th>书名</th>
                <th>作者</th>
                <th>价格</th>
            </thead>
            <tbody>
                {% for book in books %}
                    <tr>
                        <td>{{ book.name }}</td>
                        <td>{{ book.author }}</td>
                        <td>{{ book.price }}</td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
        ```

        

    - Python代码

      ```python
      @app.route('/')
      def index():
          books = [
              {
                  'name': u'西游记',
                  'author': u'吴承恩',
                  'price': 109
              },
              {
                  'name': u'红楼梦',
                  'author': u'曹雪芹',
                  'price': 200
              },
              {
                  'name': u'三国演义',
                  'author': u'罗贯中',
                  'price': 120
              },
              {
                  'name': u'水浒传',
                  'author': u'施耐庵',
                  'price': 130
              }
          ]
          return render_template('index.html',books=books)
      ```

- 过滤器

    - ```mermaid
        graph LR
        作用在模版当中的变量--过滤器--> 过滤后的值
        ```

    - default过滤器：如果当前变量不存在，这时候可以指定默认值。

       ```jinja2
         {{ avatar|default('xxx') }}
       ```

    - length过滤器：求列表或者字符串或者字典或者元组的长度。

    - 示例代码

       ```jinja2
       <body>
           <img src="{{ avatar|default('http://avatar.csdn.net/1/D/B/3_hmzkekek41.jpg') }}" alt="">
           <hr>
           <p>评论数：({{ comments|length }})</p>
           <ul>
               {% for comment in comments %}
                   <li>
                       <a href="#">{{ comment.user }}</a>
                       <p>{{ comment.content }}</p>
                   </li>
               {% endfor %}
           </ul>
       </body>
       ```

       - 常用的过滤器：
          ```
              abs(value)：返回一个数值的绝对值。示例：-1|abs
              default(value,default_value,boolean=false)：如果当前变量没有值，则会使用参数中的值来代替。示例：name|default('xiaotuo')——如果name不存在，则会使用xiaotuo来替代。boolean=False默认是在只有这个变量为undefined的时候才会使用default中的值，如果想使用python的形式判断是否为false，则可以传递boolean=true。也可以使用or来替换。
              escape(value)或e：转义字符，会将<、>等符号转义成HTML中的符号。示例：content|escape或content|e。
              first(value)：返回一个序列的第一个元素。示例：names|first
              format(value,*arags,**kwargs)：格式化字符串。比如：
          
                {{ "%s" - "%s"|format('Hello?',"Foo!") }}
                将输出：Helloo? - Foo!
              last(value)：返回一个序列的最后一个元素。示例：names|last。
              
              length(value)：返回一个序列或者字典的长度。示例：names|length。
              join(value,d=u'')：将一个序列用d这个参数的值拼接成字符串。
              safe(value)：如果开启了全局转义，那么safe过滤器会将变量关掉转义。示例：content_html|safe。
              int(value)：将值转换为int类型。
              float(value)：将值转换为float类型。
              lower(value)：将字符串转换为小写。
              upper(value)：将字符串转换为小写。
              replace(value,old,new)： 替换将old替换为new的字符串。
              truncate(value,length=255,killwords=False)：截取length长度的字符串。
              striptags(value)：删除字符串中所有的HTML标签，如果出现多个空格，将替换成一个空格。
              trim：截取字符串前面和后面的空白字符。
              string(value)：将变量转换成字符串。
              wordcount(s)：计算一个长字符串中单词的个数。
          ```

    






- 笔记
	- `{% %}`中添加条件、循环等
	- `{{  }}`中添加值
