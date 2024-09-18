python -m venv .
. .\Scripts\activate
git clone https://github.com/cursed-amari/test-task-github-api.git  
cd .\test-task-github-api\
pip install -r .\requirements.txt
Open .env and enter your API token, username, repo name
python .\gitapi.py  
