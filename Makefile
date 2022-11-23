install:
	@pip install -r requirements.txt

run:
	@streamlit run ./app/main.py --server.port 8080 --theme.base dark