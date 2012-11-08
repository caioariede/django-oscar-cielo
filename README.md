**django-oscar-cielo**

Cielo (brazilian payment gateway) module for `django-oscar`

https://github.com/tangentlabs/django-oscar

**Requirements**

* https://github.com/rpedigoni/python-cielo

**Installation**

`pip install git+http://github.com/caioariede/django-oscar-cielo.git#egg=oscar_cielo`

Or manually place it on your `PYTHON_PATH`.

**Configuration**

1. Install and configure `django-oscar`
2. Create an application. This is need to put your customizations on.
3. Copy all files under `example/` to your custom application's folder
4. In your settings file, change the call to `get_oscar_apps` to:

````python
OSCAR_APP_MODS = ('your_custom_app.apps.checkout',)
INSTALLED_APPS += tuple(get_oscar_apps(OSCAR_APP_MODS))
````

**Settings**

*Descriptions are in portuguese*

* `OSCAR_CIELO_NUMERO` - Número de afiliação junto à Cielo (Default: `''`)
* `OSCAR_CIELO_CHAVE` - Chave de acesso (Default: `''`)
* `OSCAR_CIELO_SANDBOX` - Ambiente de desenvolvimento (Default: `True`)
* `OSCAR_CIELO_PROCESSED_STATUS` - Estado do pedido após a captura (Default: `'Processado'`)

**MIT License**

<pre>Copyright (c) 2012 Caio Ariede.

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.</pre>
