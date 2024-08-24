# 仮想環境のディレクトリ名
VENV_DIR = .venv

# Pythonのバージョン指定
PYTHON = python3

# 仮想環境のPython実行ファイル
VENV_PYTHON = $(VENV_DIR)/bin/python

# 仮想環境のPIP実行ファイル
PIP = $(VENV_DIR)/bin/pip

# 仮想環境を作成し、依存パッケージをインストール
install:
	$(PYTHON) -m venv $(VENV_DIR)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# マイグレーションとアプリケーションの実行
run:
	$(VENV_PYTHON) migrate.py

# 一連のコマンドをまとめたstart
start: install run

# 仮想環境を削除
clean:
	rm -rf $(VENV_DIR)
