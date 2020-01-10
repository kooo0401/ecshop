FROM python:3.8
# Pythonがpyc filesとdiscへ書き込むことを防ぐ
ENV PYTHONDONTWRITEBYTECODE 1
# Pythonが標準入出力をバッファリングすることを防ぐ
ENV PYTHONUNBUFFERED 1
# コンテナ内にディレクトリ作成
RUN mkdir /app
# 作業ディレクトリを指定
WORKDIR /app
# requirements.txtを /appディレクトリにコピー
COPY requirements.txt /app/
RUN pip install -r requirements.txt
# ローカルのecshopルートディレクトリをコンテナのapp/配下にコピー
COPY . /app/