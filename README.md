This is the first version of the AirBnb clone. We will be building a python console and a file storage engine.

How to start the command interpreter - To evoke the command interpreter please execute the console.py script. You will need Python 3.8.5 for best use.

How to use the command interpreter - The command interpreter has 5 documented commands. namely

1. create - Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.

2. show - Prints the string representation of an instance based on the class name and id.

3. destroy - Deletes an instance based on the class name and id (save the change into the JSON file).

4. all -  Prints all string representation of all instances based or not on the class name.

5. update -  Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). 

Examples:

1. $ create BaseModel 
$ 49faff9a-6318-451f-87b6-910505c55907

2. $ show BaseModel 49faff9a-6318-451f-87b6-910505c55907
$ [BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}


3. $ all BaseModel 49faff9a-6318-451f-87b6-910505c55907
$ ["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]

4.  $ update BaseModel 49faff9a-6318-451f-87b6-910505c55907 email "aibnb@mail.com"

$ ["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401), 'email': 'aibnb@mail.com}"]

5. $ destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
$ show BaseModel 49faff9a-6318-451f-87b6-910505c55907
$ ** no instance found **
