# PhycoPlaca
interview assignment
Developed in Linux 
Input Format example: "2865 2012-11-28 15:58" 
-to run a stressTest run the command "python3 stressTest.py"
-to run the predictor for one case run "python3 predictor.py" and give the input using the above format.

## queryClass.py 
Contains the Class to solve the problem.

## queryGenerator.py 
Contains the functions to create a random input for the problem, it creates the input knowing if it is in a Pico y Placa time restriction.

### predictor.py 
Gives an output text with the input car information, and answering the question if the car is in a Pico y Placa restriction.

### predictorStressTest.py 
Return a boolean value, True if the car is in a Pico y Placa restriction False otherwise.

### generateSimpleCase.py 
Create a input problem in a .txt file. of 1 line.

### stressTest.py 
Runs a stressTest using ###predictorStressTest.py and ###queryGenerator.py.




