# PYTHON CODE SNIPPETS

##### These are a collection of short python scripts that I wrote to 
Simple Python code scripts built using [python $3.10.8$](https://python.org).

----------
**Dependencies, Technologies or Hardware requirements used:**
- None

> Python is all that is needed! 🎉

### LOCAL SETUP
To run all the snippets from this repository locally on your computer;
```console
$ git pull 'https://github.com/pseudo-safariac/short_python_scripts.git/'
```
----------

## FEATURED CODE
1. [BMI calculator](#bmi-calculator)
2. [Tkinter Tracebacks](#tkinter-tracebacks)

## BMI calculator
The script is a simple program that calculates the [Body Mass Index](https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_1.) (BMI) of a human adult. The calculation is based on Scientific research that is publicly available.

The function called receives two arguments;
- Height in metric centimetres
- Weight in metric kilograms

```python
bmi_calculation(height : float | int, weight : float | int) -> str | None
```
The function returns a string that has information on the BMI of the user.
An example of use is given below;
```console
$ py bmi_calculator.py
Enter your height in cm:
163
Enter weight in kg:
62.5

****************************************
        You are of normal weight
****************************************
```

A later update release will also feature an option to also receive the BMI index itself as an `integer|float`.

