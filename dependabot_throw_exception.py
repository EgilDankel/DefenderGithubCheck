[[package]]
name = "alabaster"
version = "0.7.12"
description = "A configurable sidebar-enabled Sphinx theme"
category = "main"
optional = false
python-versions = "*"

[[package]]
name = "atomicwrites"
version = "1.4.0"
description = "Atomic file writes."
category = "dev"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*"

[[package]]
name = "attrs"
version = "21.2.0"
description = "Classes Without Boilerplate"
category = "dev"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*"

[package.extras]
dev = ["coverage[toml] (>=5.0.2)", "hypothesis", "pympler", "pytest (>=4.3.0)", "six", "mypy", "pytest-mypy-plugins", "zope.interface", "furo", "sphinx", "sphinx-notfound-page", "pre-commit"]
docs = ["furo", "sphinx", "zope.interface", "sphinx-notfound-page"]
tests = ["coverage[toml] (>=5.0.2)", "hypothesis", "pympler", "pytest (>=4.3.0)", "six", "mypy", "pytest-mypy-plugins", "zope.interface"]
tests_no_zope = ["coverage[toml] (>=5.0.2)", "hypothesis", "pympler", "pytest (>=4.3.0)", "six", "mypy", "pytest-mypy-plugins"]

[[package]]
name = "babel"
version = "2.9.1"
description = "Internationalization utilities"
category = "main"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*"

[package.dependencies]
pytz = ">=2015.7"

[[package]]
name = "black"
version = "21.11b1"
description = "The uncompromising code formatter."
category = "dev"
optional = false
python-versions = ">=3.6.2"

[package.dependencies]
click = ">=7.1.2"
mypy-extensions = ">=0.4.3"
pathspec = ">=0.9.0,<1"
platformdirs = ">=2"
regex = ">=2021.4.4"
tomli = ">=0.2.6,<2.0.0"
typed-ast = {version = ">=1.4.2", markers = "python_version < \"3.8\" and implementation_name == \"cpython\""}
typing-extensions = ">=3.10.0.0"

[package.extras]
colorama = ["colorama (>=0.4.3)"]
d = ["aiohttp (>=3.7.4)"]
jupyter = ["ipython (>=7.8.0)", "tokenize-rt (>=3.2.0)"]
python2 = ["typed-ast (>=1.4.3)"]
uvloop = ["uvloop (>=0.15.2)"]

[[package]]
name = "certifi"
version = "2021.10.8"
description = "Python package for providing Mozilla's CA Bundle."
category = "main"
optional = false
python-versions = "*"

[[package]]
name = "charset-normalizer"
version = "2.0.8"
description = "The Real First Universal Charset Detector. Open, modern and actively maintained alternative to Chardet."
category = "main"
optional = false
python-versions = ">=3.5.0"

[package.extras]
unicode_backport = ["unicodedata2"]

[[package]]
name = "click"
version = "8.0.3"
description = "Composable command line interface toolkit"
category = "dev"
optional = false
python-versions = ">=3.6"

[package.dependencies]
colorama = {version = "*", markers = "platform_system == \"Windows\""}
importlib-metadata = {version = "*", markers = "python_version < \"3.8\""}

[[package]]
name = "colorama"
version = "0.4.4"
description = "Cross-platform colored terminal text."
category = "main"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*"

[[package]]
name = "docutils"
version = "0.17.1"
description = "Docutils -- Python Documentation Utilities"
category = "main"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*"

[[package]]
name = "flake8"
version = "4.0.1"
description = "the modular source code checker: pep8 pyflakes and co"
category = "dev"
optional = false
python-versions = ">=3.6"

[package.dependencies]
importlib-metadata = {version = "<4.3", markers = "python_version < \"3.8\""}
mccabe = ">=0.6.0,<0.7.0"
pycodestyle = ">=2.8.0,<2.9.0"
pyflakes = ">=2.4.0,<2.5.0"

[[package]]
name = "idna"
version = "3.3"
description = "Internationalized Domain Names in Applications (IDNA)"
category = "main"
optional = false
python-versions = ">=3.5"

[[package]]
name = "imagesize"
version = "1.3.0"
description = "Getting image size from png/jpeg/jpeg2000/gif file"
category = "main"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*"

[[package]]
name = "importlib-metadata"
version = "4.2.0"
description = "Read metadata from Python packages"
category = "dev"
optional = false
python-versions = ">=3.6"

[package.dependencies]
typing-extensions = {version = ">=3.6.4", markers = "python_version < \"3.8\""}
zipp = ">=0.5"

[package.extras]
docs = ["sphinx", "jaraco.packaging (>=8.2)", "rst.linker (>=1.9)"]
testing = ["pytest (>=4.6)", "pytest-checkdocs (>=2.4)", "pytest-flake8", "pytest-cov", "pytest-enabler (>=1.0.1)", "packaging", "pep517", "pyfakefs", "flufl.flake8", "pytest-black (>=0.3.7)", "pytest-mypy", "importlib-resources (>=1.3)"]

[[package]]
name = "iniconfig"
version = "1.1.1"
description = "iniconfig: brain-dead simple config-ini parsing"
category = "dev"
optional = false
python-versions = "*"

[[package]]
name = "isort"
version = "5.10.1"
description = "A Python utility / library to sort Python imports."
category = "dev"
optional = false
python-versions = ">=3.6.1,<4.0"

[package.extras]
pipfile_deprecated_finder = ["pipreqs", "requirementslib"]
requirements_deprecated_finder = ["pipreqs", "pip-api"]
colors = ["colorama (>=0.4.3,<0.5.0)"]
plugins = ["setuptools"]

[[package]]
name = "jinja2"
version = "3.0.3"
description = "A very fast and expressive template engine."
category = "main"
optional = false
python-versions = ">=3.6"

[package.dependencies]
MarkupSafe = ">=2.0"

[package.extras]
i18n = ["Babel (>=2.7)"]

[[package]]
name = "markupsafe"
version = "2.0.1"
description = "Safely add untrusted strings to HTML/XML markup."
category = "main"
optional = false
python-versions = ">=3.6"

[[package]]
name = "mccabe"
version = "0.6.1"
description = "McCabe checker, plugin for flake8"
category = "dev"
optional = false
python-versions = "*"

[[package]]
name = "mypy"
version = "0.910"
description = "Optional static typing for Python"
category = "dev"
optional = false
python-versions = ">=3.5"

[package.dependencies]
mypy-extensions = ">=0.4.3,<0.5.0"
toml = "*"
typed-ast = {version = ">=1.4.0,<1.5.0", markers = "python_version < \"3.8\""}
typing-extensions = ">=3.7.4"

[package.extras]
dmypy = ["psutil (>=4.0)"]
python2 = ["typed-ast (>=1.4.0,<1.5.0)"]

[[package]]
name = "mypy-extensions"
version = "0.4.3"
description = "Experimental type system extensions for programs checked with the mypy typechecker."
category = "dev"
optional = false
python-versions = "*"

[[package]]
name = "packaging"
version = "21.3"
description = "Core utilities for Python packages"
category = "main"
optional = false
python-versions = ">=3.6"

[package.dependencies]
pyparsing = ">=2.0.2,<3.0.5 || >3.0.5"

[[package]]
name = "pathspec"
version = "0.9.0"
description = "Utility library for gitignore style pattern matching of file paths."
category = "dev"
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,>=2.7"

[[package]]
name = "platformdirs"
version = "2.4.0"
description = "A small Python module for determining appropriate platform-specific dirs, e.g. a \"user data dir\"."
category = "dev"
optional = false
python-versions = ">=3.6"

[package.extras]
docs = ["Sphinx (>=4)", "furo (>=2021.7.5b38)", "proselint (>=0.10.2)", "sphinx-autodoc-typehints (>=1.12)"]
test = ["appdirs (==1.4.4)", "pytest (>=6)", "pytest-cov (>=2.7)", "pytest-mock (>=3.6)"]

[[package]]
name = "pluggy"
version = "1.0.0"
description = "plugin and hook calling mechanisms for python"
category = "dev"
optional = false
python-versions = ">=3.6"

[package.dependencies]
importlib-metadata = {version = ">=0.12", markers = "python_version < \"3.8\""}

[package.extras]
dev = ["pre-commit", "tox"]
testing = ["pytest", "pytest-benchmark"]

[[package]]
name = "py"
version = "1.11.0"
description = "library with cross-python path, ini-parsing, io, code, log facilities"
category = "dev"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*"

[[package]]
name = "pycodestyle"
version = "2.8.0"
description = "Python style guide checker"
category = "dev"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*"

[[package]]
name = "pyflakes"
version = "2.4.0"
description = "passive checker of Python programs"
category = "dev"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*"

[[package]]
name = "pygments"
version = "2.10.0"
description = "Pygments is a syntax highlighting package written in Python."
category = "main"
optional = false
python-versions = ">=3.5"

[[package]]
name = "pyparsing"
version = "3.0.6"
description = "Python parsing module"
category = "main"
optional = false
python-versions = ">=3.6"

[package.extras]
diagrams = ["jinja2", "railroad-diagrams"]

[[package]]
name = "pytest"
version = "6.2.5"
description = "pytest: simple powerful testing with Python"
category = "dev"
optional = false
python-versions = ">=3.6"

[package.dependencies]
atomicwrites = {version = ">=1.0", markers = "sys_platform == \"win32\""}
attrs = ">=19.2.0"
colorama = {version = "*", markers = "sys_platform == \"win32\""}
importlib-metadata = {version = ">=0.12", markers = "python_version < \"3.8\""}
iniconfig = "*"
packaging = "*"
pluggy = ">=0.12,<2.0"
py = ">=1.8.2"
toml = "*"

[package.extras]
testing = ["argcomplete", "hypothesis (>=3.56)", "mock", "nose", "requests", "xmlschema"]

[[package]]
name = "pytz"
version = "2021.3"
description = "World timezone definitions, modern and historical"
category = "main"
optional = false
python-versions = "*"

[[package]]
name = "regex"
version = "2021.11.10"
description = "Alternative regular expression module, to replace re."
category = "dev"
optional = false
python-versions = "*"

[[package]]
name = "requests"
version = "2.26.0"
description = "Python HTTP for Humans."
category = "main"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*"

[package.dependencies]
certifi = ">=2017.4.17"
charset-normalizer = {version = ">=2.0.0,<2.1.0", markers = "python_version >= \"3\""}
idna = {version = ">=2.5,<4", markers = "python_version >= \"3\""}
urllib3 = ">=1.21.1,<1.27"

[package.extras]
socks = ["PySocks (>=1.5.6,!=1.5.7)", "win-inet-pton"]
use_chardet_on_py3 = ["chardet (>=3.0.2,<5)"]

[[package]]
name = "snowballstemmer"
version = "2.2.0"
description = "This package provides 29 stemmers for 28 languages generated from Snowball algorithms."
category = "main"
optional = false
python-versions = "*"

[[package]]
name = "sphinx"
version = "4.3.1"
description = "Python documentation generator"
category = "main"
optional = false
python-versions = ">=3.6"

[package.dependencies]
alabaster = ">=0.7,<0.8"
babel = ">=1.3"
colorama = {version = ">=0.3.5", markers = "sys_platform == \"win32\""}
docutils = ">=0.14,<0.18"
imagesize = "*"
Jinja2 = ">=2.3"
packaging = "*"
Pygments = ">=2.0"
requests = ">=2.5.0"
snowballstemmer = ">=1.1"
sphinxcontrib-applehelp = "*"
sphinxcontrib-devhelp = "*"
sphinxcontrib-htmlhelp = ">=2.0.0"
sphinxcontrib-jsmath = "*"
sphinxcontrib-qthelp = "*"
sphinxcontrib-serializinghtml = ">=1.1.5"

[package.extras]
docs = ["sphinxcontrib-websupport"]
lint = ["flake8 (>=3.5.0)", "isort", "mypy (>=0.900)", "docutils-stubs", "types-typed-ast", "types-pkg-resources", "types-requests"]
test = ["pytest", "pytest-cov", "html5lib", "cython", "typed-ast"]

[[package]]
name = "sphinx-rtd-theme"
version = "1.0.0"
description = "Read the Docs theme for Sphinx"
category = "main"
optional = false
python-versions = ">=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*"

[package.dependencies]
docutils = "<0.18"
sphinx = ">=1.6"

[package.extras]
dev = ["transifex-client", "sphinxcontrib-httpdomain", "bump2version"]

[[package]]
name = "sphinxcontrib-applehelp"
version = "1.0.2"
description = "sphinxcontrib-applehelp is a sphinx extension which outputs Apple help books"
category = "main"
optional = false
python-versions = ">=3.5"

[package.extras]
lint = ["flake8", "mypy", "docutils-stubs"]
test = ["pytest"]

[[package]]
name = "sphinxcontrib-devhelp"
version = "1.0.2"
description = "sphinxcontrib-devhelp is a sphinx extension which outputs Devhelp document."
category = "main"
optional = false
python-versions = ">=3.5"

[package.extras]
lint = ["flake8", "mypy", "docutils-stubs"]
test = ["pytest"]

[[package]]
name = "sphinxcontrib-htmlhelp"
version = "2.0.0"
description = "sphinxcontrib-htmlhelp is a sphinx extension which renders HTML help files"
category = "main"
optional = false
python-versions = ">=3.6"

[package.extras]
lint = ["flake8", "mypy", "docutils-stubs"]
test = ["pytest", "html5lib"]

[[package]]
name = "sphinxcontrib-jsmath"
version = "1.0.1"
description = "A sphinx extension which renders display math in HTML via JavaScript"
category = "main"
optional = false
python-versions = ">=3.5"

[package.extras]
test = ["pytest", "flake8", "mypy"]

[[package]]
name = "sphinxcontrib-qthelp"
version = "1.0.3"
description = "sphinxcontrib-qthelp is a sphinx extension which outputs QtHelp document."
category = "main"
optional = false
python-versions = ">=3.5"

[package.extras]
lint = ["flake8", "mypy", "docutils-stubs"]
test = ["pytest"]

[[package]]
name = "sphinxcontrib-serializinghtml"
version = "1.1.5"
description = "sphinxcontrib-serializinghtml is a sphinx extension which outputs \"serialized\" HTML files (json and pickle)."
category = "main"
optional = false
python-versions = ">=3.5"

[package.extras]
lint = ["flake8", "mypy", "docutils-stubs"]
test = ["pytest"]

[[package]]
name = "toml"
version = "0.10.2"
description = "Python Library for Tom's Obvious, Minimal Language"
category = "dev"
optional = false
python-versions = ">=2.6, !=3.0.*, !=3.1.*, !=3.2.*"

[[package]]
name = "tomli"
version = "1.2.2"
description = "A lil' TOML parser"
category = "dev"
optional = false
python-versions = ">=3.6"

[[package]]
name = "typed-ast"
version = "1.4.3"
description = "a fork of Python 2 and 3 ast modules with type comment support"
category = "dev"
optional = false
python-versions = "*"

[[package]]
name = "typing-extensions"
version = "4.0.1"
description = "Backported and Experimental Type Hints for Python 3.6+"
category = "dev"
optional = false
python-versions = ">=3.6"

[[package]]
name = "urllib3"
version = "1.26.7"
description = "HTTP library with thread-safe connection pooling, file post, and more."
category = "main"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4"

[package.extras]
brotli = ["brotlipy (>=0.6.0)"]
secure = ["pyOpenSSL (>=0.14)", "cryptography (>=1.3.4)", "idna (>=2.0.0)", "certifi", "ipaddress"]
socks = ["PySocks (>=1.5.6,!=1.5.7,<2.0)"]

[[package]]
name = "zipp"
version = "3.6.0"
description = "Backport of pathlib-compatible object wrapper for zip files"
category = "dev"
optional = false
python-versions = ">=3.6"

[package.extras]
docs = ["sphinx", "jaraco.packaging (>=8.2)", "rst.linker (>=1.9)"]
testing = ["pytest (>=4.6)", "pytest-checkdocs (>=2.4)", "pytest-flake8", "pytest-cov", "pytest-enabler (>=1.0.1)", "jaraco.itertools", "func-timeout", "pytest-black (>=0.3.7)", "pytest-mypy"]

[metadata]
lock-version = "1.1"
python-versions = ">=3.7.1,<3.9"
content-hash = "05dfcbd74d7d35651d4c91e736e90c1d5eca60d01e893e2c8bc2e19bd7299560"

[metadata.files]
alabaster = [
    {file = "alabaster-0.7.12-py2.py3-none-any.whl", hash = "sha256:446438bdcca0e05bd45ea2de1668c1d9b032e1a9154c2c259092d77031ddd359"},
    {file = "alabaster-0.7.12.tar.gz", hash = "sha256:a661d72d58e6ea8a57f7a86e37d86716863ee5e92788398526d58b26a4e4dc02"},
]
atomicwrites = [
    {file = "atomicwrites-1.4.0-py2.py3-none-any.whl", hash = "sha256:6d1784dea7c0c8d4a5172b6c620f40b6e4cbfdf96d783691f2e1302a7b88e197"},
    {file = "atomicwrites-1.4.0.tar.gz", hash = "sha256:ae70396ad1a434f9c7046fd2dd196fc04b12f9e91ffb859164193be8b6168a7a"},
]
attrs = [
    {file = "attrs-21.2.0-py2.py3-none-any.whl", hash = "sha256:149e90d6d8ac20db7a955ad60cf0e6881a3f20d37096140088356da6c716b0b1"},
    {file = "attrs-21.2.0.tar.gz", hash = "sha256:ef6aaac3ca6cd92904cdd0d83f629a15f18053ec84e6432106f7a4d04ae4f5fb"},
]
babel = [
    {file = "Babel-2.9.1-py2.py3-none-any.whl", hash = "sha256:ab49e12b91d937cd11f0b67cb259a57ab4ad2b59ac7a3b41d6c06c0ac5b0def9"},
    {file = "Babel-2.9.1.tar.gz", hash = "sha256:bc0c176f9f6a994582230df350aa6e05ba2ebe4b3ac317eab29d9be5d2768da0"},
]
black = [
    {file = "black-21.11b1-py3-none-any.whl", hash = "sha256:802c6c30b637b28645b7fde282ed2569c0cd777dbe493a41b6a03c1d903f99ac"},
    {file = "black-21.11b1.tar.gz", hash = "sha256:a042adbb18b3262faad5aff4e834ff186bb893f95ba3a8013f09de1e5569def2"},
]
certifi = [
    {file = "certifi-2021.10.8-py2.py3-none-any.whl", hash = "sha256:d62a0163eb4c2344ac042ab2bdf75399a71a2d8c7d47eac2e2ee91b9d6339569"},
    {file = "certifi-2021.10.8.tar.gz", hash = "sha256:78884e7c1d4b00ce3cea67b44566851c4343c120abd683433ce934a68ea58872"},
]
charset-normalizer = [
    {file = "charset-normalizer-2.0.8.tar.gz", hash = "sha256:735e240d9a8506778cd7a453d97e817e536bb1fc29f4f6961ce297b9c7a917b0"},
    {file = "charset_normalizer-2.0.8-py3-none-any.whl", hash = "sha256:83fcdeb225499d6344c8f7f34684c2981270beacc32ede2e669e94f7fa544405"},
]
click = [
    {file = "click-8.0.3-py3-none-any.whl", hash = "sha256:353f466495adaeb40b6b5f592f9f91cb22372351c84caeb068132442a4518ef3"},
    {file = "click-8.0.3.tar.gz", hash = "sha256:410e932b050f5eed773c4cda94de75971c89cdb3155a72a0831139a79e5ecb5b"},
]
colorama = [
    {file = "colorama-0.4.4-py2.py3-none-any.whl", hash = "sha256:9f47eda37229f68eee03b24b9748937c7dc3868f906e8ba69fbcbdd3bc5dc3e2"},
    {file = "colorama-0.4.4.tar.gz", hash = "sha256:5941b2b48a20143d2267e95b1c2a7603ce057ee39fd88e7329b0c292aa16869b"},
]
docutils = [
    {file = "docutils-0.17.1-py2.py3-none-any.whl", hash = "sha256:cf316c8370a737a022b72b56874f6602acf974a37a9fba42ec2876387549fc61"},
    {file = "docutils-0.17.1.tar.gz", hash = "sha256:686577d2e4c32380bb50cbb22f575ed742d58168cee37e99117a854bcd88f125"},
]
flake8 = [
    {file = "flake8-4.0.1-py2.py3-none-any.whl", hash = "sha256:479b1304f72536a55948cb40a32dce8bb0ffe3501e26eaf292c7e60eb5e0428d"},
    {file = "flake8-4.0.1.tar.gz", hash = "sha256:806e034dda44114815e23c16ef92f95c91e4c71100ff52813adf7132a6ad870d"},
]
idna = [
    {file = "idna-3.3-py3-none-any.whl", hash = "sha256:84d9dd047ffa80596e0f246e2eab0b391788b0503584e8945f2368256d2735ff"},
    {file = "idna-3.3.tar.gz", hash = "sha256:9d643ff0a55b762d5cdb124b8eaa99c66322e2157b69160bc32796e824360e6d"},
]
imagesize = [
    {file = "imagesize-1.3.0-py2.py3-none-any.whl", hash = "sha256:1db2f82529e53c3e929e8926a1fa9235aa82d0bd0c580359c67ec31b2fddaa8c"},
    {file = "imagesize-1.3.0.tar.gz", hash = "sha256:cd1750d452385ca327479d45b64d9c7729ecf0b3969a58148298c77092261f9d"},
]
importlib-metadata = [
    {file = "importlib_metadata-4.2.0-py3-none-any.whl", hash = "sha256:057e92c15bc8d9e8109738a48db0ccb31b4d9d5cfbee5a8670879a30be66304b"},
    {file = "importlib_metadata-4.2.0.tar.gz", hash = "sha256:b7e52a1f8dec14a75ea73e0891f3060099ca1d8e6a462a4dff11c3e119ea1b31"},
]
iniconfig = [
    {file = "iniconfig-1.1.1-py2.py3-none-any.whl", hash = "sha256:011e24c64b7f47f6ebd835bb12a743f2fbe9a26d4cecaa7f53bc4f35ee9da8b3"},
    {file = "iniconfig-1.1.1.tar.gz", hash = "sha256:bc3af051d7d14b2ee5ef9969666def0cd1a000e121eaea580d4a313df4b37f32"},
]
isort = [
    {file = "isort-5.10.1-py3-none-any.whl", hash = "sha256:6f62d78e2f89b4500b080fe3a81690850cd254227f27f75c3a0c491a1f351ba7"},
    {file = "isort-5.10.1.tar.gz", hash = "sha256:e8443a5e7a020e9d7f97f1d7d9cd17c88bcb3bc7e218bf9cf5095fe550be2951"},
]
jinja2 = [
    {file = "Jinja2-3.0.3-py3-none-any.whl", hash = "sha256:077ce6014f7b40d03b47d1f1ca4b0fc8328a692bd284016f806ed0eaca390ad8"},
    {file = "Jinja2-3.0.3.tar.gz", hash = "sha256:611bb273cd68f3b993fabdc4064fc858c5b47a973cb5aa7999ec1ba405c87cd7"},
]
markupsafe = [
    {file = "MarkupSafe-2.0.1-cp36-cp36m-macosx_10_9_x86_64.whl", hash = "sha256:f9081981fe268bd86831e5c75f7de206ef275defcb82bc70740ae6dc507aee51"},
    {file = "MarkupSafe-2.0.1-cp36-cp36m-manylinux1_i686.whl", hash = "sha256:0955295dd5eec6cb6cc2fe1698f4c6d84af2e92de33fbcac4111913cd100a6ff"},
    {file = "MarkupSafe-2.0.1-cp36-cp36m-manylinux1_x86_64.whl", hash = "sha256:0446679737af14f45767963a1a9ef7620189912317d095f2d9ffa183a4d25d2b"},
    {file = "MarkupSafe-2.0.1-cp36-cp36m-manylinux2010_i686.whl", hash = "sha256:f826e31d18b516f653fe296d967d700fddad5901ae07c622bb3705955e1faa94"},
    {file = "MarkupSafe-2.0.1-cp36-cp36m-manylinux2010_x86_64.whl", hash = "sha256:fa130dd50c57d53368c9d59395cb5526eda596d3ffe36666cd81a44d56e48872"},
    {file = "MarkupSafe-2.0.1-cp36-cp36m-manylinux2014_aarch64.whl", hash = "sha256:905fec760bd2fa1388bb5b489ee8ee5f7291d692638ea5f67982d968366bef9f"},
    {file = "MarkupSafe-2.0.1-cp36-cp36m-win32.whl", hash = "sha256:6c4ca60fa24e85fe25b912b01e62cb969d69a23a5d5867682dd3e80b5b02581d"},
    {file = "MarkupSafe-2.0.1-cp36-cp36m-win_amd64.whl", hash = "sha256:b2f4bf27480f5e5e8ce285a8c8fd176c0b03e93dcc6646477d4630e83440c6a9"},
    {file = "MarkupSafe-2.0.1-cp37-cp37m-macosx_10_9_x86_64.whl", hash = "sha256:0717a7390a68be14b8c793ba258e075c6f4ca819f15edfc2a3a027c823718567"},
    {file = "MarkupSafe-2.0.1-cp37-cp37m-manylinux1_i686.whl", hash = "sha256:6557b31b5e2c9ddf0de32a691f2312a32f77cd7681d8af66c2692efdbef84c18"},
    {file = "MarkupSafe-2.0.1-cp37-cp37m-manylinux1_x86_64.whl", hash = "sha256:49e3ceeabbfb9d66c3aef5af3a60cc43b85c33df25ce03d0031a608b0a8b2e3f"},
    {file = "MarkupSafe-2.0.1-cp37-cp37m-manylinux2010_i686.whl", hash = "sha256:d7f9850398e85aba693bb640262d3611788b1f29a79f0c93c565694658f4071f"},
    {file = "MarkupSafe-2.0.1-cp37-cp37m-manylinux2010_x86_64.whl", hash = "sha256:6a7fae0dd14cf60ad5ff42baa2e95727c3d81ded453457771d02b7d2b3f9c0c2"},
    {file = "MarkupSafe-2.0.1-cp37-cp37m-manylinux2014_aarch64.whl", hash = "sha256:b7f2d075102dc8c794cbde1947378051c4e5180d52d276987b8d28a3bd58c17d"},
    {file = "MarkupSafe-2.0.1-cp37-cp37m-win32.whl", hash = "sha256:a30e67a65b53ea0a5e62fe23682cfe22712e01f453b95233b25502f7c61cb415"},
    {file = "MarkupSafe-2.0.1-cp37-cp37m-win_amd64.whl", hash = "sha256:611d1ad9a4288cf3e3c16014564df047fe08410e628f89805e475368bd304914"},
    {file = "MarkupSafe-2.0.1-cp38-cp38-macosx_10_9_x86_64.whl", hash = "sha256:be98f628055368795d818ebf93da628541e10b75b41c559fdf36d104c5787066"},
    {file = "MarkupSafe-2.0.1-cp38-cp38-manylinux1_i686.whl", hash = "sha256:1d609f577dc6e1aa17d746f8bd3c31aa4d258f4070d61b2aa5c4166c1539de35"},
    {file = "MarkupSafe-2.0.1-cp38-cp38-manylinux1_x86_64.whl", hash = "sha256:7d91275b0245b1da4d4cfa07e0faedd5b0812efc15b702576d103293e252af1b"},
    {file = "MarkupSafe-2.0.1-cp38-cp38-manylinux2010_i686.whl", hash = "sha256:01a9b8ea66f1658938f65b93a85ebe8bc016e6769611be228d797c9d998dd298"},
    {file = "MarkupSafe-2.0.1-cp38-cp38-manylinux2010_x86_64.whl", hash = "sha256:47ab1e7b91c098ab893b828deafa1203de86d0bc6ab587b160f78fe6c4011f75"},
    {file = "MarkupSafe-2.0.1-cp38-cp38-manylinux2014_aarch64.whl", hash = "sha256:97383d78eb34da7e1fa37dd273c20ad4320929af65d156e35a5e2d89566d9dfb"},
    {file = "MarkupSafe-2.0.1-cp38-cp38-win32.whl", hash = "sha256:023cb26ec21ece8dc3907c0e8320058b2e0cb3c55cf9564da612bc325bed5e64"},
    {file = "MarkupSafe-2.0.1-cp38-cp38-win_amd64.whl", hash = "sha256:984d76483eb32f1bcb536dc27e4ad56bba4baa70be32fa87152832cdd9db0833"},
    {file = "MarkupSafe-2.0.1-cp39-cp39-macosx_10_9_universal2.whl", hash = "sha256:2ef54abee730b502252bcdf31b10dacb0a416229b72c18b19e24a4509f273d26"},
    {file = "MarkupSafe-2.0.1-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:3c112550557578c26af18a1ccc9e090bfe03832ae994343cfdacd287db6a6ae7"},
    {file = "MarkupSafe-2.0.1-cp39-cp39-manylinux1_i686.whl", hash = "sha256:53edb4da6925ad13c07b6d26c2a852bd81e364f95301c66e930ab2aef5b5ddd8"},
    {file = "MarkupSafe-2.0.1-cp39-cp39-manylinux1_x86_64.whl", hash = "sha256:f5653a225f31e113b152e56f154ccbe59eeb1c7487b39b9d9f9cdb58e6c79dc5"},
    {file = "MarkupSafe-2.0.1-cp39-cp39-manylinux2010_i686.whl", hash = "sha256:4efca8f86c54b22348a5467704e3fec767b2db12fc39c6d963168ab1d3fc9135"},
    {file = "MarkupSafe-2.0.1-cp39-cp39-manylinux2010_x86_64.whl", hash = "sha256:ab3ef638ace319fa26553db0624c4699e31a28bb2a835c5faca8f8acf6a5a902"},
    {file = "MarkupSafe-2.0.1-cp39-cp39-manylinux2014_aarch64.whl", hash = "sha256:f8ba0e8349a38d3001fae7eadded3f6606f0da5d748ee53cc1dab1d6527b9509"},
    {file = "MarkupSafe-2.0.1-cp39-cp39-win32.whl", hash = "sha256:10f82115e21dc0dfec9ab5c0223652f7197feb168c940f3ef61563fc2d6beb74"},
    {file = "MarkupSafe-2.0.1-cp39-cp39-win_amd64.whl", hash = "sha256:693ce3f9e70a6cf7d2fb9e6c9d8b204b6b39897a2c4a1aa65728d5ac97dcc1d8"},
    {file = "MarkupSafe-2.0.1.tar.gz", hash = "sha256:594c67807fb16238b30c44bdf74f36c02cdf22d1c8cda91ef8a0ed8dabf5620a"},
]
mccabe = [
    {file = "mccabe-0.6.1-py2.py3-none-any.whl", hash = "sha256:ab8a6258860da4b6677da4bd2fe5dc2c659cff31b3ee4f7f5d64e79735b80d42"},
    {file = "mccabe-0.6.1.tar.gz", hash = "sha256:dd8d182285a0fe56bace7f45b5e7d1a6ebcbf524e8f3bd87eb0f125271b8831f"},
]
mypy = [
    {file = "mypy-0.910-cp35-cp35m-macosx_10_9_x86_64.whl", hash = "sha256:a155d80ea6cee511a3694b108c4494a39f42de11ee4e61e72bc424c490e46457"},
    {file = "mypy-0.910-cp35-cp35m-manylinux1_x86_64.whl", hash = "sha256:b94e4b785e304a04ea0828759172a15add27088520dc7e49ceade7834275bedb"},
    {file = "mypy-0.910-cp35-cp35m-manylinux2010_x86_64.whl", hash = "sha256:088cd9c7904b4ad80bec811053272986611b84221835e079be5bcad029e79dd9"},
    {file = "mypy-0.910-cp35-cp35m-win_amd64.whl", hash = "sha256:adaeee09bfde366d2c13fe6093a7df5df83c9a2ba98638c7d76b010694db760e"},
    {file = "mypy-0.910-cp36-cp36m-macosx_10_9_x86_64.whl", hash = "sha256:ecd2c3fe726758037234c93df7e98deb257fd15c24c9180dacf1ef829da5f921"},
    {file = "mypy-0.910-cp36-cp36m-manylinux1_x86_64.whl", hash = "sha256:d9dd839eb0dc1bbe866a288ba3c1afc33a202015d2ad83b31e875b5905a079b6"},
    {file = "mypy-0.910-cp36-cp36m-manylinux2010_x86_64.whl", hash = "sha256:3e382b29f8e0ccf19a2df2b29a167591245df90c0b5a2542249873b5c1d78212"},
    {file = "mypy-0.910-cp36-cp36m-win_amd64.whl", hash = "sha256:53fd2eb27a8ee2892614370896956af2ff61254c275aaee4c230ae771cadd885"},
    {file = "mypy-0.910-cp37-cp37m-macosx_10_9_x86_64.whl", hash = "sha256:b6fb13123aeef4a3abbcfd7e71773ff3ff1526a7d3dc538f3929a49b42be03f0"},
    {file = "mypy-0.910-cp37-cp37m-manylinux1_x86_64.whl", hash = "sha256:e4dab234478e3bd3ce83bac4193b2ecd9cf94e720ddd95ce69840273bf44f6de"},
    {file = "mypy-0.910-cp37-cp37m-manylinux2010_x86_64.whl", hash = "sha256:7df1ead20c81371ccd6091fa3e2878559b5c4d4caadaf1a484cf88d93ca06703"},
    {file = "mypy-0.910-cp37-cp37m-win_amd64.whl", hash = "sha256:0aadfb2d3935988ec3815952e44058a3100499f5be5b28c34ac9d79f002a4a9a"},
    {file = "mypy-0.910-cp38-cp38-macosx_10_9_x86_64.whl", hash = "sha256:ec4e0cd079db280b6bdabdc807047ff3e199f334050db5cbb91ba3e959a67504"},
    {file = "mypy-0.910-cp38-cp38-manylinux1_x86_64.whl", hash = "sha256:119bed3832d961f3a880787bf621634ba042cb8dc850a7429f643508eeac97b9"},
    {file = "mypy-0.910-cp38-cp38-manylinux2010_x86_64.whl", hash = "sha256:866c41f28cee548475f146aa4d39a51cf3b6a84246969f3759cb3e9c742fc072"},
    {file = "mypy-0.910-cp38-cp38-win_amd64.whl", hash = "sha256:ceb6e0a6e27fb364fb3853389607cf7eb3a126ad335790fa1e14ed02fba50811"},
    {file = "mypy-0.910-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:1a85e280d4d217150ce8cb1a6dddffd14e753a4e0c3cf90baabb32cefa41b59e"},
    {file = "mypy-0.910-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:42c266ced41b65ed40a282c575705325fa7991af370036d3f134518336636f5b"},
    {file = "mypy-0.910-cp39-cp39-manylinux1_x86_64.whl", hash = "sha256:3c4b8ca36877fc75339253721f69603a9c7fdb5d4d5a95a1a1b899d8b86a4de2"},
    {file = "mypy-0.910-cp39-cp39-manylinux2010_x86_64.whl", hash = "sha256:c0df2d30ed496a08de5daed2a9ea807d07c21ae0ab23acf541ab88c24b26ab97"},
    {file = "mypy-0.910-cp39-cp39-win_amd64.whl", hash = "sha256:c6c2602dffb74867498f86e6129fd52a2770c48b7cd3ece77ada4fa38f94eba8"},
    {file = "mypy-0.910-py3-none-any.whl", hash = "sha256:ef565033fa5a958e62796867b1df10c40263ea9ded87164d67572834e57a174d"},
    {file = "mypy-0.910.tar.gz", hash = "sha256:704098302473cb31a218f1775a873b376b30b4c18229421e9e9dc8916fd16150"},
]
mypy-extensions = [
    {file = "mypy_extensions-0.4.3-py2.py3-none-any.whl", hash = "sha256:090fedd75945a69ae91ce1303b5824f428daf5a028d2f6ab8a299250a846f15d"},
    {file = "mypy_extensions-0.4.3.tar.gz", hash = "sha256:2d82818f5bb3e369420cb3c4060a7970edba416647068eb4c5343488a6c604a8"},
]
packaging = [
    {file = "packaging-21.3-py3-none-any.whl", hash = "sha256:ef103e05f519cdc783ae24ea4e2e0f508a9c99b2d4969652eed6a2e1ea5bd522"},
    {file = "packaging-21.3.tar.gz", hash = "sha256:dd47c42927d89ab911e606518907cc2d3a1f38bbd026385970643f9c5b8ecfeb"},
]
pathspec = [
    {file = "pathspec-0.9.0-py2.py3-none-any.whl", hash = "sha256:7d15c4ddb0b5c802d161efc417ec1a2558ea2653c2e8ad9c19098201dc1c993a"},
    {file = "pathspec-0.9.0.tar.gz", hash = "sha256:e564499435a2673d586f6b2130bb5b95f04a3ba06f81b8f895b651a3c76aabb1"},
]
platformdirs = [
    {file = "platformdirs-2.4.0-py3-none-any.whl", hash = "sha256:8868bbe3c3c80d42f20156f22e7131d2fb321f5bc86a2a345375c6481a67021d"},
    {file = "platformdirs-2.4.0.tar.gz", hash = "sha256:367a5e80b3d04d2428ffa76d33f124cf11e8fff2acdaa9b43d545f5c7d661ef2"},
]
pluggy = [
    {file = "pluggy-1.0.0-py2.py3-none-any.whl", hash = "sha256:74134bbf457f031a36d68416e1509f34bd5ccc019f0bcc952c7b909d06b37bd3"},
    {file = "pluggy-1.0.0.tar.gz", hash = "sha256:4224373bacce55f955a878bf9cfa763c1e360858e330072059e10bad68531159"},
]
py = [
    {file = "py-1.11.0-py2.py3-none-any.whl", hash = "sha256:607c53218732647dff4acdfcd50cb62615cedf612e72d1724fb1a0cc6405b378"},
    {file = "py-1.11.0.tar.gz", hash = "sha256:51c75c4126074b472f746a24399ad32f6053d1b34b68d2fa41e558e6f4a98719"},
]
pycodestyle = [
    {file = "pycodestyle-2.8.0-py2.py3-none-any.whl", hash = "sha256:720f8b39dde8b293825e7ff02c475f3077124006db4f440dcbc9a20b76548a20"},
    {file = "pycodestyle-2.8.0.tar.gz", hash = "sha256:eddd5847ef438ea1c7870ca7eb78a9d47ce0cdb4851a5523949f2601d0cbbe7f"},
]
pyflakes = [
    {file = "pyflakes-2.4.0-py2.py3-none-any.whl", hash = "sha256:3bb3a3f256f4b7968c9c788781e4ff07dce46bdf12339dcda61053375426ee2e"},
    {file = "pyflakes-2.4.0.tar.gz", hash = "sha256:05a85c2872edf37a4ed30b0cce2f6093e1d0581f8c19d7393122da7e25b2b24c"},
]
pygments = [
    {file = "Pygments-2.10.0-py3-none-any.whl", hash = "sha256:b8e67fe6af78f492b3c4b3e2970c0624cbf08beb1e493b2c99b9fa1b67a20380"},
    {file = "Pygments-2.10.0.tar.gz", hash = "sha256:f398865f7eb6874156579fdf36bc840a03cab64d1cde9e93d68f46a425ec52c6"},
]
pyparsing = [
    {file = "pyparsing-3.0.6-py3-none-any.whl", hash = "sha256:04ff808a5b90911829c55c4e26f75fa5ca8a2f5f36aa3a51f68e27033341d3e4"},
    {file = "pyparsing-3.0.6.tar.gz", hash = "sha256:d9bdec0013ef1eb5a84ab39a3b3868911598afa494f5faa038647101504e2b81"},
]
pytest = [
    {file = "pytest-6.2.5-py3-none-any.whl", hash = "sha256:7310f8d27bc79ced999e760ca304d69f6ba6c6649c0b60fb0e04a4a77cacc134"},
    {file = "pytest-6.2.5.tar.gz", hash = "sha256:131b36680866a76e6781d13f101efb86cf674ebb9762eb70d3082b6f29889e89"},
]
pytz = [
    {file = "pytz-2021.3-py2.py3-none-any.whl", hash = "sha256:3672058bc3453457b622aab7a1c3bfd5ab0bdae451512f6cf25f64ed37f5b87c"},
    {file = "pytz-2021.3.tar.gz", hash = "sha256:acad2d8b20a1af07d4e4c9d2e9285c5ed9104354062f275f3fcd88dcef4f1326"},
]
regex = [
    {file = "regex-2021.11.10-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:9345b6f7ee578bad8e475129ed40123d265464c4cfead6c261fd60fc9de00bcf"},
    {file = "regex-2021.11.10-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:416c5f1a188c91e3eb41e9c8787288e707f7d2ebe66e0a6563af280d9b68478f"},
    {file = "regex-2021.11.10-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e0538c43565ee6e703d3a7c3bdfe4037a5209250e8502c98f20fea6f5fdf2965"},
    {file = "regex-2021.11.10-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:7ee1227cf08b6716c85504aebc49ac827eb88fcc6e51564f010f11a406c0a667"},
    {file = "regex-2021.11.10-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:6650f16365f1924d6014d2ea770bde8555b4a39dc9576abb95e3cd1ff0263b36"},
    {file = "regex-2021.11.10-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:30ab804ea73972049b7a2a5c62d97687d69b5a60a67adca07eb73a0ddbc9e29f"},
    {file = "regex-2021.11.10-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:68a067c11463de2a37157930d8b153005085e42bcb7ad9ca562d77ba7d1404e0"},
    {file = "regex-2021.11.10-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl", hash = "sha256:162abfd74e88001d20cb73ceaffbfe601469923e875caf9118333b1a4aaafdc4"},
    {file = "regex-2021.11.10-cp310-cp310-musllinux_1_1_aarch64.whl", hash = "sha256:b9ed0b1e5e0759d6b7f8e2f143894b2a7f3edd313f38cf44e1e15d360e11749b"},
    {file = "regex-2021.11.10-cp310-cp310-musllinux_1_1_i686.whl", hash = "sha256:473e67837f786404570eae33c3b64a4b9635ae9f00145250851a1292f484c063"},
    {file = "regex-2021.11.10-cp310-cp310-musllinux_1_1_ppc64le.whl", hash = "sha256:2fee3ed82a011184807d2127f1733b4f6b2ff6ec7151d83ef3477f3b96a13d03"},
    {file = "regex-2021.11.10-cp310-cp310-musllinux_1_1_s390x.whl", hash = "sha256:d5fd67df77bab0d3f4ea1d7afca9ef15c2ee35dfb348c7b57ffb9782a6e4db6e"},
    {file = "regex-2021.11.10-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:5d408a642a5484b9b4d11dea15a489ea0928c7e410c7525cd892f4d04f2f617b"},
    {file = "regex-2021.11.10-cp310-cp310-win32.whl", hash = "sha256:98ba568e8ae26beb726aeea2273053c717641933836568c2a0278a84987b2a1a"},
    {file = "regex-2021.11.10-cp310-cp310-win_amd64.whl", hash = "sha256:780b48456a0f0ba4d390e8b5f7c661fdd218934388cde1a974010a965e200e12"},
    {file = "regex-2021.11.10-cp36-cp36m-macosx_10_9_x86_64.whl", hash = "sha256:dba70f30fd81f8ce6d32ddeef37d91c8948e5d5a4c63242d16a2b2df8143aafc"},
    {file = "regex-2021.11.10-cp36-cp36m-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e1f54b9b4b6c53369f40028d2dd07a8c374583417ee6ec0ea304e710a20f80a0"},
    {file = "regex-2021.11.10-cp36-cp36m-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:fbb9dc00e39f3e6c0ef48edee202f9520dafb233e8b51b06b8428cfcb92abd30"},
    {file = "regex-2021.11.10-cp36-cp36m-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:666abff54e474d28ff42756d94544cdfd42e2ee97065857413b72e8a2d6a6345"},
    {file = "regex-2021.11.10-cp36-cp36m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:5537f71b6d646f7f5f340562ec4c77b6e1c915f8baae822ea0b7e46c1f09b733"},
    {file = "regex-2021.11.10-cp36-cp36m-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:ed2e07c6a26ed4bea91b897ee2b0835c21716d9a469a96c3e878dc5f8c55bb23"},
    {file = "regex-2021.11.10-cp36-cp36m-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl", hash = "sha256:ca5f18a75e1256ce07494e245cdb146f5a9267d3c702ebf9b65c7f8bd843431e"},
    {file = "regex-2021.11.10-cp36-cp36m-musllinux_1_1_aarch64.whl", hash = "sha256:74cbeac0451f27d4f50e6e8a8f3a52ca074b5e2da9f7b505c4201a57a8ed6286"},
    {file = "regex-2021.11.10-cp36-cp36m-musllinux_1_1_i686.whl", hash = "sha256:3598893bde43091ee5ca0a6ad20f08a0435e93a69255eeb5f81b85e81e329264"},
    {file = "regex-2021.11.10-cp36-cp36m-musllinux_1_1_ppc64le.whl", hash = "sha256:50a7ddf3d131dc5633dccdb51417e2d1910d25cbcf842115a3a5893509140a3a"},
    {file = "regex-2021.11.10-cp36-cp36m-musllinux_1_1_s390x.whl", hash = "sha256:61600a7ca4bcf78a96a68a27c2ae9389763b5b94b63943d5158f2a377e09d29a"},
    {file = "regex-2021.11.10-cp36-cp36m-musllinux_1_1_x86_64.whl", hash = "sha256:563d5f9354e15e048465061509403f68424fef37d5add3064038c2511c8f5e00"},
    {file = "regex-2021.11.10-cp36-cp36m-win32.whl", hash = "sha256:93a5051fcf5fad72de73b96f07d30bc29665697fb8ecdfbc474f3452c78adcf4"},
    {file = "regex-2021.11.10-cp36-cp36m-win_amd64.whl", hash = "sha256:b483c9d00a565633c87abd0aaf27eb5016de23fed952e054ecc19ce32f6a9e7e"},
    {file = "regex-2021.11.10-cp37-cp37m-macosx_10_9_x86_64.whl", hash = "sha256:fff55f3ce50a3ff63ec8e2a8d3dd924f1941b250b0aac3d3d42b687eeff07a8e"},
    {file = "regex-2021.11.10-cp37-cp37m-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e32d2a2b02ccbef10145df9135751abea1f9f076e67a4e261b05f24b94219e36"},
    {file = "regex-2021.11.10-cp37-cp37m-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:53db2c6be8a2710b359bfd3d3aa17ba38f8aa72a82309a12ae99d3c0c3dcd74d"},
    {file = "regex-2021.11.10-cp37-cp37m-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:2207ae4f64ad3af399e2d30dde66f0b36ae5c3129b52885f1bffc2f05ec505c8"},
    {file = "regex-2021.11.10-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:d5ca078bb666c4a9d1287a379fe617a6dccd18c3e8a7e6c7e1eb8974330c626a"},
    {file = "regex-2021.11.10-cp37-cp37m-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:dd33eb9bdcfbabab3459c9ee651d94c842bc8a05fabc95edf4ee0c15a072495e"},
    {file = "regex-2021.11.10-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl", hash = "sha256:05b7d6d7e64efe309972adab77fc2af8907bb93217ec60aa9fe12a0dad35874f"},
    {file = "regex-2021.11.10-cp37-cp37m-musllinux_1_1_aarch64.whl", hash = "sha256:42b50fa6666b0d50c30a990527127334d6b96dd969011e843e726a64011485da"},
    {file = "regex-2021.11.10-cp37-cp37m-musllinux_1_1_i686.whl", hash = "sha256:6e1d2cc79e8dae442b3fa4a26c5794428b98f81389af90623ffcc650ce9f6732"},
    {file = "regex-2021.11.10-cp37-cp37m-musllinux_1_1_ppc64le.whl", hash = "sha256:0416f7399e918c4b0e074a0f66e5191077ee2ca32a0f99d4c187a62beb47aa05"},
    {file = "regex-2021.11.10-cp37-cp37m-musllinux_1_1_s390x.whl", hash = "sha256:ce298e3d0c65bd03fa65ffcc6db0e2b578e8f626d468db64fdf8457731052942"},
    {file = "regex-2021.11.10-cp37-cp37m-musllinux_1_1_x86_64.whl", hash = "sha256:dc07f021ee80510f3cd3af2cad5b6a3b3a10b057521d9e6aaeb621730d320c5a"},
    {file = "regex-2021.11.10-cp37-cp37m-win32.whl", hash = "sha256:e71255ba42567d34a13c03968736c5d39bb4a97ce98188fafb27ce981115beec"},
    {file = "regex-2021.11.10-cp37-cp37m-win_amd64.whl", hash = "sha256:07856afef5ffcc052e7eccf3213317fbb94e4a5cd8177a2caa69c980657b3cb4"},
    {file = "regex-2021.11.10-cp38-cp38-macosx_10_9_x86_64.whl", hash = "sha256:ba05430e819e58544e840a68b03b28b6d328aff2e41579037e8bab7653b37d83"},
    {file = "regex-2021.11.10-cp38-cp38-macosx_11_0_arm64.whl", hash = "sha256:7f301b11b9d214f83ddaf689181051e7f48905568b0c7017c04c06dfd065e244"},
    {file = "regex-2021.11.10-cp38-cp38-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:4aaa4e0705ef2b73dd8e36eeb4c868f80f8393f5f4d855e94025ce7ad8525f50"},
    {file = "regex-2021.11.10-cp38-cp38-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:788aef3549f1924d5c38263104dae7395bf020a42776d5ec5ea2b0d3d85d6646"},
    {file = "regex-2021.11.10-cp38-cp38-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:f8af619e3be812a2059b212064ea7a640aff0568d972cd1b9e920837469eb3cb"},
    {file = "regex-2021.11.10-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:85bfa6a5413be0ee6c5c4a663668a2cad2cbecdee367630d097d7823041bdeec"},
    {file = "regex-2021.11.10-cp38-cp38-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:f23222527b307970e383433daec128d769ff778d9b29343fb3496472dc20dabe"},
    {file = "regex-2021.11.10-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl", hash = "sha256:da1a90c1ddb7531b1d5ff1e171b4ee61f6345119be7351104b67ff413843fe94"},
    {file = "regex-2021.11.10-cp38-cp38-musllinux_1_1_aarch64.whl", hash = "sha256:f5be7805e53dafe94d295399cfbe5227f39995a997f4fd8539bf3cbdc8f47ca8"},
    {file = "regex-2021.11.10-cp38-cp38-musllinux_1_1_i686.whl", hash = "sha256:a955b747d620a50408b7fdf948e04359d6e762ff8a85f5775d907ceced715129"},
    {file = "regex-2021.11.10-cp38-cp38-musllinux_1_1_ppc64le.whl", hash = "sha256:139a23d1f5d30db2cc6c7fd9c6d6497872a672db22c4ae1910be22d4f4b2068a"},
    {file = "regex-2021.11.10-cp38-cp38-musllinux_1_1_s390x.whl", hash = "sha256:ca49e1ab99593438b204e00f3970e7a5f70d045267051dfa6b5f4304fcfa1dbf"},
    {file = "regex-2021.11.10-cp38-cp38-musllinux_1_1_x86_64.whl", hash = "sha256:96fc32c16ea6d60d3ca7f63397bff5c75c5a562f7db6dec7d412f7c4d2e78ec0"},
    {file = "regex-2021.11.10-cp38-cp38-win32.whl", hash = "sha256:0617383e2fe465732af4509e61648b77cbe3aee68b6ac8c0b6fe934db90be5cc"},
    {file = "regex-2021.11.10-cp38-cp38-win_amd64.whl", hash = "sha256:a3feefd5e95871872673b08636f96b61ebef62971eab044f5124fb4dea39919d"},
    {file = "regex-2021.11.10-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:f7f325be2804246a75a4f45c72d4ce80d2443ab815063cdf70ee8fb2ca59ee1b"},
    {file = "regex-2021.11.10-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:537ca6a3586931b16a85ac38c08cc48f10fc870a5b25e51794c74df843e9966d"},
    {file = "regex-2021.11.10-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:eef2afb0fd1747f33f1ee3e209bce1ed582d1896b240ccc5e2697e3275f037c7"},
    {file = "regex-2021.11.10-cp39-cp39-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:432bd15d40ed835a51617521d60d0125867f7b88acf653e4ed994a1f8e4995dc"},
    {file = "regex-2021.11.10-cp39-cp39-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:b43c2b8a330a490daaef5a47ab114935002b13b3f9dc5da56d5322ff218eeadb"},
    {file = "regex-2021.11.10-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:962b9a917dd7ceacbe5cd424556914cb0d636001e393b43dc886ba31d2a1e449"},
    {file = "regex-2021.11.10-cp39-cp39-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:fa8c626d6441e2d04b6ee703ef2d1e17608ad44c7cb75258c09dd42bacdfc64b"},
    {file = "regex-2021.11.10-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl", hash = "sha256:3c5fb32cc6077abad3bbf0323067636d93307c9fa93e072771cf9a64d1c0f3ef"},
    {file = "regex-2021.11.10-cp39-cp39-musllinux_1_1_aarch64.whl", hash = "sha256:cd410a1cbb2d297c67d8521759ab2ee3f1d66206d2e4328502a487589a2cb21b"},
    {file = "regex-2021.11.10-cp39-cp39-musllinux_1_1_i686.whl", hash = "sha256:e6096b0688e6e14af6a1b10eaad86b4ff17935c49aa774eac7c95a57a4e8c296"},
    {file = "regex-2021.11.10-cp39-cp39-musllinux_1_1_ppc64le.whl", hash = "sha256:529801a0d58809b60b3531ee804d3e3be4b412c94b5d267daa3de7fadef00f49"},
    {file = "regex-2021.11.10-cp39-cp39-musllinux_1_1_s390x.whl", hash = "sha256:0f594b96fe2e0821d026365f72ac7b4f0b487487fb3d4aaf10dd9d97d88a9737"},
    {file = "regex-2021.11.10-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:2409b5c9cef7054dde93a9803156b411b677affc84fca69e908b1cb2c540025d"},
    {file = "regex-2021.11.10-cp39-cp39-win32.whl", hash = "sha256:3b5df18db1fccd66de15aa59c41e4f853b5df7550723d26aa6cb7f40e5d9da5a"},
    {file = "regex-2021.11.10-cp39-cp39-win_amd64.whl", hash = "sha256:83ee89483672b11f8952b158640d0c0ff02dc43d9cb1b70c1564b49abe92ce29"},
    {file = "regex-2021.11.10.tar.gz", hash = "sha256:f341ee2df0999bfdf7a95e448075effe0db212a59387de1a70690e4acb03d4c6"},
]
requests = [
    {file = "requests-2.26.0-py2.py3-none-any.whl", hash = "sha256:6c1246513ecd5ecd4528a0906f910e8f0f9c6b8ec72030dc9fd154dc1a6efd24"},
    {file = "requests-2.26.0.tar.gz", hash = "sha256:b8aa58f8cf793ffd8782d3d8cb19e66ef36f7aba4353eec859e74678b01b07a7"},
]
snowballstemmer = [
    {file = "snowballstemmer-2.2.0-py2.py3-none-any.whl", hash = "sha256:c8e1716e83cc398ae16824e5572ae04e0d9fc2c6b985fb0f900f5f0c96ecba1a"},
    {file = "snowballstemmer-2.2.0.tar.gz", hash = "sha256:09b16deb8547d3412ad7b590689584cd0fe25ec8db3be37788be3810cbf19cb1"},
]
sphinx = [
    {file = "Sphinx-4.3.1-py3-none-any.whl", hash = "sha256:048dac56039a5713f47a554589dc98a442b39226a2b9ed7f82797fcb2fe9253f"},
    {file = "Sphinx-4.3.1.tar.gz", hash = "sha256:32a5b3e9a1b176cc25ed048557d4d3d01af635e6b76c5bc7a43b0a34447fbd45"},
]
sphinx-rtd-theme = [
    {file = "sphinx_rtd_theme-1.0.0-py2.py3-none-any.whl", hash = "sha256:4d35a56f4508cfee4c4fb604373ede6feae2a306731d533f409ef5c3496fdbd8"},
    {file = "sphinx_rtd_theme-1.0.0.tar.gz", hash = "sha256:eec6d497e4c2195fa0e8b2016b337532b8a699a68bcb22a512870e16925c6a5c"},
]
sphinxcontrib-applehelp = [
    {file = "sphinxcontrib-applehelp-1.0.2.tar.gz", hash = "sha256:a072735ec80e7675e3f432fcae8610ecf509c5f1869d17e2eecff44389cdbc58"},
    {file = "sphinxcontrib_applehelp-1.0.2-py2.py3-none-any.whl", hash = "sha256:806111e5e962be97c29ec4c1e7fe277bfd19e9652fb1a4392105b43e01af885a"},
]
sphinxcontrib-devhelp = [
    {file = "sphinxcontrib-devhelp-1.0.2.tar.gz", hash = "sha256:ff7f1afa7b9642e7060379360a67e9c41e8f3121f2ce9164266f61b9f4b338e4"},
    {file = "sphinxcontrib_devhelp-1.0.2-py2.py3-none-any.whl", hash = "sha256:8165223f9a335cc1af7ffe1ed31d2871f325254c0423bc0c4c7cd1c1e4734a2e"},
]
sphinxcontrib-htmlhelp = [
    {file = "sphinxcontrib-htmlhelp-2.0.0.tar.gz", hash = "sha256:f5f8bb2d0d629f398bf47d0d69c07bc13b65f75a81ad9e2f71a63d4b7a2f6db2"},
    {file = "sphinxcontrib_htmlhelp-2.0.0-py2.py3-none-any.whl", hash = "sha256:d412243dfb797ae3ec2b59eca0e52dac12e75a241bf0e4eb861e450d06c6ed07"},
]
sphinxcontrib-jsmath = [
    {file = "sphinxcontrib-jsmath-1.0.1.tar.gz", hash = "sha256:a9925e4a4587247ed2191a22df5f6970656cb8ca2bd6284309578f2153e0c4b8"},
    {file = "sphinxcontrib_jsmath-1.0.1-py2.py3-none-any.whl", hash = "sha256:2ec2eaebfb78f3f2078e73666b1415417a116cc848b72e5172e596c871103178"},
]
sphinxcontrib-qthelp = [
    {file = "sphinxcontrib-qthelp-1.0.3.tar.gz", hash = "sha256:4c33767ee058b70dba89a6fc5c1892c0d57a54be67ddd3e7875a18d14cba5a72"},
    {file = "sphinxcontrib_qthelp-1.0.3-py2.py3-none-any.whl", hash = "sha256:bd9fc24bcb748a8d51fd4ecaade681350aa63009a347a8c14e637895444dfab6"},
]
sphinxcontrib-serializinghtml = [
    {file = "sphinxcontrib-serializinghtml-1.1.5.tar.gz", hash = "sha256:aa5f6de5dfdf809ef505c4895e51ef5c9eac17d0f287933eb49ec495280b6952"},
    {file = "sphinxcontrib_serializinghtml-1.1.5-py2.py3-none-any.whl", hash = "sha256:352a9a00ae864471d3a7ead8d7d79f5fc0b57e8b3f95e9867eb9eb28999b92fd"},
]
toml = [
    {file = "toml-0.10.2-py2.py3-none-any.whl", hash = "sha256:806143ae5bfb6a3c6e736a764057db0e6a0e05e338b5630894a5f779cabb4f9b"},
    {file = "toml-0.10.2.tar.gz", hash = "sha256:b3bda1d108d5dd99f4a20d24d9c348e91c4db7ab1b749200bded2f839ccbe68f"},
]
tomli = [
    {file = "tomli-1.2.2-py3-none-any.whl", hash = "sha256:f04066f68f5554911363063a30b108d2b5a5b1a010aa8b6132af78489fe3aade"},
    {file = "tomli-1.2.2.tar.gz", hash = "sha256:c6ce0015eb38820eaf32b5db832dbc26deb3dd427bd5f6556cf0acac2c214fee"},
]
typed-ast = [
    {file = "typed_ast-1.4.3-cp35-cp35m-manylinux1_i686.whl", hash = "sha256:2068531575a125b87a41802130fa7e29f26c09a2833fea68d9a40cf33902eba6"},
    {file = "typed_ast-1.4.3-cp35-cp35m-manylinux1_x86_64.whl", hash = "sha256:c907f561b1e83e93fad565bac5ba9c22d96a54e7ea0267c708bffe863cbe4075"},
    {file = "typed_ast-1.4.3-cp35-cp35m-manylinux2014_aarch64.whl", hash = "sha256:1b3ead4a96c9101bef08f9f7d1217c096f31667617b58de957f690c92378b528"},
    {file = "typed_ast-1.4.3-cp35-cp35m-win32.whl", hash = "sha256:dde816ca9dac1d9c01dd504ea5967821606f02e510438120091b84e852367428"},
    {file = "typed_ast-1.4.3-cp35-cp35m-win_amd64.whl", hash = "sha256:777a26c84bea6cd934422ac2e3b78863a37017618b6e5c08f92ef69853e765d3"},
    {file = "typed_ast-1.4.3-cp36-cp36m-macosx_10_9_x86_64.whl", hash = "sha256:f8afcf15cc511ada719a88e013cec87c11aff7b91f019295eb4530f96fe5ef2f"},
    {file = "typed_ast-1.4.3-cp36-cp36m-manylinux1_i686.whl", hash = "sha256:52b1eb8c83f178ab787f3a4283f68258525f8d70f778a2f6dd54d3b5e5fb4341"},
    {file = "typed_ast-1.4.3-cp36-cp36m-manylinux1_x86_64.whl", hash = "sha256:01ae5f73431d21eead5015997ab41afa53aa1fbe252f9da060be5dad2c730ace"},
    {file = "typed_ast-1.4.3-cp36-cp36m-manylinux2014_aarch64.whl", hash = "sha256:c190f0899e9f9f8b6b7863debfb739abcb21a5c054f911ca3596d12b8a4c4c7f"},
    {file = "typed_ast-1.4.3-cp36-cp36m-win32.whl", hash = "sha256:398e44cd480f4d2b7ee8d98385ca104e35c81525dd98c519acff1b79bdaac363"},
    {file = "typed_ast-1.4.3-cp36-cp36m-win_amd64.whl", hash = "sha256:bff6ad71c81b3bba8fa35f0f1921fb24ff4476235a6e94a26ada2e54370e6da7"},
    {file = "typed_ast-1.4.3-cp37-cp37m-macosx_10_9_x86_64.whl", hash = "sha256:0fb71b8c643187d7492c1f8352f2c15b4c4af3f6338f21681d3681b3dc31a266"},
    {file = "typed_ast-1.4.3-cp37-cp37m-manylinux1_i686.whl", hash = "sha256:760ad187b1041a154f0e4d0f6aae3e40fdb51d6de16e5c99aedadd9246450e9e"},
    {file = "typed_ast-1.4.3-cp37-cp37m-manylinux1_x86_64.whl", hash = "sha256:5feca99c17af94057417d744607b82dd0a664fd5e4ca98061480fd8b14b18d04"},
    {file = "typed_ast-1.4.3-cp37-cp37m-manylinux2014_aarch64.whl", hash = "sha256:95431a26309a21874005845c21118c83991c63ea800dd44843e42a916aec5899"},
    {file = "typed_ast-1.4.3-cp37-cp37m-win32.whl", hash = "sha256:aee0c1256be6c07bd3e1263ff920c325b59849dc95392a05f258bb9b259cf39c"},
    {file = "typed_ast-1.4.3-cp37-cp37m-win_amd64.whl", hash = "sha256:9ad2c92ec681e02baf81fdfa056fe0d818645efa9af1f1cd5fd6f1bd2bdfd805"},
    {file = "typed_ast-1.4.3-cp38-cp38-macosx_10_9_x86_64.whl", hash = "sha256:b36b4f3920103a25e1d5d024d155c504080959582b928e91cb608a65c3a49e1a"},
    {file = "typed_ast-1.4.3-cp38-cp38-manylinux1_i686.whl", hash = "sha256:067a74454df670dcaa4e59349a2e5c81e567d8d65458d480a5b3dfecec08c5ff"},
    {file = "typed_ast-1.4.3-cp38-cp38-manylinux1_x86_64.whl", hash = "sha256:7538e495704e2ccda9b234b82423a4038f324f3a10c43bc088a1636180f11a41"},
    {file = "typed_ast-1.4.3-cp38-cp38-manylinux2014_aarch64.whl", hash = "sha256:af3d4a73793725138d6b334d9d247ce7e5f084d96284ed23f22ee626a7b88e39"},
    {file = "typed_ast-1.4.3-cp38-cp38-win32.whl", hash = "sha256:f2362f3cb0f3172c42938946dbc5b7843c2a28aec307c49100c8b38764eb6927"},
    {file = "typed_ast-1.4.3-cp38-cp38-win_amd64.whl", hash = "sha256:dd4a21253f42b8d2b48410cb31fe501d32f8b9fbeb1f55063ad102fe9c425e40"},
    {file = "typed_ast-1.4.3-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:f328adcfebed9f11301eaedfa48e15bdece9b519fb27e6a8c01aa52a17ec31b3"},
    {file = "typed_ast-1.4.3-cp39-cp39-manylinux1_i686.whl", hash = "sha256:2c726c276d09fc5c414693a2de063f521052d9ea7c240ce553316f70656c84d4"},
    {file = "typed_ast-1.4.3-cp39-cp39-manylinux1_x86_64.whl", hash = "sha256:cae53c389825d3b46fb37538441f75d6aecc4174f615d048321b716df2757fb0"},
    {file = "typed_ast-1.4.3-cp39-cp39-manylinux2014_aarch64.whl", hash = "sha256:b9574c6f03f685070d859e75c7f9eeca02d6933273b5e69572e5ff9d5e3931c3"},
    {file = "typed_ast-1.4.3-cp39-cp39-win32.whl", hash = "sha256:209596a4ec71d990d71d5e0d312ac935d86930e6eecff6ccc7007fe54d703808"},
    {file = "typed_ast-1.4.3-cp39-cp39-win_amd64.whl", hash = "sha256:9c6d1a54552b5330bc657b7ef0eae25d00ba7ffe85d9ea8ae6540d2197a3788c"},
    {file = "typed_ast-1.4.3.tar.gz", hash = "sha256:fb1bbeac803adea29cedd70781399c99138358c26d05fcbd23c13016b7f5ec65"},
]
typing-extensions = [
    {file = "typing_extensions-4.0.1-py3-none-any.whl", hash = "sha256:7f001e5ac290a0c0401508864c7ec868be4e701886d5b573a9528ed3973d9d3b"},
    {file = "typing_extensions-4.0.1.tar.gz", hash = "sha256:4ca091dea149f945ec56afb48dae714f21e8692ef22a395223bcd328961b6a0e"},
]
urllib3 = [
    {file = "urllib3-1.26.7-py2.py3-none-any.whl", hash = "sha256:c4fdf4019605b6e5423637e01bc9fe4daef873709a7973e195ceba0a62bbc844"},
    {file = "urllib3-1.26.7.tar.gz", hash = "sha256:4987c65554f7a2dbf30c18fd48778ef124af6fab771a377103da0585e2336ece"},
]
zipp = [
    {file = "zipp-3.6.0-py3-none-any.whl", hash = "sha256:9fe5ea21568a0a70e50f273397638d39b03353731e6cbbb3fd8502a33fec40bc"},
    {file = "zipp-3.6.0.tar.gz", hash = "sha256:71c644c5369f4a6e07636f0aa966270449561fcea2e3d6747b8d23efaa9d7832"},
]