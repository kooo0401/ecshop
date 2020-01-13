FROM python:3.8

# Pythonがpyc filesとdiscへ書き込むことを防ぐ
ENV PYTHONDONTWRITEBYTECODE 1

# Pythonが標準入出力をバッファリングすることを防ぐ
ENV PYTHONUNBUFFERED 1

# コンテナ内にディレクトリ作成
RUN mkdir /app

# 作業ディレクトリを指定
WORKDIR /app

# Pipenvをインストール
RUN pip install --upgrade pip \
    && pip install pipenv

# ホストのpipfileをコンテナの作業ディレクトリにコピー
COPY Pipfile /app/Pipfile

# pipfileからパッケージをインストールしてDjango環境を構築
RUN pipenv install --system --skip-lock

# ローカルのecshopルートディレクトリをコンテナのapp/配下にコピー
COPY . /app/