# cosi217_hw

I am currently running Python 3.9.
The modules required to run the code are spacy, flask, streamlit, flask_restful, streamlit, and pandas.
I also used the ner.py file and main.css file given from class.

1) Restful API:
To start the Restful API, download the "ner.py" file and "flask_get_post.py" file. Then to run the Restful API, only load the "flask_get_post.py" file only. It is a simple website that can be used with GET and POST commands.
To get the post command, copy and paste the following into the command line: curl http://127.0.0.1:5000/ -H "Content-Type: text/plain" -d 'insert sentence here'
Replace 'insert sentence here' with any text and.
To get the get command, either click http://127.0.0.1:5000/ or write on the command line the following:  curl http://127.0.0.1:5000/

2) Flask webserver:
To start the Flask webserver, download the "flask_form_app.py" file, the index.html file from the templates folder, and the static/css/main.css file, and the "ner.py" file if the ner file is not downloaded already. In order to run the "flask_form_app.py" file correctly, ner.py and flask_form_app.py should be in the same file, the index.html should be in the templates folder, and the main.css file should be in the folder static and then the folder css.
Once the file is run, click http://127.0.0.1:5000/ and you will be directed to the Flask webserver. Insert text into the form and the text markup will be provided.

3) Streamlit:
To run the streamlit file, download the "streamlit_final.py" file and also "ner.py" file if it is not downloaded already. Run "streamlit_final.py" on the command line by adding "streamlit run" and wherever the streamlit_final.py is located. Then once that is done, the steamlit website can be shown on the local URL http://localhost:8501/ or network URL.
