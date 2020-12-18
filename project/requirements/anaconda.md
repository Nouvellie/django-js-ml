# ANACONDA
## Anaconda (python distribution platform, As SUDO!!)

```sh
$ curl -O https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh
$ sudo bash ./Anaconda3-2020.11-Linux-x86_64.sh
```

<kbd>ENTER</kbd><br>

```sh
yes
```

#### Path:

```sh
/opt/anaconda3
```

#### Do you wish the installer to initialize Anaconda3:

```sh
yes # (Important)
```

#### Conda update:

Reset the terminal first.

```sh
$ conda update -n base -c defaults conda -y
```

#### To access Conda commands with any user, edit environment:

```sh
$ sudo vim /etc/environment
```

#### [environmnet]

```sh
PATH=/opt/anaconda3/bin:$PATH
```

Restart PC.

#### Create an env with some libs: (python 3.8)

```sh
$ conda create -n <envname> mysqlclient python==3.8 -y
$ source activate <envname>
$ pip install appdirs bokeh boto boto3 cython django django-allauth django-cors-headers django-filter django-rest-auth djangorestframework djangorestframework_simplejwt dtw==1.3.3 ec2-metadata gensim gunicorn imgaug ipykernel jupyter_console jupyter_contrib_nbextensions jupyter-themer jupyter_dashboards jupyter_full_width jupyterhub jupyterlab keras marshmallow matplotlib mysql-connector-python nltk numpy opencv-python openpyxl pandas pdf2image pypng regex scipy stop-words symspellpy tensorflow==2.4.0rc4 tqdm wazeroutecalculator wfdb xlrd xlwt
```