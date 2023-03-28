# rasa-chatbot


1. 
   - Create Venv in python. Make sure if you are using the latest rasa version then check if the python version is compatible or not. For rasa 3.4.0 python 3.10 is compatible https://rasa.com/docs/rasa/installation/environment-set-up


2. Rasa initialise the project
   - Initialise the project by clonning the repo
   - Install rasa and other dependencies by ```pip install -r requirements.txt```

3. To train the data run this command:
	```rasa train```

4. Write actions if required in actions.py(it use if you want to get the data from api)

5. Write the flow in domain.yml 

6. Write the port number in endpoints.yml for running server on particular port

7. Start rasa actions server using ```rasa run actions```

8. Start rasa api server so that chatbot can communicate using this 
	```rasa run --cors "*" --enable-api```


9. For chatbot design we can use rasa own chatbot design(which has not good design) or we can use botfront which is best.
    Using botfront  we can change appearance of chat boat.we just  need to add the Script tag in any  HTML file.


10. Add the scripting tag in the HTML file and change the socket url .


References:
    1. Rasa official learning documentations:
        a. https://learning.rasa.com/
        b. https://rasa.com/docs/





		


